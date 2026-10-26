# -*- coding: utf-8 -*-
"""
simula_balanceamento.py: mede o balanceamento rodando o jogo de verdade, acelerado.

Por que existe: "essa nave está forte demais?" vira número. O script abre o
index.html num navegador sem janela, injeta o robô (simulador.js) e mede:
  1. TTK (tempo para matar) de cada nave contra warden, goblin e dragão,
     com builds típicas por nível;
  2. uma run de sobrevivência por nave (nível por minuto, inimigos vivos,
     dano que um jogador parado levaria), para ver a curva de dificuldade.

Uso:
  python ferramentas/simula_balanceamento.py                 # mede o index.html
  python ferramentas/simula_balanceamento.py --arquivo X.html --saida resultado.json
  python ferramentas/simula_balanceamento.py --rapido        # só os TTKs

Os números variam um pouco entre rodadas (o jogo tem sorteio). Compare
tendências e ordens de grandeza, não a casa decimal.
"""
import argparse, json, os, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from navegador import Navegador, url_de

NAVES = ["fighter", "warrior", "cruiser", "thunderbolt"]
ORDEM = ["rof", "dmg", "rof", "dmg", "crit"]  # build ofensiva: cadência e dano, um pouco de crítico


def pontos_de_atributo(nivel, carta_a_cada=4):
    # Por quê: a cada nível ganha-se 1 ponto, MENOS nos níveis de carta (múltiplos de 4).
    return (nivel - 1) - nivel // carta_a_cada


def build(nivel, com_cartas=False):
    # Distribui os pontos na ordem ORDEM; com_cartas soma um pacote típico de habilidades.
    attrs = {}
    for i in range(pontos_de_atributo(nivel)):
        k = ORDEM[i % len(ORDEM)]
        attrs[k] = attrs.get(k, 0) + 1
    b = {"nivel": nivel, "attrs": attrs}
    if com_cartas:
        b["ativas"] = [["jdam", 2], ["missile", 2], ["zuni", 2]]
        b["passivas"] = {"multishot": 2, "pierce": 1, "boomammo": 2}
    return b


# Cenários: (rótulo, alvo, nível do jogador, minuto da run, com cartas?)
CENARIOS = [
    ("goblin Nv5 (1 min)", "goblin", 5, 1, False),
    ("goblin Nv10 (2,5 min)", "goblin", 10, 2.5, False),
    ("goblin Nv20 (6 min)", "goblin", 20, 6, False),
    ("warden Nv15 (4 min)", "warden", 15, 4, False),
    ("warden Nv25 (8 min)", "warden", 25, 8, False),
    ("dragão Nv20 só arma", "dragao", 20, 6, False),
    ("dragão Nv20 com cartas", "dragao", 20, 6, True),
]


def roda(arquivo, rapido=False, repeticoes=2):
    sim = open(os.path.join(AQUI, "simulador.js"), encoding="utf-8").read()
    out = {"arquivo": os.path.basename(arquivo), "ttk": [], "sobrevivencia": []}
    with Navegador(1280, 720) as nav:
        nav.ir(url_de(arquivo), 2.0)
        nav.js(sim)
        for rot, alvo, nv, minuto, cartas in CENARIOS:
            for nave in NAVES:
                estilos = ["toque", "laser"] if nave == "cruiser" else [None]
                for est in estilos:
                    res = []
                    for _ in range(repeticoes):
                        opc = {"minuto": minuto, "estilo": est, "habilidades": cartas,
                               "limite": 90, "janela": 30}
                        r = nav.js(f"JSON.stringify(SIM.ttk({json.dumps(nave)},{json.dumps(build(nv, cartas))},{json.dumps(alvo)},{json.dumps(opc)}))")
                        res.append(json.loads(r))
                    # média das repetições (None = não matou dentro do limite)
                    ttks = [x["ttk"] for x in res]
                    ttk = None if any(t is None for t in ttks) else round(sum(ttks) / len(ttks), 1)
                    out["ttk"].append({"cenario": rot, "nave": nave + (f" ({est})" if est else ""),
                                       "vida": res[0]["vida"], "dps": round(sum(x["dps"] for x in res) / len(res)),
                                       "ttk": ttk})
        if not rapido:
            for nave in NAVES:
                r = nav.js(f"JSON.stringify(SIM.sobrevive({json.dumps(nave)}, 12))")
                out["sobrevivencia"].append(json.loads(r))
            for nave in NAVES:
                r = nav.js(f"JSON.stringify(SIM.sobrevive({json.dumps(nave)}, 9, {{desafio:true}}))")
                d = json.loads(r); d["modo"] = "desafio"
                out["sobrevivencia"].append(d)
        out["erros_js"] = nav.erros()
    return out


def imprime(out):
    print(f"\n## TTK (segundos para matar) | {out['arquivo']}\n")
    print("| cenário | nave | vida do alvo | dano/s | TTK |")
    print("|---|---|---:|---:|---:|")
    for x in out["ttk"]:
        print(f"| {x['cenario']} | {x['nave']} | {x['vida']} | {x['dps']} | {x['ttk'] if x['ttk'] is not None else 'não matou em 90s'} |")
    for s in out["sobrevivencia"]:
        modo = s.get("modo", "survival")
        print(f"\n### robô {s['nave']} ({modo}): nível final {s['nivel_final']}, mortes por asteroide {s['mortes_asteroide']}, "
              f"dragão apareceu {s['dragao_apareceu_seg']}s e morreu em {s['dragao_morreu_em_seg']}s, venceu {s['venceu']}")
        print("min | nível | inimigos vivos | dano/min (parado) | cartas")
        for l in s["linhas"]:
            print(f"{l['min']} | {l['nivel']} | {l['inimigos']} | {l['dano_recebido']} | {l['cartas']}")
    print("\nerros de JS:", out["erros_js"] or "nenhum")


if __name__ == "__main__":
    # o console do Windows não é UTF-8 por padrão; sem isto, emoji e acento derrubam o print
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", default=os.path.join(AQUI, "..", "index.html"))
    ap.add_argument("--saida", default=None)
    ap.add_argument("--rapido", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    res = roda(a.arquivo, a.rapido)
    imprime(res)
    if a.saida:
        with open(a.saida, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
    print(f"\n({round(time.time() - t0)}s)")
