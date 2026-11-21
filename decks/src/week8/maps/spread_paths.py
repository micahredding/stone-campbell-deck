# Projects U.S. state outlines for the national spread map (decks/src/week8/spreadmap.py) into ../spread_paths.json.
# Data: us-atlas 3.0.1 (Census cartographic boundaries, public domain), fetched from cdn.jsdelivr.net into argv[1].
import json, math, os, sys, urllib.request
CACHE = sys.argv[1] if len(sys.argv) > 1 else '/tmp/franklin-cache'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spread_paths.json')
p = os.path.join(CACHE, 'states-10m.json')
if not os.path.exists(p):
    os.makedirs(CACHE, exist_ok=True); urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/states-10m.json', p)
topo = json.load(open(p))
sx, sy = topo['transform']['scale']; tx, ty = topo['transform']['translate']
arcs = []
for arc in topo['arcs']:
    x = y = 0; pts = []
    for dx, dy in arc:
        x += dx; y += dy; pts.append((x * sx + tx, y * sy + ty))
    arcs.append(pts)
def ring(ix):
    pts = []
    for i in ix:
        a = arcs[i] if i >= 0 else arcs[~i][::-1]
        pts += a if not pts else a[1:]
    return pts
W, H = 1600, 900
LON0, LON1, LAT0, LAT1 = -125.5, -65.5, 23.8, 50.2
C = math.cos(math.radians(38))
k = min(W / ((LON1 - LON0) * C), H / (LAT1 - LAT0))
ox = (W - (LON1 - LON0) * C * k) / 2; oy = (H - (LAT1 - LAT0) * k) / 2
def P(lon, lat): return (ox + (lon - LON0) * C * k, oy + (LAT1 - lat) * k)
SKIP = {'Alaska', 'Hawaii', 'Puerto Rico', 'United States Virgin Islands', 'Guam', 'Commonwealth of the Northern Mariana Islands', 'American Samoa'}
paths = {}
for g in topo['objects']['states']['geometries']:
    nm = g['properties']['name']
    if nm in SKIP: continue
    rs = [ring(r) for r in g['arcs']] if g['type'] == 'Polygon' else [ring(r) for poly in g['arcs'] for r in poly]
    d = []
    for r in rs:
        pts = [P(*q) for q in r]
        simp = [pts[0]] + [q for a, q in zip(pts, pts[1:]) if abs(q[0] - a[0]) + abs(q[1] - a[1]) > 1.2]
        if len(simp) > 2: d.append('M' + 'L'.join('%.1f,%.1f' % q for q in simp) + 'Z')
    paths[nm] = ''.join(d)
json.dump({'W': W, 'H': H, 'lon0': LON0, 'lat1': LAT1, 'C': C, 'k': k, 'ox': ox, 'oy': oy, 'paths': paths}, open(OUT, 'w'))
print('wrote', OUT, len(paths), 'states', os.path.getsize(OUT) // 1024, 'KB')
