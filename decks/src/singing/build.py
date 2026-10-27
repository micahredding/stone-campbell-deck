# "The Whole Church Sings" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/singing/build.py  ->  decks/the-whole-church-sings-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = [R.INSTRUMENT]
SECTIONS = [
    ('Opening', '<h1>The Whole Church Sings</h1>'), ('Scripture', H % 'The fruit of our lips'),
    ('The early church', H % 'The early church sang'), ('The Reformers', H % 'The Reformers gave the song back'),
    ('Rome', H % 'Rome'), ('Not by proxy', H % 'Not by proxy'),
]
DOC_KEYS = ['sing']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('The whole church sings: the sources', H % 'The fruit of our lips', 0)]

mapdeck.build({
    'part': 'sg', 'key': 'wsg', 'chapter': 'A resource', 'title': 'The Whole Church Sings',
    'out': 'decks/the-whole-church-sings-map.html', 'source': 'decks/src/resources.py (singing)', 'built_by': 'decks/src/singing/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
