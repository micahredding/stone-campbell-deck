# -*- coding: utf-8 -*-
# "Every Lord's Day": the Supper each Sunday, across the church. The slides are the shared resource
# R.weekly(full=True) (decks/src/resources.py); Chapter 5 hangs the short form as a side path.
# Build:  python3 decks/src/weekly/build.py  ->  decks/every-lords-day-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>Every Lord&rsquo;s Day</h1>'
         '<div class=sub>The Supper each Sunday, across the whole church</div>'
         '<aside class=notes>A standalone resource deck. The Church of Christ breaks bread every Lord&rsquo;s day; so did the early church, so Calvin and Wesley wanted, so Lutheran confessions and Vatican II teach, and so the ecumenical movement asks. Distinctive only because others let it slip.</aside></section>')
S = [TITLE] + R.weekly(full=True) + [R.w4.BLACK]
