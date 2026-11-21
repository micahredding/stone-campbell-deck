# Chapter 8: map of the State of Franklin (Micah, 2026-11-21). Writes ../images/franklin-map.svg.
# Data: us-atlas 3.0.1 (Census cartographic boundaries), fetched from cdn.jsdelivr.net into a cache dir given as argv[1].
# Franklin (1784-88) is shaded by today's counties that lie within it (approximate: its western line was never settled).
import json, math, os, sys, urllib.request
CACHE = sys.argv[1] if len(sys.argv) > 1 else '/tmp/franklin-cache'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'franklin-map.svg')
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

W, H = 1600, 900
LON0, LON1, LAT1 = -86.05, -80.5, 37.45
K = W / ((LON1 - LON0) * math.cos(math.radians(36.6)))
def P(lon, lat): return ((lon - LON0) * math.cos(math.radians(36.6)) * K, (LAT1 - lat) * K)
def path(rs): return ' '.join('M' + 'L'.join('%.1f,%.1f' % P(*p) for p in r) + 'Z' for r in rs)

st = load('states-10m.json'); sa = arcs_of(st)
co = load('counties-10m.json'); ca = arcs_of(co)
FR = ('091', '019', '163', '179', '171', '059', '073', '063', '089', '029', '155', '009', '093', '057')
states = {g['properties']['name']: rings(g, sa) for g in st['objects']['states']['geometries']}
fr = [rings(g, ca) for g in co['objects']['counties']['geometries'] if g['id'][:2] == '47' and g['id'][2:] in FR]

GOLD, BONE, DIM = '#c9a24a', '#ede4d3', '#8a7f6e'
o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" font-family="IM Fell English, Georgia, serif">' % (W, H),
     '<rect width="%d" height="%d" fill="#0e0b09"/>' % (W, H)]
for name, rs in states.items():
    o.append('<path d="%s" fill="#1b1611" stroke="%s" stroke-width="1.6" stroke-linejoin="round"/>' % (path(rs), DIM))
o.append('<g fill="%s" fill-opacity=".55" stroke="%s" stroke-opacity=".3" stroke-width="1" stroke-linejoin="round">' % (GOLD, GOLD))
for rs in fr: o.append('<path d="%s"/>' % path(rs))
o.append('</g>')
def label(lon, lat, t, size=40, fill=DIM, anchor='middle', italic=False, ls=0.08):
    x, y = P(lon, lat)
    o.append('<text x="%.0f" y="%.0f" font-size="%d" fill="%s" text-anchor="%s"%s letter-spacing="%.2fem">%s</text>' % (x, y, size, fill, anchor, ' font-style="italic"' if italic else '', ls, t))
x, y = P(-83.25, 37.22); o.append('<text x="%.0f" y="%.0f" font-size="66" fill="%s" text-anchor="middle" letter-spacing=".04em" stroke="#0e0b09" stroke-width="8" paint-order="stroke">The State of Franklin</text>' % (x, y, GOLD))
o.append('<text x="%.0f" y="%.0f" font-size="36" fill="%s" text-anchor="middle" font-style="italic" stroke="#0e0b09" stroke-width="8" paint-order="stroke">1784&#8211;1788</text>' % (x, y + 46, BONE))
label(-85.3, 37.15, 'KENTUCKY', 40); label(-85.2, 35.55, 'TENNESSEE', 40); label(-81.15, 36.95, 'VIRGINIA', 40)
label(-81.25, 35.35, 'NORTH CAROLINA', 38)
def place(lon, lat, t, sub='', dx=16, dy=10, anchor='start', star=False, sdy=32):
    x, y = P(lon, lat)
    if star:
        o.append('<polygon points="%s" fill="%s" stroke="#0e0b09" stroke-width="2"/>' % (' '.join('%.1f,%.1f' % (x + (18 if i % 2 == 0 else 8) * math.sin(math.radians(i * 36)), y - (18 if i % 2 == 0 else 8) * math.cos(math.radians(i * 36))) for i in range(10)), BONE))
    else:
        o.append('<circle cx="%.1f" cy="%.1f" r="9" fill="%s" stroke="#0e0b09" stroke-width="2"/>' % (x, y, BONE))
    o.append('<text x="%.0f" y="%.0f" font-size="38" fill="%s" text-anchor="%s" stroke="#0e0b09" stroke-width="7" paint-order="stroke">%s</text>' % (x + dx, y + dy, BONE, anchor, t))
    if sub: o.append('<text x="%.0f" y="%.0f" font-size="30" fill="%s" text-anchor="%s" font-style="italic" stroke="#0e0b09" stroke-width="7" paint-order="stroke">%s</text>' % (x + dx, y + dy + sdy, GOLD, anchor, sub))
place(-82.33, 36.53, 'Sullivan County', 'John Smith born, 1784', star=True, dx=26, dy=-14, sdy=36)
place(-82.47, 36.29, 'Jonesborough', 'first capital', dx=20, dy=30, sdy=34)
place(-82.83, 36.16, 'Greeneville', 'capital', dx=-20, dy=12, anchor='end', sdy=34)
place(-85.13, 36.69, 'Stockton&#8217;s Valley', 'where he grew up', dx=0, dy=-66, anchor='middle', sdy=34)
x, y = P(-80.6, 34.97) if False else (W - 24, H - 18)
o.append('<text x="%.0f" y="%.0f" font-size="20" fill="%s" text-anchor="end" font-family="Spectral, Georgia, serif" stroke="#0e0b09" stroke-width="6" paint-order="stroke">Franklin shaded by the present-day counties it held (approximate). State lines are today&#8217;s. Data: U.S. Census Bureau (us-atlas).</text>' % (x, y, DIM))
o.append('</svg>')
open(OUT, 'w').write('\n'.join(o)); print('wrote', OUT)
