# -*- coding: utf-8 -*-
# "The Bible in Every Hand": access to Scripture as the priesthood of all. The slides are the shared
# resource R.bible() (decks/src/resources.py), with "Who interprets?" as a side path.
# Build:  python3 decks/src/scripture/build.py  ->  decks/the-bible-in-every-hand-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>The Bible in Every Hand</h1>'
         '<div class=sub>Access to Scripture in every tradition</div>'
         '<aside class=notes>A standalone resource deck. Scripture, Chrysostom, Erasmus, Tyndale, Luther, Rome from the Index to Dei Verbum, Stone and the Campbells. Side path: who interprets?</aside></section>')
S = [TITLE] + R.bible() + [R.w4.BLACK]
