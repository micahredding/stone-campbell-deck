# "Union, All His Life" as a map deck: the shared resource R.unity() as a spine, with the sources whole.
#   SITE=<class site checkout> python3 decks/src/unity/build.py  ->  decks/union-all-his-life-map.html
# Same builder as the chapters (decks/src/mapdeck.py); how the map works: decks/src/week4map/README.md.
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SECTIONS = [
    ('Opening', '<h1>Union, All His Life</h1>'),
    ('His father&rsquo;s plea', '<h2 style="max-width:none">His father&rsquo;s plea</h2>'),
    ('No party man', '<h2 style="max-width:none">No party man</h2>'),
    ('The Ancient Order', '<h2 style="max-width:none">In the middle of the Ancient Order</h2>'),
    ('Lunenburg', '<h2 style="max-width:none">Lunenburg, 1837</h2>'),
    ('The open Campbell', '<h2 style="max-width:none">The open Campbell</h2>'),
]
DOC_KEYS = ['uni', 'dna']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('Campbell on union, the sources', '<h2 style="max-width:none">His father&rsquo;s plea</h2>', 0),
             ('The whole Declaration and Address', '<h2 style="max-width:none">His father&rsquo;s plea</h2>', 1)]

mapdeck.build({
    'part': 'u', 'key': 'wu', 'chapter': 'A resource', 'title': 'Union, All His Life',
    'out': 'decks/union-all-his-life-map.html', 'source': 'decks/src/resources.py (unity)', 'built_by': 'decks/src/unity/build.py',
    'side': [], 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
