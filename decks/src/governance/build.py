# "The Assembly Governs" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/governance/build.py  ->  decks/the-assembly-governs-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [R.CONSTITUTION, R.SUCCESSION]
SECTIONS = [
    ('Opening', '<h1>The Assembly Governs</h1>'),
    ('The assembly', '<div class=eyebrow>The church as <i>ekklēsia</i>'),
    ('The consent of all', '<h2 style="max-width:none">The consent of all</h2>'),
    ('Church government', '<div class=eyebrow>Church government &middot; a resource</div>'),
]
DOC_KEYS = ['ekk', 'church', 'kjv', 'wcf', 'dna', 'will', 'cb', 'rich']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('The assembly: the sources', '<h2 style="max-width:none">The consent of all</h2>', 0),
             ('The whole church', '<h2 style="max-width:none">The consent of all</h2>', 1)]

mapdeck.build({
    'part': 'gv', 'key': 'wgv', 'chapter': 'A resource', 'title': 'The Assembly Governs',
    'out': 'decks/the-assembly-governs-map.html', 'source': 'decks/src/resources.py (ekklesia, consent, governance)', 'built_by': 'decks/src/governance/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
