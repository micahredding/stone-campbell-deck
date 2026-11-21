# Stone-Campbell congregations today, by county, for the map after the 1836-1860 spread (Micah, 2026-11-21).
# Data: 2020 U.S. Religion Census, "2020 Group by County" (Grammich et al., ASARB, 2022): Churches of Christ (167),
# Christian Churches and Churches of Christ (097), Christian Church (Disciples of Christ) (093), International Churches
# of Christ (264). County centroids from us-atlas 3.0.1 counties; same projection as spread_paths.json.
# Usage: python3 today.py CACHE_DIR  (CACHE_DIR holds 2020_USRC_Group_Detail.xlsx and counties-10m.json)
import json, os, sys, urllib.request, openpyxl
CACHE = sys.argv[1]
H_ = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(H_, '..', 'spread_paths.json')))
def P(lon, lat): return (G['ox'] + (lon - G['lon0']) * G['C'] * G['k'], G['oy'] + (G['lat1'] - lat) * G['k'])
x = os.path.join(CACHE, '2020_USRC_Group_Detail.xlsx')
if not os.path.exists(x): urllib.request.urlretrieve('https://www.usreligioncensus.org/sites/default/files/2023-06/2020_USRC_Group_Detail.xlsx', x)
c = os.path.join(CACHE, 'counties-10m.json')
if not os.path.exists(c): urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/us-atlas@3.0.1/counties-10m.json', c)
CODES = {'167': 'Churches of Christ', '097': 'Christian Churches and Churches of Christ', '093': 'Christian Church (Disciples of Christ)', '264': 'International Churches of Christ'}
ws = openpyxl.load_workbook(x, read_only=True)['2020 Group by County']
by, tot = {}, {k: [0, 0] for k in CODES}
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[3] in CODES and r[5]:
        by[r[0]] = by.get(r[0], 0) + r[5]; tot[r[3]][0] += r[5]; tot[r[3]][1] += (r[6] or 0)
topo = json.load(open(c)); sx, sy = topo['transform']['scale']; tx, ty = topo['transform']['translate']
arcs = []
for arc in topo['arcs']:
    a = b = 0; pts = []
    for dx, dy in arc: a += dx; b += dy; pts.append((a * sx + tx, b * sy + ty))
    arcs.append(pts)
def ring(ix):
    pts = []
    for i in ix:
        s = arcs[i] if i >= 0 else arcs[~i][::-1]; pts += s if not pts else s[1:]
    return pts
def centroid(pts):
    A = cx = cy = 0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:] + pts[:1]):
        f = x0 * y1 - x1 * y0; A += f; cx += (x0 + x1) * f; cy += (y0 + y1) * f
    return (cx / (3 * A), cy / (3 * A), abs(A)) if A else (pts[0][0], pts[0][1], 0)
out, missing = [], 0
geos = {g['id']: g for g in topo['objects']['counties']['geometries']}
for fips, n in by.items():
    g = geos.get(fips)
    if not g: missing += n; continue
    rs = [ring(r[0]) for r in (g['arcs'] if g['type'] == 'MultiPolygon' else [g['arcs']])]
    lon, lat, _ = max((centroid(r) for r in rs), key=lambda t: t[2])
    if lon < -125.5 or lat < 23.8: missing += n; continue      # Alaska, Hawaii, territories: off this map
    X, Y = P(lon, lat); out.append([round(X, 1), round(Y, 1), n])
json.dump({'points': out, 'totals': {CODES[k]: v for k, v in tot.items()}, 'off_map': missing}, open(os.path.join(H_, '..', 'today_points.json'), 'w'))
print(len(out), 'counties;', sum(p[2] for p in out), 'congregations on the map;', missing, 'off it;', tot)
