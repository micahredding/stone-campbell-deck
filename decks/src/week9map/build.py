# Chapter 9, "The Heckler Who Kept His Seat" (Aylett Raines, 1828; then N. T. Wright), as a map deck:
# the slides in decks/src/week9/slides.py. Same builder as Chapters 4-8 (decks/src/mapdeck.py).
#   python3 decks/src/week9map/build.py   ->  decks/chapter9.html
# Quotations: python3 decks/src/week9/check_quotes.py
# Maps: python3 decks/src/week9/maps/reserve.py <cache dir>  (writes decks/src/week9/images/map-*.svg)
import os, sys, importlib.util
_H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_H, '..'))
import mapdeck, resources as R

SIDE = []
SECTIONS = [
    ('Opening', 'Our Wild Democracy &middot; Chapter 9'),
    ('Raines, and where', 'Fredericksburg, Spotsylvania County'),
    ('Windham', 'Scottish-born, a schoolmaster in Pittsburgh'),
    ('Thomas Campbell', 'probably no man within the reformation who possessed'),
    ('Warren', 'Warren, August 1828<'),
    ('Alexander&rsquo;s proposal', 'substantially repeated what he had said in his introductory discourse'),
    ('What made it come alive?', 'come alive?'),
    ('N. T. Wright', 'Two centuries later'),
    ('Close', 'The quiz, again'),
]
def docs(between, clean): return R.docs(between, clean, [])

mapdeck.build({
    'part': '9', 'key': 'w9', 'chapter': 'Chapter 9', 'title': 'Chapter 9 &middot; The Heckler Who Kept His Seat',
    'page_title': 'Chapter 9 &middot; The Heckler Who Kept His Seat',
    'out': 'decks/chapter9.html', 'source': 'decks/src/week9/slides.py', 'built_by': 'decks/src/week9map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': R.SHORT, 'doc_doors': [], 'doc_order': R.doc_order,
})

spec = importlib.util.spec_from_file_location('w8build_slim', os.path.join(_H, '..', 'week8map', 'build.py'))
# reuse Chapter 8's slim() without re-running its builds: copy the function source
src = open(os.path.join(_H, '..', 'week8map', 'build.py')).read()
i = src.index('def slim('); j = src.index("slim('decks/chapter8.html')")
exec(src[i:j])
slim('decks/chapter9.html')
