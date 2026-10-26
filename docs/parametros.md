# Parâmetros do jogo (TWEAKS)

Gerado por `python ferramentas/gera_parametros.py` a partir do bloco `TWEAKS` do `index.html`. Não edite este arquivo: mude o valor no `index.html` e rode o script de novo.

**668 parâmetros** em 20 áreas. Como ler: o **caminho** é onde o número mora dentro do `TWEAKS` (`ships.cruiser.rail.fireDelay` = bloco `ships`, nave `cruiser`, arma `rail`, campo `fireDelay`). Unidades mais comuns: px = pixels, s = segundos, rad = radianos (6,28 = uma volta inteira).

## Áreas

- [Mundo](#world) (1)
- [Jogador](#player) (14)
- [Blaster (arma do Fighter)](#blaster) (6)
- [Habilidades ativas](#powerups) (105)
- [Passivas](#passives) (52)
- [Atributos (ganho por ponto)](#stats) (10)
- [Inimigos](#mobs) (141)
- [Motor (ajustes finos)](#engine) (26)
- [Dificuldade e spawner](#difficulty) (27)
- [Eventos do Survival](#events) (20)
- [Roteiro do modo Desafio](#desafio) (12)
- [Dragão](#dragon) (57)
- [Combo](#combo) (1)
- [Pontuação](#score) (3)
- [Alavanca (slot)](#slot) (15)
- [Roleta de atributos](#roulette) (10)
- [Naves](#ships) (144)
- [Progressão (XP e cartas)](#progression) (6)
- [Volumes](#audio) (3)
- [Música](#music) (15)

<a id="world"></a>
## Mundo

| caminho | valor | o que faz |
|---|---|---|
| `world.size` | `2600` | lado da arena em px (os pilares se reposicionam sozinhos) |

<a id="player"></a>
## Jogador

| caminho | valor | o que faz |
|---|---|---|
| `player.baseHp` | `100` | vida maxima inicial |
| `player.baseShield` | `50` | escudo maximo inicial (Energia soma stats.shieldFlat por nivel) |
| `player.baseSpeed` | `235` | velocidade base (Velocidade soma stats.speedPct por nivel) |
| `player.lives` | `3` | vidas por run |
| `player.shieldRegenDelaySec` | `3` | segundos sem tomar dano para o escudo comecar a regenerar |
| `player.shieldRegenPctPerSec` | `0.05` | escudo regenerado por segundo, em FRACAO do escudo maximo (0,05 = 5%: quanto mais Energia voce tem, mais rapido volta) |
| `player.invulnStartSec` | `2.5` | invulnerabilidade ao comecar a run |
| `player.invulnRespawnSec` | `5` | invulnerabilidade ao perder uma vida |
| `player.maxActives` | `5` | maximo de habilidades ativas (slots LMB/RMB/Q/E/R) |
| `player.magnetBaseRadius` | `90` | raio base de atracao de chips (sem a passiva Ima) |
| `player.chipPickupRadius` | `26` | raio de coleta do chip |
| `player.contactDmgMul` | `3.4` | multiplicador de dano de contato por segundo (inimigos comuns) |
| `player.deathBlastRadius` | `260` | ao perder uma vida, onda de choque que empurra e fere quem está perto (px) |
| `player.deathBlastDmg` | `80` | dano dessa onda de choque |

<a id="blaster"></a>
## Blaster (arma do Fighter)

| caminho | valor | o que faz |
|---|---|---|
| `blaster.damage` | `14` | dano por projetil (escala com atributo Dano) |
| `blaster.delay` | `0.30` | segundos entre tiros (reduzido pelo Rate of Fire) |
| `blaster.speed` | `820` | velocidade do projetil |
| `blaster.spread` | `0.05` | dispersao base (radianos) |
| `blaster.size` | `4` | tamanho visual/colisao do projetil |
| `blaster.life` | `1.1` | segundos de vida do projetil (define o alcance) |

<a id="powerups"></a>
## Habilidades ativas

| caminho | valor | o que faz |
|---|---|---|
| `powerups.missile.0.baseDamage` | `84` | dano base (escala com o atributo Dano) |
| `powerups.missile.0.areaOfEffect` | `78` | raio da explosão (px) |
| `powerups.missile.0.cooldown` | `14` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.missile.0.projectiles` | `1` | quantos projéteis dispara |
| `powerups.missile.1.baseDamage` | `84` | dano base (escala com o atributo Dano) |
| `powerups.missile.1.areaOfEffect` | `98` | raio da explosão (px) |
| `powerups.missile.1.cooldown` | `14` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.missile.1.projectiles` | `2` | quantos projéteis dispara |
| `powerups.missile.2.baseDamage` | `84` | dano base (escala com o atributo Dano) |
| `powerups.missile.2.areaOfEffect` | `118` | raio da explosão (px) |
| `powerups.missile.2.cooldown` | `14` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.missile.2.projectiles` | `3` | quantos projéteis dispara |
| `powerups.missile.3.baseDamage` | `84` | dano base (escala com o atributo Dano) |
| `powerups.missile.3.areaOfEffect` | `130` | raio da explosão (px) |
| `powerups.missile.3.cooldown` | `14` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.missile.3.projectiles` | `4` | quantos projéteis dispara |
| `powerups.missileFlight.launchSpeed` | `340` | voo do missil guiado (px/s, px/s, px/s², rad/s) |
| `powerups.missileFlight.maxSpeed` | `720` | voo do missil guiado (px/s, px/s, px/s², rad/s) |
| `powerups.missileFlight.accel` | `800` | voo do missil guiado (px/s, px/s, px/s², rad/s) |
| `powerups.missileFlight.turnRate` | `4` | voo do missil guiado (px/s, px/s, px/s², rad/s) |
| `powerups.missileFlight.lifeSec` | `5` | segundos de voo antes de explodir sozinho |
| `powerups.missileFlight.pierceFrac` | `0.4` | fracao do dano que ele causa em quem vara pelo caminho (0,4 = 40%) |
| `powerups.missileFlight.spinTurnRate` | `3` | Nv3: rad/s do rodopio antes de ir ao alvo |
| `powerups.missileFlight.napalmDmg` | `8` | Nv3: dano de cada pedaco do rastro de fogo, 8 vezes por segundo |
| `powerups.missileFlight.napalmRadius` | `16` | Nv3: largura (px) e duracao (s) do rastro de fogo |
| `powerups.missileFlight.napalmSec` | `5` | Nv3: largura (px) e duracao (s) do rastro de fogo |
| `powerups.missileFlight.salvoSpreadPx` | `70` | durante o Salvo do Thunderbolt: espalhamento dos misseis no chao (px) |
| `powerups.jdam.0.baseDamage` | `80` | dano base (escala com o atributo Dano) |
| `powerups.jdam.0.areaOfEffect` | `110` | raio da explosão (px) |
| `powerups.jdam.0.cooldown` | `13` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.jdam.0.flightTime` | `1.6` | segundos até a bomba cair |
| `powerups.jdam.1.baseDamage` | `80` | dano base (escala com o atributo Dano) |
| `powerups.jdam.1.areaOfEffect` | `145` | raio da explosão (px) |
| `powerups.jdam.1.cooldown` | `13` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.jdam.1.flightTime` | `1.5` | segundos até a bomba cair |
| `powerups.jdam.2.baseDamage` | `80` | dano base (escala com o atributo Dano) |
| `powerups.jdam.2.areaOfEffect` | `145` | raio da explosão (px) |
| `powerups.jdam.2.cooldown` | `13` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.jdam.2.flightTime` | `1.4` | segundos até a bomba cair |
| `powerups.jdam.2.clusterBombs` | `3` | bombinhas extras ao redor do impacto |
| `powerups.jdam.3.baseDamage` | `90` | Nv3 também incendeia a área |
| `powerups.jdam.3.areaOfEffect` | `170` | Nv3 também incendeia a área |
| `powerups.jdam.3.cooldown` | `13` | Nv3 também incendeia a área |
| `powerups.jdam.3.flightTime` | `1.3` | Nv3 também incendeia a área |
| `powerups.jdam.3.clusterBombs` | `4` | Nv3 também incendeia a área |
| `powerups.jdam.clusterDmgFrac` | `0.55` | bombinhas do cluster (fração da principal) |
| `powerups.jdam.clusterAoeFrac` | `0.6` | bombinhas do cluster (fração da principal) |
| `powerups.jdam.fireCount` | `7` | incêndio do Nv3 |
| `powerups.jdam.fireDurSec` | `4` | incêndio do Nv3 |
| `powerups.jdam.fireDps` | `8` | incêndio do Nv3 |
| `powerups.zuni.0.baseDamage` | `24` | dano base (escala com o atributo Dano) |
| `powerups.zuni.0.areaOfEffect` | `46` | raio da explosão (px) |
| `powerups.zuni.0.cooldown` | `30` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.zuni.0.projectiles` | `6` | quantos projéteis dispara |
| `powerups.zuni.0.fireDelay` | `0.0552` | segundos entre disparos |
| `powerups.zuni.0.coneRad` | `0.115` | abertura do leque (radianos) |
| `powerups.zuni.0.speed` | `720` | velocidade (px/s) |
| `powerups.zuni.1.baseDamage` | `24` | dano base (escala com o atributo Dano) |
| `powerups.zuni.1.areaOfEffect` | `46` | raio da explosão (px) |
| `powerups.zuni.1.cooldown` | `30` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.zuni.1.projectiles` | `10` | quantos projéteis dispara |
| `powerups.zuni.1.fireDelay` | `0.0552` | segundos entre disparos |
| `powerups.zuni.1.coneRad` | `0.115` | abertura do leque (radianos) |
| `powerups.zuni.1.speed` | `720` | velocidade (px/s) |
| `powerups.zuni.2.baseDamage` | `24` | dano base (escala com o atributo Dano) |
| `powerups.zuni.2.areaOfEffect` | `46` | raio da explosão (px) |
| `powerups.zuni.2.cooldown` | `30` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.zuni.2.projectiles` | `14` | quantos projéteis dispara |
| `powerups.zuni.2.fireDelay` | `0.0552` | segundos entre disparos |
| `powerups.zuni.2.coneRad` | `0.115` | abertura do leque (radianos) |
| `powerups.zuni.2.speed` | `720` | velocidade (px/s) |
| `powerups.zuni.3.baseDamage` | `24` | dano base (escala com o atributo Dano) |
| `powerups.zuni.3.areaOfEffect` | `46` | raio da explosão (px) |
| `powerups.zuni.3.cooldown` | `30` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.zuni.3.projectiles` | `18` | quantos projéteis dispara |
| `powerups.zuni.3.fireDelay` | `0.0552` | segundos entre disparos |
| `powerups.zuni.3.coneRad` | `0.115` | abertura do leque (radianos) |
| `powerups.zuni.3.speed` | `720` | velocidade (px/s) |
| `powerups.zuni.lifeSec` | `1.1` | segundos de voo de cada mini-foguete (define o alcance: 720 x 1,1 = ~790 px) |
| `powerups.emp.cooldown` | `41` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.emp.sweepRadius` | `900` | alcance do pulso (px): atordoa e apaga balas inimigas nesse raio |
| `powerups.emp.stunBase` | `2` | atordoamento (seg) em inimigos comuns |
| `powerups.emp.stunPerLevel` | `0.6` | atordoamento (seg) em inimigos comuns |
| `powerups.emp.shockSec` | `3` | Nv3: segundos de eletrocucao (dano em tiques, ver engine.shockDps) |
| `powerups.emp.bossStunSec` | `0.6` | atordoamento no warden |
| `powerups.emp.jetDmgBase` | `20` | dano nos jatos (nao os destroi) |
| `powerups.emp.jetDmgPerLevel` | `10` | dano nos jatos (nao os destroi) |
| `powerups.dash.cooldown` | `10` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.dash.guardDuration` | `2` | duracao do Dash Guard (imunidade toxina/meteoro + reducao de dano) |
| `powerups.dash.damageReduction` | `0.40` | fracao do dano reduzida durante o guard (0.40 = -40%) |
| `powerups.dash.speed` | `900` | velocidade do avanco |
| `powerups.dash.durationSec` | `0.20` | duracao do avanco |
| `powerups.dash.durationLv2Sec` | `0.26` | duracao no Nv2+ ("dash mais longo") |
| `powerups.dash.stunLv3Sec` | `1` | Nv3: atordoa quem voce atravessa por N segundos |
| `powerups.blackhole.baseDamage` | `7` | dano base (escala com o atributo Dano) |
| `powerups.blackhole.cooldown` | `58` | recarga em segundos (encurtada pelo Rate of Spell) |
| `powerups.blackhole.radiusBase` | `190` | raio de succao |
| `powerups.blackhole.radiusPerLevel` | `34` | raio de succao |
| `powerups.blackhole.durationSec` | `5.6` | segundos que o buraco fica aberto sugando |
| `powerups.blackhole.pullPerLevel` | `0.5` | forca extra de puxao por nivel (1 + lvl*este) |
| `powerups.blackhole.projectileSpeed` | `640` | [agora e um PROJETIL: sai na direcao da mira e so abre o buraco ao chegar] |
| `powerups.blackhole.maxRange` | `900` | se voce mirar mais longe que isso, ele arma nesse limite |
| `powerups.blackhole.collapseSec` | `0.5` | [COLAPSO: animacao de transicao quando o buraco acaba (implode e estoura)] |
| `powerups.blackhole.collapseDamage` | `60` | [COLAPSO: animacao de transicao quando o buraco acaba (implode e estoura)] |
| `powerups.blackhole.collapseRadiusMul` | `1.1` | [COLAPSO: animacao de transicao quando o buraco acaba (implode e estoura)] |

<a id="passives"></a>
## Passivas

| caminho | valor | o que faz |
|---|---|---|
| `passives.toxic.baseDamage` | `2.8` | dano base (escala com o atributo Dano) |
| `passives.toxic.durBaseSec` | `2` | duracao do fogo no chao |
| `passives.toxic.durPerLevelSec` | `0.9` | duracao do fogo no chao |
| `passives.toxic.radiusBase` | `28` | largura do rastro |
| `passives.toxic.radiusPerLevel` | `7` | largura do rastro |
| `passives.toxic.burnDps` | `4` | queimadura aplicada no Nv3 |
| `passives.toxic.burnSec` | `2` | queimadura aplicada no Nv3 |
| `passives.toxic.puffEverySec` | `0.1` | a cada quantos segundos solta um pedaco de fogo no chao (cada pedaco fere 8 vezes por segundo quem estiver nele) |
| `passives.aura.baseDamage` | `4` | dano base (escala com o atributo Dano) |
| `passives.aura.perLevel` | `4` | ganho por nível |
| `passives.aura.radiusBase` | `70` | raio no nível 1 (px) |
| `passives.aura.radiusPerLevel` | `22` | raio extra por nível (px) |
| `passives.aura.pulseBaseSec` | `0.55` | intervalo entre pulsos (menor = mais rapido) |
| `passives.aura.pulsePerLevelSec` | `0.04` | intervalo entre pulsos (menor = mais rapido) |
| `passives.aura.pulseMinSec` | `0.25` | piso do intervalo por nivel (o Rate of Spell ainda encurta depois) |
| `passives.aura.maxHitsBase` | `3` | alvos atingidos por pulso |
| `passives.aura.maxHitsPerLevel` | `2` | alvos atingidos por pulso |
| `passives.aura.dischargeChance` | `0.15` | descarga em area no Nv3 |
| `passives.aura.dischargeRadius` | `46` | descarga em area no Nv3 |
| `passives.aura.dischargeDamage` | `8` | descarga em area no Nv3 |
| `passives.chain.baseDamage` | `7` | dano base (escala com o atributo Dano) |
| `passives.chain.perLevel` | `5` | ganho por nível |
| `passives.chain.chanceBase` | `0.10` | chance de disparar por acerto |
| `passives.chain.chancePerLevel` | `0.06` | chance de disparar por acerto |
| `passives.chain.jumpsBase` | `2` | saltos = jumpsBase + nivel |
| `passives.chain.range` | `210` | alcance de cada salto |
| `passives.chain.stunLv3Sec` | `0.5` | Nv3: atordoa o ultimo alvo |
| `passives.pierce.perLevel` | `1` | inimigos extras atravessados por nivel |
| `passives.boomammo.radiusBase` | `18` | raio no nível 1 (px) |
| `passives.boomammo.radiusPerLevel` | `6` | raio extra por nível (px) |
| `passives.boomammo.dmgBase` | `3` | dano no nível 1 |
| `passives.boomammo.dmgPerLevel` | `2` | dano extra por nível |
| `passives.boomammo.knockback` | `220` | empurrão (px/s) |
| `passives.boomammo.burnDps` | `4` | queimadura aplicada no Nv3 |
| `passives.boomammo.burnSec` | `1.5` | queimadura aplicada no Nv3 |
| `passives.wingman.dmgFrac` | `[0,0.5,0.5,0.5]` | fracao do SEU dano (fixa em 50% em todos os niveis) |
| `passives.wingman.rofFrac` | `[0,0.5,0.75,1]` | fracao da SUA cadencia por nivel: 50% -> 75% -> 100% |
| `passives.wingman.drones` | `[0,1,2,2]` | quantos drones por nivel (2o drone no Nv2) |
| `passives.wingman.inheritAtLevel` | `3` | a partir deste nivel herda Tiros Perfurantes e Disparo Multiplo |
| `passives.wingman.orbitDist` | `52` | distancia do drone ate voce |
| `passives.wingman.range` | `520` | raio de busca de alvos |
| `passives.wingman.retargetSec` | `0.4` | frequencia de re-escolha de alvo quando sem alvo |
| `passives.wingman.bulletSpeed` | `760` | (Drone de Apoio: segue voce e cobre o lado oposto da sua mira) |
| `passives.multishot.shots` | `[1,2,3,4]` | total de projeteis do blaster (indice = nivel da passiva) |
| `passives.magnet.radiusPerLevel` | `120` | raio = player.magnetBaseRadius + nivel*este (Nv3 = global) |
| `passives.trophy.charges` | `[10,20,30]` | cargas por nivel (Nv1, Nv2, Nv3): cada interceptacao gasta carga |
| `passives.trophy.missileCost` | `2` | um foguete custa 2 cargas |
| `passives.trophy.normalRadius` | `55` | balas comuns: raio FIXO bem curto (nao escala) |
| `passives.trophy.missileRadius` | `[130,180,230]` | foguetes: raio por nivel (so eles escalam) |
| `passives.trophy.rechargeSec` | `10` | segundos para recarregar UMA carga (encurta com o Rate of Spell) |
| `passives.trophy.blastDmg` | `30` | Nv3: cada interceptacao explode e fere inimigos nesse raio (dano, px) |
| `passives.trophy.blastRadius` | `70` | Nv3: cada interceptacao explode e fere inimigos nesse raio (dano, px) |

<a id="stats"></a>
## Atributos (ganho por ponto)

| caminho | valor | o que faz |
|---|---|---|
| `stats.speedPct` | `0.10` | +% de velocidade por ponto de atributo |
| `stats.rofPct` | `0.42` | +% de cadência por ponto de atributo |
| `stats.damagePct` | `0.18` | +% de dano por ponto de atributo |
| `stats.shieldFlat` | `26` | + escudo máximo por ponto de atributo |
| `stats.cooldownPct` | `0.08` | -% de recarga das habilidades por ponto de atributo |
| `stats.critPct` | `0.08` | + chance de crítico por ponto de atributo |
| `stats.turnPct` | `0.12` | Manobrabilidade (exclusivo do Thunderbolt) |
| `stats.capLevels` | `10` | teto de niveis do Rate of Spell e do Dano Critico |
| `stats.critDmgBase` | `1.5` | um acerto critico causa 1,5x o dano... |
| `stats.critDmgPerChance` | `1.5` | ...mais 1,5x a sua chance de critico (com 80% de chance: 1,5 + 1,2 = 2,7x) |

<a id="mobs"></a>
## Inimigos

| caminho | valor | o que faz |
|---|---|---|
| `mobs.zombie.hp` | `34` | vida |
| `mobs.zombie.spd` | `62` | velocidade (px/s) |
| `mobs.zombie.dmg` | `9` | dano |
| `mobs.zombie.r` | `14` | raio: tamanho e colisão (px) |
| `mobs.zombie.score` | `10` | pontos ao matar |
| `mobs.zombie.xp` | `1` | chips de XP que solta ao morrer |
| `mobs.ninja.hp` | `18` | vida |
| `mobs.ninja.spd` | `180` | velocidade (px/s) |
| `mobs.ninja.dmg` | `20` | dano |
| `mobs.ninja.r` | `12` | raio: tamanho e colisão (px) |
| `mobs.ninja.score` | `30` | pontos ao matar |
| `mobs.ninja.xp` | `2` | chips de XP que solta ao morrer |
| `mobs.ninja.dashSpeed` | `720` | investida do ninja (px/s, s parado depois, chance de sumir) |
| `mobs.ninja.dashStunSec` | `1.6` | investida do ninja (px/s, s parado depois, chance de sumir) |
| `mobs.ninja.invisChance` | `0.35` | investida do ninja (px/s, s parado depois, chance de sumir) |
| `mobs.ninja.dashSec` | `0.18` | duracao da investida (s) |
| `mobs.ninja.dashEveryMinSec` | `3.2` | intervalo sorteado entre investidas (s) |
| `mobs.ninja.dashEveryMaxSec` | `4.8` | intervalo sorteado entre investidas (s) |
| `mobs.ninja.dashMinDist` | `120` | so investe com voce entre estas distancias (px) |
| `mobs.ninja.dashMaxDist` | `460` | so investe com voce entre estas distancias (px) |
| `mobs.ninja.invisSec` | `1` | quanto tempo fica invisivel quando some (s) |
| `mobs.gangM.hp` | `26` | vida |
| `mobs.gangM.spd` | `105` | velocidade (px/s) |
| `mobs.gangM.dmg` | `12` | dano |
| `mobs.gangM.r` | `13` | raio: tamanho e colisão (px) |
| `mobs.gangM.score` | `15` | pontos ao matar |
| `mobs.gangM.xp` | `1` | chips de XP que solta ao morrer |
| `mobs.gangG.hp` | `22` | vida |
| `mobs.gangG.spd` | `88` | velocidade (px/s) |
| `mobs.gangG.dmg` | `8` | dano |
| `mobs.gangG.r` | `13` | raio: tamanho e colisão (px) |
| `mobs.gangG.score` | `20` | pontos ao matar |
| `mobs.gangG.xp` | `2` | chips de XP que solta ao morrer |
| `mobs.gangG.ranged` | `true` | atira de longe; velocidade da bala (px/s) |
| `mobs.gangG.projectileSpeed` | `420` | atira de longe; velocidade da bala (px/s) |
| `mobs.gangG.keepDist` | `340` | para a esta distancia (px) e atira a cada 1,7 a 2,9 s |
| `mobs.gangG.shootMinSec` | `1.68` | para a esta distancia (px) e atira a cada 1,7 a 2,9 s |
| `mobs.gangG.shootMaxSec` | `2.88` | para a esta distancia (px) e atira a cada 1,7 a 2,9 s |
| `mobs.drone.hp` | `14` | vida |
| `mobs.drone.spd` | `130` | velocidade (px/s) |
| `mobs.drone.dmg` | `10` | dano |
| `mobs.drone.r` | `11` | raio: tamanho e colisão (px) |
| `mobs.drone.score` | `25` | pontos ao matar |
| `mobs.drone.xp` | `2` | chips de XP que solta ao morrer |
| `mobs.drone.ranged` | `true` | atira de longe; velocidade da bala (px/s) |
| `mobs.drone.projectileSpeed` | `420` | atira de longe; velocidade da bala (px/s) |
| `mobs.drone.keepDist` | `260` | idem, mais perto e mais rapido |
| `mobs.drone.shootMinSec` | `1.08` | idem, mais perto e mais rapido |
| `mobs.drone.shootMaxSec` | `1.92` | idem, mais perto e mais rapido |
| `mobs.jetdrone.limit` | `6` | máximo vivo ao mesmo tempo |
| `mobs.jetdrone.hp` | `30` | vida |
| `mobs.jetdrone.spd` | `340` | velocidade (px/s) |
| `mobs.jetdrone.dmg` | `16` | dano |
| `mobs.jetdrone.r` | `16` | raio: tamanho e colisão (px) |
| `mobs.jetdrone.score` | `60` | pontos ao matar |
| `mobs.jetdrone.xp` | `3` | chips de XP que solta ao morrer |
| `mobs.jetdrone.rateOfFire` | `6` | segundos entre um foguete e outro do mesmo jato |
| `mobs.jetdrone.projectileSpeed` | `175` | velocidade inicial do foguete (px/s) e vida dele (s) |
| `mobs.jetdrone.rocketLifeSec` | `6` | velocidade inicial do foguete (px/s) e vida dele (s) |
| `mobs.jetdrone.maxRockets` | `6` | foguetes perseguindo voce ao mesmo tempo (o mais velho explode) |
| `mobs.jetdrone.rocketMaxSpeed` | `430` | foguete mais veloz... |
| `mobs.jetdrone.rocketAccel` | `260` | foguete mais veloz... |
| `mobs.jetdrone.rocketTurnRate` | `0.8` | ...com curva limitada (0.7 +15%) |
| `mobs.jetdrone.rocketShieldDmgMul` | `3` | dano TRIPLO contra o escudo do jogador |
| `mobs.jetdrone.fireMinDist` | `180` | so dispara com voce entre estas distancias (px) |
| `mobs.jetdrone.fireMaxDist` | `520` | so dispara com voce entre estas distancias (px) |
| `mobs.jetdrone.rocketBlastRadius` | `60` | explosao do foguete: raio (px) e fracao do dano em quem esta perto |
| `mobs.jetdrone.rocketSplashFrac` | `0.7` | explosao do foguete: raio (px) e fracao do dano em quem esta perto |
| `mobs.toxwalker.hp` | `48` | vida |
| `mobs.toxwalker.spd` | `70` | velocidade (px/s) |
| `mobs.toxwalker.dmg` | `0` | dano |
| `mobs.toxwalker.r` | `15` | raio: tamanho e colisão (px) |
| `mobs.toxwalker.score` | `35` | pontos ao matar |
| `mobs.toxwalker.xp` | `3` | chips de XP que solta ao morrer |
| `mobs.toxwalker.fastChance` | `0.15` | 15% nascem na versao veloz (trilha mais forte) |
| `mobs.toxwalker.fastSpdMul` | `2` | o toxwalker veloz anda 2x mais rapido |
| `mobs.toxwalker.trailRadius` | `26` | largura da trilha toxica (px): normal e veloz |
| `mobs.toxwalker.trailFastRadius` | `30` | largura da trilha toxica (px): normal e veloz |
| `mobs.toxwalker.trailDmg` | `7` | dano da trilha (no maximo 1 vez por segundo): normal e veloz |
| `mobs.toxwalker.trailFastDmg` | `9` | dano da trilha (no maximo 1 vez por segundo): normal e veloz |
| `mobs.toxwalker.trailDurSec` | `4` | segundos que a trilha fica no chao |
| `mobs.goblin.hp` | `900` | hp/spd aqui sao so fallback: o goblin usa a formula abaixo |
| `mobs.goblin.spd` | `235` | hp/spd aqui sao so fallback: o goblin usa a formula abaixo |
| `mobs.goblin.r` | `18` | hp/spd aqui sao so fallback: o goblin usa a formula abaixo |
| `mobs.goblin.score` | `1500` | hp/spd aqui sao so fallback: o goblin usa a formula abaixo |
| `mobs.goblin.xp` | `0` | hp/spd aqui sao so fallback: o goblin usa a formula abaixo |
| `mobs.goblin.fleeTimerSec` | `20` | (hp/spd aqui sao so fallback: o goblin usa a formula abaixo) |
| `mobs.goblin.decloakRange` | `220` | (hp/spd aqui sao so fallback: o goblin usa a formula abaixo) |
| `mobs.goblin.hpMin` | `200` | vida = max(hpMin, seu DPS*hpDpsSeconds + nivel*hpPerLevel) |
| `mobs.goblin.hpDpsSeconds` | `4` | vida = max(hpMin, seu DPS*hpDpsSeconds + nivel*hpPerLevel) |
| `mobs.goblin.hpPerLevel` | `36` | vida = max(hpMin, seu DPS*hpDpsSeconds + nivel*hpPerLevel) |
| `mobs.goblin.spdStart` | `130` | velocidade cresce com o tempo de run |
| `mobs.goblin.spdPerMin` | `16` | velocidade cresce com o tempo de run |
| `mobs.goblin.spdMax` | `215` | velocidade cresce com o tempo de run |
| `mobs.goblin.rewardChips` | `14` | (hp/spd aqui sao so fallback: o goblin usa a formula abaixo) |
| `mobs.wardenAtk.spiralEverySec` | `0.12` | espiral de fundo: intervalo (s), bracos, giro (rad), velocidade, dano |
| `mobs.wardenAtk.spiralArms` | `2` | espiral de fundo: intervalo (s), bracos, giro (rad), velocidade, dano |
| `mobs.wardenAtk.spiralStepRad` | `0.4` | espiral de fundo: intervalo (s), bracos, giro (rad), velocidade, dano |
| `mobs.wardenAtk.spiralSpeed` | `200` | espiral de fundo: intervalo (s), bracos, giro (rad), velocidade, dano |
| `mobs.wardenAtk.spiralDmg` | `10` | espiral de fundo: intervalo (s), bracos, giro (rad), velocidade, dano |
| `mobs.wardenAtk.ringCount` | `28` | 0: anel completo |
| `mobs.wardenAtk.ringSpeed` | `300` | 0: anel completo |
| `mobs.wardenAtk.ringDmg` | `14` | 0: anel completo |
| `mobs.wardenAtk.dashTelegraphSec` | `0.8` | 1: investida telegrafada |
| `mobs.wardenAtk.dashDurSec` | `0.5` | 1: investida telegrafada |
| `mobs.wardenAtk.dashSpeed` | `820` | 1: investida telegrafada |
| `mobs.wardenAtk.minionRadius` | `100` | 2: invocacao de minions |
| `mobs.wardenAtk.fanWaves` | `5` | 3: leque mirado (fanArc=2 -> 5 balas por onda) |
| `mobs.wardenAtk.fanArc` | `2` | 3: leque mirado (fanArc=2 -> 5 balas por onda) |
| `mobs.wardenAtk.fanStepRad` | `0.18` | 3: leque mirado (fanArc=2 -> 5 balas por onda) |
| `mobs.wardenAtk.fanSpeed` | `240` | 3: velocidade da 1a onda, ganho por onda, dano |
| `mobs.wardenAtk.fanSpeedPerWave` | `40` | 3: velocidade da 1a onda, ganho por onda, dano |
| `mobs.wardenAtk.fanDmg` | `12` | 3: velocidade da 1a onda, ganho por onda, dano |
| `mobs.wardenAtk.flowerCount` | `20` | 4: anel duplo girado |
| `mobs.wardenAtk.flowerSpeed` | `340` | 4: anel duplo girado |
| `mobs.wardenAtk.flowerSpeed2` | `200` | 4: anel duplo girado |
| `mobs.wardenAtk.flowerOffsetRad` | `0.15` | 4: giro do 2o anel (rad) e dano |
| `mobs.wardenAtk.flowerDmg` | `12` | 4: giro do 2o anel (rad) e dano |
| `mobs.wardenAtk.crossArms` | `4` | 5: cruz rotativa |
| `mobs.wardenAtk.crossPerArm` | `6` | 5: cruz rotativa |
| `mobs.wardenAtk.crossSpeed` | `160` | 5: cruz rotativa |
| `mobs.wardenAtk.crossSpeedStep` | `45` | 5: velocidade extra de cada bala do braco e dano |
| `mobs.wardenAtk.crossDmg` | `11` | 5: velocidade extra de cada bala do braco e dano |
| `mobs.warden.limit` | `2` | máximo vivo ao mesmo tempo |
| `mobs.warden.hp` | `1260` | vida |
| `mobs.warden.spd` | `85` | velocidade (px/s) |
| `mobs.warden.dmg` | `30` | dano |
| `mobs.warden.r` | `46` | raio: tamanho e colisão (px) |
| `mobs.warden.score` | `5000` | pontos ao matar |
| `mobs.warden.xp` | `0` | chips de XP que solta ao morrer |
| `mobs.warden.firstSpawnSec` | `240` | quando o 1o warden aparece (survival) |
| `mobs.warden.respawnEverySec` | `240` | intervalo entre wardens |
| `mobs.warden.secondWardenChance` | `0.20` | chance de vir um 2o warden junto |
| `mobs.warden.hpGrowthPer4Min` | `0.8` | vida escala: hp*(1 + tempo/240 * este) |
| `mobs.warden.atkEverySec` | `3` | intervalo entre padroes de ataque |
| `mobs.warden.minionCount` | `6` | minions invocados por vez |
| `mobs.warden.bulletDmgMul` | `1` | multiplicador do dano de TODOS os projeteis do warden |
| `mobs.warden.contactDmgMul` | `3.4` | dano de contato /s (normal e na investida) |
| `mobs.warden.dashContactDmgMul` | `7` | dano de contato /s (normal e na investida) |
| `mobs.warden.deathBlastRadius` | `260` | explosao quando ele morre (px, dano nos inimigos em volta) |
| `mobs.warden.deathBlastDmg` | `90` | explosao quando ele morre (px, dano nos inimigos em volta) |

<a id="engine"></a>
## Motor (ajustes finos)

| caminho | valor | o que faz |
|---|---|---|
| `engine.autoAimRange` | `760` | ate onde a mira 'auto' trava sozinha num inimigo |
| `engine.multishotAngleStep` | `0.10` | angulo entre os projeteis do leque do blaster |
| `engine.multishotSpreadPerShot` | `0.06` | dispersao extra por projetil a mais no leque |
| `engine.twinAngleStep` | `0.09` | idem para as torretas do Warrior |
| `engine.gatlingAngleStep` | `0.06` | idem para o canhao giratorio |
| `engine.dashStunRadius` | `46` | raio do clarao do Dash Nv3 |
| `engine.magnetPullVacuum` | `1150` | velocidade do chip no EMP final do Desafio |
| `engine.magnetPullGlobal` | `700` | velocidade do chip com Ima Nv3 (global) |
| `engine.magnetPullNear` | `900` | ima normal: forca no centro do raio... |
| `engine.magnetPullMin` | `200` | ...e forca na borda |
| `engine.holePullBase` | `150` | succao do buraco negro (centro e borda) |
| `engine.holePullMin` | `70` | succao do buraco negro (centro e borda) |
| `engine.holeGrowSec` | `0.45` | tempo que o buraco leva para abrir de vez |
| `engine.holeCollapseAt` | `0.62` | fracao da animacao de colapso onde ele estoura |
| `engine.shockDps` | `7` | eletrocucao do EMP Nv3 |
| `engine.shockTickSec` | `0.4` | eletrocucao do EMP Nv3 |
| `engine.burnTickSec` | `0.5` | intervalo do dano de queimadura |
| `engine.bulletKnockback` | `0` | empurrao do TIRO no inimigo (0 = nenhum, para todas as naves) |
| `engine.explosionKnockback` | `900` | empurrao padrao das explosoes (JDAM, missil, Zuni...), em px/s |
| `engine.enemyBulletRange` | `600` | alcance (px) da bala de inimigo comum antes de sumir |
| `engine.enemyTurnRate` | `1.8` | rad/s que os inimigos viram atras de voce |
| `engine.enemyShootRange` | `560` | distancia em que inimigo de tiro comeca a atirar |
| `engine.maxGruntBullets` | `70` | teto de balas de inimigo comum vivas na tela |
| `engine.maxShooters` | `6` | inimigos atirando ao mesmo tempo |
| `engine.maxEnemyBullets` | `900` | teto absoluto de projeteis inimigos (seguranca) |
| `engine.lowHpWarnFrac` | `0.3` | abaixo desta fracao de vida comeca o batimento cardiaco |

<a id="difficulty"></a>
## Dificuldade e spawner

| caminho | valor | o que faz |
|---|---|---|
| `difficulty.spawnTable` | `[[0,'zombie'], [0,'zombie'], [0,'gangM'], [0.7,'gangG'], [1.0,'toxwalker'], [1.5,'ninja'], [2.2,'drone'], [2.2,'drone'], [2.5,'jetdrone'], [4,'ninja'], [4,'gangG']]` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.startBurst` | `10` | inimigos que ja nascem no inicio da run |
| `difficulty.firstSpawnSec` | `1.2` | segundos ate a primeira leva |
| `difficulty.spawnDistMul` | `0.62` | distancia de nascimento = maior lado da tela x isto (+0 a 200 px), fora da sua vista |
| `difficulty.spawnIntervalStart` | `0.85` | seg entre levas |
| `difficulty.spawnIntervalPerMin` | `0.07` | seg entre levas |
| `difficulty.spawnIntervalMin` | `0.14` | seg entre levas |
| `difficulty.spawnIntervalStormMul` | `0.45` | multiplicador do intervalo durante a storm (menor = mais rapido) |
| `difficulty.capStart` | `55` | teto de inimigos vivos |
| `difficulty.capPerMin` | `26` | teto de inimigos vivos |
| `difficulty.capMax` | `320` | teto de inimigos vivos |
| `difficulty.capStormMul` | `1.4` | teto de inimigos vivos |
| `difficulty.burstBase` | `2` | inimigos por leva |
| `difficulty.burstPerMin` | `0.5` | inimigos por leva |
| `difficulty.burstStormBonus` | `2` | inimigos por leva |
| `difficulty.burstFirstMinuteBonus` | `2` | inimigos por leva |
| `difficulty.hpScalePerMin` | `0.22` | escala de vida dos mobs com o tempo |
| `difficulty.hpStormMul` | `1.1` | escala de vida dos mobs com o tempo |
| `difficulty.buildScale.perAttrPoint` | `0.03` | +3% de vida por ponto de atributo seu |
| `difficulty.buildScale.perPowerLevel` | `0.06` | +6% de vida por nível de power-up/passiva seu |
| `difficulty.eliteChance` | `0.12` | chance de elite durante a storm |
| `difficulty.eliteHpMul` | `3` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.eliteDmgMul` | `1.6` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.eliteSpdMul` | `0.9` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.eliteSizeMul` | `1.4` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.eliteScoreMul` | `3` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |
| `difficulty.eliteXpMul` | `3` | [quais inimigos podem nascer e A PARTIR DE QUE MINUTO: [minuto, tipo]. Repetir um tipo aumenta a chance dele (cada linha e um bilhete no sorteio).] |

<a id="events"></a>
## Eventos do Survival

| caminho | valor | o que faz |
|---|---|---|
| `events.stormFirstSec` | `95` | proxima = min + rand(0,rnd) |
| `events.stormDurSec` | `30` | proxima = min + rand(0,rnd) |
| `events.stormEveryMinSec` | `80` | proxima = min + rand(0,rnd) |
| `events.stormEveryRndSec` | `30` | proxima = min + rand(0,rnd) |
| `events.stormBurst` | `14` | leva extra ao comecar a storm |
| `events.stormSpdMul` | `1.25` | inimigos mais rapidos na storm |
| `events.stormScoreMul` | `2` | na storm: pontos e chips valem x2 |
| `events.stormXpMul` | `2` | na storm: pontos e chips valem x2 |
| `events.astFirstSec` | `150` | asteroides: 1a vez (s), duracao (s), proxima = min + sorteio(0, rnd) |
| `events.astDurSec` | `22` | asteroides: 1a vez (s), duracao (s), proxima = min + sorteio(0, rnd) |
| `events.astEveryMinSec` | `120` | asteroides: 1a vez (s), duracao (s), proxima = min + sorteio(0, rnd) |
| `events.astEveryRndSec` | `40` | asteroides: 1a vez (s), duracao (s), proxima = min + sorteio(0, rnd) |
| `events.astCount` | `7` | asteroides simultaneos |
| `events.astSpeedMin` | `240` | velocidade sorteada de cada asteroide (px/s) |
| `events.astSpeedMax` | `380` | velocidade sorteada de cada asteroide (px/s) |
| `events.astRadiusMin` | `30` | tamanho sorteado de cada asteroide (px) |
| `events.astRadiusMax` | `52` | tamanho sorteado de cada asteroide (px) |
| `events.goblinFirstSec` | `50` | goblin: 1a vez (s) e intervalo sorteado entre min e max (s) |
| `events.goblinEveryMinSec` | `45` | goblin: 1a vez (s) e intervalo sorteado entre min e max (s) |
| `events.goblinEveryMaxSec` | `70` | goblin: 1a vez (s) e intervalo sorteado entre min e max (s) |

<a id="desafio"></a>
## Roteiro do modo Desafio

| caminho | valor | o que faz |
|---|---|---|
| `desafio.goblinAtSec` | `[60,180]` | momentos da caca ao goblin |
| `desafio.stormAtSec` | `120` | cyber storm do meio da run |
| `desafio.stormDurSec` | `30` | cyber storm do meio da run |
| `desafio.stormBurst` | `14` | cyber storm do meio da run |
| `desafio.astAtSec` | `180` | chuva de asteroides |
| `desafio.astDurSec` | `22` | chuva de asteroides |
| `desafio.astCount` | `7` | chuva de asteroides |
| `desafio.wardenAtSec` | `240` | entrada do warden |
| `desafio.finalStormAtSec` | `280` | sobrecarga final ate o EMP |
| `desafio.finalStormBurst` | `16` | sobrecarga final ate o EMP |
| `desafio.endSec` | `300` | EMP total: limpa a arena |
| `desafio.dragonIntroSec` | `3` | pausa entre o EMP e o dragao |

<a id="dragon"></a>
## Dragão

| caminho | valor | o que faz |
|---|---|---|
| `dragon.hp` | `30000` | vida base (multiplicada pela força da sua build). Era 60000 quando cada elo atingido contava dano separado |
| `dragon.score` | `10000` | pontos ao derrotar |
| `dragon.survivalEveryLevels` | `20` | no Survival, o dragão aparece a cada N níveis do jogador |
| `dragon.palettes` | `[['#ff3b30','#ffb300','#d92b20'], ['#2ecc40','#b6ff00','#1d9930'], ['#00c8ff','#aef0ff','#0090c0'], ['#9d4bff','#ff7ab0','#7a30cc'], ['#ffd23a','#ff7430','#cc9a10']]` | [corPrincipal, corDetalhe, corMandíbula]: muda a cada aparição no Survival |
| `dragon.segments` | `28` | elos do corpo (mais elos = corpo mais longo) |
| `dragon.segSpacing` | `39` | distância entre elos (comprimento total ≈ segments*segSpacing) |
| `dragon.headRadius` | `60` | raio da cabeça |
| `dragon.bodyRadius` | `44` | raio dos elos do corpo (afina até a cauda via bodyTaper) |
| `dragon.bodyTaper` | `0.8` | quanto cada elo afina em direção à cauda |
| `dragon.bodyDmgMul` | `1` | corpo recebe dano CHEIO... |
| `dragon.headDmgMul` | `1.4` | ...e a cabeça recebe 1.40x (ponto fraco) |
| `dragon.touchDps` | `20` | dano/s por encostar em qualquer parte do corpo |
| `dragon.telegraphSec` | `0.7` | [pattern 1: investida de boca aberta (curta, MUITO manobrável, mordida forte)] |
| `dragon.chargeDurSec` | `1.4` | [pattern 1: investida de boca aberta (curta, MUITO manobrável, mordida forte)] |
| `dragon.chargeSpeed` | `520` | [pattern 1: investida de boca aberta (curta, MUITO manobrável, mordida forte)] |
| `dragon.chargeTurnRate` | `3.5` | [pattern 1: investida de boca aberta (curta, MUITO manobrável, mordida forte)] |
| `dragon.chargeDamage` | `45` | [pattern 1: investida de boca aberta (curta, MUITO manobrável, mordida forte)] |
| `dragon.encircleDurSec` | `7` | [pattern 2: cerco: a cabeça orbita o jogador pela TANGENTE, espiralando p/ dentro] |
| `dragon.encircleSpeed` | `460` | [pattern 2: cerco: a cabeça orbita o jogador pela TANGENTE, espiralando p/ dentro] |
| `dragon.encircleTurnRate` | `4.5` | [pattern 2: cerco: a cabeça orbita o jogador pela TANGENTE, espiralando p/ dentro] |
| `dragon.orbitStart` | `300` | [pattern 2: cerco: a cabeça orbita o jogador pela TANGENTE, espiralando p/ dentro] |
| `dragon.orbitEnd` | `170` | [pattern 2: cerco: a cabeça orbita o jogador pela TANGENTE, espiralando p/ dentro] |
| `dragon.encircleTighten` | `1.6` | agressividade da correção da espiral (maior = fecha mais rápido) |
| `dragon.spitDurSec` | `2.4` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.spitEverySec` | `0.35` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.fireballSpeed` | `300` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.fireballDmg` | `16` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.fireballFuseSec` | `0.8` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.flakCount` | `8` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.flakSpeed` | `230` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.flakDmg` | `10` | [pattern 3: cuspe de fogo: bolas que estouram em vários projéteis] |
| `dragon.roarTelegraphSec` | `0.9` | inspirada antes do rugido |
| `dragon.roarDurSec` | `1.2` | eco do rugido (fim do pattern) |
| `dragon.roarSlowFrac` | `0.5` | velocidade do jogador cai para 50%... |
| `dragon.roarSlowDurSec` | `3` | ...por 3 segundos |
| `dragon.roarShieldLockSec` | `6` | escudo zerado só volta a regenerar depois disso |
| `dragon.strafeDurSec` | `5.5` | duração dos razantes |
| `dragon.strafeSpeed` | `560` | velocidade dos passes |
| `dragon.strafeTurnRate` | `2.6` | manobrabilidade durante o razante |
| `dragon.strafeOvershoot` | `650` | quanto ele passa ALÉM do jogador em cada corte |
| `dragon.strafeSpitEverySec` | `0.7` | cuspe de fogo durante os passes |
| `dragon.strafeChainChargeChance` | `0.5` | chance de emendar em investida (senão, cerco) |
| `dragon.cometFirstSec` | `12` | primeira chuva N seg após o início da luta |
| `dragon.cometEverySec` | `24` | COOLDOWN entre chuvas (anti-spam) |
| `dragon.strafeCometMinSec` | `6` | o razante pode ADIANTAR a chuva, mas nunca para antes disso |
| `dragon.cometRainDurSec` | `6` | duração da chuva |
| `dragon.cometSpawnEverySec` | `0.1` | ritmo de entrada dos cometas (menor = mais cometas) |
| `dragon.cometDamage` | `14` | dano de cada cometa [evento paralelo: CHUVA DE COMETAS (dispara durante qualquer pattern; dano, não mata na hora)] |
| `dragon.cometSpeedMin` | `520` | velocidade mínima do cometa (px/s) [evento paralelo: CHUVA DE COMETAS (dispara durante qualquer pattern; dano, não mata na hora)] |
| `dragon.cometSpeedMax` | `780` | velocidade máxima do cometa (px/s) [evento paralelo: CHUVA DE COMETAS (dispara durante qualquer pattern; dano, não mata na hora)] |
| `dragon.cometRadiusMin` | `10` | tamanho mínimo do cometa (px) [evento paralelo: CHUVA DE COMETAS (dispara durante qualquer pattern; dano, não mata na hora)] |
| `dragon.cometRadiusMax` | `18` | tamanho máximo do cometa (px) [evento paralelo: CHUVA DE COMETAS (dispara durante qualquer pattern; dano, não mata na hora)] |
| `dragon.giftPowers` | `3` | cartas de presente quando o dragão desperta (Desafio) [arsenal de entrada: presentes ao jogador quando o dragão desperta (SÓ no modo Desafio)] |
| `dragon.giftAttrs` | `5` | pontos de atributo de presente quando o dragão desperta (Desafio) [arsenal de entrada: presentes ao jogador quando o dragão desperta (SÓ no modo Desafio)] |
| `dragon.weaveSpeed` | `240` | velocidade enquanto serpenteia (px/s) [arsenal de entrada: presentes ao jogador quando o dragão desperta (SÓ no modo Desafio)] |
| `dragon.weaveTurnRate` | `2.2` | curva enquanto serpenteia (rad/s) [arsenal de entrada: presentes ao jogador quando o dragão desperta (SÓ no modo Desafio)] |
| `dragon.weaveBetweenSec` | `3.2` | COOLDOWN entre habilidades: tempo serpenteando antes do próximo pattern |

<a id="combo"></a>
## Combo

| caminho | valor | o que faz |
|---|---|---|
| `combo.thresholds` | `[[60,10],[35,5],[18,3],[8,2]]` | [[segundos sem tomar dano, multiplicador]: do maior para o menor] |

<a id="score"></a>
## Pontuação

| caminho | valor | o que faz |
|---|---|---|
| `score.perSecond` | `4` | pontos por segundo vivo (x combo, x storm) |
| `score.chipScore` | `2` | pontos por chip coletado |
| `score.streakBonus` | `25` | bonus por marco de killstreak = marco * este |

<a id="slot"></a>
## Alavanca (slot)

| caminho | valor | o que faz |
|---|---|---|
| `slot.chances.evolve` | `57` | sobe de nivel algo que voce ja tem |
| `slot.chances.newpow` | `19` | ganha uma habilidade nova (Nv1) |
| `slot.chances.maxpow` | `9` | leva algo que voce tem ao nivel maximo |
| `slot.chances.newmax` | `5` | habilidade nova ja no nivel maximo |
| `slot.chances.nothing` | `6` | azar: nada |
| `slot.chances.adrenaline` | `2` | buff de todos os atributos por alguns segundos |
| `slot.chances.clear` | `1` | mata a horda (menos warden, dragao e goblin) |
| `slot.chances.nocd` | `1` | habilidades sem recarga por alguns segundos |
| `slot.adrenalineDurationSec` | `15` | [newmax = ganha uma habilidade NOVA já no nível máximo] |
| `slot.adrenaline.speedMul` | `1.6` | buffs do ADRENALINE |
| `slot.adrenaline.rofMul` | `2.2` | buffs do ADRENALINE |
| `slot.adrenaline.dmgMul` | `2.2` | buffs do ADRENALINE |
| `slot.adrenaline.cdMul` | `0.5` | buffs do ADRENALINE |
| `slot.adrenaline.critBonus` | `20` | buffs do ADRENALINE |
| `slot.noCooldownsDurationSec` | `4` | [newmax = ganha uma habilidade NOVA já no nível máximo] |

<a id="roulette"></a>
## Roleta de atributos

| caminho | valor | o que faz |
|---|---|---|
| `roulette.chances.none` | `23.5` | azar: nada |
| `roulette.chances.x2` | `23.5` | +2 pontos num atributo sorteado |
| `roulette.chances.x3` | `23.5` | +3 pontos num atributo sorteado |
| `roulette.chances.two1` | `23.5` | +1 ponto em dois atributos sorteados |
| `roulette.chances.x5` | `5` | +5 pontos num atributo sorteado |
| `roulette.chances.jackpot` | `1` | +10 pontos para voce distribuir |
| `roulette.x2_points` | `2` | pontos do prêmio x2 |
| `roulette.x3_points` | `3` | pontos do prêmio x3 |
| `roulette.x5_points` | `5` | pontos do prêmio x5 |
| `roulette.jackpot_points` | `10` | pontos do JACKPOT, para distribuir |

<a id="ships"></a>
## Naves

| caminho | valor | o que faz |
|---|---|---|
| `ships.selectorEnabled` | `true` | false = pula a tela de escolha de nave |
| `ships.defaultShip` | `'fighter'` | nave usada quando o seletor está desligado |
| `ships.fighter.name` | `'Fighter'` | nome exibido |
| `ships.fighter.locked` | `false` | true = nave bloqueada (EM BREVE) |
| `ships.fighter.aim` | `'auto'` | modelo de mira (ver o topo da seção NAVES) |
| `ships.fighter.move` | `'free'` | modelo de movimento (ver o topo da seção NAVES) |
| `ships.fighter.desc` | `'Equilibrada: blaster automático que trava sozinho no alvo mais próximo.'` | texto da tela de escolha |
| `ships.fighter.speedMul` | `1` | multiplicador de velocidade da nave |
| `ships.fighter.hpMul` | `1` | multiplicador de vida da nave |
| `ships.fighter.shieldMul` | `1` | multiplicador de escudo da nave |
| `ships.fighter.weapon` | `'blaster'` | arma da nave |
| `ships.fighter.colors.hull` | `'#e8f6ff'` | cor do casco |
| `ships.fighter.colors.accent` | `'#ff2d78'` | cor de destaque |
| `ships.fighter.colors.glow` | `'#00f0ff'` | cor do brilho |
| `ships.fighter.blocked` | `[]` | power-ups que esta nave nunca recebe |
| `ships.warrior.name` | `'Warrior'` | nome exibido |
| `ships.warrior.locked` | `false` | true = nave bloqueada (EM BREVE) |
| `ships.warrior.aim` | `'mouse'` | modelo de mira (ver o topo da seção NAVES) |
| `ships.warrior.move` | `'inertia'` | modelo de movimento (ver o topo da seção NAVES) |
| `ships.warrior.accel` | `1500` | inercia leve: desliza um pouco na curva, sem virar caminhão |
| `ships.warrior.friction` | `5.5` | inercia leve: desliza um pouco na curva, sem virar caminhão |
| `ships.warrior.desc` | `'Equilibrado: Caça de assalto de torreta dupla de tiro livre. Possui inercia'` | texto da tela de escolha |
| `ships.warrior.speedMul` | `1.06` | multiplicador de velocidade da nave |
| `ships.warrior.hpMul` | `1` | multiplicador de vida da nave |
| `ships.warrior.shieldMul` | `1` | multiplicador de escudo da nave |
| `ships.warrior.weapon` | `'twin'` | arma da nave |
| `ships.warrior.twin.damage` | `8` | dano por projétil (escala com o atributo Dano) |
| `ships.warrior.twin.fireDelay` | `0.30` | segundos entre disparos |
| `ships.warrior.twin.speed` | `820` | velocidade (px/s) |
| `ships.warrior.twin.size` | `4` | tamanho do projétil (px) |
| `ships.warrior.twin.lifeSec` | `1.1` | segundos de vida do projétil (define o alcance) |
| `ships.warrior.twin.spread` | `0.03` | dispersão (radianos) |
| `ships.warrior.twin.wingOffset` | `14` | distancia de cada torreta ate o centro da nave |
| `ships.warrior.twin.convergeDist` | `420` | as duas torretas convergem nesta distancia |
| `ships.warrior.colors.hull` | `'#e6dcff'` | cor do casco |
| `ships.warrior.colors.accent` | `'#9d4bff'` | cor de destaque |
| `ships.warrior.colors.glow` | `'#c9a0ff'` | cor do brilho |
| `ships.warrior.blocked` | `[]` | power-ups que esta nave nunca recebe |
| `ships.cruiser.name` | `'Cruiser'` | nome exibido |
| `ships.cruiser.locked` | `false` | true = nave bloqueada (EM BREVE) |
| `ships.cruiser.aim` | `'mouse'` | modelo de mira (ver o topo da seção NAVES) |
| `ships.cruiser.move` | `'tank'` | modelo de movimento (ver o topo da seção NAVES) |
| `ships.cruiser.manualFire` | `true` | TIRO MANUAL no botao esquerdo: segurar CARREGA o disparo |
| `ships.cruiser.turret` | `true` | torreta central gira atras do mouse, independente do casco |
| `ships.cruiser.turretTraverse` | `6` | torreta central gira atras do mouse, independente do casco |
| `ships.cruiser.tank.turnRate` | `2` | leme: 3,1s para dar meia-volta; re com metade da forca |
| `ships.cruiser.tank.reverseFrac` | `0.5` | leme: 3,1s para dar meia-volta; re com metade da forca |
| `ships.cruiser.desc` | `'Difícil: Cruzador de batalha: A e D giram o casco, W avança, S dá ré. A TORRETA central mira onde o mouse aponta. Toque o BOTÃO ESQUERDO para o tiro rápido do railgun; segure para carregar um tiro mais forte. Com a carga CHEIA ele vira um canhão laser que você varre girando a torreta.'` | texto da tela de escolha |
| `ships.cruiser.speedMul` | `0.7` | multiplicador de velocidade da nave |
| `ships.cruiser.hpMul` | `2.75` | multiplicador de vida da nave |
| `ships.cruiser.shieldMul` | `1.4` | multiplicador de escudo da nave |
| `ships.cruiser.weapon` | `'rail'` | arma da nave |
| `ships.cruiser.radius` | `26` | raio do casco (px): maior = alvo maior |
| `ships.cruiser.previewScale` | `1.4` | zoom do desenho na tela de escolha |
| `ships.cruiser.accel` | `380` | casco de cruzador: quase 0,7s para engrenar e 1,8s deslizando |
| `ships.cruiser.friction` | `1.25` | casco de cruzador: quase 0,7s para engrenar e 1,8s deslizando |
| `ships.cruiser.rail.damage` | `68` | dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali |
| `ships.cruiser.rail.speed` | `1400` | dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali |
| `ships.cruiser.rail.size` | `6` | dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali |
| `ships.cruiser.rail.lifeSec` | `2.8` | dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali |
| `ships.cruiser.rail.rofLevelsToFloor` | `8` | (dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali) |
| `ships.cruiser.rail.fireDelay` | `2` | 0,50 tiro/s de base, 1,60 tiro/s no apice |
| `ships.cruiser.rail.minFireDelay` | `0.625` | 0,50 tiro/s de base, 1,60 tiro/s no apice |
| `ships.cruiser.rail.chargeSec` | `8` | 8s p/ carga cheia, 6s no apice |
| `ships.cruiser.rail.minChargeSec` | `6` | 8s p/ carga cheia, 6s no apice |
| `ships.cruiser.rail.beamSec` | `1.4` | quanto tempo o raio fica ligado |
| `ships.cruiser.rail.beamDmgMul` | `3` | dano/s do raio = rail.damage x isto (3 x 68 = 204/s, o mesmo de antes) |
| `ships.cruiser.rail.beamWidth` | `18` | espessura do raio (quanto mais grosso, mais facil varrer) |
| `ships.cruiser.rail.beamRange` | `3900` | alcance: atravessa o mapa inteiro |
| `ships.cruiser.rail.beamTraverseMul` | `0.35` | a torreta gira a 35% da velocidade enquanto dispara |
| `ships.cruiser.rail.beamCol` | `'#b44dff'` | (dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali) [CARGA CHEIA vira CANHAO LASER: raio continuo que voce varre com a torreta] |
| `ships.cruiser.rail.chargeDmgMul` | `2` | (dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali) [carga PARCIAL continua sendo tiro unico, escalando com o quanto voce segurou] |
| `ships.cruiser.rail.chargeSpeedMul` | `4` | (dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali) [carga PARCIAL continua sendo tiro unico, escalando com o quanto voce segurou] |
| `ships.cruiser.rail.chargeSizeMul` | `3` | (dano por tiro (era 34, mas cada tiro acertava ~2x o mesmo inimigo por bug) a cadencia melhora de forma LINEAR ate o nivel abaixo, e para de melhorar ali) [carga PARCIAL continua sendo tiro unico, escalando com o quanto voce segurou] |
| `ships.cruiser.rail.chargeCol` | `'#b44dff'` | cor da carga: ROXO (o vermelho ficou so p/ recarga) |
| `ships.cruiser.rail.readyCol` | `'#00c8ff'` | cor da torreta: azul pronta, vermelha recarregando |
| `ships.cruiser.rail.cdCol` | `'#ff3b30'` | cor da torreta: azul pronta, vermelha recarregando |
| `ships.cruiser.colors.hull` | `'#9fb8d0'` | cor do casco |
| `ships.cruiser.colors.accent` | `'#1e88e5'` | cor de destaque |
| `ships.cruiser.colors.glow` | `'#00c8ff'` | cor do brilho |
| `ships.cruiser.blocked` | `['pierce','multishot']` | power-ups que esta nave nunca recebe [carga PARCIAL continua sendo tiro unico, escalando com o quanto voce segurou] |
| `ships.thunderbolt.name` | `'Thunderbolt'` | nome exibido |
| `ships.thunderbolt.locked` | `false` | true = nave bloqueada (EM BREVE) |
| `ships.thunderbolt.aim` | `'nose'` | modelo de mira (ver o topo da seção NAVES) |
| `ships.thunderbolt.move` | `'flight'` | modelo de movimento (ver o topo da seção NAVES) |
| `ships.thunderbolt.manualFire` | `true` | TIRO MANUAL no botao esquerdo: segurou, atira; soltou, esfria |
| `ships.thunderbolt.desc` | `'Nunca para: voa na direção do mouse, W acelera e S freia. Segure o BOTÃO ESQUERDO para girar o canhão do nariz, que superaquece. A e D dão um FLIP com imunidade. Não usa: Dash.'` | texto da tela de escolha |
| `ships.thunderbolt.speedMul` | `1` | multiplicador de velocidade da nave |
| `ships.thunderbolt.hpMul` | `0.9` | multiplicador de vida da nave |
| `ships.thunderbolt.shieldMul` | `1` | multiplicador de escudo da nave |
| `ships.thunderbolt.weapon` | `'gatling'` | arma da nave |
| `ships.thunderbolt.radius` | `14` | raio do casco (px): maior = alvo maior |
| `ships.thunderbolt.flight.min` | `150` | velocidade minima, de cruzeiro e maxima (px/s) |
| `ships.thunderbolt.flight.cruise` | `320` | velocidade minima, de cruzeiro e maxima (px/s) |
| `ships.thunderbolt.flight.max` | `520` | velocidade minima, de cruzeiro e maxima (px/s) |
| `ships.thunderbolt.flight.accel` | `260` | quanto o W acelera e o S freia (px/s por segundo) |
| `ships.thunderbolt.flight.brake` | `320` | quanto o W acelera e o S freia (px/s por segundo) |
| `ships.thunderbolt.flight.turnRate` | `2.2` | rad/s (o atributo Manobrabilidade aumenta isto) |
| `ships.thunderbolt.flight.easeBack` | `0.5` | fracao da aceleracao usada p/ voltar sozinho ao cruzeiro |
| `ships.thunderbolt.flip.immunitySec` | `1.2` | duracao do giro, com imunidade |
| `ships.thunderbolt.flip.immunityAfterSec` | `1.2` | imunidade que SOBRA depois que o giro termina |
| `ships.thunderbolt.flip.cooldownSec` | `12` | recarga base, ENCURTADA pelo atributo Rate of Spell |
| `ships.thunderbolt.flip.minCooldownSec` | `8` | piso: por mais cooldown que voce tenha, nunca desce disso |
| `ships.thunderbolt.flip.slideSpeed` | `340` | slideSpeed:0 = flip sem deslocamento |
| `ships.thunderbolt.flip.slideDecayPerSec` | `6.3` | quanto o deslize do flip freia por segundo (maior = desliza menos) |
| `ships.thunderbolt.gatling.damage` | `1.2` | dano por projétil (escala com o atributo Dano) |
| `ships.thunderbolt.gatling.speed` | `1800` | velocidade (px/s) |
| `ships.thunderbolt.gatling.size` | `3.4` | tamanho do projétil (px) |
| `ships.thunderbolt.gatling.lifeSec` | `0.9` | segundos de vida do projétil (define o alcance) |
| `ships.thunderbolt.gatling.fireRateStart` | `40` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.fireRateMax` | `65` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.spinUpSec` | `4` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.heatMax` | `100` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.heatPerShot` | `0.48` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.coolPerSec` | `22.2` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.coolDelaySec` | `0.6` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.overheatLockSec` | `6` | [o cano ACELERA enquanto voce segura: comeca devagar e sobe ate o teto] |
| `ships.thunderbolt.gatling.spreadMin` | `0.04` | dispersao piora com o calor |
| `ships.thunderbolt.gatling.spreadMax` | `0.12` | dispersao piora com o calor |
| `ships.thunderbolt.gatling.heatMaxPerRofLevel` | `12.5` | ganho do "Cano Resistente" |
| `ships.thunderbolt.gatling.coolPerRofLevel` | `2.78` | ganho do "Cano Resistente" |
| `ships.thunderbolt.salvo.climbSec` | `1.0` | tempo subindo (ja invulneravel) |
| `ships.thunderbolt.salvo.durationSec` | `6.0` | tempo metralhando la de cima |
| `ships.thunderbolt.salvo.landSec` | `1.0` | tempo descendo de volta |
| `ships.thunderbolt.salvo.cooldownSec` | `50` | recarga, encurtada pelo Rate of Spell |
| `ships.thunderbolt.salvo.zoom` | `0.6` | o mapa encolhe para 60%: voce ve e alcanca muito mais |
| `ships.thunderbolt.salvo.zoomEaseSpeed` | `2.2` | rapidez da transicao de camera |
| `ships.thunderbolt.salvo.bulletSizeMul` | `2.4` | hitbox maior: o tiro pega area, nao ponto |
| `ships.thunderbolt.salvo.bulletDmgMul` | `1` | dano por tiro (x o dano normal do canhao) |
| `ships.thunderbolt.salvo.bulletSpeed` | `1600` | (tempo subindo (ja invulneravel)) |
| `ships.thunderbolt.salvo.spawnDist` | `300` | de que altura o tiro "cai" |
| `ships.thunderbolt.salvo.angleDeg` | `70` | inclinacao da queda (90 = reto de cima) |
| `ships.thunderbolt.salvo.spreadPx` | `34` | espalhamento no chao ao redor do cursor |
| `ships.thunderbolt.salvo.fireRate` | `70` | tiros por segundo durante o salvo |
| `ships.thunderbolt.salvo.abilityAoeBonus` | `0.25` | Zuni e Missil ganham +25% de area durante o salvo |
| `ships.thunderbolt.attrOverride.rof.n` | `'Cano Resistente'` | teto de 10 níveis |
| `ships.thunderbolt.attrOverride.rof.icon` | `'🌡'` | teto de 10 níveis |
| `ships.thunderbolt.attrOverride.rof.cap` | `10` | teto de 10 níveis |
| `ships.thunderbolt.attrOverride.rof.d` | `'+12,5 de capacidade de calor e +2,78/s de resfriamento por nível. No nível 10 você segura o gatilho o dobro do tempo (8s em vez de 4s)'` | (teto de 10 níveis) |
| `ships.thunderbolt.attrExtra` | `[{ id:'turn', n:'Manobrabilidade', icon:'🔄', d:'+12% de taxa de giro por nível (curva mais fechada)' }]` | [SALVO (tecla Q): sobe, some no ceu e metralha o mapa de cima por alguns segundos. Nao tem niveis: escala pelos seus atributos e passivas, como o canhao normal.] |
| `ships.thunderbolt.colors.hull` | `'#cfd8dc'` | cor do casco |
| `ships.thunderbolt.colors.accent` | `'#ffd23a'` | cor de destaque |
| `ships.thunderbolt.colors.glow` | `'#b6ff00'` | cor do brilho |
| `ships.thunderbolt.blocked` | `['dash']` | power-ups que esta nave nunca recebe [SALVO (tecla Q): sobe, some no ceu e metralha o mapa de cima por alguns segundos. Nao tem niveis: escala pelos seus atributos e passivas, como o canhao normal.] |

<a id="progression"></a>
## Progressão (XP e cartas)

| caminho | valor | o que faz |
|---|---|---|
| `progression.xpFirstLevel` | `12` | chips para ir do nivel 1 ao 2 |
| `progression.xpCurveMultiplier` | `2` | multiplica a curva inteira (maior = sobe de nivel mais devagar) |
| `progression.xpBase` | `6` | curva: mult*(base + lvl*linear + lvl^power) |
| `progression.xpLinear` | `3.2` | curva: mult*(base + lvl*linear + lvl^power) |
| `progression.xpPower` | `1.45` | curva: mult*(base + lvl*linear + lvl^power) |
| `progression.cardEveryNLevels` | `4` | carta (power-up/passiva) a cada N niveis |

<a id="audio"></a>
## Volumes

| caminho | valor | o que faz |
|---|---|---|
| `audio.master` | `0.55` | volumes (0 a 1) |
| `audio.sfx` | `0.9` | volumes (0 a 1) |
| `audio.music` | `0.32` | volumes (0 a 1) |

<a id="music"></a>
## Música

| caminho | valor | o que faz |
|---|---|---|
| `music.bpm` | `140` | andamento base: marcha funk de fliperama (Space Cadet) |
| `music.bossBpmMul` | `0.9` | warden: um pouco mais lento, porém mais pesado |
| `music.dragonBpmMul` | `1.22` | dragão: frenético e ameaçador |
| `music.eliteBpmMul` | `1.05` | andamento extra com elite, storm, reta final (13 min+) e jackpot |
| `music.stormBpmMul` | `1.08` | andamento extra com elite, storm, reta final (13 min+) e jackpot |
| `music.finaleBpmMul` | `1.12` | andamento extra com elite, storm, reta final (13 min+) e jackpot |
| `music.jackpotBpmMul` | `1.3` | andamento extra com elite, storm, reta final (13 min+) e jackpot |
| `music.bassVol` | `0.19` | baixo-metralhadora (motor do groove): reforçado |
| `music.subVol` | `0.12` | SEGUNDO baixo: sub-bass senoidal uma oitava abaixo, dobrando o riff |
| `music.droneVol` | `0.034` | drone espacial grave de fundo |
| `music.stabVol` | `0.10` | stabs de "metais" (fanfarra) |
| `music.leadVol` | `0.08` | trompete sintético (lead): mais discreto e toca menos |
| `music.drumVol` | `1` | bateria como um todo |
| `music.leadOn` | `true` | desligue camadas se quiser a base mais crua |
| `music.stabsOn` | `true` | desligue camadas se quiser a base mais crua |
