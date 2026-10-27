# -*- coding: utf-8 -*-
# "The Whole Church Sings": congregational singing as the priesthood of all believers. The slides are the shared
# resource R.singing() (decks/src/resources.py), with "The instrument question" as a side path.
# Build:  python3 decks/src/singing/build.py  ->  decks/the-whole-church-sings-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>The Whole Church Sings</h1>'
         '<div class=sub>Congregational singing in every tradition</div>'
         '<aside class=notes>A standalone resource deck. Scripture, the early church, the Reformers, Vatican II, Stone and the Campbells. Side path: the instrument question.</aside></section>')
S = [TITLE] + R.singing() + [R.w4.BLACK]
