# The union spreading, 1831-1835, and where it was refused: an SVG map in waves, one click each.
# Places and dates from the database's "Gazetteer of Local Unions" (10 Research Projects/The Lexington Union/);
# coordinates approximate (county seats stand in for unnamed sites). State outlines: us-atlas 3.0.1 (Census
# cartographic boundaries, public domain), projected in decks/src/week8/region_paths.json.
import json, math, os
_H = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(_H, 'region_paths.json')))
W, H = G['W'], G['H']; LON0, LON1, LAT0, LAT1 = G['bbox']; k = G['k']
def P(lat, lon): return ((lon - LON0) / (LON1 - LON0) * W, (LAT1 - lat) / (LAT1 - LAT0) * H)

WAVES = [   # (caption, [(name, lat, lon, label?)])
    ('1831&ndash;32: Georgetown, Lexington; Indiana and Tennessee', [
        ('Georgetown', 38.21, -84.56, None), ('Great Crossings', 38.22, -84.62, None), ('Lexington', 38.05, -84.50, ('Lexington &amp; Georgetown', 30, 34, 'start')),
        ('Rush Co., Ind.', 39.61, -85.45, ('Rush Co.', -10, 26, 'end')), ('Maury Co., Tenn.', 35.62, -87.04, ('Maury Co.', -12, 6, 'end')), ('Mount Sterling', 38.06, -83.94, None)]),
    ('1832: the Bluegrass churches; Smith and Rogers ride', [
        ('Paris', 38.21, -84.25, None), ('Millersburg', 38.30, -84.15, None), ('Carlisle', 38.31, -84.03, None), ('Somerset', 38.10, -83.88, None),
        ('Sharpsburg', 38.20, -83.93, None), ('Owingsville', 38.14, -83.76, None), ('Republican', 38.10, -84.35, None),
        ('Pendleton Co.', 38.68, -84.33, 'Pendleton Co.'), ('Calloway Co.', 36.74, -88.33, 'Calloway Co.'),
        ('McNairy Co., Tenn.', 35.17, -88.59, ('McNairy Co.', -12, 6, 'end')), ('Lock&rsquo;s Creek, Tenn.', 35.85, -86.39, 'Lock&rsquo;s Creek')]),
    ('Autumn 1832: Stone in Illinois; Missouri', [
        ('Clintonville', 38.11, -84.39, None), ('Jacksonville', 39.73, -90.23, 'Jacksonville'), ('Jersey Prairie', 39.90, -90.18, None),
        ('Carrollton', 39.30, -90.41, None), ('Troy, Mo.', 38.98, -90.98, ('Troy', -12, 22, 'end'))]),
    ('1833&ndash;34: Missouri, Indiana; Paris; Jacksonville again', [
        ('Bowling Green, Mo.', 39.34, -91.19, None), ('Fayette, Mo.', 39.15, -92.68, 'Fayette'),
        ('White River, Ind.', 39.77, -86.16, ('White River', -12, -6, 'end')), ('Silver Creek, Ind.', 39.63, -84.93, None),
        ('Paris (1834)', 38.21, -84.25, None), ('Jacksonville (1834)', 39.73, -90.23, None)]),
    ('July 1835: Lexington, at last', [('Lexington (1835)', 38.05, -84.50, None)]),
]
REFUSED = [('Liberty, Ind.', 39.64, -84.93, 'Liberty'), ('Eaton, Ohio', 39.74, -84.64, 'Eaton')]
STATES = {'Kentucky': (37.5, -85.6), 'Ohio': (40.6, -82.9), 'Indiana': (40.4, -86.4), 'Illinois': (40.6, -89.3),
          'Missouri': (38.3, -92.6), 'Tennessee': (35.45, -84.95)}

def svg():
    o = ['<svg viewBox="0 0 %.0f %.0f" style="width:min(92vw,150vh);height:auto;display:block;margin:0 auto" role=img aria-label="Map: the union of Christians and Disciples spreading from Lexington, 1831 to 1835">' % (W, H),
         '<defs><radialGradient id=uglow><stop offset=0 stop-color="#f3d27a" stop-opacity=".95"/><stop offset=".35" stop-color="#c89b3c" stop-opacity=".45"/><stop offset=1 stop-color="#c89b3c" stop-opacity="0"/></radialGradient></defs>',
         '<style>.um .st{fill:#1a1510;stroke:#5c4a33;stroke-width:1.1}.um .hi{fill:#211a12;stroke:#8a6d2c;stroke-width:1.4}'
         '.um .sl{font:italic 22px "IM Fell English",Georgia,serif;fill:#7a6e5c;text-anchor:middle}'
         '.um .pl{font:17px Spectral,Georgia,serif;fill:#ede4d3}.um .cap{font:30px "IM Fell English",Georgia,serif;fill:#c89b3c;transition:opacity .4s}.um g.frag.on:has(~ g.frag.on) .cap{opacity:0}'
         '.um .ring{fill:none;stroke:#f3d27a;stroke-width:2;opacity:0;transform-box:fill-box;transform-origin:center}'
         '.um .frag.on .ring{animation:umring 2.2s ease-out 1}'
         '@keyframes umring{0%{opacity:.9;transform:scale(.3)}100%{opacity:0;transform:scale(3.2)}}</style><g class=um>']
    for nm, d in G['paths'].items():
        o.append('<path class=%s d="%s"/>' % ('hi' if nm in STATES else 'st', d))
    for nm, (la, lo) in STATES.items():
        x, y = P(la, lo); o.append('<text class=sl x="%.0f" y="%.0f">%s</text>' % (x, y, nm))
    cy = H - 26
    o.append('<rect x="0" y="%.0f" width="%.0f" height="48" fill="#100d0a" opacity=".82"/>' % (H - 60, W * .62))
    for n, (cap, pts) in enumerate(WAVES):
        g = ['<g class=frag>']
        for nm, la, lo, lab in pts:
            x, y = P(la, lo)
            g.append('<circle cx="%.1f" cy="%.1f" r="13" fill="url(#uglow)"/><circle cx="%.1f" cy="%.1f" r="4.2" fill="#f3d27a"/><circle class=ring cx="%.1f" cy="%.1f" r="9"/>' % (x, y, x, y, x, y))
            if lab:
                t, dx, dy, an = lab if isinstance(lab, tuple) else (lab, 9, -8, 'start')
                g.append('<text class=pl x="%.1f" y="%.1f" style="text-anchor:%s">%s</text>' % (x + dx, y + dy, an, t))
        g.append('<text class=cap x="22" y="%.0f">%s</text>' % (cy, cap))
        g.append('</g>'); o.append(''.join(g))
    g = ['<g class=frag>']
    for nm, la, lo, lab in REFUSED:
        x, y = P(la, lo)
        g.append('<path d="M%.1f,%.1fl10,10m0,-10l-10,10" stroke="#c0503a" stroke-width="3" stroke-linecap=round/>' % (x - 5, y - 5))
        g.append('<text class=pl x="%.1f" y="%.1f" style="fill:#d98a74">%s</text>' % (x + 9, y + 18, lab))
    g.append('<text class=cap x="%.0f" y="70" style="fill:#d98a74;text-anchor:end">To the east: the Christian Connection refuses &rarr;</text>' % (W - 20))
    g.append('<text class=cap x="22" y="%.0f" style="fill:#d98a74">Refused: Ohio, eastern Indiana, the East (1832&ndash;1844)</text>' % cy)
    g.append('</g>'); o.append(''.join(g))
    o.append('</g></svg>')
    return ''.join(o)

def slide():
    return ('<section class="slide" style="padding:2vmin 2vmin 6vmin"><div class=eyebrow>The union spreading, 1831&ndash;1835</div>' + svg() +
            '<aside class=notes>Six clicks: five waves of union, then the refusals. From the database&rsquo;s <i>Gazetteer of Local Unions</i> (36 dated unions, 15 refusals; places approximate). '
            '(1) Georgetown in the autumn of 1831, the handshake at Lexington; already, unprompted, Rush County, Indiana (&ldquo;The Reforming Baptists and we, are all one here,&rdquo; Dec. 1831) and Maury County, Tennessee. Stone and Johnson: &ldquo;The spirit of union is spreading like fire in dry stubble.&rdquo; '
            '(2) 1832: Paris, Millersburg, Carlisle (Smith&rsquo;s letter), Montgomery and Bath counties, Republican (500 break the loaf), Pendleton County (&ldquo;a union of all present took place&rdquo;), Calloway County, McNairy County and Lock&rsquo;s Creek in Tennessee. '
            '(3) Autumn 1832: the yearly meeting at Clintonville; Stone in Illinois: &ldquo;a happy union of the two societies, Christians and Reformers, in one body or church&rdquo; at Jacksonville; Carrollton, Jersey Prairie; Troy, Missouri. '
            '(4) 1833&ndash;34: Bowling Green and Fayette, Missouri; White River and Silver Creek, Indiana; Paris enrols as one church (Aug. 1834); Jacksonville, where Stone in 1834 found two churches again and would join neither &ldquo;until they united together.&rdquo; '
            '(5) July 1835: Lexington itself, at last. '
            '(6) Refused: Liberty, Indiana (1841: &ldquo;we no longer seek for union with the Disciples&rdquo;), Preble County, Ohio; Purviance&rsquo;s Ohio churches; the eastern Christian Connection. About half of Stone&rsquo;s Christians never entered the union (<i>Encyclopedia</i>, &ldquo;Christian Connection&rdquo;). '
            'Stone, 1835: &ldquo;we have had no general council on this subject. Churches have acted in their private capacity.&rdquo; '
            '<br>If asked what became of those who refused (only if it comes up): the Christian Connection merged with the Congregationalists (1931), then into the United Church of Christ (1957). The Disciples and the UCC: &ldquo;Declaration of Ecumenical Partnership&rdquo; (1985), &ldquo;full communion&rdquo; (1989), after the Disciples recognized infant baptism as &ldquo;a legitimate form of baptism&rdquo; (1987). Recognition, not agreement. The UCC receives the creeds &ldquo;as testimonies, but not tests of the faith.&rdquo; (<i>Encyclopedia</i>; ucc.org.)</aside></section>')
