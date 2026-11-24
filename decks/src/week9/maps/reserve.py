# Chapter 9 maps (2026-11-24): Raines's road west, and the Western Reserve in 1828.
# Writes ../images/map-road.svg and ../images/map-reserve.svg.
# Data: us-atlas 3.0.1 (U.S. Census cartographic boundaries, public domain), fetched from cdn.jsdelivr.net
# into a cache dir given as argv[1]. The Reserve is shaded by today's counties that lie (mostly) within it:
# approximate, since a few counties straddle its southern line (41 N).
import json, math, os, sys, urllib.request
CACHE = sys.argv[1] if len(sys.argv) > 1 else '/tmp/usatlas-cache'
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images')
def load(name):
    os.makedirs(CACHE, exist_ok=True); p = os.path.join(CACHE, name)
    if not os.path.exists(p):
        urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/' + name, p)
    return json.load(open(p))
def arcs_of(topo):
    sx, sy = topo['transform']['scale']; tx, ty = topo['transform']['translate']; out = []
    for arc in topo['arcs']:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy; pts.append((x * sx + tx, y * sy + ty))
        out.append(pts)
    return out
def rings(geom, arcs):
    def ring(ix):
        pts = []
        for i in ix:
            a = arcs[i] if i >= 0 else arcs[~i][::-1]
            pts += a if not pts else a[1:]
        return pts
    if geom['type'] == 'Polygon': return [ring(r) for r in geom['arcs']]
    if geom['type'] == 'MultiPolygon': return [ring(r) for p in geom['arcs'] for r in p]
    return []
st = load('states-10m.json'); sa = arcs_of(st)
co = load('counties-10m.json'); ca = arcs_of(co)
states = {g['properties']['name']: rings(g, sa) for g in st['objects']['states']['geometries']}
GOLD, BONE, DIM, INK = '#c9a24a', '#ede4d3', '#8a7f6e', '#0e0b09'
W, H = 1600, 900

def make(lon0, lon1, lat1, latc):
    c = math.cos(math.radians(latc)); K = W / ((lon1 - lon0) * c)
    def P(lon, lat): return ((lon - lon0) * c * K, (lat1 - lat) * K)
    def path(rs): return ' '.join('M' + 'L'.join('%.1f,%.1f' % P(*p) for p in r) + 'Z' for r in rs)
    return P, path

def head(o):
    o += ['<svg style="width:100%%;height:100%%;display:block" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" font-family="IM Fell English, Georgia, serif">' % (W, H),
          '<rect width="%d" height="%d" fill="%s"/>' % (W, H, INK)]
def txt(o, x, y, t, size=38, fill=BONE, anchor='start', italic=False, ls=0):
    o.append('<text x="%.0f" y="%.0f" font-size="%d" fill="%s" text-anchor="%s"%s letter-spacing="%.2fem" stroke="%s" stroke-width="7" paint-order="stroke">%s</text>'
             % (x, y, size, fill, anchor, ' font-style="italic"' if italic else '', ls, INK, t))
def dot(o, x, y, r=9, fill=BONE, star=False):
    if star:
        o.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="2"/>' % (' '.join('%.1f,%.1f' % (x + (19 if i % 2 == 0 else 8) * math.sin(math.radians(i * 36)), y - (19 if i % 2 == 0 else 8) * math.cos(math.radians(i * 36))) for i in range(10)), fill, INK))
    else:
        o.append('<circle cx="%.1f" cy="%.1f" r="%d" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, r, fill, INK))
def credit(o, t):
    o.append('<text x="%d" y="%d" font-size="20" fill="%s" text-anchor="end" font-family="Spectral, Georgia, serif" stroke="%s" stroke-width="6" paint-order="stroke">%s</text>' % (W - 24, H - 18, DIM, INK, t))

# Present-day counties mostly inside the Western Reserve (incl. the Firelands): Ohio FIPS 39xxx
RES = ('007', '155', '055', '085', '035', '133', '153', '103', '093', '077', '043', '099')

# ---- 1. The road west ----
P, path = make(-88.6, -75.9, 42.55, 39.5)
o = []; head(o)
for n, rs in states.items():
    o.append('<path d="%s" fill="#1b1611" stroke="%s" stroke-width="1.4" stroke-linejoin="round"/>' % (path(rs), DIM))
o.append('<g fill="%s" fill-opacity=".5" stroke="none">' % GOLD)
for g in co['objects']['counties']['geometries']:
    if g['id'][:2] == '39' and g['id'][2:] in RES: o.append('<path d="%s"/>' % path(rings(g, ca)))
o.append('</g>')
for n, (lon, lat) in {'VIRGINIA': (-78.3, 37.2), 'KENTUCKY': (-84.4, 37.35), 'INDIANA': (-86.3, 40.0), 'OHIO': (-82.8, 40.2),
                      'PENNSYLVANIA': (-77.6, 41.0), 'WEST VIRGINIA': (-80.6, 38.75)}.items():
    x, y = P(lon, lat); txt(o, x, y, n, 34, DIM, 'middle', ls=.1)
stops = [('Fredericksburg', -77.46, 38.30, 'born, 1797/98', 0, 50, 'middle'),
         ('Jefferson County, Ky.', -85.76, 38.25, 'the family moves west', 22, 52, 'start'),
         ('Fredonia, Ind.', -86.38, 38.18, 'a Restorationist', -22, -40, 'end'),
         ('The Western Reserve', -81.1, 41.2, 'preaching at large, 1828', 0, -46, 'middle')]
pts = [P(lon, lat) for _, lon, lat, *_ in stops]
order = [0, 1, 2, 3]
d = 'M%.1f,%.1f' % pts[0]
for i in (1, 2, 3):
    (x0, y0), (x1, y1) = pts[order[i - 1]], pts[order[i]]
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2 - 70
    d += ' Q%.1f,%.1f %.1f,%.1f' % (mx, my, x1, y1)
o.append('<path d="%s" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="14 10" stroke-linecap="round"/>' % (d, GOLD))
for (t, lon, lat, sub, dx, dy, anc), (x, y) in zip(stops, pts):
    dot(o, x, y, star=(t == 'The Western Reserve'))
    txt(o, x + dx, y + dy, t, 40, BONE, anc)
    txt(o, x + dx, y + dy + 34, sub, 30, GOLD, anc, italic=True)
x, y = P(-87.9, 42.1); txt(o, x, y, 'Aylett Raines&#8217;s road west', 58, GOLD, 'start')
credit(o, 'Gold: the Western Reserve (approximate, by today&#8217;s counties). State lines are today&#8217;s. Data: U.S. Census Bureau (us-atlas).')
o.append('</svg>'); open(os.path.join(IMG, 'map-road.svg'), 'w').write('\n'.join(o))

# ---- 2. The Western Reserve, 1828 (zoomed on Portage and Trumbull) ----
P, path = make(-81.95, -80.45, 41.62, 41.2)
o = []; head(o)
o.append('<rect width="%d" height="%d" fill="#141a1e"/>' % (W, H))
for n, rs in states.items():
    o.append('<path d="%s" fill="#1b1611" stroke="%s" stroke-width="2" stroke-linejoin="round"/>' % (path(rs), DIM))
o.append('<g fill="%s" fill-opacity=".16" stroke="%s" stroke-opacity=".55" stroke-width="1.5" stroke-linejoin="round">' % (GOLD, GOLD))
for g in co['objects']['counties']['geometries']:
    if g['id'][:2] == '39' and g['id'][2:] in RES: o.append('<path d="%s"/>' % path(rings(g, ca)))
o.append('</g>')
for t, lon, lat in (('PORTAGE COUNTY', -81.17, 41.03), ('TRUMBULL COUNTY', -80.70, 41.40), ('GEAUGA', -81.17, 41.50), ('SUMMIT', -81.55, 41.03)):
    x, y = P(lon, lat); txt(o, x, y, t, 30, '#a08a5c', 'middle', ls=.14)
x, y = P(-80.475, 41.33); o.append('<text x="%.0f" y="%.0f" font-size="28" fill="%s" text-anchor="middle" letter-spacing=".14em" transform="rotate(90 %.0f %.0f)">PENNSYLVANIA</text>' % (x, y, DIM, x, y))
x, y = P(-81.93, 41.60); txt(o, x, y, 'Lake Erie', 30, '#8fa3ad', 'start', italic=True)
x, y = P(-81.93, 41.55); txt(o, x, y, 'The Western Reserve, 1828', 60, GOLD, 'start')
places = [
    ('Windham', -81.049, 41.234, 'Scott preaches', 0, -64, 'middle', False),
    ('Warren', -80.818, 41.238, 'the Association, August 1828', 26, 12, 'start', True),
    ('Ravenna', -81.242, 41.158, 'Ebenezer Williams&#8217;s home', 22, 12, 'start', False),
    ('Sandy Lake', -81.296, 41.120, 'they baptize each other', -22, 12, 'end', False),
    ('Shalersville', -81.23, 41.22, 'Williams&#8217;s pulpit', -22, 40, 'end', False),
    ('Austintown', -80.765, 41.102, 'the renunciation sermon', 22, 12, 'start', False),
]
for t, lon, lat, sub, dx, dy, anc, star in places:
    x, y = P(lon, lat); dot(o, x, y, 10, BONE, star)
    txt(o, x + dx, y + dy, t, 42, BONE, anc)
    if sub: txt(o, x + dx, y + dy + 34, sub, 30, GOLD, anc, italic=True)
x, y = P(-80.80, 41.02); txt(o, x, y, '&#8595; New Lisbon 25 mi &#183; Bethany 70 mi', 30, BONE, 'middle', italic=True)
x0, y0 = P(-81.92, 41.035); mi = 10 / (69.0 * math.cos(math.radians(41.2)))
x1, _ = P(-81.92 + mi, 41.035)
o.append('<path d="M%.0f,%.0f H%.0f" stroke="%s" stroke-width="3"/>' % (x0, y0, x1, BONE)); txt(o, (x0 + x1) / 2, y0 - 12, '10 miles', 24, BONE, 'middle')
credit(o, 'Counties of the Western Reserve, with today&#8217;s lines. Data: U.S. Census Bureau (us-atlas).')
o.append('</svg>'); open(os.path.join(IMG, 'map-reserve.svg'), 'w').write('\n'.join(o))
print('wrote map-road.svg, map-reserve.svg')
