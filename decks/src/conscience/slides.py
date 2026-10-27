# -*- coding: utf-8 -*-
# "Whose Conscience?": freedom of conscience, claimed and extended. The slides are the shared
# resource R.conscience() (decks/src/resources.py), with "The honest limits" as a side path.
# Build:  python3 decks/src/conscience/build.py  ->  decks/whose-conscience-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>Whose Conscience?</h1>'
         '<div class=sub>Freedom of conscience, claimed and extended</div>'
         '<aside class=notes>A standalone resource deck. Scripture, the early church, the Reformers and their critics, Westminster, Williams and Madison, the Campbells, Vatican II. Side path: the honest limits.</aside></section>')
S = [TITLE] + R.conscience() + [R.w4.BLACK]
