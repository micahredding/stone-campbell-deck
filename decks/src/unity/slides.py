# -*- coding: utf-8 -*-
# "Union, All His Life": Alexander Campbell on the union of all Christians, from his father's Declaration and
# Address (1809) through the Christian Baptist and The Christian System to the Lunenburg letter (1837), with
# the open Campbell beyond it. The slides are the shared resource R.unity() (decks/src/resources.py); this
# file only frames them as a deck. Build:  python3 decks/src/unity/build.py  ->  decks/union-all-his-life-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>Union, All His Life</h1>'
         '<div class=sub>Alexander Campbell and the union of all Christians, 1809&ndash;1848</div>'
         '<aside class=notes>A standalone resource deck, not part of a chapter. Thomas Campbell&rsquo;s plea for union, which Alexander made his own; the young Alexander refusing party; union kept in view through the Ancient Order years; the Lunenburg letter; and the open Campbell beyond it.</aside></section>')
S = [TITLE] + R.unity() + [R.w4.BLACK]
