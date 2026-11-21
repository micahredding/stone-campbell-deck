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
# ---- people (members 1906, 1926; adherents 1980, 2000, 2020), the measure that runs the whole way ----
FULL = {n.upper(): f for n, f in [('Alabama','01'),('Arizona','04'),('Arkansas','05'),('California','06'),('Colorado','08'),('Connecticut','09'),('Delaware','10'),('District of Columbia','11'),('Florida','12'),('Georgia','13'),('Idaho','16'),('Illinois','17'),('Indiana','18'),('Iowa','19'),('Kansas','20'),('Kentucky','21'),('Louisiana','22'),('Maine','23'),('Maryland','24'),('Massachusetts','25'),('Michigan','26'),('Minnesota','27'),('Mississippi','28'),('Missouri','29'),('Montana','30'),('Nebraska','31'),('Nevada','32'),('New Hampshire','33'),('New Jersey','34'),('New Mexico','35'),('New York','36'),('North Carolina','37'),('North Dakota','38'),('Ohio','39'),('Oklahoma','40'),('Oregon','41'),('Pennsylvania','42'),('Rhode Island','44'),('South Carolina','45'),('South Dakota','46'),('Tennessee','47'),('Texas','48'),('Utah','49'),('Vermont','50'),('Virginia','51'),('Washington','53'),('West Virginia','54'),('Wisconsin','55'),('Wyoming','56')]}
FULL['DIST. OF COLUMBIA'] = '11'; FULL['DIST OF COLUMBIA'] = '11'
P2 = {}
for yr, cc in (('1906', 'chchrist'), ('1926', 'chchrist')):
    d = pd.read_stata(os.path.join(DATA, '%sCENSCT.dta' % yr), convert_categoricals=False)
    by, miss, tot = {}, 0, {'disciples': 0, 'churches_of_christ': 0}
    for _, r in d.iterrows():
        a = int(r['disciple']) if pd.notna(r['disciple']) else 0; b = int(r[cc]) if pd.notna(r[cc]) else 0
        tot['disciples'] += a; tot['churches_of_christ'] += b
        if not a + b: continue
        f = IDX.get((FULL.get(str(r['state']).strip().upper(), '??'), norm(str(r['cntyname']))))
        if f: by[f] = by.get(f, 0) + a + b
        else: miss += a + b
    p, off = pts(by); P2[yr] = {'points': p, 'by_body': tot, 'total': sum(tot.values()), 'unplaced': miss + off, 'measure': 'members'}
    print(yr, 'members', tot, 'unplaced', miss + off)
for yr, f, cols in [('1980', 'CMS80CNT', ['CCHRIS_A', 'CCCC_A', 'DOFC_A']), ('2000', 'RCMSCY', ['chschad', 'chrchad', 'chrdiad', 'inchcad'])]:
    d = pd.read_stata(os.path.join(DATA, f + '.dta'), convert_categoricals=False)
    fc = 'fips' if 'fips' in d.columns else 'fip'
    by, tot = {}, {}
    for _, r in d.iterrows():
        n = sum(int(v) for v in (pd.to_numeric(r[x], errors='coerce') for x in cols) if pd.notna(v))
        if n: k = '%05d' % int(r[fc]); by[k] = by.get(k, 0) + n
    for x in cols: tot[x] = int(pd.to_numeric(d[x], errors='coerce').fillna(0).sum())
    p, off = pts(by); P2[yr] = {'points': p, 'by_body': tot, 'total': sum(tot.values()), 'unplaced': off, 'measure': 'adherents'}
    print(yr, 'adherents', tot, 'unplaced', off)
import openpyxl
ws = openpyxl.load_workbook(os.path.join(CACHE, '2020_USRC_Group_Detail.xlsx'), read_only=True)['2020 Group by County']
by, tot = {}, {}
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[3] in ('167', '097', '093', '264') and r[6]:
        by[r[0]] = by.get(r[0], 0) + r[6]; tot[r[3]] = tot.get(r[3], 0) + r[6]
p, off = pts(by); P2['2020'] = {'points': p, 'by_body': tot, 'total': sum(tot.values()), 'unplaced': off, 'measure': 'adherents'}
print('2020 adherents', tot, 'unplaced', off)

# ---- 1850, 1860, 1870: churches of the census category "Christian" (Disciples and the Christian Connection together),
# IPUMS NHGIS county tables NT47 (1850), NT26 (1860), NT41 (1870); extract nhgis0001 in DATA/nhgis/ ----
NH = os.path.join(DATA, 'nhgis')
if os.path.isdir(NH):
    for yr, f, cc, aa in (('1850', 'ds10_1850', 'AET002', 'AEU002'), ('1860', 'ds14_1860', 'AHL003', 'AHN003'), ('1870', 'ds17_1870', 'AK5002', 'AK6002')):
        d = pd.read_csv(os.path.join(NH, 'nhgis0001_%s_county.csv' % f), encoding='latin-1', skiprows=[1])
        by, miss, tot, seats = {}, 0, 0, 0
        for _, r in d.iterrows():
            n = int(r[cc]) if pd.notna(r[cc]) else 0; a = int(r[aa]) if pd.notna(r[aa]) else 0; tot += n; seats += a
            if not n: continue
            f2 = IDX.get((FULL.get(str(r['STATE']).strip().upper(), '??'), norm(str(r['COUNTY']))))
            if f2: by[f2] = by.get(f2, 0) + max(a, 1)
            else: miss += n
        p, off = pts(by); P2[yr] = {'points': p, 'total': tot, 'seats': seats, 'unplaced': miss, 'measure': 'churches (glow by seats)'}
        print(yr, 'churches', tot, 'seats', seats, 'unplaced', miss + off)
R['people'] = P2
json.dump(R, open(os.path.join(H_, '..', 'history_points.json'), 'w')); print('wrote history_points.json')
