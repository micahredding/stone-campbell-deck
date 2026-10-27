# "The Bible in Every Hand" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/scripture/build.py  ->  decks/the-bible-in-every-hand-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = [R.WHO_INTERPRETS]
SECTIONS = [
    ('Opening', '<h1>The Bible in Every Hand</h1>'), ('Scripture', H % 'They shall all know me'),
    ('The early church', H % 'Not only the monks'), ('The mother tongue', H % 'In the mother tongue'),
    ('Rome', H % 'Rome: from the Index to <i>Dei Verbum</i>'), ('Stone and the Campbells', H % 'Into the hands of the people'),
    ('The honest limit', H % 'The honest limit'),
]
DOC_KEYS = ['bible', 'dna']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('The Bible in every hand: the sources', H % 'They shall all know me', 0)]

mapdeck.build({
    'part': 'sc', 'key': 'wsc', 'chapter': 'A resource', 'title': 'The Bible in Every Hand',
    'out': 'decks/the-bible-in-every-hand-map.html', 'source': 'decks/src/resources.py (bible)', 'built_by': 'decks/src/scripture/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
