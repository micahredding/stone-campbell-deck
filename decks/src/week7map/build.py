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
    ('The Harbinger\'s aim', 'Side path &middot; the Harbinger&rsquo;s aim', 'subservient to this comprehensive object'),
    ('Other voices on the future', 'Side path &middot; other voices on the future', 'One future.'),
    ('The table today', 'Side path &middot; the table today', 'We already eat at the eschatological table of the Lord'),
    ('John 17', '<h2>John 17</h2>', 'Some of you say it will be effected'),
    ('Kings and priests, 1830', 'Side path &middot; kings and priests, 1830', 'without the intervention of a mediator'),   # off "What the church will be, it does now"
]
SECTIONS = [
    ('Opening', 'Our Wild Democracy &middot; Chapter 7'),
    ('Recap', 'From Ireland to Brush Run'),
    ('The Baptists', 'Alexander becomes a Baptist'),
    ('The Christian Baptist', 'Its masthead'),
    ('Excommunication', 'Baptist excommunication'),
    ('A tangent', 'They kept trying to join'),
    ('The Harbinger', '<h2>The pivot</h2>'),
    ('The future, not a timeline', 'In his own paper, he went back and forth'),
    ('About eschatology', 'Chapters 1&ndash;6, read forward'),
    ('What was distinctive', 'Their eschatology, in three marks'),
    ('A new creation', '<h2>A new creation</h2>'),
    ('The church as a microcosm', '<h2>The church as a microcosm</h2>'),
    ('Practicing the future today', '<h2>Practicing the future today</h2>'),
    ('Restoration, reframed', 'We expect <b>no new Sun</b>'),
    ('Eschatology and government', 'Eschatology and government:<br>two paths'),
    ('N. T. Wright', '<h2>N. T. Wright</h2>'),
    ('Close', 'for discussion &middot; Chapter 7'),
]
def docs(between, clean): return R.docs(between, clean, ['dna', 'rich', 'cb25', 'mh40', 'mh53'])

mapdeck.build({
    'part': '7', 'key': 'w7', 'chapter': 'Chapter 7', 'title': 'Chapter 7 &middot; Living into God&rsquo;s Future',
    'page_title': 'Chapter 7 &middot; Living into God&rsquo;s Future',
    'out': 'decks/chapter7.html', 'source': 'decks/src/week7/slides.py', 'built_by': 'decks/src/week7map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})
