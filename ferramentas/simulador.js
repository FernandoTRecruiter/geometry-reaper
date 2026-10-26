/* simulador.js: robô de testes que roda DENTRO da página do jogo.
 *
 * Por que existe: medir balanceamento jogando à mão é lento e cheio de achismo.
 * Este arquivo é injetado pelo simula_balanceamento.py e chama as funções do
 * próprio motor (update, spawnBoss, spawnDragon...) com o relógio acelerado:
 * 1 minuto de jogo roda em poucos segundos, sem desenhar a tela.
 *
 * Regras do robô:
 *  - ele nunca morre (invulnerável), mas anota o dano que teria levado;
 *  - mira sempre no alvo certo (é um jogador "perfeito" de mira);
 *  - não anda (exceto o Thunderbolt, que voa sozinho por natureza).
 * Os números servem para COMPARAR naves e versões, não para prever a sua run.
 */
'use strict';
var SIM = (function(){
  const DT = 1/60; // passo da simulação: o mesmo de um monitor de 60 Hz

  // Monta uma run "de laboratório": nave, atributos, habilidades e passivas escolhidos a dedo.
  function prepara(nave, build, minuto){
    for (const k in keys) keys[k] = false; // nenhuma tecla presa da medição anterior
    mouse.l = false;
    newRun(null);
    chosenShip = nave; G.ship = nave;
    const b = build || {};
    for (const k in (b.attrs || {})) G.attrs[k] = b.attrs[k];
    for (const [id, lvl] of (b.ativas || [])) {
      const def = ACTIVES.find(a => a.id === id); if (!def || !powerAllowed(id)) continue;
      const inst = {def, lvl, cd:0}; if (def.charges) inst.charges = maxCharges(inst);
      G.actives.push(inst);
    }
    for (const [id, lvl] of Object.entries(b.passivas || {})) if (powerAllowed(id)) G.passives[id] = lvl;
    G.p.lvl = b.nivel || 1;
    recalcStats(); G.p.hp = G.p.maxHp; G.p.shield = G.p.maxShield;
    // laboratório: ninguém nasce sozinho e nenhum evento dispara
    G.enemies.length = 0; G.ebullets.length = 0; G.chips.length = 0;
    G.nextStorm = G.nextAst = G.nextBoss = G.nextGoblin = 1e9; G.nextDragonLvl = 1e9; G.noSpawn = true;
    G.t = (minuto || 0) * 60;
    shakeX = shakeY = 0;
    state = 'sim'; // estado que o laço normal ignora: só o robô chama update()
  }

  // Põe o mouse em cima de um ponto do mundo (a mira das naves lê o mouse).
  function miraEm(x, y){ mouse.x = x - cam.x; mouse.y = y - cam.y; }

  // Mira do Thunderbolt: ele voa SEMPRE na direção do mouse. Se o mouse ficar em cima
  // do alvo, o avião acaba girando em volta dele sem nunca apontar o nariz (órbita).
  // Um piloto de verdade faz PASSADAS: mergulha, passa do alvo, se afasta e volta.
  function miraVoo(alvo){
    if (G._labFixo) { miraEm(alvo.x, alvo.y); return; } // laboratório de TTK: sem pilotagem
    const p = G.p, d = Math.hypot(alvo.x - p.x, alvo.y - p.y);
    if (p._saida > 0) { // curva fechada de um lado só, freando (S) para o raio ficar curto
      p._saida -= DT; keys.KeyS = true;
      const a = p.heading + p._lado * 1.4;
      miraEm(p.x + Math.cos(a) * 300, p.y + Math.sin(a) * 300);
      if (p._saida > 0) return;
    }
    keys.KeyS = false;
    if (d < 160) { p._saida = 1.3; p._lado = Math.random() < 0.5 ? 1 : -1; } // passou do alvo: dá a volta
    miraEm(alvo.x, alvo.y);
  }
  function mira(alvo){ if (!alvo) return; if (shipDef().flight) miraVoo(alvo); else miraEm(alvo.x, alvo.y); }
  // só atira com o nariz apontado (até ~17 graus de erro), para não esquentar o cano à toa
  function narizNoAlvo(alvo){
    if (!alvo || !shipDef().flight) return true;
    const p = G.p, want = Math.atan2(alvo.y - p.y, alvo.x - p.x);
    let da = want - p.heading; da = Math.atan2(Math.sin(da), Math.cos(da));
    return Math.abs(da) < 0.3;
  }

  // Gatilho: cada nave tem o seu jeito ideal de atirar.
  //  Cruiser 'toque': aperta e solta todo quadro (tiro rápido sem carga).
  //  Cruiser 'laser': segura até a carga cheia e solta (vira o canhão laser).
  //  Thunderbolt: segura até 97% do calor e espera esfriar até 25%.
  function gatilho(estilo, alvo){
    const SH = shipDef(), p = G.p;
    if (!SH.manualFire) { mouse.l = false; return; }
    if (!narizNoAlvo(alvo)) { mouse.l = false; return; }
    if (SH.weapon === 'rail') {
      if (estilo === 'laser') mouse.l = !p.chFull;          // segura até encher
      else mouse.l = !mouse.l;                              // toca e solta
      return;
    }
    if (SH.weapon === 'gatling') {
      const g = gatlingCfg();
      if (p.heatLockT > 0) { mouse.l = false; return; }
      if (p._esfriando) { if (p.heat <= g.heatMax * 0.25) p._esfriando = false; mouse.l = false; return; }
      if (p.heat >= g.heatMax * 0.97) { p._esfriando = true; mouse.l = false; return; }
      mouse.l = true;
    }
  }

  // Usa todas as habilidades prontas (menos o Dash, que tiraria o robô do lugar).
  function usaHabilidades(){
    const antes = state; state = 'game'; // useActive só funciona com o jogo "rodando"
    for (let i = 0; i < G.actives.length; i++) if (G.actives[i].def.id !== 'dash') useActive(i);
    state = antes;
  }

  // Um passo de jogo com o robô no controle.
  function passo(alvo, estilo, habilidades){
    G.p.invuln = Math.max(G.p.invuln, 0.5);
    mira(alvo);
    gatilho(estilo, alvo);
    if (habilidades) usaHabilidades();
    update(DT);
  }

  // TEMPO PARA MATAR (TTK): quantos segundos a nave leva para derrubar um alvo.
  //  alvo: 'warden' | 'goblin' | 'dragao'
  //  O dragão tem vida enorme: medimos o dano em `janela` segundos e projetamos.
  function ttk(nave, build, alvo, opcoes){
    const o = opcoes || {};
    prepara(nave, build, o.minuto || 0);
    let ref = null, vidaIni = 0;
    if (alvo === 'warden') { spawnBoss(); ref = G.bossRef; }
    if (alvo === 'goblin') {
      spawnGoblin(); ref = G.goblinRef; ref.spd = 0; ref.life = 1e9; // parado e sem fugir: TTK puro
      const a = Math.random() * TAU; ref.x = G.p.x + Math.cos(a) * 300; ref.y = G.p.y + Math.sin(a) * 300;
    }
    if (alvo === 'dragao') { spawnDragon(); }
    G.pendingPicks.length = 0; state = 'sim';
    vidaIni = alvo === 'dragao' ? G.dragon.maxHp : ref.maxHp;
    const limite = o.limite || 120, janela = o.janela || 40, x0 = G.p.x, y0 = G.p.y;
    G._labFixo = true;
    let t = 0;
    while (t < limite) {
      // tira do caminho o que não é o alvo (minions do warden), para medir só o alvo
      for (const e of G.enemies) if (!e.dead && !e.boss && !e.dragon && e.type !== 'goblin') e.dead = true;
      let mira;
      if (alvo === 'dragao') { if (!G.dragon) break; mira = G.dragon.segs[0]; }
      else { if (ref.dead) break; mira = ref; }
      // Thunderbolt no laboratório: "arma ideal", nariz sempre no alvo e avião parado no lugar.
      // Mede o teto do canhão; o custo de pilotar (fazer passadas) fica de fora de propósito.
      if (shipDef().flight) { G.p.x = x0; G.p.y = y0; G.p.heading = Math.atan2(mira.y - y0, mira.x - x0); }
      // warden "de treino": parado a 300 px e sem atacar, para todas as naves serem medidas igual
      if (alvo === 'warden') { ref.x = x0 + 300; ref.y = y0; ref.atkT = 99; ref.telegraph = 0; ref.dashLeft = 0; G.ebullets.length = 0; }
      passo(mira, o.estilo, o.habilidades);
      if (state !== 'sim') { G.pendingPicks.length = 0; state = 'sim'; } // fecha a carta da recompensa
      t += DT;
      if (alvo === 'dragao' && t >= janela) break;
    }
    if (alvo === 'dragao') {
      const D = G.dragon, dano = D ? (D.maxHp - D.hp) : vidaIni;
      const dps = dano / t;
      return {alvo, vida: Math.round(vidaIni), segundos_medidos: +t.toFixed(1), dps: Math.round(dps), ttk: Math.round(vidaIni / Math.max(dps, 0.01))};
    }
    return {alvo, vida: Math.round(vidaIni), ttk: ref.dead ? +t.toFixed(1) : null, dps: Math.round((vidaIni - Math.max(0, ref.hp)) / t)};
  }

  // ROBÔ DE SOBREVIVÊNCIA: joga uma run acelerada parado no meio da arena,
  // coletando todo chip (aspirador ligado) e escolhendo cartas e atributos sozinho.
  // Devolve uma linha por minuto: nível, inimigos vivos, dano que levaria etc.
  function sobrevive(nave, minutos, opcoes){
    const o = opcoes || {};
    for (const k in keys) keys[k] = false; mouse.l = false;
    newRun(o.desafio ? {id:'fivemin', n:'Desafio', timeLimit:TWEAKS.desafio ? TWEAKS.desafio.endSec : 300, fiveMin:true} : null);
    chosenShip = nave; G.ship = nave; recalcStats(); G.p.hp = G.p.maxHp; G.p.shield = G.p.maxShield;
    shakeX = shakeY = 0; state = 'sim';
    const ordem = o.ordemAtributos || ['rof','dmg','rof','dmg','crit','energy'];
    let iAttr = 0, recebido = 0, mortesAsteroide = 0;
    const dpOrig = damagePlayer, llOrig = loseLife;
    // espiões: contam o dano em vez de aplicar (o robô não pode morrer)
    damagePlayer = function(d, src, m){ if (G.p.invuln > 0 || G.p.dashT > 0) return; recebido += d; };
    loseLife = function(){ mortesAsteroide++; G.p.hp = G.p.maxHp; };
    const linhas = []; let proxMin = 1, t = 0, dragaoT0 = null, dragaoMorto = null;
    try {
      while (t < minutos * 60 && !G.over) {
        G.chipVacuum = true;
        // resolve escolhas pendentes como um jogador apressado
        let guarda = 0;
        // o motor só abre a escolha se o estado for 'game'; o robô abre na mão
        if (state === 'sim' && G.pendingPicks.length) { state = 'game'; openPick(); }
        while (state !== 'sim' && guarda++ < 50) {
          if (state === 'slot') { try { slotOpts[0].apply(); } catch (e) {} closePick(); }
          else if (state === 'attrpick') {
            let id = ordem[iAttr++ % ordem.length], tries = 0;
            while (attrMaxed(id) && tries++ < 10) id = ordem[iAttr++ % ordem.length];
            applyAttr(id); G.pendingPicks.shift();
            document.getElementById('attrPick').classList.add('hidden');
            if (G.pendingPicks.length) openPick(); else state = 'game';
          }
          if (state === 'game') state = 'sim';
          if (state === 'gameover') break;
        }
        if (G.over) break;
        // alvo: cabeça do dragão, senão warden, senão o inimigo mais perto
        let alvo = null;
        if (G.dragon) alvo = G.dragon.segs[0];
        else if (G.bossRef && !G.bossRef.dead) alvo = G.bossRef;
        else { let bd = Infinity; for (const e of G.enemies) { if (e.dead) continue; const d = dist2(G.p.x, G.p.y, e.x, e.y); if (d < bd) { bd = d; alvo = e; } } }
        // aqui o robô NÃO fica invulnerável: o espião acima conta o dano sem matar
        G.p.invuln = 0;
        mira(alvo);
        gatilho(o.estilo, alvo); usaHabilidades();
        update(DT);
        if (G.dragon && dragaoT0 === null) dragaoT0 = t;
        if (dragaoT0 !== null && !G.dragon && dragaoMorto === null) dragaoMorto = t;
        t += DT;
        if (t >= proxMin * 60) {
          linhas.push({min: proxMin, nivel: G.p.lvl, inimigos: G.enemies.filter(e => !e.dead).length,
                       abates: G.kills, dano_recebido: Math.round(recebido), cartas: G.actives.length + Object.keys(G.passives).length,
                       dragao_vida: G.dragon ? Math.round(G.dragon.hp) : null});
          recebido = 0; proxMin++;
        }
      }
    } finally { damagePlayer = dpOrig; loseLife = llOrig; state = 'menu'; }
    return {nave, linhas, mortes_asteroide: mortesAsteroide, dragao_apareceu_seg: dragaoT0 && Math.round(dragaoT0),
            dragao_morreu_em_seg: dragaoMorto !== null ? Math.round(dragaoMorto - dragaoT0) : null,
            nivel_final: G.p.lvl, venceu: !!G.won};
  }

  return {prepara, ttk, sobrevive, passo};
})();
