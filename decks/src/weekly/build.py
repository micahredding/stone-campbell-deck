# "Every Lord's Day" as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/weekly/build.py  ->  decks/every-lords-day-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

H = '<h2 style="max-width:none">%s</h2>'
SECTIONS = [
    ('Opening', '<h1>Every Lord&rsquo;s Day</h1>'),
    ('The early church', H % 'The first day of the week'),
    ('The Reformers', H % 'The Reformers wanted it back'),
    ('Rome', H % 'Rome'),
    ('The ecumenical movement', H % 'The ecumenical movement'),
]
DOC_KEYS = ['lord', 'rich']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('Every Lord&rsquo;s day: the sources', H % 'The first day of the week', 0)]

mapdeck.build({
    'part': 'wk', 'key': 'wwk', 'chapter': 'A resource', 'title': 'Every Lord&rsquo;s Day',
    'out': 'decks/every-lords-day-map.html', 'source': 'decks/src/resources.py (weekly)', 'built_by': 'decks/src/weekly/build.py',
    'side': [], 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
