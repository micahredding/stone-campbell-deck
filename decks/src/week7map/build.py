# Chapter 7, "Living into God's Future" (the Millennial Harbinger), as a map deck: the slides in
# decks/src/week7/slides.py, a spine with side paths. Same builder as Chapters 4-6 (decks/src/mapdeck.py).
#   python3 decks/src/week7map/build.py   ->  decks/chapter7.html
# Quotations: python3 decks/src/week7/check_quotes.py (the quote standard's checker against the research database).
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    R.ASSOCIATIONS,   # off the one-slide summary: the whole timeline of the Campbells' associations
    ('Other voices on the future', 'Side path &middot; other voices on the future', 'One future.'),
]
SECTIONS = [
    ('Opening', 'Our Wild Democracy &middot; Chapter 7'),
    ('Recap', 'From Ireland to Brush Run'),
    ('Institutions', 'Still seeking<br>a larger fellowship'),
    ('The Christian Baptist', 'Its masthead'),
    ('The Harbinger', '<h2>The pivot</h2>'),
    ('Their eschatology', 'How they spoke<br>about the future'),
    ('John 17', '<h2>John 17</h2>'),
    ('One future', 'Most of us are not.'),
    ('Read forward', 'Everything so far,<br>read forward'),
    ('Practiced now', 'What the church will be, it does now'),
    ('The table', 'The other<br>millennial harbinger'),
    ('Two ways', 'Two ways<br>into the world'),
    ('N. T. Wright', '<h2>N. T. Wright</h2>'),
    ('Close', 'for discussion &middot; Chapter 7'),
]
def docs(between, clean): return R.docs(between, clean, ['dna', 'rich'])

mapdeck.build({
    'part': '7', 'key': 'w7', 'chapter': 'Chapter 7', 'title': 'Chapter 7 &middot; Living into God&rsquo;s Future',
    'page_title': 'Chapter 7 &middot; Living into God&rsquo;s Future',
    'out': 'decks/chapter7.html', 'source': 'decks/src/week7/slides.py', 'built_by': 'decks/src/week7map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})
