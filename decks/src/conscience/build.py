# "Whose Conscience?" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/conscience/build.py  ->  decks/whose-conscience-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = [R.CONSCIENCE_LIMITS]
SECTIONS = [
    ('Opening', '<h1>Whose Conscience?</h1>'), ('Scripture', H % 'To his own master'),
    ('Claimed, then refused', H % 'Claimed, and then refused'), ('The other chain', H % 'The other chain'),
    ('Inside the church', H % 'Inside the church'), ('The whole church now', H % 'The whole church now'),
]
DOC_KEYS = ['consc', 'dna']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('Freedom of conscience: the sources', H % 'To his own master', 0)]

mapdeck.build({
    'part': 'cs', 'key': 'wcs', 'chapter': 'A resource', 'title': 'Whose Conscience?',
    'out': 'decks/whose-conscience-map.html', 'source': 'decks/src/resources.py (conscience)', 'built_by': 'decks/src/conscience/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
