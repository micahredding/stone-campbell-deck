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

A(Q('&ldquo;That the Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ and obedience to him in all things&hellip;&rdquo;', DA, 'Proposition 1') +
  N('The class has heard the opening clause twice; now more of it. The sentence goes on: &ldquo;according to the Scriptures, and that manifest the same by their tempers and conduct, and of none else.&rdquo; Ask: do you believe unity is given rather than built? If so, the sects are the innovation.'))

A(Q('&ldquo;That in order to do this, <b>nothing ought to be inculcated upon Christians as articles of faith; nor required of them as terms of communion, but what is expressly taught and enjoined upon them in the word of God</b>&hellip;&rdquo;', DA, 'Proposition 3') +
  N('The method. &ldquo;Expressly.&rdquo; This is the whole wager: strip terms of communion to what Scripture expressly says, and Christians will find they already agree on enough to live together.'))

A(Q('&ldquo;That although inferences and deductions from Scripture premises, when fairly inferred, may be truly called the doctrine of God&rsquo;s holy word, yet are they <b>not formally binding upon the consciences of Christians farther than they perceive the connection</b>&hellip; Therefore, no such deductions can be made terms of communion&hellip;&rdquo;', DA, 'Proposition 6') +
  N('Conscience again, now as polity. You cannot believe what you do not see, so you cannot be made to. Every council on the egg was an inference made a term of communion.'))

A(Q('&ldquo;That as it is not necessary that persons should have a particular knowledge or distinct apprehension of all Divinely revealed truths in order to entitle them to a place in the Church; <b>neither should they, for this purpose, be required to make a profession more extensive than their knowledge</b>&hellip;&rdquo;', DA, 'Proposition 8') +
  N('The one that answers Chalcedon directly: no term that excludes those who cannot understand it. The rest of the sentence: &ldquo;a profession of their faith in and obedience to him, in all things, according to his word, is all that is absolutely necessary to qualify them for admission into his Church.&rdquo;'))

A(Q('&ldquo;That all that are enabled through grace to make such a profession&hellip; should consider each other as the precious saints of God, should <b>love each other as brethren</b>, children of the same family and Father, temples of the same Spirit, members of the same body&hellip; <span style="color:var(--gold)">Whom God hath thus joined together no man should dare to put asunder.</span>&rdquo;', DA, 'Proposition 9') +
  N('The marriage line: recognition is not optional. Ask: who are we not treating as brethren, and on what term?'))

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
  '<h2 style="max-width:none">We speak&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;where the Bible speaks,</h2>'
  '<h2 style="max-width:none;margin-top:3vmin">and we are silent&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;where the Bible is silent.</h2>'
  '<h2 style="max-width:none;margin-top:5vmin">No creed&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;but Christ.</h2>'
  '<aside class=notes>Three clicks. Let the room finish each one.<br>'
  '&bull; The first is Thomas Campbell&rsquo;s own, from the meeting in 1809 that led to the Declaration and Address: &ldquo;Where the Scriptures speak, we speak; and where the Scriptures are silent, we are silent&rdquo; (Richardson, <i>Memoirs</i> 1:236).<br>'
  '&bull; The second also comes as &ldquo;No creed but the Bible.&rdquo; Accept either. Tonight is about the first form: Christ alone.</aside></section>')

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
  '<aside class=notes>Five clicks, about three minutes: last week in five pictures. The egg (325 to 1806, every instrument offered for unity left another division); Worms (Anton von Werner, 1877); Marburg (August Noack, 1867&ndash;69); the drowning (Jan Luyken, <i>Martyrs Mirror</i>, 1685); Thomas Campbell.</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3, part two</div>'
  '<h1>The Declaration<br>and Address</h1><div class=table-line></div>'
  '<div class=sub>The answer</div>'
  '<aside class=notes>Title up. &rarr; &ldquo;Last week we ended on a question. Tonight, Campbell&rsquo;s answer, and what it asks of us.&rdquo;</aside></section>')

A(pick('class="litany ideasum"').replace('<div class=eyebrow>Ideas</div>', '<div class=eyebrow>Last week&rsquo;s ideas</div>')
  .replace('All seven at once, for the room to see together before the discussion.',
           'Last week&rsquo;s seven ideas, all at once. Read them, or let the room read them; do not re-teach.'))


# ---------- THE ANSWER ----------
# 1. Christ diversifies us; only Christ can unite us.
A('<section class="slide breath"><div class=eyebrow>Last week</div>'
  '<h2 style="max-width:none">Conscience is an exercise of<br><span style="color:var(--gold)">the priesthood of all believers.</span></h2>'
  '<aside class=notes>Last week&rsquo;s fifth idea, the starting point tonight. In conscience each believer stands before God with no one in between, which is what a priest does. Luther, 1520: &ldquo;we are all consecrated priests through baptism.&rdquo; The Catechism, &sect;1546: &ldquo;The whole community of believers is, as such, priestly.&rdquo;</aside></section>')

A(Q('&ldquo;&hellip;every man must be allowed to judge for himself, as every man must bear his own judgment&mdash;<b>must give account of himself to God</b>.&rdquo;', DA, 'So conscience answers to Christ') +
  N('The Address, right after &ldquo;no man can judge for his brother,&rdquo; echoing Romans 14:12: &ldquo;every one of us shall give account of himself to God.&rdquo; Romans 14:4 is the same chapter: &ldquo;Who art thou that judgest another man&rsquo;s servant? to his own master he standeth or falleth.&rdquo;',
    '&rarr; If conscience is where I answer to Christ, then conscience is about Christ.'))

A('<section class="slide breath"><div class="litany bigl" style="align-items:center">'
  '<div class="no frag">Not to the pope.</div>'
  '<div class="no frag">Not to a council.</div>'
  '<div class="no frag">Not to me.</div>'
  '<div class="no frag" style="color:var(--gold)">To Christ.</div>'
  '</div>'
  '<aside class=notes>Four clicks. Whom does your conscience answer to?</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Christ makes us <span style="color:var(--gold)">different.</span></h2>'
  '<div class="sub" style="max-width:none">Each of us answers to him, and each of us hears him imperfectly.</div>'
  '<aside class=notes>The careful version: our differences come from each of us answering to Christ for ourselves, through finite understanding. Not every difference is Christ&rsquo;s doing; some are our errors. But the variety is what you get when Christ, not a council, is the one we answer to.</aside></section>')


A('<section class="slide"><h2 style="max-width:none">How can Christians have unity,</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">if Christ, working through us,<br>makes us so different?</h2>'
  '<aside class=notes>One click. The question we stopped on last week, now in its sharpest form. If the source of our differences is Christ himself, no instrument can remove them: not a creed, not a council, not a sword. Pause.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">There can only be one answer.</h2>'
  '<h2 class=frag style="font-size:clamp(80px,22vmin,280px);line-height:1;max-width:none;color:var(--gold);margin-top:3vmin">Christ alone</h2>'
  '<aside class=notes>One click. Say the line, let it sit, then click. Then the Preamble says it in his words.</aside></section>')

A(pickL('Christ and his simple word</b>'))

# Not another list; we will understand differently; that cannot be a boundary
A('<section class="slide breath"><h2 style="max-width:none">We will not be united by <span style="color:var(--gold)">another list.</span></h2>'
  '<div class=sub style="max-width:none">Not of propositions, not of doctrines, not of opinions.</div>'
  '<aside class=notes>Christ alone means: not Christ plus a better confession. Campbell will not offer one, not even his own.</aside></section>')

A(Q('&ldquo;And here we would ask: Have all or any of those human compilations been able to prevent divisions, to heal breaches, or to <b>produce and maintain unity of sentiment</b> even among those who have most firmly and solemnly embraced them?&rdquo;', DA, 'The record') +
  N('From the Address. The egg in one sentence: every confession on it was signed, and every one split.'))

A(Q('&ldquo;Let none imagine that the subjoined propositions are at all intended as <b>an overture toward a new creed</b> or standard for the Church, or as in any wise designed to be made a term of communion; nothing can be further from our intention.&rdquo;', DA, 'Not even his own') +
  N('Just before the thirteen propositions. He refuses to let his own list become the next one.'))

A('<section class="slide breath"><h2 style="max-width:none">We will understand <span style="color:var(--gold)">differently.</span></h2>'
  '<aside class=notes>Not a failure to be fixed: it follows from each of us answering to Christ.</aside></section>')

A(Q('&ldquo;&hellip;it appears highly questionable whether such a thing can at all be secured, by any expedient whatsoever, especially if we consider that it necessarily presupposes in so far <b>a unity or sameness of understanding</b>.&rdquo;', DA, 'One mind would need one understanding') +
  N('From the Address, on &ldquo;unity of sentiment.&rdquo; Agreement on every point would require us all to understand alike, and no expedient can produce that.'))

A(Q('&ldquo;&hellip;nor, indeed, is there anything either in Scripture or the nature of things that should induce us to expect <b>an entire unity of sentiment in the present imperfect state</b>.&rdquo;', DA, 'Campbell expected it') +
  N('From the Address. He does not expect us to agree on everything in this life.'))

A(Q('&ldquo;Nor can we conceive what desirable purpose such a unity of sentiment would serve, except to render useless some of those gracious, self-denying, and compassionate precepts of <b>mutual sympathy and forbearance</b> which the word of God enjoins upon his people.&rdquo;', DA, 'And would not want it') +
  N('The next sentence. He does not think it would be good if we did agree on everything: a church with no differences would have no use for forbearance. Difference is where love has work to do.'))

A('<section class="slide breath"><h2 style="max-width:none">So difference of understanding<br><span style="color:var(--gold)">cannot be a boundary of unity.</span></h2>'
  '<aside class=notes>If we will inevitably understand differently, then a boundary drawn at understanding will divide the church forever. Campbell draws it in two propositions.</aside></section>')

A('<section class="slide breath"><div class="litany bigl" style="align-items:center">'
  '<div class="no frag" style="margin-bottom:2.4vmin">We cannot compel anyone<br>farther than they understand.</div>'
  '<div class="no frag" style="color:var(--gold)">We cannot compel anyone<br>farther than they are required to understand.</div>'
  '</div>'
  '<aside class=notes>Two clicks. The first is Proposition 6: an inference binds a conscience only as far as it sees the connection. The second is Proposition 8: no one need understand everything to belong, so no one may be required to profess more than they know.</aside></section>')

A(pickL('>Proposition 6<'))
A(pickL('>Proposition 8<'))

# 2. Christ already unites us in the church.
A('<section class="slide breath"><h2 style="max-width:none">Christ <span style="color:var(--gold)">already</span> unites us.</h2>'
  '<aside class=notes>Christ alone is the basis of unity because in Christ the church is already one. In the church, the unity is already there. We do not build it; we see it, or we fail to.</aside></section>')

A(pickL('>Proposition 1<'))

A(Q('&ldquo;For by one Spirit are we all baptized into one body, whether we be Jews or Gentiles, whether we be bond or free; and have been all made to drink into one Spirit.&rdquo;', '1 Corinthians 12:13', 'Already') +
  N('Paul: &ldquo;are we all baptized,&rdquo; past tense; the one body is a fact before it is a task.'))

A(Q('&ldquo;&hellip;leaning upon their Beloved, and embracing each other in him, <b>holding fast the unity of the spirit</b> in the bond of peace.&rdquo;', DA, 'Holding fast') +
  N('The Address. &ldquo;Holding fast&rdquo; the unity, not making it. Ephesians 4:3 says the same: &ldquo;keep the unity of the Spirit.&rdquo; You can only keep what you already have.'))

A('<section class="slide breath"><h2 style="max-width:none">Do we <span style="color:var(--gold)">recognize</span> it?</h2>'
  '<aside class=notes>Ask it and let it hang. The church is already one; do we see it? Claim three answers: recognizing it is our visible unity.</aside></section>')

# 3. Christ is the basis of our visible unity.
A('<section class="slide breath"><h2 style="max-width:none">Christ is the basis of our <span style="color:var(--gold)">visible</span> unity.</h2>'
  '<aside class=notes>The unity is real before we see it; it becomes visible when we receive each other: at the table, in the pulpit, in the name &ldquo;brother.&rdquo;</aside></section>')

A(Q('&ldquo;Wherefore <b>receive ye one another, as Christ also received us</b> to the glory of God.&rdquo;', 'Romans 15:7', 'Receive one another') +
  N('Romans 14&ndash;15 is the passage on receiving those who differ over days and food: &ldquo;Him that is weak in the faith receive ye, but not to doubtful disputations&rdquo; (14:1).'))

A('<section class="slide breath"><h2 style="max-width:none">I receive you<br><span style="color:var(--gold)">because Christ received you.</span></h2>'
  '<aside class=notes>What we recognize in a brother is Christ&rsquo;s work. So the visible unity rests on the same ground as the real one. Put anything else there, and we are receiving on some ground other than Christ.</aside></section>')

A(Q('&ldquo;This gracious unity and unanimity in Jesus would afford <b>the best external evidence of their union with him</b>, and of their conjoint interest in the Father&rsquo;s love.&rdquo;', DA, 'What the world sees') +
  N('From the Address. Visible unity is the evidence of an invisible union. What the world is meant to see is Christ.'))

A(Q('&ldquo;That they all may be one&hellip; <b>that the world may believe</b> that thou hast sent me.&rdquo;', 'John 17:21', 'The prayer') +
  N('The prayer the Address echoes: a prayer, not a command, and for the sake of the world&rsquo;s belief.'))

A(pickL('>Proposition 9<'))

# 4. Christ is the basis of unanimity.
A('<section class="slide breath"><h2 style="max-width:none">Christ is the basis of <span style="color:var(--gold)">unanimity.</span></h2>'
  '<aside class=notes>Claim four. We are different now; Christ leads us toward one mind over time. The question is how.</aside></section>')

A(Q('&ldquo;In so far, then, as this <b>holy unity and unanimity in faith and love</b> is attained, just in the same degree is the glory of God and the happiness of men promoted and secured.&rdquo;', DA, 'Unanimity matters') +
  N('Do not let anyone hear tonight as &ldquo;doctrine does not matter.&rdquo; Campbell wants agreement: unanimity is good, and the more the better. The question is only how it is reached.'))

A(Q('&ldquo;It is not the voice of the multitude, but <b>the voice of truth</b>, that has power with the conscience; that can produce rational conviction and acceptable obedience.&rdquo;', DA, 'Not by decree') +
  N('From the Address, on a General Council. Fiat cannot compel the conscience, and must not try. A vote, a council, a decree: none of them reaches the place where belief happens. &ldquo;Rational conviction&rdquo; and &ldquo;acceptable obedience&rdquo;: only truth produces those.'))

A('<section class="slide"><div class=eyebrow>How Christ leads us into truth</div>'
  '<div class="litany tbl" style="text-align:left;gap:2.2vmin;margin-top:1.4vmin">'
  '<div class="no frag"><b style="color:var(--gold)">The Spirit.</b> &ldquo;&hellip;the Holy Spirit for our teacher and guide, to lead us into all truth&hellip;&rdquo;</div>'
  '<div class="no frag"><b style="color:var(--gold)">Scripture.</b> &ldquo;&hellip;to form their judgment by the Divine word itself, and not by any human explication of it&hellip;&rdquo;</div>'
  '<div class="no frag"><b style="color:var(--gold)">Reason.</b> &ldquo;We pretend not, therefore, to divest ourselves of reason&hellip;&rdquo;</div>'
  '</div>'
  '<div class="sub frag punch" style="max-width:none;margin-top:2.6vmin">All three speak to the conscience.</div>'
  '<aside class=notes>Four clicks, all from the Declaration and Address: the Preamble (echoing John 16:13, &ldquo;he will guide you into all truth&rdquo;); the Address&rsquo;s appeal to those who form their judgment by the word &ldquo;humbly relying upon and looking for the promised assistance of Divine teaching&rdquo;; and the Address on reason, which goes on: &ldquo;nor yet, of any of its proper and legitimate operations upon Divinely revealed truths.&rdquo;<br>'
  '&rarr; So unanimity is reached the way Christ allows: brothers reasoning together, the Spirit working on hearts, Scripture read and shared and argued over. Never by decree.</aside></section>')

# 5. Christ and his word, not our interpretations.
A('<section class="slide breath"><h2 style="max-width:none">Christ and his word,<br><span style="color:var(--gold)">not our <i>interpretations</i> of his word.</span></h2>'
  '<aside class=notes>Claim five. Last week&rsquo;s sixth idea, now as the ground of unity.</aside></section>')

A(Q('&ldquo;With you all we desire to unite in the bonds of an entire Christian unity&mdash;<b>Christ alone being the head, the center, his word the rule</b>&hellip;&rdquo;', DA, 'The Address') +
  N('The Address. When Campbell says &ldquo;Christ and his word,&rdquo; listen for what he does not say.'))

A('<section class="slide breath"><div class="litany bigl" style="align-items:center">'
  '<div class="no frag">Not Christ and <i>our understanding</i> of Christ.</div>'
  '<div class="no frag">Not Scripture and <i>our interpretation</i> of Scripture.</div>'
  '<div class="no frag" style="color:var(--gold)">Christ, and Scripture itself.</div>'
  '</div>'
  '<aside class=notes>Three clicks. Last week&rsquo;s sixth idea, now as the ground of unity. We can gather around Christ and Scripture without making our readings of Scripture the test of fellowship.<br>'
  'The objection: no one reads Scripture without interpreting it. True, and Campbell knows it. His line is not between reading and not reading; it is between what I hold and what I require of you. Next, in his words.</aside></section>')

A(Q('&ldquo;We would then no longer <b>exalt our own opinions and inferences to an equality with express revelation</b>, by condemning and rejecting our brother for differing with us in those things.&rdquo;', DA, 'Hold it. Do not require it.') +
  N('From the Address. The fault is not having opinions and inferences; it is raising them to the level of Scripture and then rejecting a brother over them.',
    'Proposition 3: nothing &ldquo;required of them as terms of communion, but what is expressly taught and enjoined upon them in the word of God.&rdquo;',
    'Proposition 6, from claim one: deductions &ldquo;do properly belong to the after and progressive edification of the Church.&rdquo;',
    '&rarr; Then say it plainly.'))

A('<section class="slide breath"><h2 style="max-width:none">Keep your reading.<br><span style="color:var(--gold)">Do not make it your brother&rsquo;s test.</span></h2>'
  '<aside class=notes>The whole of claim five in a sentence. Then the clearest example: a creed.</aside></section>')

S += spanL('>There is nothing wrong with a creed.</h2>', '>Proposition 7<')

# And yes, this is difficult.
A('<section class="slide breath"><h2 style="max-width:none">And yes, this is <span style="color:var(--gold)">difficult.</span></h2>'
  '<div class="sub frag" style="max-width:none">That is how community works.</div>'
  '<div class="sub frag punch">It is especially how Christian community works.</div>'
  '<aside class=notes>Two clicks. Say it plainly: it would be easier to sign a paper. Living with brothers who read the same Bible and see differently takes patience, and Campbell says so.</aside></section>')

A(Q('&ldquo;Ought they not, therefore, to bear with each other&mdash;&lsquo;to preserve the unity of the Spirit in the bond of peace; <b>forbearing one with another in love</b>?&rsquo;&rdquo;', DA, 'Forbearance') +
  N('From the Address, quoting Ephesians 4:2&ndash;3. The word he keeps returning to. Forbearance is not indifference: you only bear with what you actually disagree with.'))

A('<section class="slide breath"><h2 style="max-width:none">Different is not <span style="color:var(--gold)">divided.</span></h2>'
  '<aside class=notes>The conclusion of the argument. Forbearance is how different stays undivided. Division is something else: it is what we do when we will not bear the difference. Last week: &ldquo;a horrid evil.&rdquo;</aside></section>')

# Today: love, indifference, or new lines?
A('<section class="slide"><div class=eyebrow>Today</div>'
  '<h2 style="max-width:none">We have more visible unity than they did in 1809.</h2>'
  '<div class="litany bigl" style="margin-top:2.4vmin">'
  '<div class="no frag">Is it because we have extended love?</div>'
  '<div class="no frag">Or because we have stopped caring?</div>'
  '<div class="no frag" style="color:var(--gold)">Or have we just started dividing over different things?</div>'
  '</div>'
  '<aside class=notes>Three clicks; take answers after each.<br>'
  '&bull; More unity: in 1807 Thomas Campbell himself was charged by his presbytery for giving the Supper to Presbyterians outside the Seceders; suspended in February 1808, then rebuked and admonished by the synod that May. Since then: the World Council of Churches (1948); Vatican II&rsquo;s decree on ecumenism (1964), which accepts baptized Protestants as brothers; Lutheran&ndash;Catholic <i>Joint Declaration on Justification</i> (1999); full communion among Lutherans, Presbyterians, Reformed and UCC (1997). Most churches now welcome any baptized believer to the table.<br>'
  '&bull; Stopped caring: denominational loyalty has collapsed; people switch churches over music or childcare. Christian Smith&rsquo;s &ldquo;moralistic therapeutic deism&rdquo; (<i>Soul Searching</i>, 2005): if nothing much is believed, there is nothing to divide over.<br>'
  '&bull; New lines: the old lines were doctrine and polity; the new ones run through sexuality and politics. The United Methodist Church lost about a quarter of its U.S. congregations, 2019&ndash;2023; the Anglican Church in North America formed in 2009. Many congregations now sort by party more than by creed.<br>'
  '&rarr; Campbell would not accept the second answer: forbearance only means something if you care.</aside></section>')

A(Q('&ldquo;&hellip;manifesting to each other their <b>mutual charity and zeal for the truth</b>.&rdquo;', DA, 'Campbell wanted both') +
  N('From the Address. Charity without zeal is indifference; zeal without charity is the egg. Campbell asks for both at once.'))

A(Q('&ldquo;&hellip;we intend to go just as far as it will suffer us, but <b>not one hair-breadth further</b>&hellip;&rdquo;', DA, 'Charged with indifference') +
  N('The charge in his day was &ldquo;Latitudinarianism&rdquo;: that unity this broad means nothing matters. His answer, in the Address: &ldquo;If this be Latitudinarianism, it must be a good thing&hellip; for we are told, &lsquo;the commandment is exceeding broad;&rsquo; and we intend to go just as far as it will suffer us, but not one hair-breadth further.&rdquo; That is not indifference; it is a fence drawn exactly where Scripture draws it.'))

# The Churches of Christ, then our table
S += spanL('<div class=eyebrow>The Churches of Christ</div>', '>No. It means he was right.</h2>')
A(pickL('<div class=eyebrow>Our table</div>').replace('<div class="sub frag">&ldquo;&hellip;a profession more extensive than their knowledge.&rdquo;</div>', ''))
A(Q('&ldquo;&hellip;neither should they&hellip; be required to make <b>a profession more extensive than their knowledge</b>&hellip;&rdquo;', 'Proposition 8', 'The measure', 'slide room') +
  N('Hold their list against this. Which of these is a profession more extensive than their knowledge?'))

A(BLACK)

# ---------- IDEAS ----------
DISCUSS = pick('&#9670; for discussion', 0)
A(DISCUSS)
IDEAS = [
    (G('Christ diversifies us;', 'only Christ can unite us.'),
     'Each of us answers to Christ for himself (&ldquo;must give account of himself to God&rdquo;), so we will differ. Campbell expected no &ldquo;entire unity of sentiment in the present imperfect state.&rdquo; No instrument can remove differences that come from Christ. Only Christ can unite us: &ldquo;Christ and his simple word.&rdquo;'),
    (G('Christ already', 'unites us.'),
     'Proposition 1: the church is &ldquo;essentially, intentionally, and constitutionally one.&rdquo; We do not build it; we hold it fast (&ldquo;holding fast the unity of the spirit&rdquo;), or we fail to see it.'),
    (G('Christ is the basis of', 'our visible unity.'),
     'Our recognition of each other is the visible unity, and what we recognize is Christ&rsquo;s work. Proposition 8: a profession of faith in Christ is &ldquo;all that is absolutely necessary&rdquo;; Proposition 9: &ldquo;Whom God hath thus joined together no man should dare to put asunder.&rdquo;'),
    (G('Christ is the basis of', 'unanimity.'),
     'Unanimity is good: &ldquo;holy unity and unanimity in faith and love.&rdquo; But it comes the way Christ allows, by the Spirit, Scripture and reason, never by decree: &ldquo;It is not the voice of the multitude, but the voice of truth, that has power with the conscience.&rdquo;'),
    (G('Christ and his word,', 'not our <i>interpretations</i> of his word.'),
     '&ldquo;Christ alone being the head, the center, his word the rule.&rdquo; Hold your reading; do not require it. Proposition 6: inferences are &ldquo;not formally binding upon the consciences of Christians farther than they perceive the connection.&rdquo;'),
]
for k, (h, n) in enumerate(IDEAS, 1):
    A('<section class="slide idea room"><div class="eyebrow quiet">Idea %d of %d</div><h2>%s</h2><aside class=notes>%s</aside></section>'
      % (k, len(IDEAS), h, n))
plain = lambda h: re.sub(r'<span style="color:var\(--gold\)">(.*?)</span>', r'\1', h)
A('<section class="slide room"><div class=eyebrow>Ideas</div>'
  '<div class="litany ideasum" style="text-align:left;gap:1.2vmin;margin-top:2.6vmin">'
  + ''.join('<div class=no><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (k, plain(h)) for k, (h, _) in enumerate(IDEAS, 1)) +
  '</div><aside class=notes>All five at once, before the discussion.</aside></section>')
A(DISCUSS)
A(pick('stone-campbell.micahredding.com'))
A(pickL('Next week: the rise and fall of the Springfield Presbytery'))
A(BLACK)

# ---------- ADDENDUM (as in part one) ----------
_ad = [k for k, x in enumerate(L) if '>Addendum</h2>' in x]
assert len(_ad) == 1
S += L[_ad[0]:]
# the proof-sheets (Alexander and the Baptist warning): for when Alexander and baptism come up
S += spanL('<div class=eyebrow>October 1809</div>', '<div class=eyebrow>The answer</div>')


# =====================================================================================================
# 2026-10-14 RESTRUCTURE, following Micah's transcript for Oct 18 (see week3b-transcript.md).
# Everything above builds the previous order into OLD; the deck is re-assembled from OLD, from part-one
# slides (w3.S), and from new slides. Any OLD content slide not used goes to the addendum.
# =====================================================================================================
import html as _html, sys as _sys
_sys.path.insert(0, os.path.join(_H, '..', 'elements'))
from egg_anim import egg_anim_slide

OLD = S
def _plain(x):
    return re.sub(r'\s+', ' ', _html.unescape(re.sub(r'<[^>]+>', ' ', x.split('<aside')[0]))).strip()
def find(lst, text):
    hits = [x for x in lst if text in _plain(x)]
    if len(hits) > 1: hits = [x for x in hits if _plain(x).startswith(text)] or hits
    if len(hits) > 1: hits = [x for x in hits if _plain(x) == text] or hits
    assert len(hits) == 1, (text, len(hits), [_plain(h)[:60] for h in hits])
    return hits[0]
used = set()
def O(text):                       # a slide from the previous part-two order
    x = find(OLD, text); used.add(id(x)); return x
def P(text):                       # a part-one slide
    return find(w3.S, text)
G = lambda a, b: '%s <span style="color:var(--gold)">%s</span>' % (a, b)
def ST(h, notes, eyebrow='', cls='slide breath'):       # a statement slide
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    h = h.replace(' <span style="color:var(--gold)">', '<br><span style="color:var(--gold)">', 1)
    return '<section class="%s">%s<h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>' % (cls, e, h, notes)

S = []
A = S.append

# ---------- OPENING ----------
A(O('Our Wild Democracy The Story, Promise'))
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3</div>'
  '<h1>Declaration and Address,<br>part two</h1><div class=table-line></div>'
  '<aside class=notes>Title up. &rarr; &ldquo;Last week we set the Declaration and Address in its history. Tonight, Campbell&rsquo;s answer.&rdquo;</aside></section>')
used.add(id(find(OLD, 'Our Wild Democracy · Chapter 3, part two')))

# ---------- 1. RECAP: EVERY INSTRUMENT OF UNITY FAILED ----------
A(egg_anim_slide('Recap. One click per division: creeds and confessions, councils, emperors and magistrates, bishops and popes. '
                 'Every one was offered as an instrument of unity; virtually every one failed, and often created the very division it meant to overcome. '
                 'Last click: the egg breaks.'))
A(P('Why did every instrument fail?'))

# ---------- 2. BECAUSE CONSCIENCE CANNOT BE COMPELLED ----------
A(P('Worms, 1521 Conscience cannot be compelled'))
A(P('Here I stand “…my conscience is captive'))
A(Q('&ldquo;Then Peter and the other apostles answered and said, <b>We ought to obey God rather than men</b>.&rdquo;', 'Acts 5:29', 'Not incidental') +
  N('Not an incidental fact: a deep fact about Christianity itself. The church taught its people that God is obeyed before any human authority, and so every attempt at consensus by committee or council meets someone who says, &ldquo;I cannot.&rdquo;'))
A(ST(G('Every instrument of unity meets someone', 'who says: <i>I cannot.</i>'),
     'Pope, emperor, council, creed: &ldquo;here is where you must come.&rdquo; And someone always stands where Luther stood. That is why they fail, over and over.'))

# ---------- 3. A LONG CHRISTIAN TRADITION ----------
A(P('Luther did not invent this'))
A(P('A human being must always obey'))

# ---------- 4. CLAIMED, BUT NOT EXTENDED ----------
A(P('Rome rejects Luther'))
A(P('Luther rejects Zwingli'))
A(P('Zwingli rejects the An'))
A(P('Washington, Pennsylvania · 1809 Thomas Campbell How dare you put asunder?'))
A(P('Luther claimed conscience for himself. Campbell claimed'))

# ---------- 5. CONSCIENCE IS HOW CHRIST BUILDS THE BODY ----------
A(ST(G('Freedom of conscience is how Christ', 'has put his body together.'),
     'Campbell&rsquo;s move: the inability to compel conscience is not a roadblock on the way to unity. It is a constituent element of the body of Christ, an organizing principle of the church. To thwart it is to undo what Christ has done.'))
A(P('Preamble “…as no man can be judged for his brother'))
A(P('daring usurpation'))
A(P('Luther, a year before Worms'))
A(P('aboriginal Vicar'))
A(O('Last week Conscience is an exercise of the priesthood'))
A(O('So conscience answers to Christ'))
A(O('Not to the pope. Not to a council. Not to me.'))

# ---------- 6. THEN HOW CAN WE BE ONE? ----------
A(O('Christ makes us different'))
A(O('How can Christians have unity,'))
A(O('We will not be united by'))
A(O('We will understand differently'))
A(O('Campbell expected it'))
A(O('And would not want it'))

# ---------- 7. ONLY CHRIST ----------
A('<section class="slide"><h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none">How can<br>Christians<br>be united?</h2>'
  '<aside class=notes>(transcript)</aside></section>')
A(O('There can only be one answer'))
A(O('reasonably expect to find it anywhere but in Christ'))
A(pickL('a job only Christ can do').replace('&rarr; Which is not to say creeds are bad.', '&rarr; Which is not to say confessions are bad.'))
A(O('There is nothing wrong with a creed')
  .replace('There is nothing wrong with a creed.', 'There is nothing wrong with a confession.')
  .replace('But a creed cannot make us one.', 'But a confession cannot make us one.')
  .replace('Two clicks. Not anti-creed: Nicaea is true, and the room says it. The fault on the egg was never the creed; it was the job the creed was given.',
           'Two clicks. Campbell is not against confessions. For teaching, the fuller the better (Proposition 7, next). The fault on the egg was never the confession; it was the job the confession was given: to be the boundary of the body of Christ.'))
A(O('Proposition 7'))

# ---------- 8. CHRIST HAS ALREADY MADE US ONE ----------
A('<section class="slide"><h2 style="font-size:clamp(56px,12vmin,160px);line-height:1.05;max-width:none">So what do we do with this,<br>practically speaking?</h2>'
  '<aside class=notes>(transcript)</aside></section>')
A('<section class="slide breath"><h2 style="font-size:clamp(70px,17vmin,220px);line-height:1;max-width:none">Christ <span style="color:var(--gold)">already</span><br>unites us.</h2>'
  '<aside class=notes>(transcript)</aside></section>')
used.add(id(find(OLD, 'Christ already unites us.')))
A(O('Proposition 1'))
A('<section class="slide breath"><div class=eyebrow>Proposition 1, misread</div><div class="litany bigl" style="align-items:center">'
  '<div class="no frag">Not only the ones with our name on the sign.</div>'
  '<div class="no frag">Not only Rome.</div>'
  '<div class="no frag">Not only Constantinople.</div>'
  '<div class="no frag" style="color:var(--gold)">&ldquo;All those in every place.&rdquo;</div>'
  '</div>'
  '<aside class=notes>Four clicks. In Church of Christ circles the first proposition is sometimes quoted to mean the opposite of what it says: only the congregations with &ldquo;Church of Christ&rdquo; on the sign are the true church. Some Catholic and some Orthodox thinkers say the same of their own communions. Campbell says the opposite: the church on earth consists of Christians in every denomination, sect and division. Christ has made them one; we have not.</aside></section>')
A('<section class="slide breath"><div class=eyebrow>David Bentley Hart</div>'
  '<h2 style="max-width:none;font-size:clamp(52px,11vmin,130px)">&ldquo;The Myth of Schism&rdquo;</h2><div class=table-line style="margin:3vmin auto"></div>'
  '<div class=sub style="max-width:none;font-size:clamp(26px,4.6vmin,56px)">In <i>Ecumenism Today: The Universal Church in the 21st Century</i></div>'
  '<div class=sub style="max-width:none;font-size:clamp(22px,3.8vmin,46px);color:var(--bone-dim);margin-top:1.4vmin">ed. Francesca Aran Murphy and Christopher Asprey &middot; Ashgate, 2008</div>'
  '<aside class=notes>An Eastern Orthodox theologian on the schism of 1054 between the Catholic and Orthodox churches: its history, and how to think about it. Reprinted at clarion-journal.com (2014).</aside></section>')
A(Q('&ldquo;We are divided, we know, but <b>how, when, and by what authority?</b>&rdquo;', 'David Bentley Hart, &ldquo;The Myth of Schism,&rdquo; 2008', 'East and West, after 1054') +
  N('Hart, an Eastern Orthodox theologian, on the schism of 1054. In <i>Ecumenism Today: The Universal Church in the 21st Century</i>, ed. Francesca Aran Murphy and Christopher Asprey (Ashgate, 2008); reprinted at clarion-journal.com (2014).',
    'He shows how porous the wall was for centuries: shared sacraments under the Ottomans and under communist rule, Syrian parishes in America where Catholic and Orthodox belong to &ldquo;one church and one altar.&rdquo; The same paragraph: &ldquo;Can the failure of communion between two patriarchs or bishops&hellip; create a real division of sacramentally united communions from one another?&rdquo;'))
A(Q('&ldquo;&hellip;are we sure that we are? For, if not, then our division is simply sin&hellip; <b>a fiction of the will, and obedience to a lie</b>.&rdquo;', 'David Bentley Hart, &ldquo;The Myth of Schism,&rdquo; 2008', 'Are we divided?') +
  N('The full sentence: &ldquo;This is not a moral question&mdash;how do we dare to remain disunited?&mdash;but a purely canonical one: are we sure that we are? For, if not, then our division is simply sin, a habit of desire and thought that feeds upon nothing but its own perverse passions and immanent logic, a fiction of the will, and obedience to a lie.&rdquo;',
    '&rarr; The principle underneath: Christ makes the church one, and pope, bishop and council have neither the authority nor the ability to divide it. Constitutionally one, as Campbell says.'))

A(ST(G('No sect ever had the authority,', 'or the ability, to divide what Christ has joined.'),
     'Whatever our sects and sub-sects have done with their divisions and anathemas, they never had the authority or the ability to divide the body Christ made one.'))

# ---------- 9. OUR FIRST DUTY: RECOGNIZE IT ----------
A(O('Do we recognize it?'))
A(Q('&ldquo;For he that eateth and drinketh unworthily, eateth and drinketh damnation to himself, <b>not discerning the Lord&rsquo;s body</b>.&rdquo;', '1 Corinthians 11:29', 'At the table') +
  N('Paul&rsquo;s charge against the Corinthians: at the Supper they did not recognize the body of Christ in their brothers (11:17&ndash;34, the rich eating while the poor go hungry). That failure turns communion into judgment.'))
A(ST(G('When Campbell gave the Supper to other Presbyterians,', 'he was discerning the body.'),
     'The charge of 1807: he gave communion to Presbyterians outside the Seceders. He was recognizing the body of Christ across the lines his own synod drew.'))
A(O('Holding fast'))
A(O('Proposition 9'))
A(O('Receive one another'))
A(O('I receive you because Christ received you.'))
A(ST(G('Our first duty:', 'recognize what Christ has already done.'),
     'And stop pretending that anything else has taken precedence over Christ&rsquo;s own declaration and work.'))

# ---------- 10. THE WORD OF GOD, NOT INTERPRETATIONS OF IT ----------
A(O('Christ and his word, not our interpretations of his word.'))
A(P('Worms, 18 April 1521'))
A(O('Captive to the Word of God. Not to the pope'))
A(P('Word of God ≠'))
A(ST(G('Campbell is not trading the Westminster Confession', 'for an agreed reading of the Bible.'),
     'How the supremacy of the Word has often been applied among us: a new legalism, as if Campbell threw out the Confession so we could all agree on one interpretation of the Bible instead. That is not what he says, and not what he can be saying.'))
A(ST(G('If we cannot agree on the Westminster Confession,', 'how much less on all of Scripture?'),
     'Campbell knows this. United on Christ and his word means our commitment to Christ and to his word, not to a particular interpretation of it.'))
A(O('The Address “With you all we desire'))
A(O('Not Christ and our understanding'))
A(O('Hold it. Do not require it.'))
A(O('Keep your reading.'))
A(O('How Christ leads us into truth'))
A(ST(G('We are united not by a shared interpretation,', 'but by a shared commitment to Scripture itself.'),
     'Every week I meet with Christians who understand Scripture differently than I do. We wrestle with it; sometimes we move closer, sometimes farther apart. What unites us is a shared commitment to Scripture, which is part of our shared commitment to Christ: not our interpretation of Scripture, not our interpretation of Christ, but Christ himself.'))

# ---------- LANDING ----------
A(ST(G('Recognize the unity Christ has already made,', 'and strive to act accordingly.'),
     'Where Campbell lands, and where we start.'))
A(BLACK)

# ---------- IDEAS ----------
A(DISCUSS)
IDEAS = [
    (G('Freedom of conscience is how', 'Christ builds his body.'),
     'We cannot compel conscience, and Christ does not ask us to: each believer answers to him as a priest. Campbell: judging for a brother is &ldquo;a daring usurpation of his throne.&rdquo;'),
    (G('Only Christ', 'can unite us.'),
     'If Christ is the reason for our diversity, Christ is the only one who can unite us: &ldquo;anywhere but in Christ and his simple word.&rdquo; Confessions teach; they cannot be the boundary of the body.'),
    (G('Christ has already', 'made us one.'),
     'Proposition 1: &ldquo;essentially, intentionally, and constitutionally one; consisting of all those in every place.&rdquo; Not only us.'),
    (G('Our first duty is', 'to recognize it.'),
     '&ldquo;Not discerning the Lord&rsquo;s body&rdquo; (1 Corinthians 11:29). Campbell at the table with other Presbyterians: recognizing what Christ has joined.'),
    (G('Christ and his word,', 'not our <i>interpretations</i> of his word.'),
     'Luther was captive to the Word of God, not to his reading of it. &ldquo;Christ alone being the head, the center, his word the rule.&rdquo; Keep your reading; do not make it your brother&rsquo;s test.'),
]
for k, (h, n) in enumerate(IDEAS, 1):
    A('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2>%s</h2><aside class=notes>%s</aside></section>' % (k, len(IDEAS), h, n))
A('<section class="slide room"><div class=eyebrow>Ideas</div>'
  '<div class="litany ideasum" style="text-align:left;gap:1.2vmin;margin-top:2.6vmin">'
  + ''.join('<div class=no><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (k, plain(h)) for k, (h, _) in enumerate(IDEAS, 1)) +
  '</div><aside class=notes>All five at once, before the discussion.</aside></section>')
A(DISCUSS)
A(pick('stone-campbell.micahredding.com'))
A(pickL('Next week: the rise and fall of the Springfield Presbytery'))
A(BLACK)

# ---------- ADDENDUM: the old addendum, then every earlier slide this telling does not use ----------
_skip = ('Quiz', 'Idea ', 'Ideas 1.', '◆ for discussion', 'Online stone-campbell', 'Next week:')
_ai = [k for k, x in enumerate(OLD) if '>Addendum</h2>' in x][0]
for x in OLD[_ai:]:
    if id(x) not in used: A(x)
for x in OLD[:_ai]:
    if id(x) in used or not _plain(x) or _plain(x).startswith(_skip): continue
    A(x)

# ---------- each idea, where it first arrives in the talk, carries the label it has at the end ----------
for _txt, _k in (('Freedom of conscience is how Christ has put his body together.', 1),
                 ('There can only be one answer. Christ alone', 2),
                 ('Christ already unites us.', 3),
                 ('Our first duty: recognize what Christ has already done.', 4),
                 ('Christ and his word, not our interpretations of his word.', 5)):
    _i = [i for i, x in enumerate(S[:66]) if _plain(x) == _txt]
    assert len(_i) == 1, (_txt, _i)
    S[_i[0]] = re.sub(r'^(<section[^>]*>)(?:<div class=eyebrow>[^<]*</div>)?', lambda m: m.group(1) + '<div class=eyebrow>Idea %d of 5</div>' % _k, S[_i[0]], count=1)

# ---------- presenter notes = the transcript (week3b-transcript.md, one section per slide) ----------
_tx = open(os.path.join(_H, '..', '..', '..', 'week3b-transcript.md'), encoding='utf-8').read()
_sec = re.split(r'^\*\*Slide (\d+) · .*?\*\*\s*$', _tx, flags=re.M)
_NOTES = {}
for _k in range(1, len(_sec) - 1, 2):
    body = re.split(r'^(?:##|---)', _sec[_k + 1], flags=re.M)[0].strip()
    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    def _esc(p):
        p = _html.escape(p.lstrip('> ').strip(), quote=False)
        p = re.sub(r'"(\S)', r'&ldquo;\1', p); p = p.replace('"', '&rdquo;').replace("'", '&rsquo;')
        return p
    _NOTES[int(_sec[_k])] = '<br><br>'.join(('<i>%s</i>' % _esc(p)) if p.startswith('>') else _esc(p) for p in paras)
assert sorted(_NOTES) == list(range(1, len(_NOTES) + 1)), sorted(_NOTES)
for _n, _t in _NOTES.items():
    x = S[_n - 1]
    assert '<aside class=notes>' in x, _n
    S[_n - 1] = re.sub(r'<aside class=notes>.*?</aside>', lambda m: '<aside class=notes>%s</aside>' % _t, x, count=1, flags=re.S)
