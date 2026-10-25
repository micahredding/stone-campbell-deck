# Chapter 5's deck, as a map: the slides in decks/src/week5/slides.py, arranged as a spine with side
# paths, and the sources whole, every quoted passage marked. Same builder as Chapter 4 (decks/src/mapdeck.py).
#   python3 decks/src/week5map/build.py   ->  decks/week5-brush-run-map.html
# How the map works: decks/src/week4map/README.md. Anchors are phrases on a side path's first and last slide.
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck

SIDE = [
    # (label,                      first-slide anchor,                      last-slide anchor)
    ('Richardson&rsquo;s note',     '<div class=eyebrow>Richardson&rsquo;s note</div>', '<div class=eyebrow>Richardson&rsquo;s note</div>'),
    ('Who was not at the table',   'who was not at the table',              'who was not at the table'),
    ('Addendum',                   'Reference material; not part of the telling', 'What this week touched'),
]
SECTIONS = [
    ('Opening', 'Otter Creek'), ('The hook', 'The cold open.'),
    ('The sea', '<h2>Alexander and the Sea</h2>'), ('The first sermon', '<h2>His first sermon</h2>'),
    ('The Synod', '<h2>The Synod of Pittsburg</h2>'), ('Alexander answers', '<h2>Alexander Answers</h2>'),
    ('Brush Run', '<h2>Brush Run</h2>'), ('The ordination', '<h2>The Ordination</h2>'),
    ('Tying back', '<h2>Two Wills, One Bequest</h2>'), ('Close', 'for discussion'),
]

# The sources whole: Richardson's Memoirs (excerpts, in sources/), and from the class site
# (stone-campbell-site/src/documents) the Declaration and Address and the Last Will. Set SITE to the
# site checkout if it is not ~/projects/stone-campbell-site.
def docs(between, clean):
    return [
        {'key': 'rich', 'title': 'Robert Richardson, <i>Memoirs of Alexander Campbell</i>, vol. 1 (1868)',
         'sub': 'The wreck, the first sermon, the Synod&rsquo;s minutes, Alexander&rsquo;s reply, Brush Run, the ordination &middot; excerpts, machine-read from the Internet Archive scan',
         'html': clean(open(os.path.join(_H, 'sources', 'richardson-memoirs-v1-excerpts.html')).read())},
        {'key': 'dna', 'title': 'Thomas Campbell, <i>Declaration and Address</i> (1809)',
         'sub': 'The whole of it: Declaration, Address, Propositions, Appendix',
         'html': clean(between('declaration-and-address-fulltext.njk', '<h2 id="declaration">', '<!-- SOURCE CITATION -->'))},
        {'key': 'will', 'title': 'The Last Will and Testament of the Springfield Presbytery',
         'sub': 'Cane Ridge, June 28, 1804 &middot; with the Witnesses&rsquo; Address',
         'html': clean(between('last-will-fulltext.njk', '<h2 id="epigraph">', '<!-- SOURCE CITATION -->'))},
    ]

SHORT = {'rich': 'Richardson&rsquo;s <i>Memoirs</i>', 'dna': 'The Declaration and Address', 'will': 'The whole will'}
DOC_DOORS = [('Richardson&rsquo;s account, whole', '<h2>Brush Run</h2>', 0)]

# Which documents a slide's quotes are looked for in, read from its citation text.
def doc_order(vis, K):
    if 'Declaration and Address' in vis: return [K.index('dna')]
    if 'Last Will and Testament' in vis: return [K.index('will')]
    return [K.index('rich')] + [i for i in range(len(K)) if K[i] != 'rich']

mapdeck.build({
    'part': '5', 'key': 'w5', 'chapter': 'Chapter 5', 'title': 'Chapter 5 &middot; Wherever Two or Three Are Gathered',
    'out': 'decks/week5-brush-run-map.html', 'source': 'decks/src/week5/slides.py', 'built_by': 'decks/src/week5map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': SHORT, 'doc_doors': DOC_DOORS, 'doc_order': doc_order,
})
