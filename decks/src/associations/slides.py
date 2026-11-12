# -*- coding: utf-8 -*-
# "Joined, Refused, Dissolved": the Campbells' associations, 1791-1866. The slides are the shared resource
# R.associations() (decks/src/resources.py); this file only frames them as a deck.
# Build:  python3 decks/src/associations/build.py  ->  decks/joined-refused-dissolved-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>Joined, Refused, Dissolved</h1>'
         '<div class=sub>The Campbells&rsquo; associations, 1791&ndash;1866</div>'
         '<aside class=notes>A standalone resource deck, and a side path any chapter can hang (R.associations()). Research: stone-campbell-database, 08 Timelines, &ldquo;Campbell Associations Timeline.&rdquo;</aside></section>')
S = [TITLE] + R.associations() + [R.w4.BLACK]
