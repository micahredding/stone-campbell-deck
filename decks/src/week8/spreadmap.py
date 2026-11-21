# The one movement spreading after the union, 1836-1860 (Micah, 2026-11-21: "keep that going"): a national map that
# opens with the 1831-35 unions already lit (from unionmap.py), then lights the next waves, one click each.
# Dates are the earliest reports found in the Millennial Harbinger (see NOTES below); places approximate.
# State outlines: us-atlas 3.0.1 (Census, public domain), projected by maps/spread_paths.py into spread_paths.json.
import json, os, importlib.util
_H = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(_H, 'spread_paths.json')))
_s = importlib.util.spec_from_file_location('unionmap', os.path.join(_H, 'unionmap.py')); UM = importlib.util.module_from_spec(_s); _s.loader.exec_module(UM)
W, H = G['W'], G['H']
def P(lat, lon): return (G['ox'] + (lon - G['lon0']) * G['C'] * G['k'], G['oy'] + (G['lat1'] - lat) * G['k'])

WAVES = [   # (caption, [(name, lat, lon, label)]); label = (text, dx, dy, anchor) or None
    ('Already, beyond the union: the Reformers, 1828&ndash;34', [
        ('Western Reserve, Ohio', 41.10, -80.76, ('Western Reserve', 14, -12, 'start')), ('Pittsburgh', 40.44, -80.00, None),
        ('Philadelphia', 39.95, -75.17, ('Philadelphia', 14, 22, 'start')), ('New York', 40.73, -74.00, ('New York', 14, -8, 'start')),
        ('Bowling Green, Va.', 38.05, -77.35, None), ('Richmond, Va.', 37.54, -77.44, ('Virginia', 14, 24, 'start')),
        ('Little Rock', 34.75, -92.29, ('Arkansas', 14, -14, 'start')), ('Carlowsville, Ala.', 32.17, -87.00, ('Alabama', 14, 8, 'start')),
        ('Waterloo, Ala.', 34.92, -88.06, None), ('Toronto', 43.65, -79.38, ('Toronto', 0, -16, 'middle'))]),
    ('1836&ndash;39: Iowa, Michigan, Georgia, Mississippi, Wisconsin; New Brunswick; Britain', [
        ('Dubuque', 42.50, -90.66, ('Iowa 1835', -14, 6, 'end')), ('Grant Co., Wis.', 42.85, -90.71, ('Wisconsin 1838', -14, -16, 'end')),
        ('Middleville, Mich.', 42.71, -85.46, ('Michigan 1836', 0, -16, 'middle')), ('Clarke Co., Ga.', 33.95, -83.38, ('Georgia 1836', 14, 6, 'start')),
        ('Holly Springs, Miss.', 34.77, -89.45, None), ('Franklin Co., Miss.', 31.47, -90.90, ('Mississippi 1836', -14, 8, 'end')),
        ('Saint John, N.B.', 45.27, -66.06, ('New Brunswick 1839', -14, -14, 'end'))]),
    ('1840&ndash;47: Arkansas, Texas, North Carolina, Oregon', [
        ('Fayetteville, Ark.', 36.06, -94.16, None), ('Pulaski Co., Va.', 37.05, -80.78, None),
        ('Gay Hill, Tex.', 30.27, -96.48, ('Texas 1841', -14, 8, 'end')), ('Bowie Co., Tex.', 33.55, -94.40, None),
        ('Hookerton, N.C.', 35.42, -77.58, ('North Carolina 1845', 14, 8, 'start')), ('Yamhill, Ore.', 45.34, -123.19, ('Oregon 1846', 14, 8, 'start'))]),
    ('1852&ndash;57: California, Kansas; and Australia', [
        ('Stockton', 37.96, -121.29, None), ('San Jose', 37.34, -121.89, ('California 1852', 14, 8, 'start')),
        ('Timbered Hill, Kan.', 37.90, -94.80, ('Kansas 1856', -14, 26, 'end')), ('Leavenworth', 39.31, -94.92, None)]),
    ('By 1860, by their own estimate: &ldquo;upwards of 300,000&rdquo;', []),
]
NOTES = ('Five clicks. The map opens with the unions of 1831&ndash;35 already lit. After 1836 the record shows no new unions of Christians and Disciples, only refusals (the <i>Gazetteer of Local Unions</i>); what spreads is the one movement. Each light is the earliest report found in the <i>Millennial Harbinger</i> (pages from the OCR, approximate). '
 '(1) Already, beyond the union, the Campbells&rsquo; Reformers: the Western Reserve (Scott, 1827&ndash;28); Pittsburgh, Philadelphia (Bank Street, 1832), New York (1834), eastern Virginia (1832), Little Rock (1832: the Philadelphia Confession &ldquo;renounced by the church&rdquo;), Alabama (1833&ndash;34), Toronto (1834: &ldquo;a little band of reformers&hellip; about twenty in number&rdquo;). '
 '(2) 1836&ndash;39: near Dubuque, 1 Nov. 1835, a church &ldquo;of eight members&rdquo; (MH 1836, p. 88); Middleville, Michigan, &ldquo;a company of disciples in this place&rdquo; (1836); Clarke County, Georgia (1836); Mississippi (1836); Grant County, Wisconsin: &ldquo;We met on the second Lord&rsquo;s day in October, when eleven of us united together&rdquo; (1838; MH 1839); Saint John, New Brunswick (1839); Nottingham, &ldquo;a congregation of New Testament Disciples&rdquo; (MH 1837), and New Mills near Glasgow (1837). '
 '(3) 1840&ndash;47: Little Rock and Fayetteville (1840); Texas, Gay Hill (1841) and Bowie County, &ldquo;constituted a church of sixteen members&rdquo; (MH 1842); Hookerton, North Carolina: &ldquo;between twenty and thirty churches&rdquo; (MH 1845); Oregon, Yamhill: &ldquo;in March we organized a congregation upon the Book alone&rdquo;, the first in the Territory (1846, letter in MH 1848, p. 402). '
 '(4) 1852&ndash;57: &ldquo;In Stockton and San Jose there are churches. In Stockton the brethren meet weekly to break the loaf&rdquo; (MH 1852); Kansas Territory, Timbered Hill (1856) and Leavenworth (1857); Sydney, Australia (MH 1852). '
 '(5) Their own estimates, not counts: &ldquo;at least one hundred thousand&rdquo; (MH 1839); &ldquo;two hundred thousand soldiers of the Cross&rdquo; (MH 1848); 1860: &ldquo;nearly one hundred churches in Great Britain&rdquo;, &ldquo;in the United States upwards of 300,000 brethren&rdquo;, and Australia (MH 1860). The <i>Harbinger</i> itself doubted the larger figures (1857: &ldquo;This may be too large a figure&rdquo;). Nebraska: no congregation reported by 1860.')

def svg():
    o = ['<svg viewBox="0 0 %d %d" style="width:min(96vw,160vh);height:auto;display:block;margin:0 auto" role=img aria-label="Map: the Stone-Campbell movement spreading across the United States after the union, 1836 to 1860">' % (W, H),
         '<defs><radialGradient id=sglow><stop offset=0 stop-color="#f3d27a" stop-opacity=".95"/><stop offset=".35" stop-color="#c89b3c" stop-opacity=".45"/><stop offset=1 stop-color="#c89b3c" stop-opacity="0"/></radialGradient></defs>',
         '<style>.sm .st{fill:#1a1510;stroke:#5c4a33;stroke-width:1}'
         '.sm .pl{font:22px Spectral,Georgia,serif;fill:#ede4d3;paint-order:stroke;stroke:#0e0b09;stroke-width:5}'
         '.sm .cap{font:34px "IM Fell English",Georgia,serif;fill:#c89b3c;transition:opacity .4s}.sm g.frag.on:has(~ g.frag.on) .cap{opacity:0}.sm .cap0{transition:opacity .4s}.sm:has(g.frag.on) .cap0{opacity:0}'
         '.sm .ring{fill:none;stroke:#f3d27a;stroke-width:2;opacity:0;transform-box:fill-box;transform-origin:center}'
         '.sm .frag.on .ring{animation:smring 2.2s ease-out 1}'
         '@keyframes smring{0%{opacity:.9;transform:scale(.3)}100%{opacity:0;transform:scale(3.2)}}</style><g class=sm>']
    for nm, d in G['paths'].items():
        o.append('<path class=st d="%s"/>' % d)
    cy = H - 26
    o.append('<rect x="0" y="%d" width="%d" height="52" fill="#100d0a" opacity=".82"/>' % (H - 64, int(W * .7)))
    def dot(x, y, r=11):
        return '<circle cx="%.1f" cy="%.1f" r="%d" fill="url(#sglow)"/><circle cx="%.1f" cy="%.1f" r="3.8" fill="#f3d27a"/>' % (x, y, r, x, y)
    g = ['<g>']           # 1831-35, already lit
    for cap, pts in UM.WAVES:
        for nm, la, lo, lab in pts:
            x, y = P(la, lo); g.append(dot(x, y, 9))
    g.append('<text class="cap cap0" x="22" y="%d">1831&ndash;1835: the union, Kentucky outward</text></g>' % cy)
    o.append(''.join(g))
    for cap, pts in WAVES:
        g = ['<g class=frag>']
        for nm, la, lo, lab in pts:
            x, y = P(la, lo)
            g.append(dot(x, y) + '<circle class=ring cx="%.1f" cy="%.1f" r="9"/>' % (x, y))
            if lab:
                t, dx, dy, an = lab if isinstance(lab, tuple) else (lab, 12, -10, 'start')
                g.append('<text class=pl x="%.1f" y="%.1f" style="text-anchor:%s">%s</text>' % (x + dx, y + dy, an, t))
        g.append('<text class=cap x="22" y="%d">%s</text></g>' % (cy, cap)); o.append(''.join(g))
    o.append('</g></svg>')
    return ''.join(o)

def slide():
    return ('<section class="slide" style="padding:2vmin 2vmin 5vmin"><div class=eyebrow>One movement, spreading &middot; 1836&ndash;1860</div>' + svg() +
            '<aside class=notes>%s</aside></section>' % NOTES)

# ---- 1926 to today (Micah, 2026-11-21: "fill in the gap"): Stone-Campbell congregations by county, four snapshots ----
T = json.load(open(os.path.join(_H, 'today_points.json')))
HIST = json.load(open(os.path.join(_H, 'history_points.json')))
def _fmt(n): return '{:,}'.format(n)
FRAMES = [
    ('1926', HIST['1926']['points'], '1926: %s congregations' % _fmt(HIST['1926']['total']),
     'Disciples of Christ %s &middot; Churches of Christ %s (surviving census schedules)' % (_fmt(HIST['1926']['disciples']), _fmt(HIST['1926']['coc']))),
    ('1980', HIST['1980']['points'], '1980: %s congregations' % _fmt(HIST['1980']['total']),
     'Churches of Christ %s &middot; Christian Churches and Churches of Christ %s &middot; Disciples of Christ %s' % (_fmt(HIST['1980']['by_body']['CCHRIS_C']), _fmt(HIST['1980']['by_body']['CCCC_C']), _fmt(HIST['1980']['by_body']['DOFC_C']))),
    ('2000', HIST['2000']['points'], '2000: %s congregations' % _fmt(HIST['2000']['total']),
     'Churches of Christ %s &middot; Christian Churches and Churches of Christ %s &middot; Disciples of Christ %s &middot; International Churches of Christ %s' % tuple(_fmt(HIST['2000']['by_body'][k]) for k in ('chschcg', 'chrchcg', 'chrdicg', 'inchccg'))),
    ('2020', T['points'], 'Today: %s congregations, in every state' % _fmt(sum(v[0] for v in T['totals'].values())),
     'Churches of Christ 11,881 &middot; Christian Churches and Churches of Christ 4,787 &middot; Disciples of Christ 3,135 &middot; International Churches of Christ 175 (2020)'),
]
def today_svg():
    import math
    o = ['<svg viewBox="0 0 %d %d" style="width:min(96vw,160vh);height:auto;display:block;margin:0 auto" role=img aria-label="Map: Stone-Campbell congregations in the United States by county, 1926, 1980, 2000 and 2020">' % (W, H),
         '<defs><radialGradient id=tglow><stop offset=0 stop-color="#f6dc8c" stop-opacity=".9"/><stop offset=".4" stop-color="#c89b3c" stop-opacity=".35"/><stop offset=1 stop-color="#c89b3c" stop-opacity="0"/></radialGradient></defs>',
         '<style>.tm .st{fill:#1a1510;stroke:#5c4a33;stroke-width:1}.tm .lit{opacity:0;transition:opacity 1.2s ease}.tm .lit.on{opacity:1}.tm .lit.on:has(~ .lit.on){opacity:0}'
         '.tm .cap{font:34px "IM Fell English",Georgia,serif;fill:#c89b3c}.tm .sub{font:20px Spectral,Georgia,serif;fill:#a89a82}</style><g class=tm>']
    for nm, d in G['paths'].items():
        o.append('<path class=st d="%s"/>' % d)
    o.append('<rect x="0" y="%d" width="%d" height="84" fill="#100d0a" opacity=".82"/>' % (H - 92, int(W * .86)))
    for yr, pts, cap, sub in FRAMES:
        g = ['<g class="lit frag">', '<g style="mix-blend-mode:screen">']
        for x, y, n in sorted(pts, key=lambda p: p[2]):
            g.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="url(#tglow)"/>' % (x, y, 4 + 3.4 * math.sqrt(n)))
        for x, y, n in pts:
            g.append('<circle cx="%.1f" cy="%.1f" r="1.5" fill="#f6dc8c"/>' % (x, y))
        g.append('</g><text class=cap x="22" y="%d">%s</text><text class=sub x="24" y="%d">%s</text></g>' % (H - 50, cap, H - 18, sub))
        o.append(''.join(g))
    o.append('</g></svg>')
    return ''.join(o)

def today_slide():
    h = HIST
    return ('<section class="slide" style="padding:2vmin 2vmin 5vmin"><div class=eyebrow>From 1926 to today</div>' + today_svg() +
            '<aside class=notes>Four clicks: 1926, 1980, 2000, today. Every Stone-Campbell congregation counted, by county; each glow grows with the number in that county. '
            '1926: the U.S. Census of Religious Bodies, which since 1906 had counted the Disciples of Christ and the Churches of Christ separately; these are the %s surviving congregation schedules (Disciples %s, Churches of Christ %s), digitized by American Religious Ecologies (religiousecologies.org); %s could not be placed by county. '
            '1980: %s congregations (Churches of Christ %s; Christian Churches and Churches of Christ %s, counted apart from the Disciples since 1971; Disciples %s). 2000: %s. Today (2020): 19,978; about 3.25 million adherents. '
            'Not every year counted every body (1952 and 1971 lack the Churches of Christ), so those years are left out. Places by county seat-area centroid; Alaska, Hawaii and Puerto Rico off the map. '
            'Sources: American Religious Ecologies, 1926 schedules (RRCHNM); <i>Churches and Church Membership in the United States, 1980</i> and <i>Religious Congregations and Membership Study, 2000</i> (county files, ARDA, thearda.com); <i>2020 U.S. Religion Census</i> (ASARB, 2022). Figures are as each body reported them.</aside></section>') % (
        _fmt(h['1926']['total']), _fmt(h['1926']['disciples']), _fmt(h['1926']['coc']), _fmt(h['1926']['unplaced']),
        _fmt(h['1980']['total']), _fmt(h['1980']['by_body']['CCHRIS_C']), _fmt(h['1980']['by_body']['CCCC_C']), _fmt(h['1980']['by_body']['DOFC_C']), _fmt(h['2000']['total']))
