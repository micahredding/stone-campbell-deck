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

# ---- today (Micah, 2026-11-21): every Stone-Campbell congregation in the 2020 U.S. Religion Census, by county ----
T = json.load(open(os.path.join(_H, 'today_points.json')))
def today_svg():
    import math
    o = ['<svg viewBox="0 0 %d %d" style="width:min(96vw,160vh);height:auto;display:block;margin:0 auto" role=img aria-label="Map: Stone-Campbell congregations in the United States today, by county, 2020">' % (W, H),
         '<defs><radialGradient id=tglow><stop offset=0 stop-color="#f6dc8c" stop-opacity=".9"/><stop offset=".4" stop-color="#c89b3c" stop-opacity=".35"/><stop offset=1 stop-color="#c89b3c" stop-opacity="0"/></radialGradient></defs>',
         '<style>.tm .st{fill:#1a1510;stroke:#5c4a33;stroke-width:1}.tm .lit{opacity:0;transition:opacity 2.4s ease}.tm .lit.on{opacity:1}'
         '.tm .cap{font:34px "IM Fell English",Georgia,serif;fill:#c89b3c}.tm .sub{font:20px Spectral,Georgia,serif;fill:#a89a82}</style><g class=tm>']
    for nm, d in G['paths'].items():
        o.append('<path class=st d="%s"/>' % d)
    g = ['<g class="lit frag" style="mix-blend-mode:screen">']
    for x, y, n in sorted(T['points'], key=lambda p: p[2]):
        g.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="url(#tglow)"/>' % (x, y, 4 + 3.4 * math.sqrt(n)))
    for x, y, n in T['points']:
        g.append('<circle cx="%.1f" cy="%.1f" r="1.5" fill="#f6dc8c"/>' % (x, y))
    g.append('</g>'); o.append(''.join(g))
    tot = sum(v[0] for v in T['totals'].values())
    o.append('<rect x="0" y="%d" width="%d" height="84" fill="#100d0a" opacity=".82"/>' % (H - 92, int(W * .78)))
    o.append('<text class=cap x="22" y="%d">Today: %s congregations, in every state</text>' % (H - 50, '{:,}'.format(tot)))
    o.append('<text class=sub x="24" y="%d">Churches of Christ 11,881 &middot; Christian Churches and Churches of Christ 4,787 &middot; Disciples of Christ 3,135 &middot; International Churches of Christ 175 (2020)</text>' % (H - 18))
    o.append('</g></svg>')
    return ''.join(o)

def today_slide():
    t = T['totals']
    return ('<section class="slide" style="padding:2vmin 2vmin 5vmin"><div class=eyebrow>The Stone-Campbell movement today</div>' + today_svg() +
            '<aside class=notes>One click: the lights come up. Every Stone-Campbell congregation in the 2020 U.S. Religion Census, by county; each glow grows with the number of congregations in that county (%s counties; %s congregations in Alaska, Hawaii and Puerto Rico are off the map). '
            'Churches of Christ: 11,881 congregations, 1,422,331 adherents. Christian Churches and Churches of Christ: 4,787 and 1,379,041. Christian Church (Disciples of Christ): 3,135 and 398,072. International Churches of Christ: 175 and 53,612. Together some 20,000 congregations and about 3.25 million adherents. '
            'The three main streams divided later (the Churches of Christ counted separately from 1906; the Christian Churches from the Disciples by the 1960s&ndash;70s): one family, from one handshake. Not counted here: the churches abroad, larger than the American ones in some places. '
            'Source: Clifford Grammich et al., <i>2020 U.S. Religion Census: Religious Congregations &amp; Adherents Study</i> (Association of Statisticians of American Religious Bodies, 2022), Group by County. Figures are as each body reported them.</aside></section>') % (len(T['points']), T['off_map'])
