# -*- coding: utf-8 -*-
"""The egg, animated (2026-10-14): one slide, one click per division, then the break.

The same history as the Christendom sequence (christendom.py: states, tears, pattern fills, captions), drawn
as a single figure that changes in place. The egg keeps its height on every step and only widens as the
divisions multiply; every label is a free element that glides with its piece (a new label slides out from
the piece it split from); the last click breaks the egg into drifting shards.

Use:   from egg_anim import egg_anim_slide, EGG_ANIM_CSS, EGG_ANIM_JS
       S.append(egg_anim_slide())   # needs christendom.PATDEFS on the page and CHRISTENDOM_CSS (colors)
       page CSS += EGG_ANIM_CSS;  page body += EGG_ANIM_JS (once, after the deck)
Standalone + PNG frames:  python3 decks/src/elements/build_egg_anim.py
"""
import json, math, random, re, os
import christendom as C

ORDER = C.ORDER                    # '0', '325', ... '1806'
STEPS = ORDER + ['break']
R = 230                            # egg half-height, fixed on every step
CY = 0
MINW, GAP = 70, 20                 # narrowest piece, gap between pieces
K = C.K

# ---------- captions: the headline and line of each division slide ----------
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'christendom.py')).read()
CAP = {k1: (t, l) for t, l, k0, k1 in re.findall(r"D\('(.*?)',\s*'(.*?)',\s*'(\w+)', '(\w+)'", _src, re.S)}
CAP['0'] = ('Christendom&rsquo;s search for unity', 'One church.')
CAP['519'] = ('519 &middot; The schism healed', 'Rome and Constantinople reconciled, the seam still showing.')
CAP['break'] = ('&hellip;and today', 'Too many divisions to count.')

def _widths(units, key):
    n_equal = sum(1 for u in units if tuple(u[0]) != C.ARIAN_KEY or key in ('0', '325'))
    w_eq = max(MINW, 2 * R / max(n_equal, 1))
    return [(C.SHRINK.get(key, 0) * MINW / C.MINW if tuple(u[0]) == C.ARIAN_KEY and key not in ('0', '325') else w_eq)
            for u in units]

def geom(key):
    """slice paths and outline polygons, unit centers and widths, seams, for one state"""
    units = C.ST[key]
    ws = _widths(units, key)
    B = sum(ws); rx = B / 2; ry = R
    joined = C.JOIN.get(key, set())
    def yy(px):
        t = max(-1.0, min(1.0, px / rx)) if rx > 0 else 0
        return ry * math.sqrt(max(0.0, 1 - t * t))
    ext = {}; x = -rx
    for (idx, lab, col, dying), w in zip(units, ws):
        sw = w / len(idx)
        for j, i in enumerate(idx): ext[i] = (x + j * sw, x + (j + 1) * sw)
        x += w
    shift = {}; sh = 0.0; last = None; tot = 0
    for (idx, lab, col, dying), w in zip(units, ws):
        if w <= 0:
            for i in idx: shift[i] = sh
            continue
        if last is not None and last not in joined: sh += GAP; tot += GAP
        for i in idx: shift[i] = sh
        last = idx[-1]
    for i in shift: shift[i] -= tot / 2
    def edge(xx, y0, y1, amps, top):
        return [(xx + amps[(k if top else K - k) - 1], y0 + (y1 - y0) * k / K) for k in range(1, K)]
    def arc(a, b, top, n=10):
        pts = []
        for q in range(n + 1):
            px = a + (b - a) * q / n
            pts.append((px, CY - yy(px) if top else CY + yy(px)))
        return pts
    paths, polys, seams = {}, {}, {}
    for i in range(C.N):
        a0, b0 = ext[i]; s = shift[i]; sa, sb = a0 + s, b0 + s
        ya, yb = yy(a0), yy(b0)
        ar = C._amp(key, i); al = C._amp(key, i - 1)
        d = 'M%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f' % (sa, CY - ya, rx, ry, sb, CY - yb)
        right = edge(sb, CY - yb, CY + yb, ar, True); left = edge(sa, CY + ya, CY - ya, al, False)
        for px, py in right: d += ' L%.1f,%.1f' % (px, py)
        d += ' L%.1f,%.1f A%.1f,%.1f 0 0 1 %.1f,%.1f' % (sb, CY + yb, rx, ry, sa, CY + ya)
        for px, py in left: d += ' L%.1f,%.1f' % (px, py)
        paths[i] = d + ' Z'
        top = [(px + s, py) for px, py in arc(a0, b0, True)]
        bot = [(px + s, py) for px, py in arc(b0, a0, False)]
        polys[i] = top + right + [(sb, CY + yb)] + bot[1:] + left
        if i in C.JAG:
            sd = 'M%.1f,%.1f' % (sb, CY - yb)
            for px, py in right: sd += ' L%.1f,%.1f' % (px, py)
            seams[i] = sd + ' L%.1f,%.1f' % (sb, CY + yb)
    cents = []
    for (idx, lab, col, dying), w in zip(units, ws):
        a = ext[idx[0]][0] + shift[idx[0]]; b = ext[idx[-1]][1] + shift[idx[-1]]
        cents.append(((a + b) / 2, w))
    return dict(paths=paths, polys=polys, seams=seams, cents=cents, width=B + tot, yy=yy, shift=shift, ext=ext, xoff=0)

# ---------- labels: laid out per state in rows under the egg, each tracking its piece ----------
F = 40                             # label size
ROW0, ROWH = R + 2.4 * F, 2.4 * F
def _lw(text):
    return max(len(l) for l in text.split('|')) * 0.5 * F + 34
def layout(key, g):
    units = C.ST[key]
    items = []
    for u, (cx, w) in zip(units, g['cents']):
        if u[1] and w > 0: items.append([u[1], cx, u[3], tuple(u[0])])
    items.sort(key=lambda t: t[1])
    rows_end = []
    out = {}
    for text, cx, dying, unit in items:
        half = _lw(text) / 2
        for r in range(6):
            if r == len(rows_end): rows_end.append(-1e9)
            if rows_end[r] < cx - half:
                rows_end[r] = cx + half; break
        out[text] = dict(x=cx, y=ROW0 + r * ROWH, dim=dying, unit=unit, row=r, yb=g['yy'](cx - g['xoff']) + 8)
    return out

def build():
    G = {k: geom(k) for k in ORDER}
    LAY = {k: layout(k, G[k]) for k in ORDER}
    W = max(g['width'] for g in G.values()) + 120
    rows = max(max([v['row'] for v in L.values()] or [0]) for L in LAY.values()) + 1
    top = -R - 110; H = 2 * R + 110 + 1.4 * F + rows * ROWH   # room above: the egg sits well below the title, and the shards drift up into it
    # label tracks: every label on every step; absent = parked (invisible) at the piece it comes from / goes to
    names = []
    for k in ORDER:
        for t in LAY[k]:
            if t not in names: names.append(t)
    def owner(k, slice_i):
        for t, v in LAY[k].items():
            if slice_i in v['unit']: return v
        # the slice belongs to an unlabeled unit (the plain egg): its center
        return dict(x=0, y=ROW0, unit=(), yb=R)
    lab = {}
    for t in names:
        present = [i for i, k in enumerate(ORDER) if t in LAY[k]]
        first, last = present[0], present[-1]
        seq = []
        for i, k in enumerate(ORDER):
            if t in LAY[k]:
                v = LAY[k][t]; seq.append([round(v['x'], 1), round(v['y'], 1), 0.55 if v['dim'] else 1, round(min(v['yb'], v['y'] - F), 1)])
            else:
                ref = LAY[ORDER[first]][t]['unit'][0] if i < first else LAY[ORDER[last]][t]['unit'][0]
                o = owner(k, ref); seq.append([round(o['x'], 1), round(o['y'], 1), 0, round(o['y'] - F, 1)])
        seq.append([seq[-1][0], seq[-1][1], 0, seq[-1][3]])        # the break: labels go
        lab[t] = seq
    # pieces
    piece = []
    for i in range(C.N):
        seq = []
        for k in ORDER:
            units = C.ST[k]; g = G[k]
            u = next(u for u in units if i in u[0]); w = dict(zip([tuple(x[0]) for x in units], [c[1] for c in g['cents']]))[tuple(u[0])]
            op = 0 if w <= 0 else (0.35 if u[3] else 1)
            seq.append([g['paths'][i], C._fill(k, tuple(u[0]), u[2]), op])
        seq.append([seq[-1][0], seq[-1][1], 0])
        piece.append(seq)
    seam = []
    for b in C.JAG:
        seam.append([[G[k]['seams'][b], 1 if b in C.JOIN.get(k, set()) else 0] for k in ORDER] + [[G[ORDER[-1]]['seams'][b], 0]])
    # shards: the 1806 egg, each piece cracked into a few fragments that drift apart on the last click
    rnd = random.Random(11)
    g = G['1806']; shards = []
    for i in range(C.N):
        poly = g['polys'][i]
        fill = piece[i][-2][1]
        if piece[i][-2][2] == 0: continue
        xs = [p[0] for p in poly]; x0, x1 = min(xs), max(xs)
        ycuts = sorted(rnd.uniform(-R * .75, R * .75) for _ in range(rnd.choice((2, 3, 3, 4))))
        bands = [-R * 2] + ycuts + [R * 2]
        for b in range(len(bands) - 1):
            ta, tb = rnd.uniform(-22, 22), rnd.uniform(-22, 22)
            ya, yb = bands[b], bands[b + 1]
            # a slanted band (convex quad), ccw for the clipper
            quad = [(x0 - 50, ya + ta), (x0 - 50, yb + tb), (x1 + 50, yb - tb), (x1 + 50, ya - ta)]
            if b == 0: quad = [(x0 - 50, ya), (x0 - 50, yb + tb), (x1 + 50, yb - tb), (x1 + 50, ya)]
            if b == len(bands) - 2: quad = [(x0 - 50, ya + ta), (x0 - 50, yb), (x1 + 50, yb), (x1 + 50, ya - ta)]
            c = C._clip(poly, quad[::-1]) or C._clip(poly, quad)
            if len(c) < 3: continue
            mx = sum(p[0] for p in c) / len(c); my = sum(p[1] for p in c) / len(c)
            dist = math.hypot(mx, my * 1.6) or 1
            tx = mx * .16 + mx / dist * rnd.uniform(14, 34) + rnd.uniform(-10, 10)
            ty = my * .30 + my / dist * rnd.uniform(14, 30) + rnd.uniform(-8, 8)
            shards.append(dict(d='M' + ' L'.join('%.1f,%.1f' % p for p in c) + ' Z', fill=fill,
                               t='translate(%.1fpx,%.1fpx) rotate(%.1fdeg)' % (tx, ty, rnd.uniform(-9, 9)), ox=round(mx, 1), oy=round(my, 1)))
    caps = [list(CAP[k]) for k in STEPS]
    return dict(W=W, top=top, H=H, piece=piece, lab=lab, seam=seam, shards=shards, caps=caps, n=len(STEPS))

def egg_anim_slide(notes=None):
    D = build()
    out = []
    out.append('<g class="eg-pieces">' + ''.join(
        '<path class="eg-p" d="%s" style="fill:%s;opacity:%s"/>' % (p[0][0], p[0][1], p[0][2]) for p in D['piece']) + '</g>')
    out.append(''.join('<path class="eg-seam" d="%s" style="opacity:0"/>' % s[0][0] for s in D['seam']))
    out.append('<g class="eg-shards">' + ''.join(
        '<path class="eg-sh" d="%s" style="fill:%s;transform-origin:%spx %spx;--t:%s"/>' % (s['d'], s['fill'], s['ox'], s['oy'], s['t'])
        for s in D['shards']) + '</g>')
    labs = []
    for t, seq in D['lab'].items():
        lines = t.split('|')
        x, y, o = seq[0][:3]
        labs.append('<g class="eg-l%s" data-k="%s" style="transform:translate(%.1fpx,%.1fpx);opacity:%s">'
                    '<text text-anchor="middle">%s</text></g>' % (
            ' dim' if any(s[2] == .55 for s in seq) else '', t, x, y, o,
            ''.join('<tspan x="0" dy="%s">%s</tspan>' % ('0' if j == 0 else '1.05em', l) for j, l in enumerate(lines))))
    out.append('<g class="eg-leads">' + ''.join('<path class="eg-lead" d="M%.1f,%.1f L%.1f,%.1f" style="opacity:%s"/>' % (
        seq[0][0], seq[0][3], seq[0][0], seq[0][1] - F * .95, seq[0][2]) for t, seq in D['lab'].items()) + '</g>')
    out.append('<g class="eg-labels">' + ''.join(labs) + '</g>')
    svg = '<svg class="eggfig" viewBox="%.0f %.0f %.0f %.0f" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (
        -D['W'] / 2, D['top'], D['W'], D['H'], ''.join(out))
    data = dict(piece=[[[s[0], s[1], s[2]] for s in p] for p in D['piece']],
                lab=[[t, D['lab'][t]] for t in D['lab']], seam=D['seam'], caps=D['caps'])
    steps = ''.join('<div class="frag eggstep"></div>' for _ in range(D['n'] - 1))
    if notes is None:
        notes = ('%d clicks, one division each, then the break. The egg keeps its height and only widens; each label rides with its piece. '
                 'Steps: ' % (D['n'] - 1) + ' &middot; '.join(re.sub(r' &middot;.*', '', c[0]) for c in D['caps'][1:]) +
                 '.<br>The full notes for each division are on the Christendom slides (christendom.py).')
    return ('<section class="slide eggslide"><h2 class="eg-t">%s</h2><div class="eg-line">%s</div>%s%s'
            '<script type="application/json" class="eg-data">%s</script>'
            '<aside class=notes>%s</aside></section>' % (D['caps'][0][0], D['caps'][0][1], svg, steps,
                                                         json.dumps(data, separators=(',', ':')).replace('</', '<\\/'), notes))

EGG_ANIM_CSS = '''
  /* ---- the egg, animated ---- */
  #deck .eggslide{justify-content:flex-start;padding-top:5vmin;gap:0}
  #deck .eggslide h2.eg-t{font-size:clamp(36px,6.8vmin,86px);max-width:none;transition:opacity .35s ease}
  #deck .eggslide .eg-line{margin-top:1vmin;font-family:Spectral,Georgia,serif;font-style:italic;font-size:clamp(16px,2.8vmin,34px);line-height:1.35;white-space:nowrap;color:var(--bone-dim);transition:opacity .35s ease}
  #deck .eggslide .eg-fade{opacity:0}
  #deck .eggslide .eggfig{margin-top:1.5vmin;width:96vw;max-height:78vh;display:block;overflow:visible}
  #deck .eggslide .eggstep{height:0}
  .eggfig .eg-p{stroke-width:1.5;stroke-linejoin:round;transition:d .9s cubic-bezier(.6,0,.3,1),fill .7s ease .25s,opacity .6s ease}
  .eggfig .eg-seam{fill:none;stroke:var(--ground);stroke-width:5;stroke-linejoin:round;transition:d .9s cubic-bezier(.6,0,.3,1),opacity .5s ease}
  .eggfig .eg-sh{opacity:0;transform:none;stroke:var(--ground);stroke-width:3;stroke-linejoin:round;transition:transform 1.8s cubic-bezier(.15,.7,.2,1),opacity 0s}
  .eggfig.broken .eg-sh{opacity:1;transform:var(--t)}
  .eggfig.broken .eg-p{opacity:0!important;transition:none}
  .eggfig [class^="eg-l"]{transition:transform .9s cubic-bezier(.6,0,.3,1),opacity .5s ease}
  .eggfig text{font-family:"IM Fell English",Georgia,serif;font-size:40px;fill:var(--bone)}
  .eggfig .eg-lead{stroke:var(--bone-dim);stroke-width:1.5;fill:none;transition:d .9s cubic-bezier(.6,0,.3,1),opacity .5s ease}
  .eggfig .eg-labels text{paint-order:stroke;stroke:var(--ground);stroke-width:10px;stroke-linejoin:round}
  .eggfig .eg-l.dim text{fill:var(--smoke);font-style:italic}
'''

EGG_ANIM_JS = '''<script>
(function(){
  document.querySelectorAll('.eggslide').forEach(function(sl){
    var D=JSON.parse(sl.querySelector('.eg-data').textContent);
    var svg=sl.querySelector('.eggfig'), P=svg.querySelectorAll('.eg-p'), Sm=svg.querySelectorAll('.eg-seam');
    var L={};svg.querySelectorAll('[data-k]').forEach(function(g){L[g.getAttribute('data-k')]=g});
    var t=sl.querySelector('.eg-t'), ln=sl.querySelector('.eg-line'), steps=[].slice.call(sl.querySelectorAll('.eggstep'));
    var last=-1;
    function apply(){
      var k=steps.filter(function(s){return s.classList.contains('on')}).length;
      if(k===last)return;last=k;
      P.forEach(function(p,i){var s=D.piece[i][k];p.style.d='path("'+s[0]+'")';p.style.fill=s[1];p.style.stroke=s[1];p.style.opacity=s[2]});
      Sm.forEach(function(p,i){var s=D.seam[i][k];p.style.d='path("'+s[0]+'")';p.style.opacity=s[1]});
      D.lab.forEach(function(e){var g=L[e[0]],s=e[1][k];g.style.transform='translate('+s[0]+'px,'+s[1]+'px)';g.style.opacity=s[2]});
      var LD=svg.querySelectorAll('.eg-lead');D.lab.forEach(function(e,i){var s=e[1][k];LD[i].style.d='path("M'+s[0]+','+s[3]+' L'+s[0]+','+(s[1]-38)+'")';LD[i].style.opacity=s[2]?.55:0});
      svg.classList.toggle('broken',k===D.caps.length-1);
      var c=D.caps[k];
      if(t.innerHTML!==c[0]){t.classList.add('eg-fade');ln.classList.add('eg-fade');
        setTimeout(function(){t.innerHTML=c[0];ln.innerHTML=c[1];t.classList.remove('eg-fade');ln.classList.remove('eg-fade')},350)}
    }
    new MutationObserver(apply).observe(sl,{attributes:true,subtree:true,attributeFilter:['class']});
    apply();
  });
})();
</script>'''
