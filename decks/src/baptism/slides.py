# -*- coding: utf-8 -*-
# "One Baptism": baptism as union and as every Christian's ordination. The slides are the shared
# resource R.baptism() (decks/src/resources.py), with "The honest limits" as a side path.
# Build:  python3 decks/src/baptism/build.py  ->  decks/one-baptism-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>One Baptism</h1>'
         '<div class=sub>Baptism in every tradition</div>'
         '<aside class=notes>A standalone resource deck. Ephesians 4, the early church, baptism as ordination, Buffalo Creek and Brush Run, Lunenburg, Lima and Magdeburg. Side path: the honest limits.</aside></section>')
S = [TITLE] + R.baptism() + [R.w4.BLACK]
