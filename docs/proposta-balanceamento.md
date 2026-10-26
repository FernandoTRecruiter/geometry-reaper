# Proposta de balanceamento (para o Fernando decidir)

O que está aqui **não foi aplicado**: são mudanças de gosto ou de identidade das naves. Cada item traz o problema medido, a recomendação e o número a mexer no `TWEAKS`. O que já foi aplicado está no `CHANGELOG.md`.

## Mini dicionário

- **Dano por segundo (DPS):** quanto de vida a nave tira de um alvo por segundo, em média.
- **Tempo para matar (TTK):** segundos para derrubar um alvo. TTK = vida do alvo / DPS.
- **Build:** o conjunto de atributos e cartas que você montou na run.
- **Carta morta:** opção que aparece para escolher mas não muda nada no jogo.

## Como os números foram medidos

`python ferramentas/simula_balanceamento.py` abre o jogo num navegador sem janela e um robô joga acelerado. O robô mira perfeito e não morre, então os tempos são o **melhor caso**: na sua mão, desviando, a luta demora mais. Servem para comparar naves entre si.

Build típica usada: 1 ponto de atributo por nível (menos nos níveis de carta), na ordem cadência, dano, cadência, dano, crítico. "Com cartas" = JDAM Nv2, Míssil Nv2, Zuni Nv2, Disparo Múltiplo Nv2, Tiros Perfurantes Nv1 e Munição Explosiva Nv2 (o que a nave puder pegar). Warden de treino: parado a 300 px, sem atacar.

### Tempo para matar, versão 1.2 (segundos)

| Alvo | Fighter | Warrior | Cruiser (toque) | Cruiser (laser) | Thunderbolt |
|---|---:|---:|---:|---:|---:|
| Goblin, Nv10 (2,5 min) | 7,5 | 7,1 | 11,7 | 18,4 | 11,3 |
| Warden, Nv15 (4 min) | 11,1 | 10,0 | 26,4 | 54,1 | 39,3 |
| Warden, Nv25 (8 min) | 11,2 | 10,0 | 18,2 | 54,9 | 42,6 |
| Dragão Nv20, só a arma | 126 | 105 | 244 | 455 | 403 |
| Dragão Nv20, com cartas | 45 | 36 | 171 | 222 | 53 |

O goblin foge em 20 s. O Thunderbolt foi medido com o nariz sempre no alvo (o teto da arma, sem o custo de pilotar).

## 1. Cruiser fraco contra chefes (prioridade alta)

**Problema.** Contra a horda o Cruiser vai bem (o railgun atravessa a fila inteira), mas contra alvo único ele leva 2,4x o tempo do Fighter no warden e 4x no dragão com cartas. Antes da versão 1.2 ele parecia forte contra o dragão só por causa de dois bugs (dano contado em cada elo e acerto repetido do tiro perfurante). Além disso, o Cruiser não pode pegar **Disparo Múltiplo**, a carta que mais multiplica dano contra alvo grande (no Fighter, as passivas levam o dragão de 332 para 1337 de dano/s; no Cruiser, de 177 para 188).

**Recomendação.** Duas mudanças pequenas:

| Parâmetro | Hoje | Proposto | Efeito medido |
|---|---|---|---|
| `ships.cruiser.rail.damage` | 68 | 95 | warden Nv15: 26 s para 19 s; dragão com cartas: 171 s para 140 s |
| `ships.cruiser.rail.beamDmgMul` | 3 | 2.15 | mantém o laser em ~204 de dano/s (não mexe nele) |

Mesmo assim o dragão continua longo para o Cruiser. Para fechar a diferença de verdade, a saída é de design: dar ao Cruiser um substituto do Disparo Múltiplo (as quatro bases vermelhas de torreta já desenhadas no casco são o lugar natural).

## 2. Thunderbolt não escala (prioridade alta)

**Problema.** O atributo de cadência dele virou "Cano Resistente", que só aumenta quanto tempo você segura o gatilho. As outras naves ganham +42% de dano por segundo a cada ponto de Rate of Fire; o Thunderbolt ganha só com o atributo Dano (+18%). Resultado: no warden ele leva 39 s no Nv15 e 43 s no Nv25 (piora relativa com o tempo), contra 11 s do Fighter. E isso é o teto, com mira perfeita.

**Recomendação.**

| Parâmetro | Hoje | Proposto | Efeito medido |
|---|---|---|---|
| `ships.thunderbolt.gatling.damage` | 1.2 | 2.2 | warden Nv15: 39 s para 21 s; Nv25: 43 s para 23 s |

Alternativa mais fiel ao conceito (pede código): o Cano Resistente também acelerar o cano, por exemplo +6% de `fireRateMax` por nível. Assim o atributo passa a escalar dano como nas outras naves.

## 3. Laser do Cruiser é uma armadilha contra alvo único (média)

**Problema.** Segurar 8 s para o laser rende 56 de dano/s no warden Nv15; tocar o gatilho rende 114. O laser só compensa contra uma fila de inimigos, mas o jogador aprende que "carga cheia = mais forte" e cai na armadilha.

**Recomendação.**

| Parâmetro | Hoje | Proposto | Efeito medido |
|---|---|---|---|
| `ships.cruiser.rail.chargeSec` | 8 | 4 | warden Nv15 com laser: 54 s para 32 s |
| `ships.cruiser.rail.minChargeSec` | 6 | 2.5 | idem no Nv25: 55 s para 31 s |

O toque continua melhor contra alvo único, mas a diferença cai de 2x para 1,2x.

## 4. Vida do dragão (confirmar o valor aplicado)

Apliquei 30000 (era 60000) para compensar a correção do dano por elo. Tempo do robô com a build típica com cartas, no Nv20:

| `dragon.hp` | Fighter | Warrior | Thunderbolt | Cruiser |
|---|---:|---:|---:|---:|
| 20000 (igual à luta de antes da correção) | 30 s | 24 s | 35 s | 114 s |
| **30000 (aplicado)** | 45 s | 36 s | 53 s | 171 s |
| 60000 (número antigo) | 90 s | 72 s | 106 s | 342 s |

**Recomendação:** manter 30000 e jogar uma luta de verdade. Se ficar longa na mão, 25000.

## 5. Dragão do Survival apaga o warden sem recompensa (média)

**Problema.** No Survival o dragão aparece no nível 20, que o robô atinge entre 4:10 e 5:40, logo depois do warden das 4:00. A limpeza da arena mata o warden **sem dar a carta** dele.

**Recomendação (pede código):** se houver warden vivo, o dragão espera ele morrer; ou a limpeza entrega a carta do warden. Prefiro a espera: mantém duas lutas separadas.

## 6. Goblin quase impossível para o Cruiser na prática (baixa)

**Problema.** Parado, o Cruiser mata o goblin em 10 a 12 s (cabe nos 20 s). Mas o goblin foge a 130 a 215 px/s e fica invisível a mais de 220 px; o Cruiser anda no máximo a 164 px/s, com inércia de navio. A conta fecha no papel e não fecha no controle.

**Recomendação (pede código):** o goblin fugir 30% mais devagar quando você joga de Cruiser. Aumentar `mobs.goblin.decloakRange` também ajudaria, mas facilita para todas as naves.

## 7. Fim de jogo achata (baixa, hipótese)

**Problema.** Por volta de 10 min o intervalo entre levas chega ao piso (`spawnIntervalMin` 0,14 s) e o teto de inimigos chega a 320 (`capMax`). Depois disso só a vida dos inimigos cresce, e devagar (+22% por minuto, linear), enquanto o dano do jogador cresce multiplicado (cadência x dano). No robô do Fighter, o dano recebido por minuto para de subir depois dos 9 min.

**Recomendação:** testar `difficulty.hpScalePerMin` de 0.22 para 0.30 e ver se o fim da run volta a apertar. É a parte menos confiável da análise: o robô fica parado, um jogador de verdade não.

## 8. Pilotagem do Thunderbolt (gosto)

**Problema.** Se você deixa o mouse em cima do alvo, o avião entra em órbita em volta dele e nunca aponta o nariz (raio mínimo de curva: 68 px a 150 px/s). É preciso fazer passadas. O robô simples ficou preso nisso e no modo Desafio não chegou ao nível 10.

**Recomendação:** é a identidade da nave, então eu não mudaria a física. Uma ajuda leve: o canhão corrigir até ~8 graus na direção do inimigo mais próximo do nariz.

## O que está equilibrado (não mexer)

- **Fighter x Warrior:** o Warrior tem ~10% mais dano por segundo (duas torretas de 8 contra um tiro de 14) e mira livre; o Fighter tem mira automática e o Drone de Apoio exclusivo. Troca justa.
- **Warden:** o tempo para matar fica estável entre o Nv15 e o Nv25 (~11 s no Fighter), sinal de que a vida dele acompanha a build.
- **Goblin:** 7 a 9 s no Fighter em qualquer fase, com folga dentro dos 20 s.
- **Roleta de atributos:** rende em média 2 pontos contra 1 garantido, mas em atributos sorteados. Vale para quem não precisa de um atributo específico, e a escolha direta segue útil para quem precisa.
