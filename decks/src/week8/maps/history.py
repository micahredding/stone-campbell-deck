# Stone-Campbell congregations by county in 1926, 1980 and 2000, for the "filling the gap" map (Micah, 2026-11-21).
# 1926: American Religious Ecologies (religiousecologies.org, RRCHNM), surviving schedules of the 1926 U.S. Census of
#   Religious Bodies, Disciples of Christ (66) and Churches of Christ (55), counted by the county each record names.
# 1980, 2000: Churches and Church Membership in the United States 1980 (Counties) and the Religious Congregations and
#   Membership Study 2000 (County File), from the ARDA (thearda.com), Stata files.
# Usage: python3 history.py DATA_DIR CACHE_DIR   (DATA_DIR: c1926.json, CMS80CNT.dta, RCMSCY.dta; CACHE_DIR: counties-10m.json)
import json, os, sys, re
import pandas as pd
DATA, CACHE = sys.argv[1], sys.argv[2]
H_ = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(H_, '..', 'spread_paths.json')))
def P(lon, lat): return (G['ox'] + (lon - G['lon0']) * G['C'] * G['k'], G['oy'] + (G['lat1'] - lat) * G['k'])
topo = json.load(open(os.path.join(CACHE, 'counties-10m.json'))); sx, sy = topo['transform']['scale']; tx, ty = topo['transform']['translate']
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
CEN, NAME = {}, {}
for g in topo['objects']['counties']['geometries']:
    rs = [ring(r[0]) for r in (g['arcs'] if g['type'] == 'MultiPolygon' else [g['arcs']])]
    lon, lat, _ = max((centroid(r) for r in rs), key=lambda t: t[2])
    if lon < -125.5 or lat < 23.8: continue
    CEN[g['id']] = P(lon, lat); NAME[g['id']] = g['properties']['name']
ST = dict(AL='01', AZ='04', AR='05', CA='06', CO='08', CT='09', DE='10', DC='11', FL='12', GA='13', ID='16', IL='17', IN='18', IA='19', KS='20', KY='21', LA='22', ME='23', MD='24', MA='25', MI='26', MN='27', MS='28', MO='29', MT='30', NE='31', NV='32', NH='33', NJ='34', NM='35', NY='36', NC='37', ND='38', OH='39', OK='40', OR='41', PA='42', RI='44', SC='45', SD='46', TN='47', TX='48', UT='49', VT='50', VA='51', WA='53', WV='54', WI='55', WY='56')
def norm(s): return re.sub(r'[^a-z]', '', s.lower().replace('saint', 'st').replace('st.', 'st'))
IDX = {}
for f, n in NAME.items(): IDX.setdefault((f[:2], norm(n)), f)
def pts(byfips):
    out, off = [], 0
    for f, n in byfips.items():
        if f in CEN: x, y = CEN[f]; out.append([round(x, 1), round(y, 1), int(n)])
        else: off += n
    return out, off
R = {}
# 1926
c = json.load(open(os.path.join(DATA, 'c1926.json'))); by, miss, den = {}, {}, {'66': 0, '55': 0}
for k, n in c.items():
    d, st, cn = k.split('|'); den[d] += n
    f = IDX.get((ST.get(st, '??'), norm(cn or '')))
    if f: by[f] = by.get(f, 0) + n
    else: miss[k] = n
p, off = pts(by)
R['1926'] = {'points': p, 'total': sum(den.values()), 'disciples': den['66'], 'coc': den['55'], 'unplaced': sum(miss.values()) + off}
print('1926 unplaced', sum(miss.values()), sorted(miss.items(), key=lambda t: -t[1])[:12])
for yr, f, cols in [('1980', 'CMS80CNT', ['DOFC_C', 'CCCC_C', 'CCHRIS_C']), ('2000', 'RCMSCY', ['chrdicg', 'chrchcg', 'chschcg', 'inchccg'])]:
    d = pd.read_stata(os.path.join(DATA, f + '.dta'), convert_categoricals=False)
    fc = 'fips' if 'fips' in d.columns else 'fip'
    by, tot = {}, {}
    for _, r in d.iterrows():
        n = sum(int(pd.to_numeric(r[x], errors='coerce') or 0) for x in cols if pd.notna(pd.to_numeric(r[x], errors='coerce')))
        fips = '%05d' % int(r[fc])
        if n: by[fips] = by.get(fips, 0) + n
    for x in cols: tot[x] = int(pd.to_numeric(d[x], errors='coerce').fillna(0).sum())
    p, off = pts(by)
    R[yr] = {'points': p, 'total': sum(tot.values()), 'by_body': tot, 'unplaced': off}
    print(yr, sum(tot.values()), 'unplaced', off)
json.dump(R, open(os.path.join(H_, '..', 'history_points.json'), 'w')); print('wrote history_points.json')
