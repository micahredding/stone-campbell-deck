# "The Synod and the Reply" (Chapter 5 reserve) as a map deck. Same builder as the chapters (decks/src/mapdeck.py).
#   SITE=<class site checkout> python3 decks/src/reserve5/build.py  ->  decks/reserve-synod-and-reply-map.html
import os, sys
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = [
    R.WESTMINSTER,
    ('Richardson&rsquo;s note', '<div class=eyebrow>Richardson&rsquo;s note</div>', '<div class=eyebrow>Richardson&rsquo;s note</div>'),
]
SECTIONS = [
    ('Opening', '<h1>The Synod and the Reply</h1>'),
    ('The Synod', '<h2>The Synod of Pittsburg</h2>'), ('Alexander answers', '<h2>Alexander Answers</h2>'),
    ('Brush Run, more', 'by no means considers itself a Church'),
]
DOC_KEYS = ['rich', 'wcf', 'dna', 'will', 'kjv']
def docs(between, clean): return R.docs(between, clean, DOC_KEYS)
DOC_DOORS = [('Richardson&rsquo;s account, whole', '<h2>The Synod of Pittsburg</h2>', 0),
             ('The Westminster Confession, whole', '<h2>The Synod of Pittsburg</h2>', 1)]

mapdeck.build({
    'part': 'r5', 'key': 'wr5', 'chapter': 'In reserve', 'title': 'The Synod and the Reply (Chapter 5 reserve)',
    'out': 'decks/reserve-synod-and-reply-map.html', 'source': 'decks/src/week5/slides.py (RES)', 'built_by': 'decks/src/reserve5/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': DOC_DOORS, 'doc_order': R.doc_order,
})
