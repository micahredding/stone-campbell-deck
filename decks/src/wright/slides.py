# -*- coding: utf-8 -*-
# "Wright and the Founders": N. T. Wright on the church as "the small working model of new creation", set beside
# Thomas Campbell, Alexander Campbell and Barton Stone. The slides are the shared resource R.wright()
# (decks/src/resources.py). Build:  python3 decks/src/wright/build.py  ->  decks/wright-and-the-founders-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>Wright and the Founders</h1>'
         '<div class=sub>N. T. Wright and the Stone-Campbell movement on the church as the future in miniature</div>'
         '<aside class=notes>A standalone resource deck, in six movements: a taste of new creation; its substance is unity; visible unity; practiced; a sign to the powers; it draws the world.</aside></section>')
S = [TITLE] + R.wright() + [R.w4.BLACK]
