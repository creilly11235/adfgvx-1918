/* The pinned graphics of the article. Each chapter's graphic is built from
   window.STORY_DATA and shows one state per passage; story-scroll.js calls
   go(state) when the reader moves from one passage to the next. */
(() => {
  'use strict';
  const D = window.STORY_DATA;
  const COORD = 'ADFGVX';
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');

  function node(tag, className, text) {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = text;
    return el;
  }
  function card(text, kind) {
    return node('span', 't ' + kind, text);
  }
  // Symbol chips in groups of five, as the log prints them.
  function groupLine(groups, perLine, mark) {
    const wrap = node('div', 'glog');
    for (let i = 0; i < groups.length; i += perLine) {
      const line = node('div', 'glog-line');
      groups.slice(i, i + perLine).forEach((group, j) => {
        const chip = node('span', 'glog-group', group);
        if (mark) mark(chip, i + j);
        line.append(chip);
      });
      wrap.append(line);
    }
    return wrap;
  }
  // The 6 by 6 square with its row and column labels.
  function square(cells, highlight) {
    const wrap = node('div', 'sq');
    wrap.append(node('span', 'sq-corner'));
    COORD.split('').forEach(ch => wrap.append(node('span', 'sq-label sq-col', ch)));
    for (let r = 0; r < 6; r++) {
      wrap.append(node('span', 'sq-label sq-row', COORD[r]));
      for (let c = 0; c < 6; c++) {
        const ch = cells[r * 6 + c];
        const cell = node('span', 'sq-cell' + (ch === '?' ? ' is-unknown' : ''), ch === '?' ? '·' : ch);
        cell.dataset.row = COORD[r];
        cell.dataset.col = COORD[c];
        if (highlight) highlight(cell, r, c, ch);
        wrap.append(cell);
      }
    }
    return wrap;
  }
  function label(text) {
    return node('p', 'glabel', text);
  }

  /* Chapter 1. ANGRIFF through the square and the key 3 1 4 2. */
  class HowGraphic {
    constructor(host) {
      const ex = D.example;
      this.host = host;
      this.root = node('div', 'g-how');
      // The message.
      this.msg = node('div', 'g-row');
      this.msgLetters = ex.word.split('').map((ch, i) => {
        const pair = node('span', 'g-pair');
        pair.append(card(ch, 'decoded'));
        const syms = node('span', 'g-syms');
        syms.append(card(ex.interim[2 * i], 'encoded'), card(ex.interim[2 * i + 1], 'encoded'));
        pair.append(syms);
        this.msg.append(pair);
        return pair;
      });
      this.msgLabel = label('The message');
      // The square, with the first letter's row and column marked.
      this.sqLabel = label('The square used from 10 to 12 November 1918');
      this.sq = square(ex.square, (cell, r, c, ch) => {
        if (ch === ex.word[0]) cell.classList.add('is-hit');
        if (COORD[r] === ex.interim[0]) cell.classList.add('is-row');
        if (COORD[c] === ex.interim[1]) cell.classList.add('is-col');
      });
      // The transposition block under the key.
      this.blkLabel = label('Written under the key 3 1 4 2');
      this.blk = node('div', 'blk');
      this.blk.style.setProperty('--cols', ex.key.length);
      this.keyCells = ex.key.map(k => { const el = node('span', 'blk-key', String(k)); this.blk.append(el); return el; });
      this.blkCells = ex.interim.split('').map((ch, i) => {
        const el = card(ch, 'encoded');
        el.dataset.col = i % ex.key.length;
        this.blk.append(el);
        return el;
      });
      // The cipher read off column by column.
      this.ctLabel = label('Read off column by column, in the order of the numbers');
      this.ct = node('div', 'g-row g-ct');
      this.ctCols = ex.columns.map((col, i) => {
        const w = node('span', 'g-col');
        w.dataset.rank = ex.key[i];
        col.split('').forEach(ch => w.append(card(ch, 'encoded')));
        return w;
      });
      [...this.ctCols].sort((a, b) => a.dataset.rank - b.dataset.rank).forEach(w => this.ct.append(w));
      this.ctGroups = node('div', 'g-row g-ct');
      ex.groups.forEach(g => { const w = node('span', 'g-col'); g.split('').forEach(ch => w.append(card(ch, 'encoded'))); this.ctGroups.append(w); });
      this.root.append(this.msgLabel, this.msg, this.sqLabel, this.sq, this.blkLabel, this.blk, this.ctLabel, this.ct, this.ctGroups);
      host.append(this.root);
      this.show(0);
    }
    show(stage) {
      const r = this.root;
      r.dataset.stage = stage;
      const vis = (el, on) => el.classList.toggle('is-off', !on);
      vis(this.sqLabel, stage >= 1 && stage <= 2); vis(this.sq, stage >= 1 && stage <= 2);
      vis(this.blkLabel, stage >= 3 && stage <= 4); vis(this.blk, stage >= 3 && stage <= 4);
      vis(this.ctLabel, stage === 4); vis(this.ct, stage === 4);
      vis(this.ctGroups, stage === 5);
      this.msgLabel.textContent = stage >= 5 ? 'The message and its cryptogram' : 'The message';
      this.msgLetters.forEach((pair, i) => {
        pair.classList.toggle('is-shown', stage >= 2 || (stage === 1 && i === 0));
        pair.classList.toggle('is-focus', stage === 1 && i === 0);
      });
      this.blkCells.forEach(el => el.classList.toggle('is-read', stage === 4));
      this.keyCells.forEach(el => el.classList.toggle('is-read', stage === 4));
      if (stage === 4) this.readOff();
      else this.ctCols.forEach(w => w.classList.remove('is-on'));
    }
    readOff() {
      if (this.timers) this.timers.forEach(clearTimeout);
      this.timers = [];
      const order = [...this.ctCols].sort((a, b) => a.dataset.rank - b.dataset.rank);
      order.forEach((w, i) => {
        w.classList.remove('is-on');
        const show = () => {
          w.classList.add('is-on');
          const col = this.ctCols.indexOf(w);
          this.blkCells.forEach(el => el.classList.toggle('is-lit', Number(el.dataset.col) === col));
          this.keyCells.forEach((el, k) => el.classList.toggle('is-lit', k === col));
        };
        if (reduced.matches) show(); else this.timers.push(setTimeout(show, 350 + i * 700));
      });
    }
    foot() { return this.root.getBoundingClientRect().bottom; }
  }

  /* Chapter 2. Every entry of Childs's log as one cell. */
  class LogGraphic {
    constructor(host) {
      this.root = node('div', 'g-log');
      this.label = label('The 688 entries of the log, in order');
      this.grid = node('div', 'loggrid');
      this.cells = D.grid.map(row => {
        const el = node('span', 'logcell');
        el.dataset.group = row.group;
        if (row.ours) el.dataset.ours = '1';
        if (row.schmeh) el.dataset.schmeh = '1';
        el.title = row.id + ', page ' + row.page + ', ' + row.date + ', ' + row.status;
        this.grid.append(el);
        return el;
      });
      this.legend = node('div', 'legend');
      this.root.append(this.label, this.grid, this.legend);
      host.append(this.root);
      this.show(1);
    }
    show(stage) {
      this.root.dataset.stage = stage;
      const c = D.counts;
      const items = [];
      if (stage >= 2) items.push(['solved', 'read with a published key']);
      if (stage >= 3) items.push(['schmeh', 'on Schmeh’s list of unsolved messages']);
      if (stage >= 4) items.push(['ours', 'first published here']);
      items.push(['unsolved', stage >= 2 ? 'no solution published here' : 'one entry']);
      this.legend.replaceChildren(...items.map(([k, text]) => {
        const item = node('span');
        const dot = node('i'); dot.dataset.group = k;
        item.append(dot, text);
        return item;
      }));
      this.label.textContent = stage >= 4 ? c.ours + ' entries first read here, among ' + c.total + ' in the log'
        : stage >= 3 ? c.schmehRecords + ' entries on Schmeh’s list, among ' + c.total + ' in the log'
        : stage >= 2 ? c.readable + ' of the ' + c.total + ' entries read under a published key'
        : 'The ' + c.total + ' entries of the log, in order';
    }
    foot() { return this.legend.getBoundingClientRect().bottom; }
  }

  /* Chapter 3. Message 2305, the gap and the fill. */
  class GapGraphic {
    constructor(host) {
      const m = D.featured.m2305;
      this.m = m;
      this.root = node('div', 'g-gap');
      this.label = label('');
      // The log's 44 groups, eight to a line, and the four restored groups.
      const groups = m.groups.slice();
      const restored = groups.slice(0, m.gap.groupIndex).concat(Array(m.gap.groupCount).fill('·····'), groups.slice(m.gap.groupIndex));
      this.log = groupLine(restored, m.groupsPerLine, (chip, i) => {
        if (i >= m.gap.groupIndex && i < m.gap.groupIndex + m.gap.groupCount) chip.classList.add('is-gap');
      });
      // The transposition block, lost letters as gaps.
      this.blk = node('div', 'blk blk-plain');
      this.blk.style.setProperty('--cols', m.rowWidth);
      this.blkCells = m.plainBlank.split('').map((ch, i) => {
        const el = card(ch === '-' ? '' : ch, ch === '-' ? 'lost' : 'decoded');
        el.dataset.i = i;
        this.blk.append(el);
        return el;
      });
      // The six candidates of the first lost letter.
      const first = m.candidates[0];
      this.cand = node('div', 'g-cand');
      this.cand.append(node('span', 'g-cand-label', 'The first lost letter kept its ' + first.kind + ' symbol, so it is one of'));
      const row = node('span', 'g-row');
      first.cells.forEach(ch => row.append(card(ch, ch === first.chosen ? 'decoded' : 'faint')));
      this.cand.append(row);
      // The reading.
      this.read = node('div', 'g-read');
      this.readDe = node('p', 'g-read-de', m.german);
      this.readEn = node('p', 'g-read-en', m.english);
      this.read.append(this.readDe, this.readEn);
      this.root.append(this.label, this.log, this.blk, this.cand, this.read);
      host.append(this.root);
      this.show(1);
    }
    show(stage) {
      const m = this.m;
      const r = this.root;
      r.dataset.stage = stage;
      const vis = (el, on) => el.classList.toggle('is-off', !on);
      vis(this.log, stage <= 2);
      vis(this.blk, stage >= 3 && stage <= 5);
      vis(this.cand, stage === 4);
      vis(this.read, stage === 6);
      this.log.classList.toggle('show-gap', stage >= 2);
      this.blkCells.forEach((el, i) => {
        const lost = m.plainBlank[i] === '-';
        if (!lost) return;
        const filled = stage >= 5;
        el.textContent = filled ? m.plain[i] : '';
        el.classList.toggle('filled', filled);
        el.classList.toggle('is-focus', stage === 4 && i === m.candidates[0].letter);
      });
      this.label.textContent = stage >= 6 ? 'The reading, expanded and translated'
        : stage === 5 ? 'The block with all ' + m.lostLetters + ' lost letters filled'
        : stage === 4 ? 'Each lost letter has six candidates'
        : stage === 3 ? 'The block of ' + m.width + ' columns, one lost letter at the start of every row'
        : stage === 2 ? 'The four lost groups, at the start of the fifth line'
        : 'Part 1 as the log prints it, ' + m.symbolsInLog + ' symbols in ' + m.groups.length + ' groups';
    }
    foot() { return this.root.getBoundingClientRect().bottom; }
  }

  /* Chapter 4. Page 153, a key from 120 letters. */
  class KeyGraphic {
    constructor(host) {
      const p = D.featured.p153;
      this.p = p;
      this.root = node('div', 'g-key');
      this.label = label('');
      const part5 = p.parts[0], part6 = p.parts[1];
      this.log = node('div');
      this.log.append(node('p', 'g-sub', 'Part 5, ' + part5.symbolsInLog + ' symbols'), groupLine(part5.groups, 7),
        node('p', 'g-sub', 'Part 6, ' + part6.symbolsInLog + ' symbols, three groups lost'), groupLine(part6.groups, 7, (chip, i) => { if (/^-+$/.test(part6.groups[i])) chip.classList.add('is-gap'); }));
      // The block of part 5 under the 18 column key, columns coloured by kind.
      this.blk = node('div', 'blk blk-wide');
      this.blk.style.setProperty('--cols', p.width);
      this.keyCells = p.key.map(k => { const el = node('span', 'blk-key', String(k)); this.blk.append(el); return el; });
      const interim = part5.interimRows.join('');
      this.blkCells = interim.split('').map((ch, i) => {
        const el = card(ch, 'encoded');
        el.dataset.kind = i % 2 === 0 ? 'row' : 'col';
        this.blk.append(el);
        return el;
      });
      this.blkLegend = node('div', 'legend');
      [['row', 'a column of row labels'], ['col', 'a column of column labels']].forEach(([k, text]) => {
        const item = node('span'); const dot = node('i'); dot.dataset.kind = k; item.append(dot, text); this.blkLegend.append(item);
      });
      // The square.
      this.sq = square(p.square);
      // The reading in the rows of the block.
      this.read = node('div', 'g-readblk');
      const rowsOf = (text, w) => { const out = []; for (let i = 0; i < text.length; i += w) out.push(text.slice(i, i + w)); return out; };
      [['Part 5', part5.plain], ['Part 6', part6.plain]].forEach(([name, text]) => {
        const b = node('div', 'blk blk-plain');
        b.style.setProperty('--cols', p.rowWidth);
        text.split('').forEach(ch => {
          const lower = ch !== ch.toUpperCase();
          b.append(card(ch === '_' ? '' : ch.toUpperCase(), ch === '_' ? 'lost' : lower ? 'decoded filled' : 'decoded'));
        });
        this.read.append(node('p', 'g-sub', name), b);
      });
      this.text = node('div', 'g-read');
      this.text.append(node('p', 'g-read-de', p.german), node('p', 'g-read-en', p.english));
      this.root.append(this.label, this.log, this.blk, this.blkLegend, this.sq, this.read, this.text);
      host.append(this.root);
      this.show(1);
    }
    show(stage) {
      const p = this.p;
      this.root.dataset.stage = stage;
      const vis = (el, on) => el.classList.toggle('is-off', !on);
      vis(this.log, stage === 1);
      vis(this.blk, stage === 2); vis(this.blkLegend, stage === 2);
      vis(this.sq, stage === 3);
      vis(this.read, stage === 4);
      vis(this.text, stage === 5);
      this.label.textContent = stage >= 5 ? 'The reading, expanded and translated'
        : stage === 4 ? 'The two parts read in the rows of the block'
        : stage === 3 ? 'The square, with the ' + p.knownCells + ' cells the two parts use'
        : stage === 2 ? 'Part 5 under the ' + p.width + ' column key, each column of one kind'
        : 'The two surviving parts, ' + p.letters + ' letters in all';
    }
    foot() { return this.root.getBoundingClientRect().bottom; }
  }

  /* Chapter 5. The scores behind the two readings, on a number line. */
  class CheckGraphic {
    constructor(host) {
      const c153 = D.featured.p153.checks, c2305 = D.featured.m2305.checks;
      this.root = node('div', 'g-check');
      this.label = label('');
      this.panelA = this.line('Page 153, score of the whole pair', -310, -258, [
        {v: c153.shuffledBest, text: 'best of ten shuffled copies', kind: 'null', lift: 4},
        {v: c153.next, text: 'next best key', kind: 'null', lift: 4},
        {v: c153.plantedBar, text: 'bar set by planted keys', kind: 'bar', lift: 50},
        {v: c153.winner, text: 'the key found', kind: 'hit', lift: 4},
      ]);
      this.panelB = this.line('Message 2305, score per letter of the best fill', -4.3, -1.9, [
        {v: (c2305.shuffledScores[0] + c2305.shuffledScores[1]) / 2, span: c2305.shuffledScores, text: 'wrong keys and shuffled copies', kind: 'null', lift: 4},
        {v: c2305.plantedMedian, text: 'median of ' + c2305.plantedTotal + ' planted messages', kind: 'bar', lift: 56},
        {v: c2305.realScore, text: 'the reading', kind: 'hit', lift: 4},
      ]);
      this.panelC = node('div', 'g-check-notes');
      [
        'A second search, written without seeing the first, returned the same ' + D.featured.p153.width + ' column order.',
        'Run blind on the two part message of 13 November, the search returned the key George Lasry published in 2017, with the same ' + c153.page187.cells + ' square cells.',
        'The reading of message 2305, encrypted again, gives back all ' + D.featured.m2305.symbolsInLog + ' intercepted symbols.',
      ].forEach(text => this.panelC.append(node('p', 'g-check-note', text)));
      this.root.append(this.label, this.panelA, this.panelB, this.panelC);
      host.append(this.root);
      this.show(1);
    }
    line(title, lo, hi, marks) {
      const panel = node('div', 'nline');
      panel.append(node('p', 'g-sub', title));
      const track = node('div', 'nline-track');
      const pos = v => ((v - lo) / (hi - lo) * 100).toFixed(2) + '%';
      marks.forEach(mark => {
        const el = node('div', 'nline-mark ' + mark.kind);
        el.style.left = pos(mark.v);
        if (mark.span) { el.style.left = pos(mark.span[1]); el.style.width = ((mark.span[0] - mark.span[1]) / (hi - lo) * 100).toFixed(2) + '%'; el.classList.add('is-span'); }
        el.style.setProperty('--lift', (mark.lift || 4) + 'px');
        const tag = node('span', 'nline-tag');
        tag.append(node('b', '', mark.span ? mark.span[1] + ' to ' + mark.span[0] : String(mark.v)), node('span', '', mark.text));
        el.append(tag);
        track.append(el);
      });
      const axis = node('div', 'nline-axis');
      axis.append(node('span', '', String(lo)), node('span', '', 'higher is more like German'), node('span', '', String(hi)));
      panel.append(track, axis);
      return panel;
    }
    show(stage) {
      this.root.dataset.stage = stage;
      const vis = (el, on) => el.classList.toggle('is-off', !on);
      vis(this.panelA, stage === 1);
      vis(this.panelB, stage === 2);
      vis(this.panelC, stage === 3);
      this.label.textContent = stage === 3 ? 'Three further checks'
        : stage === 2 ? 'The fill of message 2305 against its controls'
        : 'The page 153 key against its controls';
    }
    foot() { return this.root.getBoundingClientRect().bottom; }
  }

  const KINDS = {how: HowGraphic, log: LogGraphic, gap: GapGraphic, key: KeyGraphic, check: CheckGraphic};

  /* The interface story-scroll.js drives. States are the data-s names of the
     passages; each graphic maps them to a stage number. */
  class Graphic {
    constructor(el) {
      this.el = el;
      this.host = el.querySelector('.gbody');
      const kind = el.dataset.g;
      this.stages = JSON.parse(el.dataset.stages || '{}');
      this.inner = new KINDS[kind](this.host);
      this.visible = true;
      this.state = null;
    }
    stageOf(state) {
      return this.stages[state] ?? 0;
    }
    go(state) {
      this.state = state;
      this.inner.show(this.stageOf(state));
      this.el.dispatchEvent(new Event('inktail'));
    }
    // Before the first passage arrives the graphic holds its opening state.
    hold() { this.inner.show(this.stageOf(this.state) ? Math.min(this.stageOf(this.state), this.firstStage()) : 0); }
    firstStage() { return Math.min(...Object.values(this.stages)); }
    restart() { this.go(this.state); }
    pause() {}
    resume() {}
    frame() {}
    foot() { return this.inner.foot(); }
  }

  window.StoryGraphics = {Graphic};
})();
