# "The Priesthood of All Believers" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/priesthood/build.py  ->  decks/priesthood-of-all-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = [R.TABLE]
SECTIONS = [
    ('Opening', '<h1>The Priesthood of All Believers</h1>'), ('Scripture', H % 'A royal priesthood'),
    ('The early church', H % 'The early church remembered'), ('Luther', H % 'Luther, 1520'), ('Rome', H % 'Rome'),
    ('Orthodox &amp; Lima', H % 'The Orthodox, and the ecumenical movement'), ('The Campbells', H % 'Kings and priests to God'),
]
DOC_KEYS = ['priest', 'church', 'kjv', 'rich', 'acr', 'tbl']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('The priesthood of all: the sources', H % 'Luther, 1520', 0),
             ('The whole church', H % 'Rome', 1)]

mapdeck.build({
    'part': 'pr', 'key': 'wpr', 'chapter': 'A resource', 'title': 'The Priesthood of All Believers',
    'out': 'decks/priesthood-of-all-map.html', 'source': 'decks/src/resources.py (priesthood)', 'built_by': 'decks/src/priesthood/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
