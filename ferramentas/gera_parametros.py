# -*- coding: utf-8 -*-
"""
gera_parametros.py: lê o bloco TWEAKS do index.html e escreve docs/parametros.md.

Por que existe: o TWEAKS é a fonte única de balanceamento (mais de 600 números).
Ler o código para achar "onde muda a vida do dragão" é chato; este script monta
uma tabela por área com o CAMINHO exato (ex.: ships.cruiser.rail.fireDelay),
o valor atual e a explicação, tirada do comentário // que está ao lado do valor.
Rode de novo sempre que mudar o TWEAKS: a tabela nunca fica velha.

Uso:  python ferramentas/gera_parametros.py   (só Python, sem instalar nada)
"""
import os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
HTML = os.path.join(RAIZ, "index.html")
SAIDA = os.path.join(RAIZ, "docs", "parametros.md")

# Explicação padrão para chaves que se repetem sem comentário próprio (ex.: hp de cada inimigo).
GLOSSARIO = {
    "hp": "vida", "spd": "velocidade (px/s)", "dmg": "dano", "r": "raio: tamanho e colisão (px)",
    "score": "pontos ao matar", "xp": "chips de XP que solta ao morrer", "limit": "máximo vivo ao mesmo tempo",
    "baseDamage": "dano base (escala com o atributo Dano)", "areaOfEffect": "raio da explosão (px)",
    "cooldown": "recarga em segundos (encurtada pelo Rate of Spell)", "projectiles": "quantos projéteis dispara",
    "fireDelay": "segundos entre disparos", "coneRad": "abertura do leque (radianos)", "speed": "velocidade (px/s)",
    "flightTime": "segundos até a bomba cair", "clusterBombs": "bombinhas extras ao redor do impacto",
    "name": "nome exibido", "desc": "texto da tela de escolha", "locked": "true = nave bloqueada (EM BREVE)",
    "speedMul": "multiplicador de velocidade da nave", "hpMul": "multiplicador de vida da nave",
    "shieldMul": "multiplicador de escudo da nave", "weapon": "arma da nave", "blocked": "power-ups que esta nave nunca recebe",
    "colors": "cores da nave", "hull": "cor do casco", "accent": "cor de destaque", "glow": "cor do brilho",
    "aim": "modelo de mira (ver o topo da seção NAVES)", "move": "modelo de movimento (ver o topo da seção NAVES)",
    "damage": "dano por projétil (escala com o atributo Dano)", "size": "tamanho do projétil (px)",
    "lifeSec": "segundos de vida do projétil (define o alcance)", "spread": "dispersão (radianos)",
    "radius": "raio do casco (px): maior = alvo maior", "previewScale": "zoom do desenho na tela de escolha",
    "accel": "aceleração (px/s²)", "friction": "atrito: quanto freia sozinho por segundo",
    "perLevel": "ganho por nível", "radiusBase": "raio no nível 1 (px)", "radiusPerLevel": "raio extra por nível (px)",
    "dmgBase": "dano no nível 1", "dmgPerLevel": "dano extra por nível", "knockback": "empurrão (px/s)",
    "burnDps": "dano por segundo da queimadura", "burnSec": "duração da queimadura (s)",
    "chanceBase": "chance no nível 1", "chancePerLevel": "chance extra por nível",
    "speedPct": "+% de velocidade por ponto de atributo", "rofPct": "+% de cadência por ponto de atributo",
    "damagePct": "+% de dano por ponto de atributo", "shieldFlat": "+ escudo máximo por ponto de atributo",
    "cooldownPct": "-% de recarga das habilidades por ponto de atributo", "critPct": "+ chance de crítico por ponto de atributo",
    "master": "volume geral (0 a 1)", "sfx": "volume dos efeitos (0 a 1)", "music": "volume da música (0 a 1)",
    "cometDamage": "dano de cada cometa", "cometSpeedMin": "velocidade mínima do cometa (px/s)",
    "cometSpeedMax": "velocidade máxima do cometa (px/s)", "cometRadiusMin": "tamanho mínimo do cometa (px)",
    "cometRadiusMax": "tamanho máximo do cometa (px)", "giftPowers": "cartas de presente quando o dragão desperta (Desafio)",
    "giftAttrs": "pontos de atributo de presente quando o dragão desperta (Desafio)",
    "weaveSpeed": "velocidade enquanto serpenteia (px/s)", "weaveTurnRate": "curva enquanto serpenteia (rad/s)",
    "x2_points": "pontos do prêmio x2", "x3_points": "pontos do prêmio x3", "x5_points": "pontos do prêmio x5",
    "jackpot_points": "pontos do JACKPOT, para distribuir", "selectorEnabled": "false = pula a tela de escolha de nave",
    "defaultShip": "nave usada quando o seletor está desligado",
}

AREAS = {  # título amigável de cada área (chave de primeiro nível do TWEAKS)
    "world": "Mundo", "player": "Jogador", "blaster": "Blaster (arma do Fighter)", "powerups": "Habilidades ativas",
    "passives": "Passivas", "stats": "Atributos (ganho por ponto)", "mobs": "Inimigos", "engine": "Motor (ajustes finos)",
    "difficulty": "Dificuldade e spawner", "events": "Eventos do Survival", "desafio": "Roteiro do modo Desafio",
    "dragon": "Dragão", "combo": "Combo", "score": "Pontuação", "slot": "Alavanca (slot)", "roulette": "Roleta de atributos",
    "ships": "Naves", "progression": "Progressão (XP e cartas)", "audio": "Volumes", "music": "Música",
}


class Leitor:
    """Lê o objeto JavaScript do TWEAKS guardando, para cada valor, a linha onde ele está."""

    def __init__(self, texto, linha0):
        self.t, self.i, self.linha0 = texto, 0, linha0

    def linha(self):
        return self.linha0 + self.t.count("\n", 0, self.i)

    def pula(self):
        # Pula espaços e comentários (os comentários são lidos à parte, por linha).
        while self.i < len(self.t):
            c = self.t[self.i]
            if c.isspace():
                self.i += 1
            elif self.t.startswith("//", self.i):
                self.i = self.t.find("\n", self.i)
                if self.i < 0:
                    self.i = len(self.t)
            elif self.t.startswith("/*", self.i):
                self.i = self.t.find("*/", self.i) + 2
            else:
                break

    def valor(self):
        self.pula()
        c = self.t[self.i]
        if c == "{":
            return self.objeto()
        if c == "[":
            return self.lista()
        if c in "'\"":
            fim = self.i + 1
            while self.t[fim] != c:
                fim += 2 if self.t[fim] == "\\" else 1
            s = self.t[self.i:fim + 1]
            self.i = fim + 1
            return ("folha", s, self.linha())
        m = re.compile(r"[-+0-9.eE]+|true|false|null").match(self.t, self.i)
        if not m:
            raise ValueError(f"valor inesperado na linha {self.linha()}: {self.t[self.i:self.i+30]!r}")
        self.i = m.end()
        return ("folha", m.group(0), self.linha())

    def lista(self):
        ini = self.i
        prof = 0
        while True:  # lista vira UM valor só (texto compacto), como aparece no código
            c = self.t[self.i]
            if c in "'\"":
                self.i = self.t.index(c, self.i + 1)
            elif c == "[":
                prof += 1
            elif c == "]":
                prof -= 1
                if prof == 0:
                    self.i += 1
                    break
            self.i += 1
        bruto = self.t[ini:self.i]
        sem_coment = re.sub(r"//[^\n]*", "", bruto)
        compacto = re.sub(r"\s+", " ", sem_coment).replace("[ ", "[").replace(" ]", "]").strip()
        return ("folha", re.sub(r",\s*\]", "]", compacto), self.linha())

    def objeto(self):
        linha_abre = self.linha()
        self.i += 1
        itens = []
        while True:
            self.pula()
            if self.t[self.i] == "}":
                self.i += 1
                return ("obj", itens, linha_abre)
            m = re.compile(r"[A-Za-z_$][\w$]*|\d+").match(self.t, self.i)
            chave = m.group(0)
            linha_chave = self.linha()
            self.i = m.end()
            self.pula()
            assert self.t[self.i] == ":", f"esperava ':' na linha {self.linha()}"
            self.i += 1
            v = self.valor()
            itens.append((chave, v, linha_chave))
            self.pula()
            if self.t[self.i] == ",":
                self.i += 1


def comentarios_por_linha(linhas):
    """Para cada linha: o comentário // ao lado do código, e se a linha é SÓ comentário."""
    lado, so, coluna = {}, {}, {}
    for n, l in enumerate(linhas, 1):
        pos = achar_barra_barra(l)
        if pos < 0:
            continue
        txt = l[pos + 2:].strip()
        if l[:pos].strip() == "":
            so[n] = txt
            coluna[n] = pos
        else:
            lado[n] = txt
    return lado, so, coluna


def achar_barra_barra(l):
    # Acha "//" que não está dentro de texto entre aspas (ex.: URLs não existem aqui, mas cores '#fff' sim).
    dentro = None
    for k, c in enumerate(l):
        if dentro:
            if c == dentro:
                dentro = None
        elif c in "'\"":
            dentro = c
        elif l.startswith("//", k):
            return k
    return -1


def limpa(txt):
    # "|" quebraria a tabela; o travessão (código 2014) vira vírgula, pela regra de escrita do projeto
    return txt.replace("|", "/").replace("\u2014", ",").strip()


def main():
    html = open(HTML, encoding="utf-8").read()
    ini = html.index("const TWEAKS = {")
    fim = html.index("FIM DOS TWEAKS")
    linhas = html.splitlines()
    linha_ini = html.count("\n", 0, ini) + 1
    corpo = html[ini + len("const TWEAKS = "):fim]
    arvore = Leitor(corpo, linha_ini).valor()
    lado, so, coluna = comentarios_por_linha(linhas)

    # Continuação: linha só de comentário, mais recuada que o código da linha anterior, que tinha comentário.
    cont = {}
    for n in sorted(so):
        ant = n - 1
        while ant in cont:
            ant = cont[ant]
        if ant in lado:
            recuo = len(linhas[ant - 1]) - len(linhas[ant - 1].lstrip())
            if coluna[n] > recuo + 4:
                lado[ant] = lado[ant] + " " + so[n]
                cont[n] = ant

    def nota_de_secao(linha_chave, linha_obj):
        # Comentário solto mais próximo ACIMA da chave, dentro do mesmo objeto (ex.: "pattern 2: cerco").
        n = linha_chave - 1
        while n > linha_obj:
            if n in so and n not in cont:
                bloco = []  # junta o bloco inteiro de linhas de comentário seguidas
                while n > linha_obj and n in so and n not in cont:
                    bloco.insert(0, so[n])
                    n -= 1
                return " ".join(bloco)
            n -= 1
        return ""

    tabelas = []  # (area, [(caminho, valor, explicacao)])

    def anda(no, caminho, linha_obj, herdado, area_linhas):
        tipo, conteudo, _ = no
        for chave, v, linha_chave in conteudo:
            cam = f"{caminho}.{chave}" if caminho else chave
            if v[0] == "obj":
                nota_obj = lado.get(linha_chave, "")
                anda(v, cam, v[2], nota_obj or herdado, area_linhas)
                continue
            _, valor, linha_valor = v
            exp = lado.get(linha_valor) or lado.get(linha_chave) or ""
            if not exp:
                sec = nota_de_secao(linha_chave, linha_obj)
                base = GLOSSARIO.get(chave, "")
                partes = [p for p in (base, f"({herdado})" if herdado and not base else "", f"[{sec}]" if sec else "") if p]
                exp = " ".join(partes)
            area_linhas.append((cam, valor, limpa(exp)))

    for chave, v, linha_chave in arvore[1]:
        linhas_area = []
        if v[0] == "obj":
            anda(v, chave, v[2], lado.get(linha_chave, ""), linhas_area)
        else:
            linhas_area.append((chave, v[1], limpa(lado.get(v[2], ""))))
        tabelas.append((chave, linhas_area))

    total = sum(len(l) for _, l in tabelas)
    out = ["# Parâmetros do jogo (TWEAKS)", "",
           "Gerado por `python ferramentas/gera_parametros.py` a partir do bloco `TWEAKS` do `index.html`. "
           "Não edite este arquivo: mude o valor no `index.html` e rode o script de novo.", "",
           f"**{total} parâmetros** em {len(tabelas)} áreas. Como ler: o **caminho** é onde o número mora dentro do `TWEAKS` "
           "(`ships.cruiser.rail.fireDelay` = bloco `ships`, nave `cruiser`, arma `rail`, campo `fireDelay`). "
           "Unidades mais comuns: px = pixels, s = segundos, rad = radianos (6,28 = uma volta inteira).", "",
           "## Áreas", ""]
    for area, l in tabelas:
        out.append(f"- [{AREAS.get(area, area)}](#{area}) ({len(l)})")
    for area, l in tabelas:
        out += ["", f'<a id="{area}"></a>', f"## {AREAS.get(area, area)}", "", "| caminho | valor | o que faz |", "|---|---|---|"]
        for cam, valor, exp in l:
            out.append(f"| `{cam}` | `{valor.replace('|', '/')}` | {exp} |")
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    sem = sum(1 for _, l in tabelas for x in l if not x[2])
    print(f"{SAIDA}: {total} parâmetros, {sem} sem explicação")
    if "--sem-explicacao" in sys.argv:
        for _, l in tabelas:
            for cam, valor, exp in l:
                if not exp:
                    print("  ", cam, valor)


if __name__ == "__main__":
    # o console do Windows não é UTF-8 por padrão; sem isto, emoji e acento derrubam o print
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
