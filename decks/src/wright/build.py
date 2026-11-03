# "Wright and the founders" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   python3 decks/src/wright/build.py  ->  decks/wright-and-the-founders-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SIDE = []
SECTIONS = [
    ('Opening', '<h2 style="max-width:none">The small working model of new creation</h2>'), ('A taste of new creation', H % 'A taste of new creation'),
    ('Its substance is unity', H % 'Its substance is unity'), ('Visible', H % 'Visible, not only spiritual'),
    ('Practiced', H % 'Practiced'), ('A sign to the powers', H % 'A sign to the powers'), ('It draws the world', H % 'It draws the world'),
]
DOC_KEYS = ['wrt']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('Wright and the founders: the sources', H % 'A taste of new creation', 0)]

mapdeck.build({
    'part': 'wr', 'key': 'wwf', 'chapter': 'A resource', 'title': 'Wright and the Founders',
    'out': 'decks/wright-and-the-founders-map.html', 'source': 'decks/src/resources.py (wright)', 'built_by': 'decks/src/wright/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
