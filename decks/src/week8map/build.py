# Chapter 8, "The Handshake at Lexington" (the Stone-Campbell union, 1831-1835), as a map deck: the slides in
# decks/src/week8/slides.py, a spine with side paths. Same builder as Chapters 4-7 (decks/src/mapdeck.py).
#   python3 decks/src/week8map/build.py   ->  decks/chapter8.html
# Quotations: python3 decks/src/week8/check_quotes.py
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    ('The fire', 'The Fire</i>', '<div class=eyebrow>The fire<'),   # off 'raised among the raccoons' (Micah, 2026-11-21: a side path for now)
    R.TABLE,          # off Lexington, February 1832: who may serve the table
    R.CIRCLE,         # off Stone, Christian Messenger 1828: Campbell's circle, Christ the centre
    R.CREED,          # off Scott, 1832: No creed but...
]
SECTIONS = [
    ('Opening', 'Our Wild Democracy &middot; Chapter 8'),
    ('Recap', 'Story so far'),
    ('Two movements, much in common', 'Our movement, our tradition'),
    ('Lexington', 'Hill Street, Lexington'),
    ('The whole history of division', 'Two thousand years of division &middot; 1'),
    ('The handshake', 'come together?</span></h2>'),
    ('It took years', 'It took years</h2>'),
    ('It worked', 'one movement, one history.'),
    ('Christ... or the Bible?', 'Christ&hellip; or the Bible?</h2>'),
    ('Close', 'for discussion &middot; Chapter 8'),
]
def docs(between, clean): return R.docs(between, clean, ['wil32', 'lex', 'mh32a', 'crd', 'tbl'])

mapdeck.build({
    'part': '8', 'key': 'w8', 'chapter': 'Chapter 8', 'title': 'Chapter 8 &middot; The Handshake at Lexington',
    'page_title': 'Chapter 8 &middot; The Handshake at Lexington',
    'out': 'decks/chapter8.html', 'source': 'decks/src/week8/slides.py', 'built_by': 'decks/src/week8map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})


# ---- slim the output for phones (Micah, 2026-11-21: "The slideshow on phone is hanging") ----
# Re-encode embedded images larger than 40 KB as WebP, no longer side than 1400 px; ask the browser to decode lazily.
def slim(path, max_side=1400, min_bytes=40_000, quality=68):
    import base64, io, re
    from PIL import Image
    h = open(path).read(); before = len(h); cache = {}
    def sub(m):
        mime, data = m.group(1), m.group(2)
        if len(data) * 3 // 4 < min_bytes: return m.group(0)
        if data in cache: return cache[data]
        im = Image.open(io.BytesIO(base64.b64decode(data)))
        im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') and 'transparency' in im.info or im.mode in ('RGBA', 'LA') else 'RGB')
        if max(im.size) > max_side: im.thumbnail((max_side, max_side), Image.LANCZOS)
        bio = io.BytesIO(); im.save(bio, 'WEBP', quality=quality, method=6)
        out = 'data:image/webp;base64,' + base64.b64encode(bio.getvalue()).decode()
        if len(out) >= len(m.group(0)): out = m.group(0)
        cache[data] = out; return out
    h = re.sub(r'data:image/(jpeg|jpg|png);base64,([A-Za-z0-9+/=]+)', sub, h)
    h = re.sub(r'<img(?![^>]*\bdecoding=)', '<img decoding="async"', h)
    open(path, 'w').write(h)
    print('slimmed %s: %.1f MB -> %.1f MB' % (path, before / 1e6, len(h) / 1e6))
slim('decks/chapter8.html')
