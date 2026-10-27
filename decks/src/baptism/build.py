# "One Baptism" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/baptism/build.py  ->  decks/one-baptism-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = [R.BAPTISM_LIMITS]
SECTIONS = [
    ('Opening', '<h1>One Baptism</h1>'), ('The early church', H % 'Buried with him'),
    ('Ordination', H % 'Every Christian&rsquo;s ordination'), ('Brush Run', H % 'Brush Run goes under the water'),
    ('Lunenburg', H % 'Not even immersion'), ('The whole church now', H % 'The whole church now'),
]
DOC_KEYS = ['bapt']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('One baptism: the sources', '<div class=eyebrow>Ephesians 4:4&ndash;6</div>', 0)]

mapdeck.build({
    'part': 'bp', 'key': 'wbp', 'chapter': 'A resource', 'title': 'One Baptism',
    'out': 'decks/one-baptism-map.html', 'source': 'decks/src/resources.py (baptism)', 'built_by': 'decks/src/baptism/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
