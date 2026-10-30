# Chapter 5's deck, as a map: the slides in decks/src/week5/slides.py, arranged as a spine with side
# paths, and the sources whole, every quoted passage marked. Same builder as Chapter 4 (decks/src/mapdeck.py).
#   python3 decks/src/week5map/build.py   ->  decks/week5-brush-run-map.html
# How the map works: decks/src/week4map/README.md. Anchors are phrases on a side path's first and last slide.
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    # (label,                      first-slide anchor,                      last-slide anchor)
    # Arranged by the chapter's four arguments: creeds as tests; who may serve; who may ordain; the whole church on governance by the people.
    ('Creeds as tests',            'Side path &middot; creeds as tests',    'They may not fence the table.'),
    ('Becoming Baptists',          'Brush Run&rsquo;s overture, fall 1813', 'they became Baptists.'),
    R.WEEKLY,
    ('Who may serve?',             '<h2>Who serves the table?</h2>',        'Hosted by any.'),
    ('Who may ordain?',            R.GOVERNANCE[1],                         R.GOVERNANCE[2]),
    R.UNIVERSALS,
    R.EKKLESIA,
    R.CONSTITUTION,
    ('Addendum',                   'Reference material; not part of the telling', 'What this week touched'),
]
SECTIONS = [
    ('Opening', 'Otter Creek'), ('Your questions', '<h2 style="max-width:none">Your questions</h2>'), ('The sea', '<h2>Alexander and the Sea</h2>'),
    ('Glasgow', 'He went to hear other preachers.'), ('Reunion', '<h2>Family Reunion</h2>'),
    ('Brush Run', '<h2>Brush Run</h2>'), ('The Synod', 'request to be received into ministerial'),
    ('Session one close', 'for discussion &middot; session one'), ('Session two', 'data-session=2'),
    ('Church formed', '<h2>Brush Run Church Formed</h2>'), ('The first Supper', '<h2>The First Supper</h2>'),
    ('The ordination', '<h2>The Ordination</h2>'), ('Why the people?', '<h2>Why the people?</h2>'),
    ('Close', 'for discussion &middot; session two'),
]

# The sources whole, from the shared library (decks/src/resources.py): Richardson's Memoirs (excerpts),
# the Declaration and Address, the Last Will, the Westminster Confession, Scripture (KJV), and Stone's
# own account. Set SITE to the class site checkout if it is not ~/projects/stone-campbell-site.
DOC_KEYS = ['rich', 'dna', 'will', 'wcf', 'kjv', 'stone', 'apology', 'cb', 'church', 'acr', 'ekk', 'tbl', 'lord', 'fnd', 'priest']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
SHORT = R.SHORT
DOC_DOORS = [('Richardson&rsquo;s account, whole', '<h2>Brush Run</h2>', 0),
             ('The whole Declaration and Address', '<h2>Why the people?</h2>', 1),
             ('The whole will', '<h2>Why the people?</h2>', 2),
             ('Scripture on the church (KJV)', 'Wherever Two or Three<br>Are Gathered', 4)]
doc_order = R.doc_order

mapdeck.build({
    'part': '5', 'key': 'w5', 'chapter': 'Chapter 5', 'title': 'Chapter 5 &middot; Wherever Two or Three Are Gathered',
    'out': 'decks/week5-brush-run-map.html', 'source': 'decks/src/week5/slides.py', 'built_by': 'decks/src/week5map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': SHORT, 'doc_doors': DOC_DOORS, 'doc_order': doc_order,
})
