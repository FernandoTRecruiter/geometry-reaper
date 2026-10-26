# Changelog

## 1.2 (22/10/2026): auditoria de bugs e balanceamento

Tudo medido com `ferramentas/simula_balanceamento.py` (robô que joga acelerado no navegador) e conferido com `ferramentas/testa_jogo.py`. A versão anterior falha em 12 das 14 checagens do teste; esta passa nas 14.

### Bugs corrigidos

| # | O que acontecia | O que mudou | Como foi conferido |
|---|---|---|---|
| 1 | A carta **LIMPAR** da alavanca prometia "menos goblin e warden", mas matava o goblin e dava carta extra e 14 chips de graça. | O goblin é poupado, junto com warden e dragão. | Teste: goblin vivo, horda morta, 0 cartas ganhas (antes: goblin morto, 1 carta). |
| 2 | **Cruiser:** o Rate of Fire para de melhorar no nível 8 (`rail.rofLevelsToFloor`), mas o jogo seguia oferecendo o atributo: do 9º ponto em diante era carta morta. | O atributo trava no teto (some das escolhas e da roleta) e a descrição mostra o teto. | Teste: 11 tentativas resultam em 8 pontos (antes: 11). |
| 3 | **Pausa** quebrava com erro de JavaScript se o Thunderbolt tivesse a Manobrabilidade (atributo exclusivo dele). | A tela de pausa usa o nome do atributo da nave. | Teste: pausa abre e mostra "Manobrabilidade +2" (antes: `TypeError`). |
| 4 | **Dragão:** os 28 elos dividem uma vida só, mas cada elo atingido contava dano separado. Uma explosão que pegava 11 elos tirava 6x o dano; um tiro que atravessava o corpo contava em cada elo. | Cada golpe (tiro, explosão, pulso, tique do laser) conta **uma vez** no dragão, pelo maior dano entre os elos atingidos (acertar a cabeça ainda vale 1,4x). | Teste: explosão de 100 em 11 elos tira 100 (antes: 624). |
| 5 | **Projétil perfurante** (railgun, Tiros Perfurantes, míssil) acertava o mesmo inimigo em todo quadro em que ainda estava dentro dele: o railgun batia 4x no warden e 2x num zumbi, e o dano mudava com a taxa de quadros do monitor. | Cada projétil acerta cada inimigo uma vez. | Teste: tiro de 50 num alvo grande causa 50 (antes: 200). |
| 6 | **Flip do Thunderbolt** freava 10% por quadro: num monitor de 144 Hz deslizava menos da metade do que num de 60 Hz. | O freio é por segundo (`flip.slideDecayPerSec`). | Teste: diferença 60 Hz x 144 Hz de 2,9% (antes: 56,6%). |
| 7 | **Zoom do Salvo** mostra mais arena, mas o jogo só desenhava o que cabia na tela sem zoom: inimigos e chips da borda sumiam e a grade do chão não cobria tudo. | O recorte e a grade acompanham o zoom. | Teste do recorte + foto `docs/salvo.png`. |
| 8 | **HUD do Thunderbolt:** o nome e a barra do warden saíam por cima da barra de calor do canhão. | As barras de chefe sobem quando a nave tem barra de calor. | Foto `docs/salvo.png`. |
| 9 | **HUD:** as bolinhas de vida eram sempre 3, mesmo mudando `player.lives`. | Seguem o TWEAKS. | Teste (o HUD lê `TWEAKS.player.lives`). |
| 10 | **Textos que mentiam:** ADRENALINE dizia "+50 em todos os atributos" (o real é 1,6x velocidade, 2,2x cadência, 2,2x dano, metade do cooldown, +80% de crítico); a descrição do Cruiser e o manual falavam de "tiro vermelho de dobro de dano" (a carga cheia virou canhão laser); o manual tinha números fixos (3 vidas, flip de 2,4 s, goblin em 20 s, storm a cada 80 a 110 s, "atributos sem limite"); passiva nova aparecia como "Nível 0 → 1". | Os textos saem do TWEAKS ou foram corrigidos. | Teste: com `lives=7` o manual diz "7 vidas"; texto do ADRENALINE confere com o TWEAKS. |
| 11 | A vida do goblin estimava o dano do Cruiser como 1,5x o tiro (carga parcial), mas o melhor uso contra alvo único é o toque sem carga. | A estimativa usa dano / recarga. | Simulação: goblin do Cruiser morre em 10 a 12 s parado (Fighter: 7 a 9 s). |

### Balanceamento aplicado

| Parâmetro | Antes | Depois | Por quê |
|---|---|---|---|
| `dragon.hp` | 60000 | 30000 | Com o bug 4 corrigido a luta ficou ~3x mais longa (build típica Nv20 com cartas: Fighter de 29 s para 89 s de robô). 30000 deixa em 45 s: um pouco mais longa que antes, sem virar maratona. |
| `ships.cruiser.rail.damage` | 34 | 68 | Com o bug 5 corrigido cada tiro acerta uma vez em vez de ~2 nos inimigos comuns; dobrar o dano mantém o Cruiser limpando a horda como antes. |
| `ships.cruiser.rail.beamDmgMul` | 6 | 3 | O laser não tinha o bug; 3 x 68 = 204 de dano/s, o mesmo de antes. |

### Customização: números que saíram do motor e foram para o TWEAKS

Cada um com comentário explicando o que faz e a unidade. Total: 668 parâmetros, todos com explicação em `docs/parametros.md`.

- `difficulty.spawnTable` (quais inimigos nascem e a partir de que minuto), `startBurst`, `firstSpawnSec`, `spawnDistMul`
- `desafio.*`: o roteiro inteiro do modo Desafio (goblins, storm, asteroides, warden, sobrecarga, EMP, entrada do dragão)
- `stats.critDmgBase`, `stats.critDmgPerChance` (multiplicador do crítico)
- `powerups.missileFlight.lifeSec`, `pierceFrac`, `spinTurnRate`, `napalmDmg`, `napalmRadius`, `napalmSec`, `salvoSpreadPx`
- `powerups.zuni.lifeSec`, `powerups.emp.shockSec`, `passives.trophy.blastDmg` e `blastRadius`
- `passives.toxic.puffEverySec`, `passives.aura.pulseMinSec`
- `mobs.ninja.dashSec`, `dashEveryMinSec`, `dashEveryMaxSec`, `dashMinDist`, `dashMaxDist`, `invisSec`
- `mobs.gangG` e `mobs.drone`: `keepDist`, `shootMinSec`, `shootMaxSec`; `engine.enemyBulletRange`
- `mobs.jetdrone.fireMinDist`, `fireMaxDist`, `rocketBlastRadius`, `rocketSplashFrac`; `mobs.toxwalker.fastSpdMul`
- `mobs.warden.deathBlastRadius` e `deathBlastDmg`; `player.deathBlastRadius` e `deathBlastDmg`; `engine.explosionKnockback`
- `events.astSpeedMin`, `astSpeedMax`, `astRadiusMin`, `astRadiusMax`; `ships.thunderbolt.flip.slideDecayPerSec`

### Outros

- Versão exibida no menu: BETA 1.1 para BETA 1.2.
- Sem o caractere travessão nos textos do jogo (troca por dois-pontos).
- Ferramentas novas em `ferramentas/`: `gera_parametros.py`, `testa_jogo.py`, `simula_balanceamento.py`, `simulador.js`, `navegador.py`.
