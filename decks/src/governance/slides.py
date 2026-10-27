# -*- coding: utf-8 -*-
# "The Assembly Governs": church government as the congregation's, from Paul's ekklesia through the consent of the
# people in every tradition to Brush Run. Assembled from shared resources (decks/src/resources.py): ekklesia(),
# consent(), governance(), with constitution() and succession() as side paths.
# Build:  python3 decks/src/governance/build.py  ->  decks/the-assembly-governs-map.html
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
R = _load('resources', 'resources.py')
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

TITLE = ('<section class="slide breath"><div class=eyebrow>Our Wild Democracy &middot; a resource</div>'
         '<h1>The Assembly Governs</h1>'
         '<div class=sub>Church government in every tradition</div>'
         '<aside class=notes>A standalone resource deck. Three movements: the word Paul chose (the citizens&rsquo; assembly); the consent of the people, remembered in every tradition; and church government in Scripture, the Last Will and the Campbells. Side paths: confession or constitution; against succession.</aside></section>')
CONSENT = ('<section class="slide breath"><div class=eyebrow>The Assembly Governs</div><h2 style="max-width:none">The consent of all</h2>'
           '<div class=sub>Cyprian, Leo, Luther, the Orthodox, Rome</div>'
           '<aside class=notes>Every tradition remembers a time, or holds a principle, in which the whole people chose and consented.</aside></section>')
END = R.CARD('The assembly chooses.<br>' + R.G('Christ governs.'),
             'The end. The congregation is the fountain of office; Christ is its head; every other office answers to that.')
S = [TITLE] + R.ekklesia() + [CONSENT] + R.consent() + R.governance() + R.constitution() + R.succession() + [END, R.w4.BLACK]
