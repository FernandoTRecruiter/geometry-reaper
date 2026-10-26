# -*- coding: utf-8 -*-
"""
testa_jogo.py: abre o jogo num navegador sem janela, joga um pouco e confere os bugs corrigidos.

Por que existe: mudar um número no TWEAKS pode quebrar o jogo sem aviso.
Este teste responde em 1 minuto: "o jogo abre? roda sem erro? os bugs
que já corrigimos continuam corrigidos?". E tira as fotos das telas principais.

Uso:
  python ferramentas/testa_jogo.py                     # testa o index.html e grava fotos em docs/
  python ferramentas/testa_jogo.py --arquivo velho.html --sem-fotos   # roda as checagens em outra versão

Saída: uma linha por checagem (OK / FALHOU) e a lista de erros de JavaScript.
"""
import argparse, os, sys, time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from navegador import Navegador, url_de

RAIZ = os.path.dirname(AQUI)

# Cada checagem é um trecho de JavaScript que devolve [passou?, detalhe].
# Todas começam com newRun(): uma run limpa, sem depender da anterior.
CHECAGENS = [
    ("Carta LIMPAR poupa o goblin",
     """newRun(null); G.ship='fighter'; recalcStats(); G.enemies.length=0; spawnBurst(8); spawnGoblin();
        const gob=G.goblinRef; clearAllEnemies();
        const vivos=G.enemies.filter(e=>!e.dead&&e.type!=='goblin').length;
        [!gob.dead && vivos===0 && G.pendingPicks.length===0, 'goblin vivo='+!gob.dead+', horda viva='+vivos+', cartas ganhas='+G.pendingPicks.length]"""),
    ("Cruiser: Rate of Fire trava no teto do railgun (sem carta morta)",
     """newRun(null); G.ship='cruiser'; recalcStats(); const n=TWEAKS.ships.cruiser.rail.rofLevelsToFloor;
        for(let i=0;i<n+3;i++) applyAttr('rof');
        [G.attrs.rof===n && attrMaxed('rof'), 'pontos em rof depois de '+(n+3)+' tentativas: '+G.attrs.rof+' (teto '+n+')']"""),
    ("Pausa funciona com atributo exclusivo (Manobrabilidade)",
     """newRun(null); G.ship='thunderbolt'; recalcStats(); G.attrs.turn=2; state='game';
        let erro=''; try{ setPause(true); }catch(e){ erro=String(e); }
        const txt=document.getElementById('pauseStats').textContent; setPause(false); state='menu';
        [!erro && txt.includes('Manobrabilidade'), erro||txt.slice(0,80)]"""),
    ("Texto do ADRENALINE bate com o TWEAKS",
     """newRun(null); const t=reelFinalFace('adrenaline');
        [!t.includes('+50') && t.includes(TWEAKS.slot.adrenaline.rofMul+'x'), t.replace(/<[^>]+>/g,' ').replace(/\\s+/g,' ').slice(0,140)]"""),
    ("Dragão: uma explosão conta UMA vez, mesmo pegando vários elos",
     """newRun(null); G.ship='fighter'; recalcStats(); G.p.critA=0; spawnDragon(); G.pendingPicks.length=0;
        const D=G.dragon, s=D.segs[10], hp0=D.hp;
        let elos=0; for(const e of D.segs) if(Math.hypot(e.x-s.x,e.y-s.y)<200) elos++;
        buildGrid(); explode(s.x,s.y,200,100,'#fff'); // a grade espacial precisa conhecer os elos recém-criados
        const perdeu=hp0-D.hp, teto=100*TWEAKS.dragon.headDmgMul*G.p.dmgMul+0.01;
        [perdeu>0 && perdeu<=teto, 'elos no raio='+elos+', vida perdida='+Math.round(perdeu)+' (teto de um golpe='+Math.round(teto)+')']"""),
    ("Projétil perfurante acerta cada inimigo uma vez só",
     """newRun(null); G.ship='cruiser'; recalcStats(); G.p.critA=0; G.enemies.length=0; G.noSpawn=true;
        spawnEnemy('zombie'); const e=G.enemies[0]; e.r=46; e.x=G.p.x+200; e.y=G.p.y; e.hp=e.maxHp=1e6; e.spd=0;
        G.bullets.push({x:G.p.x+20,y:G.p.y,vx:1400,vy:0,dmg:50,size:6,col:'#fff',pierce:999,t:0,life:2,boom:0,rail:true});
        for(let i=0;i<40;i++){ e.stun=9; G.p.invuln=9; update(1/60); }
        const dano=Math.round(1e6-e.hp); [dano===50, 'dano de um tiro de 50 num alvo grande: '+dano]"""),
    ("Flip do Thunderbolt desliza igual a 60 Hz e a 144 Hz",
     """const desl=(hz)=>{ newRun(null); G.ship='thunderbolt'; recalcStats(); state='game'; G.enemies.length=0; G.noSpawn=true;
          G.p.heading=0; G.p.throttle=0.0001; mouse.x=W; mouse.y=H/2; /* mouse à direita: o avião segue reto */ const x0=G.p.x, y0=G.p.y; doFlip(1);
          const n=Math.round(TWEAKS.ships.thunderbolt.flip.immunitySec*hz); let lat=0;
          for(let i=0;i<n;i++){ const y=G.p.y; G.p.invuln=9; update(1/hz); lat+=G.p.y-y; }
          state='menu'; return lat; };
        const a=desl(60), b=desl(144), d=Math.abs(a-b)/Math.max(1,Math.abs(a));
        [d<0.08, 'deslize lateral 60 Hz='+a.toFixed(0)+' px, 144 Hz='+b.toFixed(0)+' px (diferença '+(d*100).toFixed(1)+'%)']"""),
    ("Vidas no HUD seguem TWEAKS.player.lives",
     """[String(drawHUD).includes('TWEAKS.player.lives'), 'drawHUD lê TWEAKS.player.lives']"""),
    ("Zoom do Salvo não esconde quem está na borda",
     """newRun(null); G.zoom=0.6; const visivel=!foraDaTela(W+150,H/2,40); G.zoom=1; const fora=foraDaTela(W+150,H/2,40);
        [visivel && fora, 'ponto 150 px além da borda: com zoom 0,6 desenha='+visivel+', sem zoom desenha='+!fora]"""),
    ("Roteiro do Desafio vem do TWEAKS",
     """const ant=TWEAKS.desafio.wardenAtSec; TWEAKS.desafio.wardenAtSec=2;
        newRun({id:'fivemin',n:'Desafio',timeLimit:300,fiveMin:true}); G.ship='fighter'; recalcStats(); state='game';
        for(let i=0;i<200;i++){ G.p.invuln=9; update(1/60); if(state!=='game'){ G.pendingPicks.length=0; state='game'; } }
        state='menu'; TWEAKS.desafio.wardenAtSec=ant;
        [bossCount()===1, 'wardens aos 3,3 s com wardenAtSec=2: '+bossCount()]"""),
    ("Tabela de spawn vem do TWEAKS",
     """const ant=TWEAKS.difficulty.spawnTable; TWEAKS.difficulty.spawnTable=[[0,'jetdrone']];
        newRun(null); const tipos=allowedTypes(); TWEAKS.difficulty.spawnTable=ant;
        [tipos.length===1&&tipos[0]==='jetdrone', JSON.stringify(tipos)]"""),
    ("Manual usa os números do TWEAKS",
     """const ant=TWEAKS.player.lives; TWEAKS.player.lives=7; const h=manualPages().map(p=>p.html).join(' ');
        TWEAKS.player.lives=ant; [h.includes('7 vidas') && h.includes(TWEAKS.mobs.goblin.fleeTimerSec+' segundos'), 'manual com lives=7 diz "7 vidas": '+h.includes('7 vidas')]"""),
]


def centro(nav, seletor):
    # Centro de um elemento na tela, para clicar "de verdade" com o mouse.
    r = nav.js(f"(()=>{{const e=document.querySelector({seletor!r}); if(!e) return null; const b=e.getBoundingClientRect(); return [b.x+b.width/2, b.y+b.height/2];}})()")
    return r


def roda(arquivo, fotos=True):
    pasta = os.path.join(RAIZ, "docs")
    resultados, erros = [], []
    with Navegador(1280, 720) as nav:
        nav.ir(url_de(arquivo), 2.5)
        # 1) menu abre sem erro
        resultados.append(("Menu abre sem erro de JavaScript", not nav.erros(), f"{len(nav.erros())} erro(s)"))
        if fotos:
            nav.foto(os.path.join(pasta, "menu.png"))
        # 2) jogar de verdade: clicar Survival, escolher a nave, a carta inicial e andar
        nav.clicar(*centro(nav, "#btnSurvival")); nav.esperar(0.8)
        if fotos:
            nav.foto(os.path.join(pasta, "naves.png"))
        nav.clicar(*centro(nav, "#shipGrid .ship-card")); nav.esperar(0.6)
        nav.clicar(*centro(nav, "#startCards .card")); nav.esperar(0.3)
        nav.js("dispatchEvent(new KeyboardEvent('keydown',{code:'KeyD',key:'d'}))")
        nav.js("dispatchEvent(new KeyboardEvent('keydown',{code:'KeyW',key:'w'}))")
        nav.esperar(2.0)
        nav.js("dispatchEvent(new KeyboardEvent('keyup',{code:'KeyD',key:'d'}))")
        nav.js("dispatchEvent(new KeyboardEvent('keyup',{code:'KeyW',key:'w'}))")
        nav.esperar(3.0)
        t = nav.js("G?G.t:0")
        resultados.append(("Run de verdade roda (cliques e teclas)", nav.js("state") in ("game", "slot", "attrpick") and t > 3,
                           f"estado={nav.js('state')}, tempo de jogo={t:.1f}s, abates={nav.js('G.kills')}"))
        if fotos:
            nav.js("document.querySelectorAll('.toast').forEach(t=>t.remove())")
            nav.foto(os.path.join(pasta, "jogo.png"))
        # 3) checagens dos bugs corrigidos (cada uma isolada)
        for nome, js in CHECAGENS:
            try:
                ok, det = nav.js("(()=>{ " + js_ultimo_valor(js) + " })()")
                resultados.append((nome, bool(ok), det))
            except Exception as ex:
                resultados.append((nome, False, str(ex)[:200]))
        # 4) fotos das telas especiais
        if fotos:
            nav.js("document.querySelectorAll('.toast').forEach(t=>t.remove())")
            nav.js("""(()=>{ newRun(null); chosenShip='fighter'; G.ship='fighter'; beginRun(); G.p.lvl=8;
                       G.pendingPicks.push('power'); openPick(); })()"""); nav.esperar(1.0)
            nav.foto(os.path.join(pasta, "slot.png"))
            nav.js("""(()=>{ document.getElementById('slot').classList.add('hidden'); cleanupLever();
                       newRun(null); chosenShip='fighter'; G.ship='fighter'; beginRun();
                       G.attrs.rof=4; G.attrs.dmg=4; recalcStats(); G.passives.multishot=2; G.p.lvl=20;
                       spawnDragon(); G.pendingPicks.length=0; G.p.invuln=999; })()"""); nav.esperar(4.0)
            nav.js("document.querySelectorAll('.toast').forEach(t=>t.remove())")
            nav.foto(os.path.join(pasta, "dragao.png"))
            nav.js("""(()=>{ newRun(null); chosenShip='thunderbolt'; G.ship='thunderbolt'; beginRun(); G.t=240;
                       spawnBurst(60); G.p.invuln=999; doSalvo(); mouse.l=true; })()"""); nav.esperar(3.2)
            nav.js("document.querySelectorAll('.toast').forEach(t=>t.remove())")
            nav.foto(os.path.join(pasta, "salvo.png"))
            nav.js("mouse.l=false")
        erros = nav.erros()
    return resultados, erros


def js_ultimo_valor(js):
    # As checagens terminam num array [ok, detalhe]; aqui viram "return [ok, detalhe]".
    corpo = js.strip()
    i = corpo.rfind("[")
    # acha o último "[" que começa uma instrução (depois de ";" ou no começo)
    while i >= 0:
        antes = corpo[:i].rstrip()
        if antes == "" or antes.endswith(";") or antes.endswith("}"):
            return corpo[:i] + " return " + corpo[i:]
        i = corpo.rfind("[", 0, i)
    return "return " + corpo


if __name__ == "__main__":
    # o console do Windows não é UTF-8 por padrão; sem isto, emoji e acento derrubam o print
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", default=os.path.join(RAIZ, "index.html"))
    ap.add_argument("--sem-fotos", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    res, erros = roda(a.arquivo, not a.sem_fotos)
    falhas = 0
    for nome, ok, det in res:
        falhas += 0 if ok else 1
        print(f"[{'OK' if ok else 'FALHOU'}] {nome}: {det}")
    print(f"\nerros de JavaScript na sessão inteira: {len(erros)}")
    for e in erros[:15]:
        print("   ", e)
    print(f"{len(res) - falhas}/{len(res)} checagens passaram ({round(time.time() - t0)}s)")
    sys.exit(1 if falhas or erros else 0)
