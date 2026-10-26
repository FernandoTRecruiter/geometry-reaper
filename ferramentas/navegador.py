# -*- coding: utf-8 -*-
"""
navegador.py: abre o Edge (ou o Chrome) sem janela e conversa com ele pelo
protocolo de depuração (CDP). É a base dos testes e das simulações.

Por que existe: o jogo é um HTML com canvas. Para testar de verdade é preciso
um navegador rodando o JavaScript, apertando teclas e tirando foto. O CDP faz
isso sem instalar nada além do pacote websocket-client.

Uso:
    from navegador import Navegador
    with Navegador(1280, 720) as nav:
        nav.ir("file:///C:/.../index.html")
        print(nav.js("document.title"))
        nav.foto("tela.png")
        print(nav.erros())

Requisitos: Python 3.8+, `pip install websocket-client`, Edge ou Chrome instalado.
"""
import base64, json, os, shutil, socket, subprocess, sys, tempfile, time, urllib.request

import websocket  # pip install websocket-client

# Onde costumam estar os navegadores (o primeiro que existir é usado).
CANDIDATOS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]


def acha_navegador():
    # Por quê: cada máquina tem o navegador num lugar; a variável NAVEGADOR deixa escolher.
    escolhido = os.environ.get("NAVEGADOR")
    if escolhido and os.path.exists(escolhido):
        return escolhido
    for c in CANDIDATOS:
        if os.path.exists(c):
            return c
    raise RuntimeError("Nenhum Edge/Chrome encontrado. Defina a variável NAVEGADOR com o caminho.")


def porta_livre(inicio=9400):
    # Por quê: porta que já responde é de outro programa; usamos uma que ninguém ocupa.
    for p in range(inicio, inicio + 300):
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:
                return p
    raise RuntimeError("sem porta livre")


class Navegador:
    """Um navegador sem janela, com perfil próprio e descartável."""

    def __init__(self, largura=1280, altura=720, escala=1):
        self.w, self.h, self.escala = largura, altura, escala

    def __enter__(self):
        # Passo 1: abrir o navegador numa porta livre, com perfil temporário só nosso.
        self.porta = porta_livre()
        self.perfil = tempfile.mkdtemp(prefix=f"gr-nav{self.porta}-")
        args = [acha_navegador(), "--headless=new", f"--remote-debugging-port={self.porta}",
                f"--user-data-dir={self.perfil}", "--no-first-run", "--no-default-browser-check",
                "--disable-sync", "--hide-scrollbars", "--allow-file-access-from-files",
                "--disable-background-timer-throttling", "--disable-renderer-backgrounding",
                "--disable-backgrounding-occluded-windows", "--autoplay-policy=no-user-gesture-required",
                "--enable-unsafe-swiftshader", "about:blank"]
        extra = {}
        if sys.platform == "win32":
            extra["creationflags"] = 0x00000008 | 0x00000200  # sem console, grupo próprio
        self.proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL, **extra)
        # Passo 2: esperar a porta responder e pegar a aba em branco que nós abrimos.
        alvo = None
        for _ in range(100):
            try:
                abas = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{self.porta}/json", timeout=1).read())
                alvo = next((x for x in abas if x.get("type") == "page"), None)
                if alvo:
                    break
            except Exception:
                pass
            time.sleep(0.25)
        if not alvo:
            raise RuntimeError("o navegador não abriu a porta de depuração")
        self.ws = websocket.create_connection(alvo["webSocketDebuggerUrl"], suppress_origin=True, timeout=600)
        self.n, self.eventos = 0, []
        for m in ("Runtime.enable", "Page.enable", "Log.enable"):
            self.cmd(m)
        self.tamanho(self.w, self.h)
        return self

    def __exit__(self, *a):
        # Fecha só o navegador que abrimos e apaga o perfil temporário.
        try:
            self.cmd("Browser.close")
        except Exception:
            pass
        time.sleep(0.5)
        try:
            self.proc.kill()
        except Exception:
            pass
        shutil.rmtree(self.perfil, ignore_errors=True)

    def cmd(self, metodo, **params):
        # Manda um comando e espera a resposta com o mesmo número; eventos no meio são guardados.
        self.n += 1
        meu = self.n
        self.ws.send(json.dumps({"id": meu, "method": metodo, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == meu:
                if "error" in msg:
                    raise RuntimeError(f"{metodo}: {msg['error']}")
                return msg.get("result", {})
            self.eventos.append(msg)

    def esperar(self, segundos):
        # Deixa o tempo passar lendo eventos (é assim que os erros de JS chegam).
        fim = time.time() + segundos
        self.ws.settimeout(0.2)
        while time.time() < fim:
            try:
                self.eventos.append(json.loads(self.ws.recv()))
            except Exception:
                pass
        self.ws.settimeout(600)

    def tamanho(self, w, h):
        self.w, self.h = w, h
        self.cmd("Emulation.setDeviceMetricsOverride", width=w, height=h,
                 deviceScaleFactor=self.escala, mobile=False)

    def ir(self, url, espera=2.0):
        self.cmd("Page.navigate", url=url)
        self.esperar(espera)

    def js(self, expr, espera=0.0):
        # Roda JavaScript na página e devolve o valor (precisa ser serializável em JSON).
        r = self.cmd("Runtime.evaluate", expression=expr, awaitPromise=True, returnByValue=True)
        if r.get("exceptionDetails"):
            d = r["exceptionDetails"]
            raise RuntimeError("JS falhou: " + (d.get("exception", {}).get("description") or d.get("text", ""))[:600])
        if espera:
            self.esperar(espera)
        return r.get("result", {}).get("value")

    def tecla(self, code, key=None, segurar=0.0):
        # Aperta uma tecla "de verdade" (o jogo ouve keydown/keyup na janela).
        key = key or code.replace("Key", "").lower()
        self.js(f"dispatchEvent(new KeyboardEvent('keydown',{{code:'{code}',key:'{key}',bubbles:true}}))")
        if segurar:
            self.esperar(segurar)
        self.js(f"dispatchEvent(new KeyboardEvent('keyup',{{code:'{code}',key:'{key}',bubbles:true}}))")

    def clicar(self, x, y, botao="left"):
        for t in ("mousePressed", "mouseReleased"):
            self.cmd("Input.dispatchMouseEvent", type=t, x=x, y=y, button=botao, clickCount=1)

    def foto(self, saida):
        img = self.cmd("Page.captureScreenshot", format="png")
        with open(saida, "wb") as f:
            f.write(base64.b64decode(img["data"]))
        return saida

    def erros(self):
        # Junta exceções, console.error e erros de log (ignora favicon, que o arquivo local não tem).
        out = []
        for e in self.eventos:
            m = e.get("method")
            if m == "Runtime.exceptionThrown":
                d = e["params"]["exceptionDetails"]
                out.append("EXCECAO: " + (d.get("exception", {}).get("description") or d.get("text", ""))[:400])
            elif m == "Runtime.consoleAPICalled" and e["params"].get("type") == "error":
                out.append("console.error: " + " ".join(str(x.get("value", x.get("description", ""))) for x in e["params"]["args"])[:400])
            elif m == "Log.entryAdded" and e["params"]["entry"].get("level") == "error":
                txt = e["params"]["entry"].get("text", "")
                if "favicon" not in txt:
                    out.append("log: " + txt[:300])
        return out


def url_de(caminho):
    # Caminho do disco vira endereço file:/// que o navegador entende.
    return "file:///" + os.path.abspath(caminho).replace("\\", "/")
