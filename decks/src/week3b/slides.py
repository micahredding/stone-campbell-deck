# -*- coding: utf-8 -*-
# Chapter 3, part two — The Declaration & Address: the answer (for Oct 18, 2026).
# Part one (Oct 11) stopped at "How do Christians achieve unity? / Next week." This deck recaps and answers it.
# Slides shared with part one are taken from decks/src/week3/slides.py, so a fix there shows up here too.
# Build:  python3 decks/src/week3b/build.py   ->  decks/week3b-declaration-address-part-two.html
import importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('w3slides', os.path.join(_H, '..', 'week3', 'slides.py'))
w3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(w3)
PATDEFS, CHRISTENDOM_CSS = w3.PATDEFS, w3.CHRISTENDOM_CSS

def pick(marker, nth=None):
    """the part-one slide containing marker (must be unique unless nth is given)"""
    hits = [x for x in w3.S if marker in x]
    assert hits and (nth is not None or len(hits) == 1), (marker, len(hits))
    return hits[nth or 0]

def span(first, last):
    """part-one slides from the one containing first through the one containing last, in order"""
    i = [k for k, x in enumerate(w3.S) if first in x]
    j = [k for k, x in enumerate(w3.S) if last in x]
    assert len(i) == 1 and len(j) == 1 and i[0] <= j[0], (first, last, i, j)
    return w3.S[i[0]:j[0] + 1]

G = lambda a, b: '%s <span style="color:var(--gold)">%s</span>' % (a, b)
BLACK = '<section class="slide"><aside class=notes>Black.</aside></section>'

S = []
A = S.append

# ---------- OPENING ----------
A(pick('Our Wild<br>Democracy'))

A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none">Luther claimed conscience for himself&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;Campbell claimed it for his brother.</h2>'
  '<aside class=notes>One click. Let the room finish it. Last week&rsquo;s turn in one line.</aside></section>')

CAP = 'font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(16px,2.6vmin,31px);line-height:1.3;margin-top:1.2vmin;color:var(--bone)'
IMG = 'width:100%;height:30vh;object-fit:cover;border-radius:.4vmin'
def card(img, cap, r, fit=''):
    return ('<figure class="shot frag" style="--r:%sdeg"><img src="%s" alt="" style="%s%s"><figcaption style="%s">%s</figcaption></figure>'
            % (r, img, IMG, fit, CAP, cap))
A('<section class="slide"><div class="eyebrow quiet">Last week &middot; The Declaration and Address, 1809</div>'
  '<div class="shots recapshots" style="gap:3vmin">'
  + card('IMG_EGG', '<b>325&ndash;1806.</b> Creeds, councils, edicts, swords. Every instrument of unity divides.', '-1.5', ';object-fit:contain;background:#110e0b')
  + card('IMG_WORMSPIC', '<b>Worms, 1521.</b> Conscience cannot be compelled.', '1.2')
  + card('IMG_MARBURGPIC', '<b>Marburg, 1529.</b> Luther will not grant it to Zwingli.', '-1')
  + card('IMG_MANZ', '<b>Zurich, 1527.</b> Zwingli will not grant it to the Anabaptists.', '1.8')
  + card('IMG_TCAMPBELL', '<b>1809.</b> &ldquo;No man can judge for his brother.&rdquo; How dare you put asunder?', '-1.2') +
  '</div>'
  '<div class="sub frag" style="max-width:none;margin-top:2.6vmin">So how do Christians achieve unity?</div>'
  '<aside class=notes>Six clicks, about three minutes: last week in five pictures. The egg (325 to 1806, every instrument offered for unity left another division); Worms (Anton von Werner, 1877); Marburg (August Noack, 1867&ndash;69); the drowning (Jan Luyken, <i>Martyrs Mirror</i>, 1685); Thomas Campbell. Then the question we stopped on.</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3, part two</div>'
  '<h1>The Declaration<br>and Address</h1><div class=table-line></div>'
  '<div class=sub>The answer</div>'
  '<aside class=notes>Title up. &rarr; &ldquo;Last week we ended on a question. Tonight, Campbell&rsquo;s answer, and what it asks of us.&rdquo;</aside></section>')

A(pick('class="litany ideasum"').replace('<div class=eyebrow>Ideas</div>', '<div class=eyebrow>Last week&rsquo;s ideas</div>')
  .replace('All seven at once, for the room to see together before the discussion.',
           'Last week&rsquo;s seven ideas, all at once. Read them, or let the room read them; do not re-teach.'))

A('<section class="slide"><h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none">How do<br>Christians achieve<br>unity?</h2>'
  '<div class="sub frag" style="max-width:none">&ldquo;That they all may be one&hellip; that the world may believe that thou hast sent me.&rdquo;<br><span style="font-size:.7em;color:var(--bone-dim)">John 17:21</span></div>'
  '<aside class=notes>The question we stopped on. Then the prayer: a prayer, not a command, and for the sake of the world&rsquo;s belief. Pause before the answer.</aside></section>')

# ---------- THE ANSWER (part one's material from "Christ alone" through Campbell's answer) ----------
S += span('>Christ alone</h2>', '<div class=eyebrow>The answer</div>')

A(BLACK)

# ---------- IDEAS ----------
DISCUSS = pick('&#9670; for discussion', 0)
A(DISCUSS)
IDEAS = [
    (G('Only Christ', 'can make us one.'),
     'The Preamble: we cannot &ldquo;reasonably expect to find it anywhere but in Christ and his simple word.&rdquo; Every instrument on the egg was asked to do a job only Christ can do.'),
    (G('There is nothing wrong with a creed.', 'But a creed cannot make us one.'),
     'Proposition 7: doctrinal exhibitions &ldquo;may be highly expedient&rdquo;; they are not to be made terms of communion. A creed can teach; it cannot unite.'),
    (G('The church is', 'already one.'),
     'Proposition 1: &ldquo;essentially, intentionally, and constitutionally one.&rdquo; Unity is given, not built; the divisions are the innovation.'),
    (G('Make anything else a term of communion,', 'and it will divide us.'),
     'Propositions 6, 8 and 9: nothing binding &ldquo;farther than they perceive the connection&rdquo;; no one excluded for what they do not yet know. The Churches of Christ have lived the proof.'),
    (G('It refused to be a creed,', 'and its heirs made it one.'),
     'Resolution IV: &ldquo;by no means considers itself a Church.&rdquo; Proposition 7&rsquo;s warning applies to the Declaration itself: honor it as a plea, not a pattern.'),
    (G('The rule that opens the table', 'can also cut.'),
     'Andrew Munro on the proof-sheets: &ldquo;if you follow these out, you must become a Baptist.&rdquo; Campbell&rsquo;s answer committed the next generation before anyone knew where it led.'),
]
for k, (h, n) in enumerate(IDEAS, 1):
    A('<section class="slide idea room"><div class="eyebrow quiet">Idea %d of %d</div><h2>%s</h2><aside class=notes>%s</aside></section>'
      % (k, len(IDEAS), h, n))
plain = lambda h: re.sub(r'<span style="color:var\(--gold\)">(.*?)</span>', r'\1', h)
A('<section class="slide room"><div class=eyebrow>Ideas</div>'
  '<div class="litany ideasum" style="text-align:left;gap:1.2vmin;margin-top:2.6vmin">'
  + ''.join('<div class=no><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (k, plain(h)) for k, (h, _) in enumerate(IDEAS, 1)) +
  '</div><aside class=notes>All six at once, before the discussion.</aside></section>')
A(DISCUSS)
A(pick('stone-campbell.micahredding.com'))
A(pick('Next week: the rise and fall of the Springfield Presbytery'))
A(BLACK)

# ---------- ADDENDUM (as in part one) ----------
_ad = [k for k, x in enumerate(w3.S) if '>Addendum</h2>' in x]
assert len(_ad) == 1
S += w3.S[_ad[0]:]
