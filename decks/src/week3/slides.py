# -*- coding: utf-8 -*-
# Week 3 deck content — The Declaration & Address.
# The Christendom sequence (325–1806, the egg) is a reusable element: decks/src/elements/christendom.py.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import os
_HERE = os.path.dirname(os.path.abspath(__file__))
import re, math

def C(name, note=''):   # chapter card
    return ('<section class="slide breath sect"><h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (name, note))

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'elements'))
from christendom import christendom_slides, PATDEFS, CHRISTENDOM_CSS

def Q(quote, cite='', eyebrow='', cls='slide', sub=''):   # a quotation alone
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    c = '<div class=cite>%s</div>' % cite if cite else ''
    n = len(re.sub(r'<[^>]+>|&[a-z]+;', 'x', quote))
    size = ' xlong' if n > 260 else ' long' if n > 150 else ''
    bg = '<div class=bg><div class="bgimg lutherbg"></div></div>' if 'dimbg' in cls else ''
    return '<section class="%s">%s%s<p class="bigquote%s"><span class=q>%s</span></p>%s%s' % (cls, bg, e, size, quote, sub, c)
def N(*bul):
    return '<aside class=notes>' + '<br>'.join('&bull; ' + x for x in bul) + '</aside></section>'
DA = 'Declaration and Address, 1809'

S = []
A = S.append
_D = __file__.rsplit('/', 1)[0]

# ---------- CLASS TITLE (as in the Chapter 2 deck) ----------
A('<section class="slide" style="padding-bottom:10vmin"><div class="eyebrow quiet" style="font-size:clamp(16px,3vmin,36px)">Otter Creek &middot; Fall 2026</div>'
  '<h1 style="font-size:min(19vmin,11.5vw);line-height:1.02;max-width:none">Our Wild<br>Democracy</h1>'
  '<p class=sub style="font-size:min(5vmin,3.6vw);max-width:none;margin-top:2vmin">The Story, Promise, and Future<br>of the Churches of Christ</p>'
  '<aside class=notes>The class title, as every week. Then the chapter.</aside></section>')

# ---------- RECAP: Chapter 2 in pictures (images from decks/src/week2) ----------
A('<section class="slide recapslide"><div class="eyebrow quiet">Last week &middot; Thomas Campbell&rsquo;s Heresy Trial</div>'
  '<div class=shots style="gap:3vmin">'
  '<figure class="shot frag" style="--r:-1.5deg"><img src="IMG_TCAMPBELL" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Ireland.</b> Twice he works to unite the Seceders; twice his church courts shut it down.</figcaption></figure>'
  '<figure class="shot frag" style="--r:1.2deg"><img src="IMG_SHIP" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>April 1807.</b> He sails for America.</figcaption></figure>'
  '<figure class="shot frag" style="--r:-1deg"><img src="IMG_MAP" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Western Pennsylvania.</b> Presbyterians who had not received communion in years.</figcaption></figure>'
  '<figure class="shot frag" style="--r:1.8deg"><img src="IMG_TOKEN" alt="" style="width:100%;height:30vh;object-fit:cover;border-radius:.4vmin"><figcaption style="font-family:Spectral,Georgia,serif;font-variant:normal;text-transform:none;letter-spacing:0;font-size:clamp(15px,2.4vmin,28px);line-height:1.35;margin-top:1.2vmin;color:var(--bone)"><b>Conemaugh, August 1807.</b> He opens the table. He is tried and censured for it.</figcaption></figure>'
  '</div>'
  '<div class="sub frag" style="max-width:none;margin-top:3vmin">Put out, he preaches in a grove. That autumn they ask him to write down what they stand for.</div>'
  '<aside class=notes>Five clicks, about two minutes: the story so far in four pictures. Thomas Campbell (portrait); the ship (Robert Salmon, 1809, a ship of the kind, not the <i>Brutus</i>); Howell&rsquo;s 1792 map of Pennsylvania; a Scottish communion token, 1750, the fence at the table. Last week ended on the first sentence of what he wrote: the church of Christ upon earth is essentially, intentionally, and constitutionally one.</aside></section>')

# ---------- TITLE ----------
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 3</div>'
  '<h1>The Declaration<br>and Address</h1><div class=table-line></div>'
  '<div class=sub>Washington, Pennsylvania &middot; 1809</div>'
  '<aside class=notes>Title up. &rarr; &ldquo;Last week we ended on one sentence: the church of Christ upon earth is essentially, intentionally, and constitutionally one. Today: why anyone would need to write it.&rdquo; Then the Design of Religion. The hour: Design 4 &middot; Evils and proposition 10 6 &middot; Christendom 10 &middot; Preamble 3 &middot; conscience and the brother 10 (break here if short: &ldquo;Next week &middot; The answer&rdquo;) &middot; the solution 3 &middot; Propositions 10 &middot; our table 8 &middot; reception and proof-sheets 5.</aside></section>')

# ---------- 1 THE DESIGN OF RELIGION ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Design of Religion</h2><div class=table-line></div>'
  '<aside class=notes>Start here. The Address is the long part, to &ldquo;all that love our Lord Jesus Christ, in sincerity, throughout all the Churches.&rdquo; Its first paragraph is the premise under everything that follows.</aside></section>')

A(Q('&ldquo;That it is the grand design and native tendency of our holy religion <b>to reconcile and unite men to God, and to each other, in truth and love</b>, to the glory of God, and their own present and eternal good&hellip;&rdquo;', DA, 'The Design of Religion') +
  N('Stop before &ldquo;will not, we presume, be denied.&rdquo; Stand one, asked lightly: is unity what Christianity is <i>for</i>? If yes, every century of division is the religion failing its own purpose.', '&ldquo;In truth and love&rdquo;: both sides, from the first sentence. The motto later is &ldquo;Union in Truth.&rdquo;'))

A(Q('&ldquo;&hellip;the first and foundation truth of our Christianity is <b>union with him</b>, and the very next to it in order, <b>union with each other in him</b>.&rdquo;', DA, 'The Design of Religion') +
  N('The design sentence in its own order: union with him first, union with each other in him next. Unity is not a project beside the faith; it follows from it. That is proposition 1 in a sentence: given, not constructed.', 'Later in the Address, the &ldquo;bewildered Church has, for hundreds of years past, been rending and dividing herself into factions, for Christ&rsquo;s sake, and for the truth&rsquo;s sake.&rdquo; The egg, in his words.'))

A(Q('&ldquo;The nativity of its Divine author was announced from heaven, by a host of angels, with high acclamations of <b>&lsquo;Glory to God in the highest, and on earth peace and good-will toward men.&rsquo;</b>&rdquo;', DA, 'The Design of Religion') +
  N('Back to the first paragraph. The proof he offers is Luke 2: the religion was announced as peace.'))

A(Q('&ldquo;In so far, then, as this holy unity and unanimity in faith and love is attained, <b>just in the same degree</b> is the glory of God and the happiness of men promoted and secured.&rdquo;', DA, 'The Design of Religion') +
  N('&ldquo;Just in the same degree.&rdquo; Unity is not a bonus on top of the religion; it is the measure of it. Then: what does division cost?'))

# ---------- 2 THE EVILS OF DIVISION ----------
A('<section class="slide breath sect"><div class=eyebrow>The Address</div><h2>The Evils of Division</h2><div class=table-line></div>'
  '<aside class=notes>What division costs. Practical, not doctrinal. Build the list one line at a time and let the room map each one onto now.</aside></section>')

A('<section class="slide"><div class=eyebrow>Proposition 10</div>'
  '<h2>&ldquo;Division among the Christians is a horrid evil, fraught with many evils.&rdquo;</h2>'
  '<div class=litany>'
  '<div class="no frag">&ldquo;It is <b>antichristian</b>, as it destroys the visible unity of the body of Christ; as if he were divided against himself&hellip;&rdquo;</div>'
  '<div class="no frag">&ldquo;It is <b>antiscriptural</b>, as being strictly prohibited by his sovereign authority&hellip;&rdquo;</div>'
  '<div class="no frag">&ldquo;It is <b>antinatural</b>, as it excites Christians to contemn, to hate, and oppose one another, who are bound&hellip; to love each other as brethren&hellip;&rdquo;</div>'
  '</div><div class=cite>' + DA + '</div>'
  '<aside class=notes>Three clicks, verbatim. First what division <i>is</i>; the Evils list that follows is what it costs. Against Christ, against Scripture, against nature: a body excommunicating part of itself. Elided from the first: &ldquo;excluding and excommunicating a part of himself.&rdquo; From the second: &ldquo;a direct violation of his express command.&rdquo; Last clause: &ldquo;In a word, it is productive of confusion and of every evil work.&rdquo;<br>'
  '&rarr; Then what it costs.</aside></section>')

A('<section class="slide"><div class=eyebrow>&ldquo;What awful and distressing effects have those sad divisions produced!&rdquo;</div>'
  '<div class=litany>'
  '<div class="no frag">&ldquo;congregations <b>broken to pieces</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;large settlements and tracts of country&hellip; <b>entirely destitute of a Gospel ministry</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;How seldom do many&hellip; enjoy the dispensations of the Lord&rsquo;s Supper, <b>that great ordinance of unity and love</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;the tone of discipline relaxed&hellip; lest their people should leave them, and&hellip; <b>find refuge in the bosom of another party</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;the weak stumbled, the graceless and profane hardened, <b>the mouths of infidels opened</b> to blaspheme religion&rdquo;</div>'
  '</div><div class=cite>' + DA + '</div>'
  '<aside class=notes>Five clicks, all verbatim from the Evils of Division. The Supper line ties to the Table arc of the whole class. The last two land hardest in 2026: members who can leave for the church down the road, and the mouths of infidels.<br>(Dropped: those &ldquo;who live at the door of a preached Gospel, dare not in conscience go to hear it.&rdquo; Restore if useful.)</aside></section>')

A(Q('&ldquo;Say, dear brethren, <b>are not these things so?</b>&rdquo;', DA, 'The Evils of Division') +
  N('His own question, to the room. Let them answer.', '&rarr; Then: it was not for want of trying. Here is fifteen hundred years of trying.'))

# ---------- 4 CHRISTENDOM'S SEARCH FOR UNITY (the egg) ----------
S += christendom_slides()


# ---------- 5 THE PREAMBLE: REST, AND DESPAIR ----------
A('<section class="slide breath sect"><div class=eyebrow>The Declaration</div><h2>Preamble</h2><div class=table-line></div>'
  '<div class=sub>The sentiments of the people of the grove.</div>'
  '<aside class=notes>Summer 1809. The people following Thomas Campbell from farmhouse to maple grove have become something, and they need to say what. The Declaration is the short part, written for them. After the egg: this is what the people of the grove wanted, and why they despaired of getting it the old way.</aside></section>')

A(Q('&ldquo;&hellip;tired and sick of the bitter jarrings and janglings of a party spirit, <b>we would desire to be at rest</b>; and, were it possible, we would also desire to adopt and recommend such measures as would give rest to our brethren throughout all the churches&hellip;&rdquo;', DA, 'Preamble') +
  N('The line everyone remembers. Say it slowly. &ldquo;Rest&rdquo; is the word they chose, not &ldquo;victory.&rdquo;'))

A(Q('&ldquo;This desirable rest, however, <b>we utterly despair</b> either to find for ourselves, or to be able to recommend to our brethren, by continuing amid the diversity and rancor of party contentions, the veering uncertainty and clashings of human opinions&hellip;&rdquo;', DA, 'Preamble') +
  N('Stop here. Do not read the next clause yet.', '&rarr; Before the answer, name the issue underneath all of it. Why can none of those instruments work?'))


# ---------- 6 THE ISSUE: FREEDOM OF CONSCIENCE ----------
A(C('Why did every instrument fail?', 'Card. Fifteen hundred years of creeds, councils and swords, and a document that despairs of the old way. The next slide names the reason underneath.'))

A('<section class="slide bleed" style="padding-bottom:5vmin"><div class=bg><div class="bgimg lutherbg"></div></div>'
  '<div class=credit>Anton von Werner, <i>Luther at the Diet of Worms</i>, 1877 &middot; public domain</div>'
  '<div class=eyebrow>Worms, 1521</div>'
  '<h2 style="font-size:clamp(56px,13vmin,170px);line-height:1.02;max-width:none">Conscience cannot<br>be compelled.</h2>'
  '<aside class=notes>Asked to recant. (&ldquo;Here I stand, I can do no other&rdquo; is the famous form; the earliest printed accounts add it, the transcript does not. Say &ldquo;as the story goes.&rdquo;)<br>&rarr; This is why no instrument on the egg could work: a creed can name who agrees, and a sword can make people say it, but neither can make anyone believe.</aside></section>')

A(Q('&ldquo;&hellip;my conscience is captive to the Word of God. I cannot and will not recant anything, since <b>it is neither safe nor right to go against conscience</b>.&rdquo;', 'Martin Luther at Worms, 18 April 1521', 'Here I stand', 'slide bleed midbleed dimbg') +
  N('The line everyone remembers. Say it slowly. (&ldquo;Here I stand, I can do no other&rdquo; is the famous form; the earliest printed accounts add it, the transcript does not.)', '&rarr; Then what conscience is, and the whole sentence it ends.'))

A('<section class="slide breath"><h2 style="max-width:none">Conscience is not &ldquo;I can do what I want.&rdquo;</h2>'
  '<div class="sub frag punch">It is &ldquo;I must.&rdquo;</div>'
  '<aside class=notes>One click. His word is <i>captive</i>: bound, not free. Conscience here is not a preference but an obligation before God. &ldquo;Neither safe nor right to go against conscience&rdquo;: not safe, because he must answer to God for it.</aside></section>')

A(Q('&ldquo;<b style="font-size:1.18em">Unless I am convinced by the testimony of the Scriptures or by clear reason</b><span style="font-size:.78em">&hellip; I am bound by the Scriptures&hellip; and my conscience is captive to the Word of God. I cannot and will not recant anything, since <b>it is neither safe nor right to go against conscience</b>. May God help me. Amen.</span>&rdquo;', 'Martin Luther at Worms, 18 April 1521', 'Worms, 18 April 1521', 'slide wormsfull bleed midbleed dimbg') +
  N('The whole sentence, two trims on screen: &ldquo;I have quoted,&rdquo; and the parenthesis &ldquo;(for I do not trust either in the pope or in councils alone, since it is well known that they have often erred and contradicted themselves).&rdquo; Councils have erred: the egg, in his words.', 'Note how it starts: &ldquo;Unless I am convinced.&rdquo; He holds his own reading open to correction. That is the opposite of &ldquo;I can do what I want.&rdquo; (Translations vary; this is the common English form.)'))

A('<section class="slide breath"><h2 style="max-width:none;line-height:1.15;font-size:clamp(48px,9.5vmin,120px)">Word of God<span class=frag style="display:block;color:var(--gold);font-size:1.6em;line-height:1">&ne;</span><span class=frag style="display:block"><i>interpretations</i> of the Word of God</span></h2>'
  '<aside class=notes>Two clicks. What Luther is captive to. Not the pope&rsquo;s reading, not a council&rsquo;s, not even his own: &ldquo;Unless I am convinced by the testimony of the Scriptures or by clear reason.&rdquo; He can be corrected by the Word, so his reading is not the Word. That is what keeps conscience from becoming &ldquo;I can do what I want&rdquo;: it answers to something outside itself.</aside></section>')

A('<section class="slide breath"><div class=eyebrow>Luther did not invent this</div>'
  '<h2 style="max-width:none;font-size:clamp(52px,11vmin,140px);line-height:1.08">Even a mistaken<br>conscience binds.</h2>'
  '<div class=sub style="max-width:none;margin-top:2.6vmin;font-family:\'IM Fell English SC\',Georgia,serif;font-style:normal;letter-spacing:.1em;color:var(--smoke)">Thomas Aquinas, c. 1270 &middot; paraphrased</div>'
  '<aside class=notes>Aquinas, two and a half centuries before Worms, <i>Summa Theologiae</i> I-II q.19 a.5 (&ldquo;whether an erring conscience binds&rdquo;): &ldquo;every will at variance with reason, whether right or erring, is always evil.&rdquo; Even believing in Christ, willed against one&rsquo;s reason, is evil.<br>&rarr; Rome condemned Luther; it never stopped teaching this.<br>(Avoid the Aquinas line about dying excommunicated, <i>Sentences</i> IV d.38: its meaning is disputed.)</aside></section>')

A('<section class="slide breath">'
  '<div class=litany style="gap:5vmin">'
  '<div class="no frag" style="font-size:clamp(40px,8vmin,100px);line-height:1.15">&ldquo;He must not be forced to act contrary to his conscience.&rdquo;<span class=lcite>Vatican II, 1965</span></div>'
  '<div class="no frag" style="font-size:clamp(40px,8vmin,100px);line-height:1.15">&ldquo;A human being must always obey the certain judgment of his conscience.&rdquo;<span class=lcite>Catechism of the Catholic Church, 1992</span></div>'
  '</div>'
  '<aside class=notes>Two clicks. The same teaching, in Rome&rsquo;s own words today.<br>&bull; Vatican II, <i>Dignitatis Humanae</i> &sect;3 (Catechism &sect;1782): &ldquo;No merely human power can either command or prohibit acts of this kind.&rdquo;<br>&bull; Catechism &sect;1790 continues: &ldquo;If he were deliberately to act against it, he would condemn himself.&rdquo;<br>&bull; The honest gap: Gregory XVI, <i>Mirari Vos</i> (1832), called liberty of conscience for everyone &ldquo;that absurd and erroneous proposition.&rdquo; Rome reached Campbell&rsquo;s conclusion in 1965.<br>&rarr; Back to the egg: you can compel conformity; you cannot compel communion.</aside></section>')

A(Q('&ldquo;His conscience is man&rsquo;s most secret core and his sanctuary. <b>There he is alone with God</b>, whose voice echoes in his depths.&rdquo;', '<i>Catechism of the Catholic Church</i> &sect;1776 &middot; quoting Vatican II', 'Why it binds') +
  N('Why it binds: conscience is where a person stands before God with no one in between, and that is what a priest is. Catechism &sect;1546: &ldquo;The whole community of believers is, as such, priestly.&rdquo;', 'Source: <i>Gaudium et Spes</i> &sect;16, which opens: &ldquo;a law which he has not laid upon himself but which he must obey.&rdquo; That is &ldquo;I must.&rdquo;'))

A(Q('&ldquo;Conscience is the aboriginal <b>Vicar of Christ</b>.&rdquo;', 'John Henry Newman, 1875 &middot; quoted in the <i>Catechism of the Catholic Church</i> &sect;1778', 'The Catechism', cls='slide breath') +
  N('Let it sit. &ldquo;Aboriginal&rdquo; means first: before pope or council, Christ&rsquo;s first representative in a person is conscience. And it is in the Catechism.', 'Newman, <i>Letter to the Duke of Norfolk</i> (1875) &sect;5. Same letter: &ldquo;I shall drink&mdash;to the Pope, if you please,&mdash;still, to Conscience first, and to the Pope afterwards.&rdquo;'))

A(Q('&ldquo;&hellip;whoever comes out of the water of baptism can boast that he is already <b>a consecrated priest, bishop, and pope</b>&hellip;&rdquo;', 'Martin Luther, <i>To the Christian Nobility of the German Nation</i>, 1520 &middot; <i>Luther&rsquo;s Works</i> 44', 'Luther, a year before Worms', sub='<div class="sub frag" style="max-width:none">No one can stand before God in your place.<br>So no one can read the Word in your place.</div>') +
  N('One click. A year before Worms: &ldquo;we are all consecrated priests through baptism, as St. Peter says in I Peter 2[:9].&rdquo; No one can stand before God for you.', 'The sentence goes on: &ldquo;although of course it is not seemly that just anybody should exercise such office.&rdquo;'))


A('<section class="slide breath sect"><h2>Priesthood of all believers</h2><div class=table-line></div>'
  '<div class="sub frag">Every believer: the Spirit within, united with Christ, answering to God directly.</div>'
  '<aside class=notes>Card, one click. The ground under Worms: why conscience is an obligation and not a preference. No one can stand before God in your place, so no one can read the Word in your place either. It names what the last slides have shown, Catholic and Luther alike. Then Worms beside Washington, and Marburg: Luther could not grant it to Zwingli.</aside></section>')

A('<section class="slide"><div class=eyebrow>Worms, 1521 &middot; Washington, Pennsylvania, 1809</div>'
  '<div class=litany style="display:grid;grid-template-columns:1fr 1fr;column-gap:5vmin;row-gap:2.4vmin;text-align:left;max-width:92vw">'
  '<div class=eyebrow style="margin:0">Luther</div><div class=eyebrow style="margin:0">The Declaration and Address</div>'
  '<div class="no frag">&ldquo;my conscience is <b>captive to the Word of God</b>&rdquo;</div><div class="no frag">&ldquo;to this alone we feel ourselves <b>Divinely bound</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;I do not trust either in the pope or <b>in councils alone</b>&rdquo;</div><div class="no frag">&ldquo;not <b>the voice of the multitude</b>, but the voice of truth&rdquo;</div>'
  '<div class="no frag">&ldquo;<b>unless I am convinced</b> by the testimony of the Scriptures or by clear reason&rdquo;</div><div class="no frag">&ldquo;not formally binding&hellip; <b>farther than they perceive the connection</b>&rdquo;</div>'
  '<div class="no frag">&ldquo;neither safe nor right <b>to go against conscience</b>&rdquo;</div><div class="no frag">&ldquo;<b>no man can judge for his brother</b>&rdquo;</div>'
  '</div>'
  '<aside class=notes>Eight clicks, left then right on each row. Every line on the right is already on the left. The right column: the Preamble; the Address on a General Council; proposition 6; the Preamble again. Only the last row moves: Luther says <i>I</i> may not go against my conscience; Campbell says <i>no one</i> may go against his brother&rsquo;s.<br>That last row is exactly where Luther stopped. Marburg, after the next slide, shows where.</aside></section>')

A('<section class="slide breath"><h2 style="font-size:clamp(56px,12vmin,150px);line-height:1.05;max-width:none">How far can<br>Luther take this?</h2>'
  '<aside class=notes>He has claimed conscience for himself, before the emperor. Ask it plainly: will he grant it to the next man? Then Marburg.</aside></section>')

A('<section class="slide bleed"><div class=bg><div class="bgimg marburgbg"></div></div>'
  '<div class=credit>August Noack, <i>Religionsgespr&auml;ch zu Marburg 1529</i> (detail), 1867&ndash;69 &middot; public domain</div>'
  '<div class=eyebrow>Marburg &middot; October 1529</div>'
  '<h2>Luther and Zwingli.</h2>'
  '<div class="sub frag">He could not share the Lord&rsquo;s table with a brother who read the Lord&rsquo;s table differently.</div>'
  '<aside class=notes>The painting (detail): Luther, in the fur collar, holds Zwingli off; Zwingli points upward. In the full canvas Luther&rsquo;s hand is on <i>est</i> chalked on the table (&ldquo;this <i>is</i> my body&rdquo;). Fourteen articles agreed; on the fifteenth, everything but the bodily presence. Luther: &ldquo;Ihr habt einen andern Geist&rdquo;, &ldquo;You have a different spirit.&rdquo; As the accounts have it, he would not take Zwingli&rsquo;s hand as a brother&rsquo;s.<br>&rarr; Two men, both captive to the same Word. Only one would grant the other that.</aside></section>')

A('<section class="slide breath"><h2 style="max-width:none">Luther claimed conscience for himself.<br><span style="color:var(--gold)">Campbell claimed it for his brother.</span></h2>'
  '<aside class=notes>Say it once and stop. Not a new principle: the same principle, extended to the brother. Luther is not the villain here: the man of Worms and the man of Marburg were equally sincere. That is the point: conscience claimed for yourself is only half a sentence, and Campbell finishes it. This is the chapter in one line.</aside></section>')

A(Q('&ldquo;&hellip;as no man can be judged for his brother, so <b>no man can judge for his brother</b>; every man must be allowed to judge for himself, as every man must bear his own judgment&mdash;must give account of himself to God.&rdquo;', DA, 'Preamble') +
  N('The Preamble&rsquo;s second sentence: the half Luther could not say at Marburg. Not a right claimed but an impossibility stated: you cannot believe for someone else. Zurich and 1806 on the egg were the magistrate trying. The first sentence, just before it: &ldquo;it is high time for us not only to think, but also to act, for ourselves&hellip; to this alone we feel ourselves Divinely bound to be conformed, as by this alone, we must be judged.&rdquo;'))

A(Q('&ldquo;That every such judgment is an express violation of the law of Christ, <b>a daring usurpation of his throne</b>, and a gross intrusion upon the rights and liberties of his subjects.&rdquo;', DA, 'Preamble') +
  N('The very next sentence. &ldquo;Such judgment&rdquo; is the one just before it: &ldquo;no man has a right to judge his brother, except in so far as he manifestly violates the express letter of the law.&rdquo; Whoever judges his brother&rsquo;s conscience is sitting on Christ&rsquo;s throne.'))

A(Q('&ldquo;&hellip;<b>judging and rejecting each other in matters wherein the Lord hath not judged</b>, in a flat contradiction to his expressly revealed will.&rdquo;', DA, 'The Appendix') +
  N('The Appendix names this as one of two great evils provoking the Lord against the churches; the other is &ldquo;the taking and giving of unjust offenses.&rdquo; He then quotes James 4:12: &ldquo;There is one Lawgiver, who is able to save and to destroy: who art thou that judgest another?&rdquo; And: &ldquo;we judge him, not for his opinions, but for his presumption.&rdquo;'))

A(Q('&ldquo;We dare not, therefore, patronize <b>the rejection of God&rsquo;s dear children</b>, because they may not be able to see alike in matters of human inference&mdash;of private opinion.&rdquo;', DA, 'The Appendix') +
  N('Say &ldquo;God&rsquo;s dear children&rdquo; slowly. The sentence continues: &ldquo;and such we esteem all things not expressly revealed and enjoined in the word of God. If otherwise, we know not what private opinion means.&rdquo;'))

A(Q('&ldquo;&hellip;members of the same body, subjects of the same grace, objects of the same Divine love, bought with the same price, and joint-heirs of the same inheritance. <b>Whom God hath thus joined together no man should dare to put asunder.</b>&rdquo;', DA, 'Proposition 9') +
  N('The marriage line, turned on the brother. Every phrase is something God did, not something we agreed to. If God joined them, rejecting a brother is putting asunder what God joined.', 'Proposition 9 returns in full in the Propositions section.'))

A('<section class="slide rejslide"><div class=eyebrow>Worms &middot; 1521</div>'
  '<figure style="margin:0"><img src="IMG_WORMSPIC" alt=""><figcaption>Anton von Werner, <i>Luther at the Diet of Worms</i>, 1877</figcaption></figure>'
  '<h2>Rome rejects Luther.</h2>'
  '<aside class=notes>Four slides, no clicks, one beat each. Same rhythm every time; let the room hear the pattern before you name it. Rome: excommunication (January 1521), then the Edict of Worms (May 1521) makes him an outlaw.</aside></section>')

A('<section class="slide rejslide"><div class=eyebrow>Marburg &middot; 1529</div>'
  '<figure style="margin:0"><img src="IMG_MARBURGPIC" alt=""><figcaption>August Noack, <i>Religionsgespr&auml;ch zu Marburg 1529</i> (detail), 1867&ndash;69</figcaption></figure>'
  '<h2>Luther rejects Zwingli.</h2>'
  '<aside class=notes>The man rejected at Worms, eight years later: &ldquo;You have a different spirit.&rdquo; No common table over the bodily presence.</aside></section>')

A('<section class="slide rejslide"><div class=eyebrow>Zurich &middot; 1527</div>'
  '<figure style="margin:0"><img src="IMG_MANZ" alt=""><figcaption>Jan Luyken, <i>Martyrs Mirror</i>, 1685 &middot; hand-colored</figcaption></figure>'
  '<h2>Zwingli rejects the Anabaptists.</h2>'
  '<aside class=notes>His own students, Grebel and Manz, over infant baptism. Zurich&rsquo;s council, with Zwingli&rsquo;s support, made rebaptism a capital crime (March 1526); Felix Manz was drowned in the Limmat, 5 January 1527, the first Protestant executed by Protestants. The picture is from the <i>Martyrs Mirror</i>, the Anabaptists&rsquo; own book of martyrs: an Anabaptist held under at the riverbank, as Manz was in the Limmat. (Zurich&rsquo;s own chronicle shows Manz&rsquo;s drowning too: Heinrich Thomann&rsquo;s 1605 copy of Bullinger.) Two years later, at Marburg, Zwingli would ask Luther for the hand he had refused Manz.<br>Each one was rejected for his conscience, and each one rejected the next man for his.</aside></section>')

A('<section class="slide rejslide"><div class=eyebrow>Washington, Pennsylvania &middot; 1809</div>'
  '<figure style="margin:0"><img src="IMG_TCAMPBELL" alt="" style="max-height:56vh"><figcaption>Thomas Campbell</figcaption></figure>'
  '<h2 style="color:var(--gold);font-size:clamp(44px,9vmin,116px)">How dare you put asunder?</h2>'
  '<aside class=notes>Then Campbell, turning Proposition 9 on all of them: &ldquo;Whom God hath thus joined together no man should dare to put asunder.&rdquo; Not one of the four was rejected for denying Christ. Each was rejected by a brother. Pause before moving on.</aside></section>')

A('<section class="slide"><aside class=notes>Black.</aside></section>')

A('<section class="slide"><h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none">How do<br>Christians achieve<br>unity?</h2>'
  '<aside class=notes>The question the whole hour has been circling. Let it hang.</aside></section>')

A('<section class="slide breath"><h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none;color:var(--gold)">Next week</h2>'
  '<aside class=notes>Campbell&rsquo;s answer is next week. Then the ideas from tonight.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 1 of 7</div>'
  '<h2>Unity is <span style="color:var(--gold)">given, not built.</span></h2>'
  '<aside class=notes>Union with him first; union with each other in him next. From the Design of Religion: &ldquo;the first and foundation truth of our Christianity is union with him, and the very next to it in order, union with each other in him.&rdquo;</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 2 of 7</div>'
  '<h2>Division is <span style="color:var(--gold)">a horrid evil.</span></h2>'
  '<aside class=notes>Not a difference of opinion: a wound in the body of Christ. Proposition 10: &ldquo;anti-christian, as it destroys the visible unity of the body of Christ.&rdquo; And the Evils of Division litany.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 3 of 7</div>'
  '<h2>Every instrument <span style="color:var(--gold)">failed.</span></h2>'
  '<aside class=notes>Creeds, councils, edicts, swords: each was offered for unity, and each left another division. The egg, 325 to 1806.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 4 of 7</div>'
  '<h2>Conscience <span style="color:var(--gold)">cannot be compelled.</span></h2>'
  '<aside class=notes>It binds because there you answer to God, as his priest. Worms; Aquinas; Vatican II and the Catechism (&ldquo;alone with God&rdquo;); Newman; Luther in 1520 on the baptized as priests.</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 5 of 7</div>'
  '<h2>Conscience is an exercise of <span style="color:var(--gold)">the priesthood of all believers.</span></h2>'
  '<aside class=notes>Why conscience binds: it is where each believer stands before God, as his priest. The Catechism (&ldquo;alone with God&rdquo;; &ldquo;the whole community of believers is, as such, priestly&rdquo;); Newman (&ldquo;the aboriginal Vicar of Christ&rdquo;); Luther in 1520 (&ldquo;a consecrated priest, bishop, and pope&rdquo;).</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 6 of 7</div>'
  '<h2>Commitment to the Word of God, <span style="color:var(--gold)">not <i>interpretations</i> of the Word of God.</span></h2>'
  '<aside class=notes>Luther at Worms: &ldquo;Unless I am convinced by the testimony of the Scriptures or by clear reason.&rdquo; Captive to the Word itself: not the pope&rsquo;s reading, not a council&rsquo;s, not even his own. That is what keeps conscience from becoming &ldquo;I can do what I want.&rdquo;</aside></section>')

A('<section class="slide idea room"><div class="eyebrow quiet">Idea 7 of 7</div>'
  '<h2>No one may judge <span style="color:var(--gold)">for his brother.</span></h2>'
  '<aside class=notes>Luther claimed conscience for himself; Campbell claimed it for his brother. The Preamble (&ldquo;no man can judge for his brother&rdquo;), the Appendix (&ldquo;We dare not&hellip; patronize the rejection of God&rsquo;s dear children&rdquo;), Proposition 9, and the chain of rejections.</aside></section>')

A('<section class="slide room"><div class=eyebrow>&#9670; for discussion</div>'
  '<h2>What is beautiful here? What do we carry forward?</h2>'
  '<aside class=notes>Backup prompts (off the slide): Who have we treated the way Luther treated Zwingli, over a reading of Scripture? What instrument do we reach for when we want unity: a statement, a rule, a vote?<br>If the room is slow: &ldquo;Have you ever been the brother someone else judged for?&rdquo;</aside></section>')

A(open(_HERE + '/../week2/w1_siteslide.html').read().replace('<br>&rarr; Then, if the room wants more, the addendum is next.', ''))

A('<section class="slide"><aside class=notes>Black.</aside></section>')

# ---------- WHY CAMPBELL COULD GO FURTHER: THE SWORD, AND THIS COUNTRY ----------
A('<section class="slide"><h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none">What can<br>unite<br>Christians?</h2>'
  '<div class="sub frag">&ldquo;That they all may be one&hellip; that the world may believe that thou hast sent me.&rdquo;<br><span style="font-size:.7em;color:var(--bone-dim)">John 17:21</span></div>'
  '<aside class=notes>The question, now that the reason is named. Then the prayer: a prayer, not a command, and for the sake of the world&rsquo;s belief. Pause on it before the answer.</aside></section>')

A('<section class="slide breath"><div class=eyebrow>Next week</div>'
  '<h2 style="font-size:clamp(60px,14vmin,180px);line-height:1.02;max-width:none">The answer.</h2>'
  '<aside class=notes>The stopping point if time runs out: end on the question, and open next week with &ldquo;Christ alone.&rdquo; If you are continuing, skip this slide (one more click) and go straight on.</aside></section>')

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
  '<aside class=notes>Close. They built something, watched it succeed, and then did something almost without precedent in church history: they wrote a will for it. Chapter 4, October 18.</aside></section>')

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
