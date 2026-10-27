# -*- coding: utf-8 -*-
# "The Priesthood of All Believers": every tradition confesses it; the Stone-Campbell churches tried to practice it.
# The slides are the shared resource R.priesthood() (decks/src/resources.py), with "Who keeps the table" as a
# side path off Campbell at the table. Build:  python3 decks/src/priesthood/build.py  ->  decks/priesthood-of-all-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>The Priesthood of All Believers</h1>'
         '<div class=sub>Confessed by every tradition</div>'
         '<aside class=notes>A standalone resource deck. Scripture, Tertullian, Luther, Vatican II and the 2024 Synod, the Orthodox, the Lima text, and the Campbells. Side path: who keeps the table.</aside></section>')
S = [TITLE] + R.priesthood(table=R.table()) + [R.w4.BLACK]
