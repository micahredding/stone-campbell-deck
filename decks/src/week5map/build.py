# Chapters 5 and 6, as map decks: the slides in decks/src/week5/slides.py, arranged as a spine with side
# paths, and the sources whole, every quoted passage marked. Same builder as Chapter 4 (decks/src/mapdeck.py).
#   python3 decks/src/week5map/build.py   ->  decks/chapter5.html (Chapter 5)
#                                         and decks/chapter6.html (Chapter 6)
# How the map works: decks/src/week4map/README.md. Anchors are phrases on a side path's first and last slide.
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    # (label,                      first-slide anchor,                      last-slide anchor)
    # Arranged by the chapter's four arguments: creeds as tests; who may serve; who may ordain; the whole church on governance by the people.
    ('Your questions',             '<h2 style="max-width:none">Your questions</h2>', 'Uniformity in God&rsquo;s time.'),
    ('The Haldanes&rsquo; mission', 'Everything or nothing', 'The Church of Scotland on missions, 1796'),
    ('Creeds as tests',            'Side path &middot; creeds as tests',    'They may not fence the table.'),
    ('Two ways not to become a sect', '<h2 style="max-width:none">Two ways not to become a sect</h2>', 'they became Baptists.'),
    ('Unity, or uniformity?',      'Unity, or uniformity?</h2>',            'Uniformity in God&rsquo;s time.'),   # Chapter 6 only: off the recap card
    # R.WEEKLY: moved out of Chapter 6 (Micah, 2026-11-03); see decks/every-lords-day-map.html
    ('Images for Whose orders?',   'Side path &middot; images for Whose orders?', 'Luther burns the papal bull'),   # Chapter 6: off "Whose orders?", for Micah to inspect
    ('A testimony to the people&rsquo;s authority', 'Side path &middot; it shall not be so among you', 'among you.</span>'),   # Chapter 6: off "Who gave them that authority?"
    ('What they read',             'Side path &middot; the people&rsquo;s authority in Scripture', 'I would advise to take the brethren'),
    ('Who may serve?',             '<h2>Who serves the table?</h2>',        'Hosted by any.'),
    ('Who may ordain?',            R.GOVERNANCE[1],                         R.GOVERNANCE[2]),
    R.UNIVERSALS,
    R.EKKLESIA,
    R.CONSTITUTION,
    ('Addendum',                   'Reference material; not part of the telling', 'What this week touched'),
]
SECTIONS = [   # Chapter 5's deck (to the black slide after "Next time"), then Chapter 6's
    ('Opening', 'Otter Creek'), ('The sea', 'Alexander and the Sea</h2>'),
    ('Glasgow', 'He went to hear other preachers.'), ('Reunion', '<h2>Family Reunion</h2>'),
    ('Seeking communion', 'as the Society was not a Church'), ('The Synod', 'Christian communion <b>cannot be granted</b>'),
    ('Close', 'for discussion &middot; Chapter 5'),
]
SECTIONS6 = [
    ('Opening', 'data-session=2'),
    ('Church formed', 'data-mark=formed'), ('The first Supper', 'data-mark=supper'),
    ('The ordination', '<h2>The Ordination</h2>'), ('Why the people?', '<h2 style="max-width:none">The other chain</h2>'),
    ('Close', 'for discussion &middot; Chapter 6'),
]

# The sources whole, from the shared library (decks/src/resources.py): Richardson's Memoirs (excerpts),
# the Declaration and Address, the Last Will, the Westminster Confession, Scripture (KJV), and Stone's
# own account. Set SITE to the class site checkout if it is not ~/projects/stone-campbell-site.
DOC_KEYS = ['rich', 'dna', 'will', 'wcf', 'kjv', 'stone', 'apology', 'cb', 'church', 'acr', 'ekk', 'tbl', 'lord', 'fnd', 'priest', 'tcl']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
SHORT = R.SHORT
DOC_DOORS = [('Thomas&rsquo;s letters home', 'October 1808: the family sails', 15),
             ('Richardson&rsquo;s account, whole', 'The Campbells seek out Presbyterian Communion', 0),
             ('The whole Declaration and Address', 'Alexander Campbell&rsquo;s position.</span>', 1),
             ('The whole will', 'Alexander Campbell&rsquo;s position.</span>', 2),
             ('Scripture on the church (KJV)', 'Wherever Two or Three<br>Are Gathered', 4)]
doc_order = R.doc_order

# Two decks, two chapters (Micah, 2026-11-01): Chapter 5 runs to the black slide after "Next time";
# Chapter 6 starts at its own Otter Creek opening. Same slides.py, sliced.
def _split(S):
    n = [i for i, x in enumerate(S) if 'Next time: Brush Run' in x]
    assert len(n) == 1 and 'notes>Black.' in S[n[0] + 1], 'expected a black slide after Next time'
    return n[0] + 1
ONE_SIDE = ('The Haldanes&rsquo; mission', 'Your questions', 'Creeds as tests', 'Two ways not to become a sect')
ONE_DOORS = ('Thomas&rsquo;s letters home', 'Richardson&rsquo;s account, whole')
base = {'part': '5', 'title': 'Chapter 5 &middot; Wherever Two or Three Are Gathered', 'source': 'decks/src/week5/slides.py',
        'built_by': 'decks/src/week5map/build.py', 'docs': docs, 'short': SHORT, 'doc_order': doc_order}
mapdeck.build(dict(base, key='w5', chapter='Chapter 5', page_title='Chapter 5 &middot; Alexander Campbell and the Sea',
    out='decks/chapter5.html', keep=lambda S: (0, _split(S)),
    side=[x for x in SIDE if x[0] in ONE_SIDE], sections=SECTIONS,
    doc_doors=[x for x in DOC_DOORS if x[0] in ONE_DOORS],
    link_doors=[('for discussion &middot; Chapter 5', 'Your questions')]))
mapdeck.build(dict(base, key='w6', chapter='Chapter 6', page_title='Chapter 6 &middot; Wherever Two or Three Are Gathered',
    out='decks/chapter6.html', keep=lambda S: (_split(S) + 1, len(S) - 1),
    side=[x for x in SIDE if x[0] not in ONE_SIDE], sections=SECTIONS6,
    doc_doors=[x for x in DOC_DOORS if x[0] not in ONE_DOORS]))
