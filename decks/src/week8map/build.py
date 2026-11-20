# Chapter 8, "The Handshake at Lexington" (the Stone-Campbell union, 1831-1835), as a map deck: the slides in
# decks/src/week8/slides.py, a spine with side paths. Same builder as Chapters 4-7 (decks/src/mapdeck.py).
#   python3 decks/src/week8map/build.py   ->  decks/chapter8.html
# Quotations: python3 decks/src/week8/check_quotes.py
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    R.TABLE,          # off Lexington, February 1832: who may serve the table
    R.CREED,          # off Scott, 1832: No creed but...
]
SECTIONS = [
    ('Opening', 'Our Wild Democracy &middot; Chapter 8'),
    ('Recap', 'The story so far'),
    ('Two movements, much in common', 'Our movement, our tradition'),
    ('Lexington', 'Hill Street, Lexington'),
    ('The whole history of division', 'Two thousand years of division &middot; 1'),
    ('The handshake', 'The proposition</h2>'),
    ('It took years', 'It took years</h2>'),
    ('It worked', 'one movement, one history.'),
    ('Uniting on the Bible', 'Uniting on the Bible</h2>'),
    ('Close', 'for discussion &middot; Chapter 8'),
]
def docs(between, clean): return R.docs(between, clean, ['wil32', 'lex', 'mh32a', 'crd', 'tbl'])

mapdeck.build({
    'part': '8', 'key': 'w8', 'chapter': 'Chapter 8', 'title': 'Chapter 8 &middot; The Handshake at Lexington',
    'page_title': 'Chapter 8 &middot; The Handshake at Lexington',
    'out': 'decks/chapter8.html', 'source': 'decks/src/week8/slides.py', 'built_by': 'decks/src/week8map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})
