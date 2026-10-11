# -*- coding: utf-8 -*-
# Chapter 3, part two — The Declaration & Address: the answer (for Oct 18, 2026).
# Part one (Oct 11) stopped at "How do Christians achieve unity? / Next week." This deck recaps and answers it.
# The opening reuses part-one slides from decks/src/week3/slides.py (title, ideas list, discussion, site); the
# answer material and the addendum were moved here from part one after it was taught.
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

# ---------- part one's prepared material we did not reach (moved here from decks/src/week3/slides.py) ----------
Q, N, C, DA = w3.Q, w3.N, w3.C, w3.DA
L = []
A = L.append
# ---------- THE SOLUTION ----------
A('<section class="slide breath"><h2 style="font-size:clamp(80px,22vmin,280px);line-height:1;max-width:none;color:var(--gold)">Christ alone</h2>'
  '<aside class=notes>Let it sit. Then the Preamble says it in his words.</aside></section>')

# ---------- 7 THE SOLUTION ----------

A(Q('&ldquo;&hellip;nor, indeed, can we reasonably expect to find it anywhere but in <b>Christ and his simple word</b>, which is the same yesterday, to-day, and forever.&rdquo;', DA, 'Preamble, continued') +
  N('The clause you stopped before. Now it has fifteen hundred years behind it.', '&rarr; Thomas Campbell saw only one answer: given a people called to follow their conscience, given that no council could forever bind it, the only thing Christians could unite on was Christ himself.'))

A(Q('&ldquo;&hellip;taking the Divine word alone for our rule; the Holy Spirit for our teacher and guide, to lead us into all truth; and <b>Christ alone, as exhibited in the word</b>, for our salvation&hellip;&rdquo;', DA, 'Preamble, continued') +
  N('Guard: it is not creedless. &ldquo;Christ alone, <i>as exhibited in the word</i>.&rdquo; The fence is what Scripture expressly says, and nothing else. The propositions say how.'))

A('<section class="slide breath"><h2 style="max-width:32ch">Every time we hand a creed, a council, or a magistrate<br><span style="color:var(--gold)">a job only Christ can do</span>, it fails.</h2>'
  '<aside class=notes>The chapter&rsquo;s thesis, right after Campbell&rsquo;s answer (&ldquo;anywhere but in Christ&rdquo;). Point back at the egg: every one of those was a good instrument given the wrong job. Campbell names the job in the Address: creeds were &ldquo;designed and embraced for the purpose of promoting and securing that desirable unity and purity which the Bible alone, without those helps, would be insufficient to maintain and secure.&rdquo; That is the job description, and no document can do it.<br>'
  '&rarr; Which is not to say creeds are bad.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">There is nothing wrong with a creed.</h2>'
  '<div class="sub frag" style="max-width:none">But a creed cannot make us one.</div>'
  '<div class="sub frag punch">Only Christ can do that.</div>'
  '<aside class=notes>Two clicks. Not anti-creed: Nicaea is true, and the room says it. The fault on the egg was never the creed; it was the job the creed was given.</aside></section>')

A(Q('&ldquo;&hellip;doctrinal exhibitions of the great system of Divine truths&hellip; <b>be highly expedient, and the more full and explicit they be for those purposes, the better</b>; yet&hellip; they ought not to be made terms of Christian communion&hellip;&rdquo;', DA, 'Proposition 7') +
  N('Campbell says it himself: write the fullest confession you can. Just do not make it the door. Elided: &ldquo;and defensive testimonies in opposition to prevailing errors&rdquo;; &ldquo;as these must be in a great measure the effect of human reasoning, and of course must contain many inferential truths.&rdquo;',
    'The sentence ends: &ldquo;the Church from the beginning did, and ever will, consist of little children and young men, as well as fathers.&rdquo;'))

# ---------- 6 THE PROPOSITIONS ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Thirteen Propositions</h2><div class=table-line></div>'
  '<div class=sub>Five of them.</div>'
  '<aside class=notes>Offered, the Address says just before them, not &ldquo;as an overture toward a new creed or standard for the Church, or as in any wise designed to be made a term of communion.&rdquo; Remember Chalcedon said the same. Read 1, 3, 6, 8, 9; the gold clause is the one to say twice.</aside></section>')

A(Q('&ldquo;That the Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ and obedience to him in all things according to the Scriptures, and that manifest the same by their tempers and conduct, and of none else&hellip;&rdquo;', DA, 'Proposition 1') +
  N('The class has heard the opening clause twice; now the whole sentence. Stand two: do you believe unity is given rather than built? If so, the sects are the innovation.'))

A(Q('&ldquo;That in order to do this, <b>nothing ought to be inculcated upon Christians as articles of faith; nor required of them as terms of communion, but what is expressly taught and enjoined upon them in the word of God</b>&hellip;&rdquo;', DA, 'Proposition 3') +
  N('The method. &ldquo;Expressly.&rdquo; This is the whole wager: strip terms of communion to what Scripture expressly says, and Christians will find they already agree on enough to live together.'))

A(Q('&ldquo;That although inferences and deductions from Scripture premises, when fairly inferred, may be truly called the doctrine of God&rsquo;s holy word, yet are they <b>not formally binding upon the consciences of Christians farther than they perceive the connection</b>&hellip; Therefore, no such deductions can be made terms of communion&hellip;&rdquo;', DA, 'Proposition 6') +
  N('Conscience again, now as polity. You cannot believe what you do not see, so you cannot be made to. Every council on the egg was an inference made a term of communion.'))

A(Q('&ldquo;That as it is not necessary that persons should have a particular knowledge or distinct apprehension of all Divinely revealed truths in order to entitle them to a place in the Church; <b>neither should they, for this purpose, be required to make a profession more extensive than their knowledge</b>&hellip;&rdquo;', DA, 'Proposition 8') +
  N('The one that answers Chalcedon directly: no term that excludes those who cannot understand it. The rest of the sentence: &ldquo;a profession of their faith in and obedience to him, in all things, according to his word, is all that is absolutely necessary to qualify them for admission into his Church.&rdquo;'))

A(Q('&ldquo;That all that are enabled through grace to make such a profession&hellip; should consider each other as the precious saints of God, should <b>love each other as brethren</b>, children of the same family and Father, temples of the same Spirit, members of the same body&hellip; Whom God hath thus joined together no man should dare to put asunder.&rdquo;', DA, 'Proposition 9') +
  N('The marriage line. Stand four: who are we not treating as brethren, and on what term?'))

# ---------- 7 OUR TABLE ----------
A('<section class="slide room"><div class=eyebrow>Our table</div>'
  '<h2>What do we require of someone before they sit at our table?</h2>'
  '<div class="sub frag">&ldquo;&hellip;a profession more extensive than their knowledge.&rdquo;</div>'
  '<aside class=notes>Discussion, eight minutes. Have them list what we actually require. Then proposition 8 against the list: which of these is a profession more extensive than their knowledge? Every room has its Munro item; ours is not infant baptism. Leave it open. Set it against the Evils list: division already costs that; what would unity cost?</aside></section>')

# ---------- 8 THE RECEPTION ----------
A('<section class="slide room"><div class=eyebrow>The Churches of Christ</div>'
  '<h2>We have kept dividing.</h2>'
  '<div class="sub frag">We have all lived it.</div>'
  '<div class="sub frag punch">Does that mean Thomas Campbell was wrong?</div>'
  '<aside class=notes>Two clicks. Let the first one sit: everyone in the room has a story of a split, a congregation, a family. Look back at the tree: one cup, non-class, non-institutional, instrumental, premillennial. Then ask the question and let them answer before the next slide.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">No. It means he was right.</h2>'
  '<div class="sub frag" style="max-width:none">Every division since has come from someone<br>offering another answer than Christ.</div>'
  '<div class="sub frag punch">There is no other answer. There never will be.</div>'
  '<aside class=notes>Two clicks. Campbell diagnosed the problem correctly; the divisions are what it looks like when his point is not taken as deeply as it merits. Cups, classes, institutions, instruments, the millennium: every one was made a term of communion, asked to do the job only Christ can do. It did what every instrument on the egg did.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Make anything else a term of communion,<br><span style="color:var(--gold)">and it will not make us one.<br>It will divide us again.</span></h2>'
  '<aside class=notes>The thesis card, brought home: the egg was not only their history. It is ours. Proposition 3 was the remedy: nothing required as terms of communion &ldquo;but what is expressly taught and enjoined upon them in the word of God.&rdquo;</aside></section>')

# ---------- 9 THE PROOF-SHEETS ----------
A('<section class="slide"><div class=eyebrow>October 1809</div>'
  '<h2>Alexander, twenty-one, three weeks off the ship, reads the proof-sheets as they come from the printer.</h2>'
  '<aside class=notes>Two sentences of Glasgow: the family wrecked off Islay, ten months in Glasgow, and the son refusing the Seceder communion token on his own, an ocean away from his father&rsquo;s break. On the road from Philadelphia they find out they have each broken with the same fence, through the same table. Then the proof-sheets.</aside></section>')

A(Q('&ldquo;Sir&hellip; these words, however plausible in appearance, are not sound. For if you follow these out, <b>you must become a Baptist</b>.&rdquo;', 'Rev. Riddle, a neighboring Presbyterian minister, to Alexander &middot; Richardson, <i>Memoirs</i> 1:251', 'The warning') +
  N('Alexander presses the question on his father: will these principles not mean giving up infant baptism? He buys every pro-infant-baptism treatise in Andrew Munro&rsquo;s own bookshop to find out.'))

A(Q('&ldquo;We make our appeal to the law and to the testimony. <b>Whatever is not found therein we must of course abandon.</b>&rdquo;', 'Thomas Campbell to his son, every time &middot; Richardson 1:252', 'The answer') +
  N('The father&rsquo;s answer committed the next generation before anyone knew where it led. Within three years the logic runs its course; that is a later week.'))

A('<section class="slide"><h2>Next week: the rise and fall of the Springfield Presbytery.</h2>'
  '<div class="sub frag">Five years before this was printed, the men of Cane Ridge had already tried to live it.</div>'
  '<aside class=notes>Close. They built something, watched it succeed, and then did something almost without precedent in church history: they wrote a will for it. Chapter 4, October 25.</aside></section>')

A('<section class="slide"><aside class=notes>Black.</aside></section>')

# ---------- ADDENDUM (reference; not part of the telling) ----------
A(C('Addendum', 'Reference material; not part of the telling.'))

# parked from the conscience section (after "It is 'I must.'")
A('<section class="slide breath"><h2 style="max-width:none">Captive to the Word of God.</h2>'
  '<div class=litany style="align-items:center">'
  '<div class="no frag">Not to the pope&rsquo;s reading of it.</div>'
  '<div class="no frag">Not to a council&rsquo;s.</div>'
  '<div class="no frag">Not even to his own.</div>'
  '<div class="no frag">Not to what he thinks it says.</div>'
  '<div class="no frag" style="color:var(--gold)">To the Word of God itself.</div>'
  '</div>'
  '<aside class=notes>Five clicks; slow down on &ldquo;not even to his own.&rdquo; The proof is the first clause of the sentence: &ldquo;Unless I am convinced by the testimony of the Scriptures or by clear reason.&rdquo; He can still be corrected by the Word, so he is not treating his own reading as the Word. What binds him is the Word itself, and his conscience is where he answers to God for how faithfully he reads it. That is why no council can do it for him: an obligation cannot be handed to someone else.</aside></section>')

A('<section class="slide"><div class=eyebrow>What every one of them had in common</div>'
  '<h2>Every one had a sword behind it.</h2>'
  '<div class=litany>'
  '<div class="no frag">Constantine &middot; Theodosius &middot; Marcian &middot; Zeno &middot; the papal legates</div>'
  '<div class="no frag">Charles V &middot; the council of Zurich &middot; Philip of Hesse &middot; Parliament &middot; William and Mary</div>'
  '<div class="no frag">the patrons &middot; the burgess oath &middot; <b>the magistrate</b></div>'
  '</div>'
  '<aside class=notes>Three clicks, back across the egg: who stood behind each instrument. Emperors convened Nicaea (Constantine), Constantinople (Theodosius I), Ephesus (Theodosius II) and Chalcedon (Marcian), and issued the Henotikon (Zeno); legates carried Rome&rsquo;s bull in 1054; Charles V issued the Edict of Worms; Zurich&rsquo;s council ruled and drowned; Philip of Hesse called Marburg; Parliament imposed Westminster; the crown settled 1690; Parliament&rsquo;s Patronage Act made the Secession; a civic oath made the Burgher split; and the last split was over whether the magistrate may enforce religion at all.<br>'
  '&rarr; Back to the egg for a moment: every instrument on it could be enforced. Luther lived under the same swords: Charles V at Worms, Philip of Hesse calling Marburg. Campbell did not, which is why he could take Worms further.</aside></section>')

A(Q('&ldquo;What dreary effects of those accursed divisions are to be seen, even in this highly favored country, <b>where the sword of the civil magistrate has not as yet learned to serve at the altar</b>.&rdquo;', DA, 'The Address &middot; why 1809, why here') +
  N('From the Evils of Division paragraph, just before &ldquo;congregations broken to pieces.&rdquo; The Address says it outright later: &ldquo;A country happily exempted from the baneful influence of a civil establishment of any peculiar form of Christianity.&rdquo;',
    'The First Amendment was eighteen years old; Pennsylvania had never had an established church. For the first time in the story, nobody could enforce a creed. So unity could not be imposed here. It would have to be found.',
    'A few decades after one Declaration of Independence, another.'))

A(Q('&ldquo;That this Society <b>by no means considers itself a Church</b>, nor does at all assume to itself the powers peculiar to such a society&hellip; but merely as voluntary advocates for Church reformation&hellip;&rdquo;', DA, 'Resolution IV') +
  N('The one resolution to keep: voluntary advocates for reform, not a new church.'))

A('<section class="slide"><div class=eyebrow>The reception</div>'
  '<div class=litany>'
  '<div class="no frag">October 1810 &middot; the Synod of Pittsburgh refuses Christian and ministerial communion. <b>Nobody joins.</b></div>'
  '</div>' +
  N('Candor beat, one click. A unity plea addressed to every party and joined, in the event, by almost no one; the synod&rsquo;s refusal is Week 5&rsquo;s opening.', '&rarr; And the movement it started? We know what happened next.'))

def pickL(marker):
    hits = [x for x in L if marker in x]
    assert len(hits) == 1, (marker, len(hits))
    return hits[0]

def spanL(first, last):
    i = [k for k, x in enumerate(L) if first in x]; j = [k for k, x in enumerate(L) if last in x]
    assert len(i) == 1 and len(j) == 1 and i[0] <= j[0], (first, last, i, j)
    return L[i[0]:j[0] + 1]

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
S += spanL('>Christ alone</h2>', '<div class=eyebrow>The answer</div>')

A(BLACK)

# ---------- IDEAS ----------
DISCUSS = pick('&#9670; for discussion', 0)
A(DISCUSS)
IDEAS = [
    (G('Only Christ', 'can make us one.'),
     'The Preamble: we cannot &ldquo;reasonably expect to find it anywhere but in Christ and his simple word.&rdquo; Every instrument on the egg was asked to do a job only Christ can do.'),
    (G('There is nothing wrong with a creed.', 'But a creed cannot make us one.'),
     'Proposition 7: although doctrinal exhibitions doctrinal exhibitions &ldquo;may be highly expedient&rdquo;; they are not to be made terms of communion.ldquo;be highly expedient,doctrinal exhibitions &ldquo;may be highly expedient&rdquo;; they are not to be made terms of communion.rdquo; they are not to be made terms of communion. A creed can teach; it cannot unite.'),
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
A(pickL('Next week: the rise and fall of the Springfield Presbytery'))
A(BLACK)

# ---------- ADDENDUM (as in part one) ----------
_ad = [k for k, x in enumerate(L) if '>Addendum</h2>' in x]
assert len(_ad) == 1
S += L[_ad[0]:]
