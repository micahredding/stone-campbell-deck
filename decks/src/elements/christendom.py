# -*- coding: utf-8 -*-
"""Christendom's search for unity — a reusable slide element (2026-10-07).

One egg, carved from Nicaea (325) to the Seceder splits (1806): every living piece an equal share, the
Arian remnant thinning away, the Henotikon's awkward join, zigzag / wave / battlement / crack tears,
pattern fills, a finale of the egg in dozens of shards, and a time-scaled tree of divisions.

Use:   from christendom import christendom_slides, PATDEFS, CHRISTENDOM_CSS
       S += christendom_slides()        # 17 sections: card, 14 divisions, shards, tree
The build must put PATDEFS once in the page outside any slide (hidden slides blank pattern defs),
and append CHRISTENDOM_CSS to the engine stylesheet. Engine: the Week 1/2 deck engine (engine.css/js).
"""
import re, math, random

def C(name, note=''):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))

# ---------- the split illustration ----------
# One body, carved cumulatively from 325 to 1806. A slide has a BEFORE and an AFTER state, each a list of
# units = (slice indices, label, color, dying). Every living unit gets an equal share of the body, floored at
# MINW, so the body is a circle that becomes an ellipse as the pieces multiply; the Arian remnant thins after
# 451 and is gone by 1530. The body is re-rounded in every state, so the outermost pieces always carry the
# curve. Each slice's path is computed per state and the click morphs it (CSS transition on `d`).
CX, CY, R, H_, MINW, GAP = 0, 200, 170, 660, 84, 26
N = 16
LEAVES = [('east', 1), ('oriental', 1), ('orthodox', 1), ('catholic', 1), ('lutheran', 1), ('anglican', 1),
          ('independents', 1), ('reformed', 1), ('covenanters', 1), ('scotland', 1), ('b_old', 1), ('b_new', 1),
          ('a_old', 1), ('a_new', 1), ('anabaptists', 1), ('arian', 1)]
def U(a, b=None): return list(range(a, (b if b is not None else a) + 1))
ARIAN_KEY = (15,)
SHRINK = {'381': 104, '431': 86, '451': 72, '482': 58, '519': 58, '1054': 40}   # the Arian remnant, outlawed in 381; absent from 1530 on = gone

def _widths(units, key):
    living = [u for u in units if tuple(u[0]) != ARIAN_KEY or key in ('0', '325') or key in SHRINK]
    n_equal = sum(1 for u in units if tuple(u[0]) != ARIAN_KEY or key in ('0', '325'))
    w_eq = max(MINW, 2 * R / max(n_equal, 1))
    ws = []
    for u in units:
        k = tuple(u[0])
        if k == ARIAN_KEY and key not in ('0', '325'):
            ws.append(SHRINK.get(key, 0))
        else:
            ws.append(w_eq)
    return ws

ORDER = ['0', '325', '381', '431', '451', '482', '519', '1054', '1530', '1527', '1529', '1646', '1690', '1733', '1747', '1806']
# boundary after slice b tears in this style from this state on. Styles: zig (Easter egg), wave, step
# (battlements), crack (Humpty Dumpty). By 1806 every boundary still straight cracks too.
JAG = {2: ('1054', 'zig'), 3: ('1530', 'zig'), 13: ('1527', 'wave'), 4: ('1529', 'step'),
       5: ('1646', 'crack'), 6: ('1646', 'crack'), 7: ('1646', 'crack'), 8: ('1690', 'wave'),
       9: ('1733', 'step'), 11: ('1747', 'crack'), 10: ('1806', 'zig'), 12: ('1806', 'zig'),
       0: ('1806', 'crack'), 1: ('1806', 'crack')}
JOIN = {'519': {2}}              # boundaries with no gap in this state: the Henotikon's awkward join, seam showing
K = 16                           # segments per edge (every edge carries the points; amplitude 0 = straight)
import random
_cr = {}
def _shape(style, b):
    """per-k offset multipliers for an edge, k = 1..K-1"""
    if style == 'zig':   return [1 if (k // 2) % 2 == 0 else -1 for k in range(1, K)], 9
    if style == 'wave':  return [math.sin(2 * math.pi * 2 * k / K) for k in range(1, K)], 11
    if style == 'step':  return [1 if (k // 4) % 2 == 0 else -1 for k in range(1, K)], 7
    if style == 'crack':
        if b not in _cr:
            rnd = random.Random(1000 + b); _cr[b] = [rnd.uniform(-1, 1) for _ in range(1, K)]
        return _cr[b], 10
    return [0] * (K - 1), 0
def _amp(key, b):
    st = JAG.get(b)
    if not st or ORDER.index(key) < ORDER.index(st[0]): return [0] * (K - 1)
    mult, a = _shape(st[1], b)
    return [m * a for m in mult]
# pattern fills: unit key -> (state from which, style). Dots, hatching, checks: other kinds of separation.
PAT = {(14,): ('1527', 'dots'), (6,): ('1646', 'hatch'), (8,): ('1690', 'dots'), (9,): ('1733', 'checks'),
       (10, 11): ('1747', 'hatch'), (10,): ('1806', 'hatch'), (11,): ('1806', 'dots'),
       (12,): ('1806', 'checks'), (13,): ('1806', 'dots')}
def _fill(key, unit, col):
    pt = PAT.get(unit)
    if pt and ORDER.index(key) >= ORDER.index(pt[0]) and col in ('c1', 'c2', 'c3', 'c4'):
        return 'url(#p-%s-%s)' % (pt[1], col)
    return 'var(--%s)' % ('bone-dim' if col == 'bone' else col)
PATDEFS = '<defs>' + ''.join(
    '<pattern id="p-dots-%s" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" style="fill:var(--%s)"/><circle cx="7" cy="7" r="2.6" style="fill:var(--bone);opacity:.6"/></pattern>'
    '<pattern id="p-hatch-%s" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" style="fill:var(--%s)"/><rect width="4" height="12" style="fill:var(--bone);opacity:.4"/></pattern>'
    '<pattern id="p-checks-%s" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="16" height="16" style="fill:var(--%s)"/><rect width="8" height="8" style="fill:var(--bone);opacity:.3"/><rect x="8" y="8" width="8" height="8" style="fill:var(--bone);opacity:.3"/></pattern>'
    % (c, c, c, c, c, c) for c in ('c1', 'c2', 'c3', 'c4')) + '</defs>'

def _geom(units, key):
    """Per-slice path for this state, plus per-unit (center, width), the drawn extent, and seam paths."""
    ws = _widths(units, key)
    B = sum(ws); rx = B / 2
    n_live = sum(1 for w in ws if w > 0)
    ry = R + 10 * max(0, n_live - 4)    # the egg gets taller as it widens, so it stays big on screen
    joined = JOIN.get(key, set())
    # gaps: one between each pair of living units, unless joined
    order_slices = [i for u in units for i in u[0]]
    x = CX - rx
    paths = {}; centers = []; seams = {}
    def yy(px):
        t = max(-1.0, min(1.0, (px - CX) / rx)) if rx > 0 else 0
        return ry * math.sqrt(max(0.0, 1 - t * t))
    # first pass: slice extents in body coordinates (no gaps)
    ext = {}
    for (idx, lab, col, dying), w in zip(units, ws):
        n = len(idx); sw = w / n
        for j, i in enumerate(idx):
            ext[i] = (x + j * sw, x + (j + 1) * sw)
        x += w
    # shifts: accumulate a GAP after each living unit's last slice unless that boundary is joined
    shift = {}; sh = 0.0; last_living = None
    total_gaps = 0
    for (idx, lab, col, dying), w in zip(units, ws):
        if w <= 0:
            for i in idx: shift[i] = sh
            continue
        if last_living is not None and last_living not in joined:
            sh += GAP; total_gaps += GAP
        for i in idx: shift[i] = sh
        last_living = idx[-1]
    for i in shift: shift[i] -= total_gaps / 2
    def edge(xx, y0, y1, amps, k_from_top):
        """interior points of a vertical edge from y0 to y1 (K segments), offset by amps[k-1] (indexed from the top)."""
        pts = []
        for k in range(1, K):
            t = k / K
            y = y0 + (y1 - y0) * t
            kk = k if k_from_top else K - k
            pts.append((xx + amps[kk - 1], y))
        return pts
    for i in range(N):
        sa, sb = ext[i]; sa += shift[i]; sb += shift[i]
        ya, yb = yy(ext[i][0]), yy(ext[i][1])
        ar = _amp(key, i); al = _amp(key, i - 1)
        d = 'M%.2f,%.2f A%.2f,%.2f 0 0 1 %.2f,%.2f' % (sa, CY - ya, rx, ry, sb, CY - yb)
        for px, py in edge(sb, CY - yb, CY + yb, ar, True): d += ' L%.2f,%.2f' % (px, py)
        d += ' L%.2f,%.2f A%.2f,%.2f 0 0 1 %.2f,%.2f' % (sb, CY + yb, rx, ry, sa, CY + ya)
        for px, py in edge(sa, CY + ya, CY - ya, al, False): d += ' L%.2f,%.2f' % (px, py)
        d += ' Z'
        paths[i] = d
        if i in JAG:   # seam along this boundary (drawn only when joined)
            sd = 'M%.2f,%.2f' % (sb, CY - yb)
            for px, py in edge(sb, CY - yb, CY + yb, ar, True): sd += ' L%.2f,%.2f' % (px, py)
            sd += ' L%.2f,%.2f' % (sb, CY + yb)
            seams[i] = sd
    for (idx, lab, col, dying), w in zip(units, ws):
        a = ext[idx[0]][0] + shift[idx[0]]; b_ = ext[idx[-1]][1] + shift[idx[-1]]
        centers.append(((a + b_) / 2, w))
    return paths, centers, B + total_gaps, seams

def split(pre, post, k0, k1, k2=None):
    p0, c0, w0, s0 = _geom(pre, k0); p1, c1, w1, s1 = _geom(post, k1)
    p2, s2 = (_geom(post, k2)[0], _geom(post, k2)[3]) if k2 else (p1, s1)
    col0 = {}; col1 = {}; dy0 = {}; dy1 = {}; unit0 = {}; unit1 = {}; wid0 = {}; wid1 = {}
    base = lambda c: 'var(--%s)' % ('bone-dim' if c == 'bone' else c)
    st0 = {}; st1 = {}
    for u, (cx_, w) in zip(pre, c0):
        for i in u[0]: col0[i] = _fill(k0, tuple(u[0]), u[2]); st0[i] = col0[i]; unit0[i] = tuple(u[0]); dy0[i] = u[3]; wid0[i] = w
    for u, (cx_, w) in zip(post, c1):
        for i in u[0]: col1[i] = _fill(k1, tuple(u[0]), u[2]); st1[i] = col1[i]; unit1[i] = tuple(u[0]); dy1[i] = u[3]; wid1[i] = w
    out = []
    for i in range(N):
        cls = 'piece' + (' dying0' if dy0[i] else '') + (' dying1' if dy1[i] else '') + \
              (' gone0' if wid0[i] <= 0 else '') + (' gone1' if wid1[i] <= 0 else '')
        out.append('<g class="%s" style="--d0:path(\'%s\');--d1:path(\'%s\');--d2:path(\'%s\');--k0:%s;--k1:%s;--s0:%s;--s1:%s"><path d="%s" vector-effect="non-scaling-stroke"/></g>'
                   % (cls, p0[i], p1[i], p2[i], col0[i], col1[i], st0[i], st1[i], p0[i]))
    # seams: visible in a state where the boundary is joined
    j0 = JOIN.get(k0, set()); j1 = JOIN.get(k1, set()); j2 = JOIN.get(k2, set()) if k2 else set()
    for b in JAG:
        cls = 'seam' + (' on0' if b in j0 else '') + (' on1' if b in j1 else '') + (' on2' if b in j2 else '')
        out.append('<path class="%s" d="%s" style="--d0:path(\'%s\');--d1:path(\'%s\');--d2:path(\'%s\')" vector-effect="non-scaling-stroke"/>'
                   % (cls, s0[b], s0[b], s1[b], s2[b]))
    pre_keys = {tuple(u[0]) for u in pre}; post_keys = {tuple(u[0]) for u in post}
    RY = R + 10 * max(0, max(sum(1 for _, w in c0 if w > 0), sum(1 for _, w in c1 if w > 0)) - 4)
    def label(u, center, row, cls, w):
        idx, lab, col, dying = u
        if not lab or w <= 0: return ''
        y = CY + RY + 44 + row * 60
        lines = lab.split('|')
        return '<text class="plab %s%s" x="%.0f" y="%d" text-anchor="middle">%s</text>' % (
            cls, ' dim' if dying else '', center, y,
            ''.join('<tspan x="%.0f" dy="%d">%s</tspan>' % (center, 0 if j == 0 else 32, l) for j, l in enumerate(lines)))
    rows = lambda units: 1 if len(units) <= 2 else (2 if len(units) <= 8 else 3)
    r0 = rows(pre); r1 = rows(post)
    for k, (u, (cx_, w)) in enumerate(zip(pre, c0)):
        if tuple(u[0]) not in post_keys: out.append(label(u, cx_, k % r0, 'pre', w))
    for k, (u, (cx_, w)) in enumerate(zip(post, c1)):
        out.append(label(u, cx_, k % r1, 'keep' if tuple(u[0]) in pre_keys else 'post', w))
    W = max(w0, w1) + 100
    Hv = CY + RY + 44 + (max(r0, r1) - 1) * 60 + 40 + 16   # only as tall as the label rows in use, so small bodies draw big
    return '<svg class="splitfig" viewBox="%.0f 0 %.0f %d" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (CX - W / 2, W, Hv, ''.join(out))

def D(title, line, pre, post, notes, heal=None, cut=False):
    """pre/post/heal are state keys into ST. Headline + line at once; click = the split; a second click = heal."""
    healer = '<div class="frag healer"></div>' if heal else ''
    wide = ' wide' if len(ST[post]) >= 11 else ''     # late, wide eggs bleed up under the title for more room
    return ('<section class="slide divslide%s%s"><h2>%s</h2>'
            '<div class=line>%s</div>'
            '<div class="failure frag">%s</div>%s'
            '<aside class=notes>%s</aside></section>' % (
                ' cuttable' if cut else '', wide, title, line, split(ST[pre], ST[post], pre, post, heal), healer, notes))


# ---------- the finale: a shattered egg, too many pieces to count ----------
NAMES = ['Roman Catholic', 'Eastern Orthodox', 'Oriental Orthodox', 'Church of the East', 'Coptic', 'Armenian', 'Ethiopian',
    'Syriac', 'Greek Orthodox', 'Russian Orthodox', 'Old Believers', 'Old Catholic', 'Maronite', 'Mar Thoma',
    'Lutheran (ELCA)', 'Lutheran (LCMS)', 'Lutheran (WELS)', 'Anglican', 'Episcopal', 'Methodist', 'Wesleyan',
    'Free Methodist', 'Nazarene', 'Southern Baptist', 'American Baptist', 'Free Will Baptist', 'Primitive Baptist',
    'Independent Baptist', 'Presbyterian (PCUSA)', 'Presbyterian (PCA)', 'Orthodox Presbyterian', 'Cumberland Presbyterian',
    'Reformed (RCA)', 'Christian Reformed', 'Congregational', 'United Church of Christ', 'Disciples of Christ',
    'Christian Church', 'Church of Christ', 'Church of Christ (one cup)', 'Church of Christ (non-class)',
    'Church of Christ (non-institutional)', 'Church of Christ (instrumental)', 'Mennonite', 'Amish', 'Hutterite',
    'Brethren', 'Quaker', 'Moravian', 'Salvation Army', 'Assemblies of God', 'Church of God (Cleveland)',
    'Foursquare', 'Apostolic', 'Oneness Pentecostal', 'Holiness', 'Seventh-day Adventist', 'Plymouth Brethren',
    'Evangelical Free', 'Evangelical Covenant', 'Vineyard', 'Calvary Chapel', 'Non-denominational', 'Waldensian',
    'Covenanters', 'Seceders', 'Relief Church', 'Free Church of Scotland', 'Wee Frees', 'Church of Scotland',
    'Associate Reformed', 'Primitive Methodist', 'AME', 'AME Zion', 'CME', 'National Baptist', 'Progressive Baptist',
    'Church of God in Christ', 'Reformed Baptist', 'Landmark Baptist', 'Two-Seed Baptist', 'Hard-Shell Baptist',
    'Dunkers', 'River Brethren', 'Schwenkfelders', 'Shakers', 'Stone-ites', 'Campbellites']

def _clip(poly, clip):
    """Sutherland-Hodgman: clip polygon by a convex polygon (both lists of (x,y), ccw)."""
    out = poly
    for i in range(len(clip)):
        a, b = clip[i], clip[(i + 1) % len(clip)]
        inp = out; out = []
        if not inp: break
        def inside(p): return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= 0
        def inter(p, q):
            x1, y1, x2, y2 = a[0], a[1], b[0], b[1]; x3, y3, x4, y4 = p[0], p[1], q[0], q[1]
            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) or 1e-9
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
        s_ = inp[-1]
        for e in inp:
            if inside(e):
                if not inside(s_): out.append(inter(s_, e))
                out.append(e)
            elif inside(s_): out.append(inter(s_, e))
            s_ = e
    return out

def shatter(seed=7, cols=15, rows=7):
    rnd = random.Random(seed)
    W, H, cx, cy, rx, ry = 2500, 1100, 1250, 540, 930, 370
    egg = [(cx + rx * math.cos(2 * math.pi * k / 72), cy + ry * math.sin(2 * math.pi * k / 72)) for k in range(72)]
    # jittered grid vertices over the bounding box
    gx = [cx - rx + (2 * rx) * i / cols for i in range(cols + 1)]
    gy = [cy - ry + (2 * ry) * j / rows for j in range(rows + 1)]
    V = {}
    for i in range(cols + 1):
        for j in range(rows + 1):
            jx = rnd.uniform(-.42, .42) * (2 * rx / cols); jy = rnd.uniform(-.42, .42) * (2 * ry / rows)
            V[(i, j)] = (gx[i] + jx, gy[j] + jy)
    shards = []
    for i in range(cols):
        for j in range(rows):
            poly = [V[(i, j)], V[(i + 1, j)], V[(i + 1, j + 1)], V[(i, j + 1)]]
            # split some cells diagonally for smaller shards
            cells = [poly] if rnd.random() < .55 else [[poly[0], poly[1], poly[2]], [poly[0], poly[2], poly[3]]]
            for c in cells:
                c = _clip(c, egg)
                if len(c) < 3: continue
                area = abs(sum(c[k][0] * c[(k + 1) % len(c)][1] - c[(k + 1) % len(c)][0] * c[k][1] for k in range(len(c)))) / 2
                if area < 600: continue
                shards.append((c, area))
    names = NAMES[:]; rnd.shuffle(names)
    out = []
    pats = ['', '', '', 'dots', 'hatch', 'checks']
    for c, area in sorted(shards, key=lambda t: -t[1]):
        mx = sum(p[0] for p in c) / len(c); my = sum(p[1] for p in c) / len(c)
        dx, dy = mx - cx, my - cy; dist = math.hypot(dx, dy) or 1
        # spread: scale every shard's position out from the center, plus a little random push and tilt
        tx, ty = dx * 0.30 + dx / dist * rnd.uniform(6, 16) + rnd.uniform(-5, 5), dy * 0.30 + dy / dist * rnd.uniform(6, 16) + rnd.uniform(-5, 5)
        rot = rnd.uniform(-5, 5)
        col = rnd.choice(['c1', 'c2', 'c3', 'c4']); pat = rnd.choice(pats)
        fill = 'url(#p-%s-%s)' % (pat, col) if pat else 'var(--%s)' % col
        jag = []
        zig = rnd.random() < .4          # this shard's edges: regular Easter-egg teeth, or torn
        for k in range(len(c)):
            a_, b_ = c[k], c[(k + 1) % len(c)]
            ex, ey = b_[0] - a_[0], b_[1] - a_[1]; L = math.hypot(ex, ey) or 1
            nx, ny = -ey / L, ex / L
            segs = max(2, int(L / (14 if zig else 22)))
            jag.append(a_)
            for q in range(1, segs):
                t = q / segs
                amp = (7 if q % 2 else -7) if zig else rnd.uniform(-1, 1) * min(7, L * .08)
                jag.append((a_[0] + ex * t + nx * amp, a_[1] + ey * t + ny * amp))
        d = 'M' + ' L'.join('%.1f,%.1f' % p for p in jag) + ' Z'
        out.append('<g transform="translate(%.1f,%.1f) rotate(%.1f,%.1f,%.1f)"><path d="%s" style="fill:%s;stroke:var(--ground);stroke-width:4;stroke-linejoin:round"/>'
                   % (tx, ty, rot, mx, my, d, fill))
        # label if there is room
        w = max(p[0] for p in c) - min(p[0] for p in c); h = max(p[1] for p in c) - min(p[1] for p in c)
        if names and area > 3200 and w > 60 and h > 24:
            name = names.pop()
            fs = max(11, min(19, (w - 10) / (0.52 * len(name))))
            if fs >= 11:
                out.append('<text class="shardlab" x="%.1f" y="%.1f" text-anchor="middle" style="font-size:%.1fpx">%s</text>' % (mx, my + fs * .35, fs, name))
            else:
                names.append(name)
        out.append('</g>')
    return '<svg class="shards" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (W, H, ''.join(out))


# ---------- the tree of divisions ----------
# (name, year, children). A leaf is a church that still exists; year = when it parted from its parent.
def T(name, year, *kids): return (name, year, list(kids))
TREE = T('the Church', 100,
  T('Arian', 325, T('Arian kingdoms †c.650', 650)),
  T('Church of the East', 431, T('Assyrian Church of the East', 431), T('Chaldean Catholic', 1552), T('Ancient Church of the East', 1968)),
  T('Oriental Orthodox', 451, T('Coptic', 451), T('Armenian', 451), T('Syriac', 451), T('Ethiopian', 451), T('Malankara', 1653), T('Eritrean', 1993)),
  T('Eastern Orthodox', 1054, T('Greek', 1054), T('Russian', 1448, T('Old Believers', 1666)), T('Serbian', 1219), T('Romanian', 1872), T('OCA', 1970)),
  T('Catholic West', 1054,
    T('Roman Catholic', 1054, T('Old Catholic', 1870), T('Polish National Catholic', 1897), T('Maronite', 1182)),
    T('Waldensian', 1173),
    T('Hussite · Moravian', 1457),
    T('Protestant', 1517,
      T('Lutheran', 1530, T('ELCA', 1988), T('LCMS', 1847), T('WELS', 1850), T('Church of Sweden', 1593)),
      T('Anabaptist', 1525, T('Mennonite', 1536, T('Amish', 1693), T('Old Order Mennonite', 1872)), T('Hutterite', 1528),
        T('Brethren', 1708, T('Dunkers', 1708), T('River Brethren', 1778))),
      T('Reformed', 1529,
        T('Continental Reformed', 1529, T('Reformed Church in America', 1628), T('Christian Reformed', 1857), T('Schwenkfelders', 1540)),
        T('Church of England', 1534,
          T('Episcopal', 1789), T('Anglican Church in N. America', 2009),
          T('Methodist', 1784, T('United Methodist', 1968), T('Wesleyan', 1843), T('Free Methodist', 1860), T('AME', 1816), T('AME Zion', 1821), T('CME', 1870),
            T('Nazarene', 1908), T('Salvation Army', 1865),
            T('Pentecostal', 1906, T('Assemblies of God', 1914), T('Church of God (Cleveland)', 1886), T('Church of God in Christ', 1907),
              T('Foursquare', 1923), T('Oneness · Apostolic', 1916))),
          T('Puritan', 1560,
            T('Congregational', 1620, T('United Church of Christ', 1957)),
            T('Baptist', 1609, T('Southern Baptist', 1845), T('American Baptist', 1907), T('National Baptist', 1880), T('Free Will Baptist', 1727),
              T('Primitive Baptist', 1827), T('Landmark Baptist', 1851), T('Independent Baptist', 1920), T('Seventh Day Baptist', 1671)),
            T('Quaker', 1650)),
          T('Plymouth Brethren', 1830), T('Adventist', 1863)),
        T('Church of Scotland', 1560,
          T('Covenanters', 1690, T('Reformed Presbyterian', 1743)),
          T('Secession', 1733,
            T('Burgher', 1747, T('Old Light Burgher', 1799), T('New Light Burgher', 1799)),
            T('Anti-Burgher', 1747, T('Old Light Anti-Burgher', 1806), T('New Light Anti-Burgher', 1806))),
          T('Relief Church', 1761),
          T('Free Church of Scotland', 1843, T('Wee Frees', 1900)),
          T('Presbyterian (USA)', 1706, T('PCUSA', 1983), T('PCA', 1973), T('Orthodox Presbyterian', 1936), T('Cumberland Presbyterian', 1810),
            T('Associate Reformed', 1782))),
        T('Evangelical Free', 1884), T('Evangelical Covenant', 1885), T('Vineyard', 1982), T('Calvary Chapel', 1965), T('Non-denominational', 1970)),
      T('Stone–Campbell', 1832,
        T('Disciples of Christ', 1968), T('Christian Churches', 1927),
        T('Churches of Christ', 1906, T('one cup', 1915), T('non-class', 1920), T('non-institutional', 1955), T('instrumental', 1906), T('premillennial', 1930))))))

def tree_svg():
    W, H = 2000, 1150
    X0, X1, Y0, Y1 = 40, 1660, 40, 1130
    def xs(y):   # time scale: 100–1500 takes the left 40%, 1500–2000 the right 60%
        return X0 + (X1 - X0) * ((y - 100) / 1400 * .40 if y <= 1500 else .40 + (y - 1500) / 500 * .60)
    leaves = []
    def count(n):
        if not n[2]: leaves.append(n); return 1
        return sum(count(k) for k in n[2])
    count(TREE)
    pitch = (Y1 - Y0) / (len(leaves) - 1)
    pos = {}
    def place(n, fam):
        if not n[2]:
            y = Y0 + leaves.index(n) * pitch; pos[id(n)] = (xs(n[1]), y, fam); return y
        ys = [place(k, fam if fam else k) for k in n[2]]
        y = sum(ys) / len(ys); pos[id(n)] = (xs(n[1]), y, fam); return y
    place(TREE, None)
    fams = {id(k): c for k, c in zip(TREE[2], ['smoke', 'c3', 'c2', 'c4', 'c1'])}
    out = []; placed = []
    def draw(n, depth):
        x, y, fam = pos[id(n)]
        col = fams.get(id(fam), 'bone-dim') if fam else 'bone-dim'
        if n[2]:
            kys = [pos[id(k)][1] for k in n[2]]
            kx = min(pos[id(k)][0] for k in n[2])
            # trunk: a vertical bar at this node's x spanning the children, then elbows out to each child
            out.append('<line class="tb" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" style="stroke:var(--%s)"/>' % (x, min(kys), x, max(kys), col))
            for k in n[2]:
                kx_, ky_, kf = pos[id(k)]
                kc = fams.get(id(kf), col) if kf else col
                out.append('<line class="tb" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" style="stroke:var(--%s)"/>' % (x, ky_, kx_, ky_, kc))
                draw(k, depth + 1)
            size = 22 if depth == 0 else (17 if depth <= 2 else 13)
            out.append('<circle class="tn" cx="%.1f" cy="%.1f" r="%d" style="fill:var(--%s)"/>' % (x, y, 5 if depth <= 2 else 3, col))
            label = n[0] if depth == 0 else '%s %d' % (n[0], n[1])
            tw = len(label) * size * 0.5; anchor = 'start' if depth == 0 else 'end'
            lx = x + 12 if depth == 0 else x - 8
            x0_ = lx if depth == 0 else lx - tw
            # try above, below, then further out, against labels already placed
            for dy in (-6, size + 2, -6 - size - 4, 2 * size + 6, -6 - 2 * size - 8, 3 * size + 10):
                ly = y + dy
                box = (x0_, ly - size, x0_ + tw, ly + 3)
                if not any(not (box[2] < b[0] or box[0] > b[2] or box[3] < b[1] or box[1] > b[3]) for b in placed): break
            placed.append(box)
            text = n[0] if depth == 0 else '%s <tspan class="yr">%d</tspan>' % (n[0], n[1])
            out.append('<text class="tl" x="%.1f" y="%.1f" text-anchor="%s" style="font-size:%dpx">%s</text>' % (lx, ly, anchor, size, text))
        else:
            out.append('<line class="tb leafline" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" style="stroke:var(--%s)"/>' % (x, y, X1 + 20, y, col))
            cls = ' dead' if '†' in n[0] else ''
            out.append('<text class="lf%s" x="%.1f" y="%.1f" style="font-size:12.5px">%s</text>' % (cls, X1 + 28, y + 4, n[0]))
    draw(TREE, 0)
    # time ticks
    for yr in (325, 451, 1054, 1517, 1700, 1900, 2000):
        out.append('<line class="tick" x1="%.1f" y1="%d" x2="%.1f" y2="%d"/><text class="tk" x="%.1f" y="%d" text-anchor="middle">%d</text>' % (xs(yr), Y0 - 22, xs(yr), Y1 + 10, xs(yr), Y0 - 28, yr))
    return '<svg class="tree2" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (W, H, ''.join(out))

# ---------- the states, in order ----------
ARIAN = (U(15), 'Arian', 'smoke', True)
EAST = (U(0), 'Church of|the East', 'c3', False)
ORIENTAL = (U(1), 'Oriental|Orthodox', 'c2', False)
ORTHODOX = (U(2), 'Orthodox|East', 'c4', False)
CATHOLIC = (U(3), 'Catholic', 'c2', False)
LUTHERAN = (U(4), 'Lutheran', 'c3', False)
ANGLICAN = (U(5), 'Church of|England', 'c4', False)
INDEP = (U(6), 'Independents', 'c2', False)
REFORMED = (U(7), 'Continental|Reformed', 'c3', False)
COVEN = (U(8), 'Covenanters', 'c4', False)
SCOTLAND = (U(9), 'Church of|Scotland', 'c2', False)
ANABAP = (U(14), 'Anabaptists', 'c4', False)
ST = {}
ST['0']    = [(U(0, 15), '', 'bone', False)]
ST['325']  = [(U(0, 14), 'Nicene', 'c1', False), ARIAN]
ST['381']  = [(U(0, 14), 'Nicene', 'c1', False), (U(15), 'Arian|Goths', 'smoke', True)]
ST['431']  = [EAST, (U(1, 14), 'the imperial|Church', 'c1', False), ARIAN]
ST['451']  = [EAST, ORIENTAL, (U(2, 14), 'Chalcedonian', 'c1', False), ARIAN]
ST['482']  = [EAST, ORIENTAL, (U(2), 'Constantinople', 'c4', False), (U(3, 14), 'Rome', 'c1', False), ARIAN]
ST['519']  = ST['482']
ST['1054'] = [EAST, ORIENTAL, ORTHODOX, (U(3, 14), 'Catholic|West', 'c1', False), ARIAN]
ST['1530'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, (U(4, 14), 'Protestant', 'c1', False), ARIAN]
ST['1527'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, (U(4, 13), 'Protestant', 'c1', False), ANABAP, ARIAN]
ST['1529'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, (U(5, 13), 'Reformed', 'c1', False), ANABAP, ARIAN]
ST['1646'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, ANGLICAN, INDEP, REFORMED, (U(8, 13), 'Church of|Scotland', 'c1', False), ANABAP, ARIAN]
ST['1690'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, ANGLICAN, INDEP, REFORMED, COVEN, (U(9, 13), 'Church of|Scotland', 'c1', False), ANABAP, ARIAN]
ST['1733'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, ANGLICAN, INDEP, REFORMED, COVEN, SCOTLAND, (U(10, 13), 'Seceders', 'c1', False), ANABAP, ARIAN]
ST['1747'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, ANGLICAN, INDEP, REFORMED, COVEN, SCOTLAND, (U(10, 11), 'Burgher', 'c3', False), (U(12, 13), 'Anti-|Burgher', 'c1', False), ANABAP, ARIAN]
ST['1806'] = [EAST, ORIENTAL, ORTHODOX, CATHOLIC, LUTHERAN, ANGLICAN, INDEP, REFORMED, COVEN, SCOTLAND,
              (U(10), 'Burgher|Old Light', 'c3', False), (U(11), 'Burgher|New Light', 'c4', False),
              (U(12), 'Anti-Burgher|Old Light', 'c2', False), (U(13), 'Anti-Burgher|New Light', 'c3', False), ANABAP, ARIAN]


S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]
FLOW_SVG = re.search(r'<svg.*?</svg>', open(_D + '/../../elements/christendom-divisions.html').read(), re.S).group(0)
# keep the element's class names clear of the deck engine's .sub / .lab / .x rules
FLOW_SVG = FLOW_SVG.replace('class="sub"', 'class="fsub"').replace('class="lab"', 'class="flab"').replace('class="x"', 'class="fx"')
NOTES = {
"325": "Constantine had just reunited the empire (324) and found the church at war over whether the Son is God. He convened the council himself. The creed condemned Arius with the word <i>homoousios</i>.<br>Failure: Constantine was baptized on his deathbed by an Arian sympathizer; his son pushed the empire Arian; Athanasius was exiled five times. Jerome: &ldquo;the whole world groaned and found itself Arian.&rdquo;<br>&rarr; The first creed written to unite the church did not unite the two sides; it named them.",
"381": "Theodosius made the Nicene faith imperial law (<i>Cunctos populos</i>, 380) and called the council (381). It finished the creed churches say today. Thirty-six Macedonian bishops, who denied the Spirit&rsquo;s full divinity, walked out.<br>Failure: Arianism did not die; it left the empire. The Goths, Vandals and Lombards who took the West stayed Arian into the 500s and 600s. Canon 3 ranked Constantinople second after Rome, &ldquo;because it is New Rome&rdquo;: the seed of 1054.<br>&rarr; The council finished the creed; the emperor made it law; the church that refused it moved across the border.",
"431": "Nestorius objected to <i>Theotokos</i>; Cyril of Alexandria opened the council before John of Antioch arrived. Each side deposed the other&rsquo;s leader, and the emperor arrested both. A Formula of Reunion patched it in 433.<br>Canon 7 forbade any &ldquo;different faith&rdquo; beside Nicaea&rsquo;s: the ban the next council breaks, and the one the East cites against the West in 1054.<br>The Church of the East (Persia) refused Ephesus and has been separate since: today the Assyrian Church of the East.<br>&rarr; Plant the canon. &ldquo;We will come back to that.&rdquo;",
"451": "Chalcedon reaffirmed Ephesus&rsquo;s ban on new creeds, then issued the Definition (&ldquo;in two natures&rdquo;) and said it was a definition, not a creed. The 381 creed is first read into the record here. Egypt, Armenia, Ethiopia, the Syriac churches refused it: the Oriental Orthodox, non-Chalcedonian to this day (Copts, Armenians, Ethiopians, Eritreans, Syriacs, Malankara).<br>&rarr; The rhyme to plant: &ldquo;not a new creed.&rdquo; The thirteen propositions will say the same words.',",
"482": "Zeno&rsquo;s Henotikon (&ldquo;instrument of union&rdquo;), drafted with Patriarch Acacius, tried to reconcile both sides by affirming Nicaea, Ephesus and Cyril and passing over Chalcedon in silence. It did not win Egypt back. Pope Felix III excommunicated Acacius (484), and Rome and Constantinople were out of communion until 519.<br>&rarr; A document literally named &ldquo;instrument of union&rdquo; produced the first schism between Rome and Constantinople.",
"1054": "The Filioque (&ldquo;and the Son&rdquo;) entered the creed in Spain (Toledo 589), spread through the Frankish church, and was adopted at Rome about 1014. The East objected to the content and to the unilateral change, citing Ephesus Canon 7. Cardinal Humbert&rsquo;s legation (1054) also contested leavened bread and papal primacy; on 16 July he laid the bull on the altar; Patriarch Cerularius anathematized the legates. The date is conventional; the estrangement was long and the 1204 sack sealed it. Mutual anathemas lifted 1965, communion not restored.<br>&rarr; How do two churches with the same creed divide over the creed? Which version, and who decides.',",
"1530": "1517 the theses. Rome answers with the bull <i>Exsurge Domine</i> (1520) and excommunicates Luther (3 January 1521). Charles V summons him to the imperial diet at Worms; he appears on 17&ndash;18 April 1521 and will not recant. The Edict of Worms (May 1521) declares him an outlaw and bans his writings. The instrument is the emperor&rsquo;s edict, meant to hold the West together; it holds nothing, and the West is in two.<br>We come back to this room after the Preamble: Luther at Worms is the conscience thread.<br>&rarr; An edict can outlaw a man. It cannot make him recant.",
"1527": "The one instrument on the egg that was not a creed: unity by force. After the 1525 disputations, Zurich&rsquo;s council ordered infants baptized and rebaptizers banished, then (March 1526) drowned. Felix Manz died 5 January 1527, the first Protestant executed by Protestants. Schleitheim (February 1527) set out believer&rsquo;s baptism and separation from the sword; Sattler was burned that May.<br>Six years after Worms: the first split inside Protestantism. It comes back after Proposition 9.<br>&rarr; Unity by creed fails; unity by force fails worse.",
"1529": "Marburg Colloquy, 1&ndash;4 October 1529, called by Philip of Hesse to unite the Protestants politically and theologically. The Marburg Articles: agreement on fourteen, and on the fifteenth (the Supper) agreement on everything except whether Christ&rsquo;s body is bodily present. Luther&rsquo;s line to the Swiss: &ldquo;Ihr habt einen andern Geist.&rdquo; Lutheran and Reformed have been separate confessional families since. The Formula of Concord (1577) settled Lutheran infighting by excluding the Reformed.<br>&rarr; Thomas Campbell will call the Supper &ldquo;that great ordinance of unity and love.&rdquo; It is the one thing they could not agree on.',",
"1646": "Solemn League and Covenant (1643): Scotland&rsquo;s price for joining Parliament&rsquo;s war was a common Presbyterian settlement for all three kingdoms. The Westminster Assembly (1643&ndash;49) produced the Confession (1646) and catechisms. The Independents (the &ldquo;Dissenting Brethren&rdquo;) argued against Presbyterian government inside the Assembly. Parliament never fully established it in England; the Restoration (1660) restored bishops; the Act of Uniformity (1662) ejected about two thousand ministers, the Great Ejection. Scotland adopted the Confession in 1647 and keeps it.<br>&rarr; The confession Thomas Campbell was tried under was written to unite three kingdoms. It produced nonconformity.',",
"1690": "William and Mary&rsquo;s settlement (1690) abolished bishops and established Presbyterianism with the Westminster Confession, but without the Covenants, which the state did not renew. The Cameronians (Society People) refused to enter and became the Reformed Presbyterian Church (1743 as a presbytery). The Episcopalians went out the other side.<br>Cuttable: the Secession slide carries the Scottish story on its own.',",
"1733": "The Patronage Act (1712) restored lay patrons&rsquo; right to present ministers. Erskine&rsquo;s synod sermon (October 1732) attacked it; the Assembly rebuked him (1733); he and three others (Wilson, Moncrieff, Fisher) protested, were suspended, and formed the Associate Presbytery (December 1733). Deposed 1740. The Seceders renewed the Covenants; the Week 2 litany note has this.<br>&rarr; His tradition began as a protest against imposed authority.',",
"1747": "The oath, required of burgesses in Edinburgh, Glasgow and Perth: &ldquo;the true religion presently professed within this realm and authorized by the laws thereof.&rdquo; Burghers: it means only &ldquo;not Catholic.&rdquo; Anti-Burghers: it blesses the church we left. The synod split April 1747 (Associate Synod vs General Associate Synod); the Anti-Burghers excommunicated the Burghers (1748&ndash;49), and the two could not take communion together. Thomas Campbell was Anti-Burgher. The Week 2 litany note covers why it felt so large (the Testimony, the Covenants).<br>&rarr; This is the rule Conemaugh broke, and the room already knows it.',",
"1799": "The Burghers split 1799 (Original Burghers, Old Light), the Anti-Burghers 1806 (Constitutional Associate Presbytery, Old Light) over whether the civil magistrate has power in religion (Westminster Confession ch. 23). Campbell sided with the Old Lights by friendship more than conviction (Foster; Week 2 note). He sailed April 1807.<br>Cuttable: the Week 2 litany already told this. Keep if the room needs the landing.',"
}

def christendom_slides():
    S = []
    A = S.append
    # ---------- CHRISTENDOM'S SEARCH FOR UNITY ----------
    A(C('Christendom&rsquo;s Search for Unity',
        'Card. Lands after the Preamble&rsquo;s despair (&ldquo;amid the diversity and rancor of party contentions&rdquo;) and before &ldquo;anywhere but in Christ.&rdquo; One click per slide. Eight to ten minutes with every slide; 1690 and 1799 are marked cuttable in their notes.'))

    A(D('325 &middot; Council of Nicaea',
        'Arians against non-Arians. A creed, and fifty-six more years of war.',
        '0', '325', NOTES['325']))

    A(D('381 &middot; Council of Constantinople',
        'Is the Spirit God too? The creed we still say, the Arians outlawed, and the Goths still Arian.',
        '325', '381', NOTES['381']))

    A(D('431 &middot; Council of Ephesus',
        'Does Mary bear God? A canon forbidding new creeds, and the Church of the East gone.',
        '381', '431', NOTES['431']))

    A(D('451 &middot; Council of Chalcedon',
        'One nature or two? A Definition, &ldquo;not a new creed,&rdquo; and Egypt gone.',
        '431', '451', NOTES['451']))

    A(D('482 &middot; Instrument of Union',
        'Zeno needs Egypt back. The Henotikon, and thirty-five years of schism with Rome.',
        '451', '482', NOTES['482'], heal='519'))

    A(D('1054 &middot; The Filioque',
        'One word added to the creed. Legates sent to settle it, and East and West apart.',
        '519', '1054', NOTES['1054']))

    A(D('1521 &middot; The Diet of Worms',
        'Luther before the emperor. An edict to silence him, and the West in two.',
        '1054', '1530', NOTES['1530']))

    A(D('1527 &middot; Zurich',
        'No creed this time. The magistrate. A council ruling, the sword, and Felix Manz drowned.',
        '1530', '1527', NOTES['1527']))

    A(D('1529 &middot; The Marburg Colloquy',
        'The Lord&rsquo;s Supper. Fourteen articles agreed, and &ldquo;you have a different spirit.&rdquo;',
        '1527', '1529', NOTES['1529']))

    A(D('1646 &middot; The Westminster Confession',
        'Three kingdoms at war. One confession for all three, and two thousand ministers ejected.',
        '1529', '1646', NOTES['1646']))

    A(D('1690 &middot; The Revolution Settlement',
        'Scotland after the Revolution. Presbytery restored, and the Covenanters outside.',
        '1646', '1690', NOTES['1690'], cut=True))

    A(D('1733 &middot; The Secession',
        'Patrons appoint ministers. Erskine rebuked, and four ministers walk out.',
        '1690', '1733', NOTES['1733']))

    A(D('1747 &middot; The Burgess Oath',
        'May a Seceder swear it? A synod vote, and mutual excommunication.',
        '1733', '1747', NOTES['1747']))

    A(D('1799 &middot; 1806 &middot; Old Light, New Light',
        'May the magistrate enforce religion? Revised Testimonies, and each synod in two.',
        '1747', '1806', NOTES['1799'], cut=True))

    A('<section class="slide divslide shatterslide"><h2>&hellip;and today</h2>'
      '<div class=line>Too many divisions to count.</div>'
      '<div class="failure frag">' + shatter() + '</div>'
      '<aside class=notes>The egg, shattered. Dozens of pieces, many of them named, the names chosen to make the room smile (four kinds of Church of Christ are in there). No click; it is simply on screen.<br>'
      '&rarr; Every one of these was somebody&rsquo;s instrument of unity.</aside></section>')

    A('<section class="slide treeslide2"><div class="eyebrow quiet">The tree of divisions</div>' + tree_svg() +
      '<aside class=notes>Every branch is a church leaving another, placed at its year; time runs left to right, with the Reformation given most of the width. The leaves at the right edge are churches that still exist. Simplified and partial on purpose: the real tree does not fit on a wall.<br>'
      '&rarr; Not one of these produced unity. Not one held even the people who signed it.</aside></section>')
    return S

CHRISTENDOM_CSS = '  /* ---- the division slides: headline / line / split ---- */\n  :root{--c1:#c89b3c;--c2:#a84a33;--c3:#5f8aa3;--c4:#6f9a6a;--bone:#ede4d3}\n  #deck .divslide{justify-content:flex-start;padding-top:5vmin;gap:0}\n  #deck .divslide h2{font-size:clamp(36px,6.8vmin,86px);max-width:none}\n  #deck .divslide .line{margin-top:1vmin;font-family:Spectral,Georgia,serif;font-style:italic;font-size:clamp(16px,2.8vmin,34px);line-height:1.35;max-width:none;white-space:nowrap;color:var(--bone-dim)}\n  #deck .divslide .failure{margin-top:1vmin;width:100%;display:flex;justify-content:center}\n  #deck .divslide h2,#deck .divslide .line{position:relative;z-index:2;text-shadow:0 0 .6vmin var(--ground),0 0 1.4vmin var(--ground),0 0 2.4vmin var(--ground)}\n  #deck .divslide.wide .failure{margin-top:-6vh}#deck .divslide.wide .splitfig{height:min(80vh,88vmin)}#deck .divslide.wide h2,#deck .divslide.wide .line{background:var(--ground);padding:0 .5em;border-radius:.25em}\n  #deck .divslide .splitfig{height:min(72vh,80vmin);width:auto;max-width:98vw;display:block}\n  /* the figure is on screen before the click as the before-state; the click moves it to the after-state */\n  #deck .divslide .failure.frag{opacity:1;transform:none}\n  .splitfig .piece path{d:var(--d0);fill:var(--k0);stroke:var(--s0);stroke-width:1.5;transition:d .9s cubic-bezier(.6,0,.3,1),fill .7s ease .25s,stroke .3s ease,opacity .7s ease .25s}\n  .splitfig .piece.gone0 path{opacity:0}.failure.on .piece.gone1 path{opacity:0!important}\n  .splitfig .piece.dying0 path{opacity:.35}.failure.on .piece path{opacity:1}.failure.on .piece.dying1 path{opacity:.35}\n  .failure.on .piece path{d:var(--d1);fill:var(--k1);stroke:var(--s1)}\n  .splitfig .seam{d:var(--d0);fill:none;stroke:var(--ground);stroke-width:5;stroke-linejoin:round;opacity:0;transition:d .9s cubic-bezier(.6,0,.3,1),opacity .5s ease}\n  .splitfig .seam.on0{opacity:1}.failure.on .seam{d:var(--d1);opacity:0}.failure.on .seam.on1{opacity:1}\n  #deck .divslide:has(.healer.on) .failure.on .seam{d:var(--d2);opacity:0}#deck .divslide:has(.healer.on) .failure.on .seam.on2{opacity:1}\n  #deck .shatterslide .shards{height:min(70vh,78vmin);width:auto;max-width:96vw;display:block}\n  .shards .shardlab{font-family:"IM Fell English",Georgia,serif;fill:var(--bone);paint-order:stroke;stroke:var(--ground);stroke-width:3px;stroke-linejoin:round;pointer-events:none}\n  .splitfig .plab{font-family:"IM Fell English",Georgia,serif;font-size:30px;fill:var(--bone);transition:opacity .6s ease}\n  .splitfig .plab.post{opacity:0;transition-delay:.6s}.failure.on .plab.post{opacity:1}\n  .splitfig .plab.pre{opacity:1}.failure.on .plab.pre{opacity:0;transition-delay:0s}\n  .splitfig .plab.dim{fill:var(--smoke);font-style:italic}\n  /* the Henotikon: a second click closes the gap again, leaving a gold seam */\n  .healer{height:0}\n  #deck .divslide:has(.healer.on) .failure.on .piece path{d:var(--d2)}\n  \n  \n  /* ---- the tree of divisions ---- */\n  #deck .treeslide2{padding:2vmin 3vmin 4vmin;justify-content:center}#deck .treeslide2 .eyebrow{margin-bottom:.6vmin}\n  #deck .treeslide2 .tree2{height:min(84vh,88vmin);width:auto;max-width:96vw;display:block}\n  .tree2 .tb{stroke-width:1.6;fill:none;stroke-linecap:round}.tree2 .leafline{opacity:.45}\n  .tree2 .tn{stroke:var(--ground);stroke-width:2}\n  .tree2 .tl{font-family:"IM Fell English",Georgia,serif;fill:var(--bone);paint-order:stroke;stroke:var(--ground);stroke-width:5px;stroke-linejoin:round}\n  .tree2 .tl .yr{font-family:"IM Fell English SC",Georgia,serif;fill:var(--gold);font-size:.8em;letter-spacing:.08em}\n  .tree2 .lf{font-family:Spectral,Georgia,serif;fill:var(--bone-dim)}.tree2 .lf.dead{fill:var(--smoke);font-style:italic}\n  .tree2 .tick{stroke:var(--ink-brown);stroke-width:1;stroke-dasharray:2 6}.tree2 .tk{font-family:"IM Fell English SC",Georgia,serif;font-size:13px;letter-spacing:.14em;fill:var(--smoke)}\n'
