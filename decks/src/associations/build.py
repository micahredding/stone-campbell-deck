# "Joined, Refused, Dissolved": the Campbells' associations, 1791-1866, as a map deck (the shared resource
# R.associations() as its spine).   python3 decks/src/associations/build.py  ->  decks/joined-refused-dissolved-map.html
# Same builder as the chapters (decks/src/mapdeck.py); research: stone-campbell-database, 08 Timelines/Campbell Associations Timeline.md
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SECTIONS = [
    ('Opening', 'The Campbells&rsquo; associations,<br>1791&ndash;1866'),
    ('Ireland', 'The Seceder Presbyterians'),
    ('Glasgow', 'Alexander leaves the Seceders'),
    ('Pennsylvania', 'Out of the Presbyterians'),
    ('Brush Run', '<h2 style="max-width:none">Brush Run</h2>'),
    ('The Baptists', 'Redstone and Mahoning'),
    ('Union', 'With Stone&rsquo;s Christians'),
    ('Cooperation', 'Societies by consent'),
    ('Two moves', 'Two moves, again and again'),
]
def docs(between, clean): return R.docs(between, clean, [])

mapdeck.build({
    'part': 'as', 'key': 'was', 'chapter': 'A resource', 'title': 'Joined, Refused, Dissolved',
    'out': 'decks/joined-refused-dissolved-map.html', 'source': 'decks/src/resources.py (associations)', 'built_by': 'decks/src/associations/build.py',
    'side': [], 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})
