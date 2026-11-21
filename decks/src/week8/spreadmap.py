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

WAVES = []      # (caption, [(name, lat, lon, label or None)]) -- filled from the research
ABROAD = ''     # caption line for churches abroad, if any
NOTES = ''

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
