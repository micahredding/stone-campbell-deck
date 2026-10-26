# -*- coding: utf-8 -*-
# "The Synod and the Reply": material taken out of Chapter 5 (October 2026) and kept in reserve for another
# day: the Synod of Pittsburg's refusal of Thomas Campbell (1810), his reply to the
# Synod on clergy and laity, and other Brush Run slides. The slides live in decks/src/week5/slides.py (RES);
# this file frames them as a deck. Build:  python3 decks/src/reserve5/build.py  ->  decks/reserve-synod-and-reply-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w5 = _load('w5slides', 'week5/slides.py')
PATDEFS, CHRISTENDOM_CSS = w5.PATDEFS, w5.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; in reserve</div>'
         '<h1>The Synod and the Reply</h1>'
         '<div class=sub>Washington, Pennsylvania &middot; 1810</div>'
         '<aside class=notes>Material taken out of Chapter 5 and kept for another day: the Synod of Pittsburg refusing Thomas Campbell and Alexander&rsquo;s reply on clergy and laity.</aside></section>')
S = [TITLE] + w5.RES + [w5.BLACK]
