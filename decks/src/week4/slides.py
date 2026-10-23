# -*- coding: utf-8 -*-
# Chapter 4 — The Last Will and Testament of the Springfield Presbytery (taught after Chapter 3b).
# Built with the Chapter 3 engine:  PART=4 python3 decks/src/week3/build.py   (or python3 decks/src/week4/build.py)
# Two ideas: institutional self-sacrifice, in the name of unity; authority returns to the gathered congregation.
# Sources: the Last Will and the Witnesses' Address (Cane Ridge, 28 June 1804), and Stone's autobiography in
# The Biography of Eld. Barton Warren Stone (1847), ch. VII. Checked against the class site's full texts.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('w3bslides', os.path.join(_H, '..', 'week3b', 'slides.py'))
w3b = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(w3b)
w3 = w3b.w3
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

def C(name, note='', eyebrow=''):   # chapter card
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    return ('<section class="slide breath sect">%s<h2>%s</h2><div class=table-line></div>'
            '<aside class=notes>%s</aside></section>' % (e, name, note))
Q, N = w3.Q, w3.N
def CARD(html, note, eyebrow='', style=''):   # a statement on its own
    e = '<div class=eyebrow>%s</div>' % eyebrow if eyebrow else ''
    return '<section class="slide breath">%s<h2 style="max-width:none%s">%s</h2><aside class=notes>%s</aside></section>' % (e, style, html, note)
G = lambda t: '<span style="color:var(--gold)">%s</span>' % t
plain = lambda h: re.sub(r'<span style="color:var\(--gold\)">(.*?)</span>', r'\1', h).replace('<br>', ' ')
BLACK = '<section class="slide"><aside class=notes>Black.</aside></section>'

WILL = 'Last Will and Testament of the Springfield Presbytery, 1804'
WIT = 'The Witnesses&rsquo; Address, 1804'
STONE = 'Barton W. Stone, <i>Biography</i> (1847)'

IDEAS = [
    ('Exit<br>' + G('without excommunication.'),
     'They withdrew &ldquo;from their jurisdiction, but not from their communion,&rdquo; and would not un-church the men un-churching them. Thomas Campbell, five years later, the same move: he kept the practice he was condemned for, but &ldquo;he need not impose them upon others, by anywise requiring their approbation.&rdquo;'),
    ('Institutional self-sacrifice,<br>' + G('in the name of unity.'),
     'The presbytery was nine months old and thriving, and it willed itself to &ldquo;die, be dissolved, and sink into union with the Body of Christ at large.&rdquo; When their own institution began to stand where only Christ should stand, they let it die.'),
    ('Authority returns<br>' + G('to the gathered congregation.'),
     'Each church to &ldquo;choose her own preacher&hellip; admit members&hellip; remove offences; and never henceforth delegate her right of government to any man or set of men whatever.&rdquo; The priesthood of all believers, as polity.'),
    ('Freedom<br>' + G('requires forbearance.'),
     '&ldquo;Pray more and dispute less.&rdquo; A church that has given up its courts has nothing left to settle its quarrels but patience and prayer, and the will says so in the same breath as it gives up the courts.'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>'
            % (k, len(IDEAS), h, n))

S = []
A = S.append

# ---------- OPENING ----------
A(w3b.S[0])                                     # the class title

A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none">We speak&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;where the Bible speaks,</h2>'
  '<h2 style="max-width:none;margin-top:3vmin">and we are silent&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;where the Bible is silent.</h2>'
  '<h2 style="max-width:none;margin-top:5vmin">No creed&hellip;</h2>'
  '<h2 class=frag style="max-width:none;color:var(--gold);margin-top:.6vmin">&hellip;but Christ.</h2>'
  '<aside class=notes>Three clicks. Let the room finish each one.<br>'
  '&bull; The first is Thomas Campbell&rsquo;s, 1809: &ldquo;Where the Scriptures speak, we speak; and where the Scriptures are silent, we are silent&rdquo; (Richardson, <i>Memoirs</i> 1:236).<br>'
  '&bull; The second also comes as &ldquo;No creed but the Bible.&rdquo; Accept either. Tonight&rsquo;s five men said it first, in 1803: &ldquo;all authoritative creeds, but the Bible alone.&rdquo;</aside></section>')

_sum = [x for x in w3b.S if 'class="litany ideasum"' in x and '<div class=eyebrow>Ideas</div>' in x]
assert len(_sum) == 1
A(_sum[0].replace('Christ builds his body.', 'Christ has built his body.').replace('<div class=eyebrow>Ideas</div>', '<div class=eyebrow>Last week&rsquo;s ideas</div>')
  .replace('All five at once, before the discussion.', 'Last week&rsquo;s five ideas, all at once. Read them, or let the room read them; do not re-teach.<br>&rarr; &ldquo;Tonight, five years earlier: men who acted on idea three before Campbell wrote it down.&rdquo;'))

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 4</div>'
  '<h1>The Last Will<br>and Testament</h1><div class=table-line></div>'
  '<div class=sub>Cane Ridge, Kentucky &middot; June 28, 1804</div>'
  '<aside class=notes>Title up. The frame for the hour is a will-reading: who died, of what, what they left, and to whom.<br>'
  'The hour: the will&rsquo;s opening 3 &middot; the trial and the garden 10 &middot; the cost 4 &middot; it worked, and the problem 8 &middot; the reading of the will 12 &middot; our table 8 &middot; close 5.</aside></section>')

# ---------- THE HOOK ----------
A('<section class="slide breath"><h2 style="max-width:none;font-size:clamp(48px,10vmin,128px);line-height:1.1">&ldquo;We will, that this body die,</h2>'
  '<h2 class=frag style="max-width:none;font-size:clamp(32px,6vmin,80px);line-height:1.2;margin-top:3vmin">' + G('be dissolved, and sink into union with the Body of Christ at large&hellip;') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + WILL + '</div>'
  '<aside class=notes>The cold open. One click. Read the first line and stop; let &ldquo;die&rdquo; sit before the rest comes up.<br>'
  '&rarr; &ldquo;A church body wrote that about itself. How did we get here?&rdquo;</aside></section>')

A(Q('&ldquo;The Presbytery of Springfield, sitting at Cane Ridge&hellip; being, through a gracious Providence, <b>in more than ordinary bodily health, growing in strength and size daily</b>, and in perfect soundness and composure of mind; but knowing that it is appointed for all delegated bodies once to die&hellip; do make and ordain this our Last Will and Testament&hellip;&rdquo;', WILL, 'June 28, 1804') +
  N('Who is &ldquo;this body&rdquo;? The will&rsquo;s opening, in the legal form of a real will. Read it slowly; the joke is in &ldquo;more than ordinary bodily health.&rdquo; Nobody makes a will because they are growing in strength and size daily.',
    '&rarr; This church body was nine months old, and thriving.'))

A('<section class="slide room"><h2>Why would a church body that was <span style="color:var(--gold)">thriving</span> write its own will?</h2>'
  '<aside class=notes>Ask it and take one or two guesses. Don&rsquo;t answer. &rarr; &ldquo;To find out, go back to what five preachers were preaching, and the trial it led to in Lexington.&rdquo;</aside></section>')

# ---------- 1 THE TRIAL ----------
A(Q('&ldquo;The distinguishing doctrine preached by us was, that <b>God loved the world &mdash; the whole world</b>, and sent his Son to save them, on condition that they believed in him &mdash; that the gospel was the means of salvation &mdash; but that this means would never be effectual to this end, until believed and obeyed by us &mdash; that God required us to believe in his Son, and had given us sufficient evidence in his Word to produce faith in us, if attended to by us &mdash; that <b>sinners were capable of understanding and believing this testimony</b>, and of acting upon it by coming to the Saviour and obeying him, and from him obtaining salvation and the Holy Spirit.&rdquo;', STONE, 'What the five preached') +
  N('Context for the trial: what the revival preachers were preaching. Stone names the five just before this: McNemar, Thompson, Dunlavy, Marshall, and himself, &ldquo;whose doctrine was different from that taught in the Confession of Faith.&rdquo; Purviance, then a candidate, held it too.',
    'Against Westminster: Christ died for the elect only, and the sinner can do nothing until God first regenerates him. Here: the whole world, and the sinner is able to believe.'))

A(Q('&ldquo;We urged upon the sinner to <b>believe now</b>, and receive salvation &mdash; that in vain they looked for the Spirit to be given them, while they remained in unbelief &mdash; they must believe before the Spirit or salvation would be given them &mdash; that God was as willing to save them now, as he ever was, or ever would be&mdash; that <b>no previous qualification was required</b>, or necessary in order to believe in Jesus, and come to him &mdash; that if they were sinners, this was their divine warrant to believe in him, and to come to him for salvation &mdash; that <b>Jesus died for all</b>, and that all things were now ready.&rdquo;', STONE) +
  N('The same paragraph, continued. &ldquo;No previous qualification&rdquo; is the open table again, as doctrine: nothing stands between the sinner and Christ.',
    'Stone says this is the doctrine of their <i>Apology</i>, and that he later dissented from its account of the Atonement.'))

A(Q('&ldquo;When we began first to preach these things, the people appeared as just awakened from the sleep of ages &mdash; <b>they seemed to see for the first time that they were responsible beings</b>&hellip;&rdquo;', STONE) +
  N('The sentence goes on: &ldquo;and that a refusal to use the means appointed, was a damning sin.&rdquo;',
    'Then the reaction: &ldquo;The sticklers for orthodoxy amongst us writhed under these doctrines&rdquo;; they &ldquo;painfully saw their Confession of Faith neglected.&rdquo;',
    '&rarr; And the first one they went after was McNemar.'))

A(Q('&ldquo;&hellip;first took McNemar through their <b>fiery ordeal</b>, for preaching these anti-calvinistic doctrines.&rdquo;', STONE, 'Richard McNemar, 1770&ndash;1839') +
  N('McNemar, a revival preacher in Ohio. His crime: preaching what the revival preached, that the gospel offer is open to everyone and anyone may respond. That is not what the Westminster Confession says, and every Presbyterian minister had sworn to the Confession.',
    'The &ldquo;ordeal&rdquo; was his own presbytery, the Washington Presbytery (Stone&rsquo;s sentence calls it &ldquo;the Presbytery of Springfield, in Ohio&rdquo;; the records say Washington, and the name would only confuse here). The Synod of Kentucky censured that presbytery for not dealing with him, and his case came up to the Synod at Lexington, September 1803.'))

A('<section class="slide"><div class=eyebrow>The Synod of Kentucky &middot; Lexington, September 1803</div>'
  '<h2>Richard McNemar is on trial.</h2>'
  '<div class=sub>Four other ministers are watching.<br>They preach what he preaches.</div>'
  '<aside class=notes>The four: Robert Marshall, John Dunlavy, John Thompson, and Barton Stone, the minister of Cane Ridge. Same machinery as Chapter 2, on the other side of the mountains.</aside></section>')

A('<section class="slide plateslide tight"><figure class="plate short"><img src="IMG_STONE" alt="" style="max-height:58vh"><figcaption>Barton W. Stone, 1772&ndash;1844 &middot; minister of Cane Ridge and Concord</figcaption></figure>'
  '<p class="bigquote long" style="margin-top:2vmin"><span class=q>&ldquo;It was plainly hinted to us, that <b>we would not be forgotten</b> by the Synod.&rdquo;</span></p>'
  '<aside class=notes>Stone, whom the room met at Cane Ridge in Chapter 1. &ldquo;We waited anxiously for the issue, till we plainly saw it would be adverse to him, and consequently to us all.&rdquo;</aside></section>')

A(Q('&ldquo;In a short recess of Synod, we five withdrew to a private garden, where, after prayer for direction, and a free conversation, with a perfect unanimity we drew up a protest&hellip; and a declaration of our independence, and of our <b>withdrawal from their jurisdiction, but not from their communion</b>.&rdquo;', STONE, 'The garden') +
  N('Five men, a recess, a garden, prayer. &ldquo;A declaration of our independence&rdquo;: his words, twenty-seven years after the other one. The protest is dated 10 September 1803.'))

A(Q('&ldquo;This protest we immediately presented to the Synod, through their Moderator &mdash; it was altogether unexpected by them, and produced very unpleasant feelings; and <b>a profound silence for a few minutes ensued</b>.&rdquo;', STONE) +
  N('Let the room have a few seconds of silence of its own.'))

A(CARD('They left the court.<br>' + G('They did not leave the table.'),
  'The chapter in one line. The men about to put them out were still their brothers, and they would not put anyone out in return. Last week&rsquo;s first idea, lived: conscience claimed for the brother, even the brother who judges you.'))

A(IDEA(1))

A(Q('&ldquo;&hellip;no man can relinquish his opinions or practices till once convinced that they are wrong&hellip; One thing, however, he may do: when not bound by an express command, <b>he need not impose them upon others, by anywise requiring their approbation</b>&hellip;&rdquo;', 'Thomas Campbell, <i>Declaration and Address</i>, 1809 &middot; Appendix', 'Five years later, the same move') +
  N('Chapter 2: the Seceders tried and censured Thomas Campbell for giving the Supper to other Presbyterians. He did not give the practice up, and he did not require his judges to adopt it. That is exit without excommunication from the other side: keep your practice; do not make it your brother&rsquo;s test.',
    'The sentence continues: &ldquo;and when this is done, the things, to them, are as good as dead, yea, as good as buried, too, being thus removed out of the way.&rdquo;'))

A(Q('&ldquo;&hellip;we plead a privilege, which is granted in the Confession of Faith, chap. 1. sec. 9, 10&hellip; that <b>the infallible rule of interpreting Scripture, is not the Confession of Faith</b>, nor any human writings whatever, but the Scripture itself.&rdquo;', 'The five, letter to their congregations, September 1803 &middot; in Stone, <i>Biography</i> (1847)', 'Quoting the Confession against itself') +
  N('Their circular letter, drafted at the new presbytery&rsquo;s first meeting and signed by all five; it says the protest made the same plea. &ldquo;We wish to pay all due deference to the Confession of Faith, and other writings of our pious fathers; but&hellip;&rdquo;',
    'The same letter: &ldquo;We do not desire, nor do we consider ourselves to be separated from the Presbyterian church&hellip; we will admit to communion as formerly, and desire to be admitted. It is not our design to form a party.&rdquo;',
    '&rarr; The book they were tried by says it is not the final word. Next slide: what it actually says.'))

A('<section class="slide"><div class=eyebrow>Westminster Confession, 1646 &middot; chapter 1</div>'
  '<div class=litany style="text-align:left;gap:3.4vmin;margin-top:1.4vmin;max-width:88vw">'
  '<div class="no frag"><b style="color:var(--gold)">1.9</b> &ldquo;The infallible rule of interpretation of Scripture, is <b>the Scripture itself</b>&hellip;&rdquo;</div>'
  '<div class="no frag"><b style="color:var(--gold)">1.10</b> &ldquo;The supreme Judge, by which all controversies of religion are to be determined, and all decrees of councils&hellip; are to be examined&hellip; can be no other but <b>the Holy Spirit speaking in the Scripture</b>.&rdquo;</div>'
  '</div>'
  '<aside class=notes>Two clicks. The Synod tried them by the Confession; the Confession says every council&rsquo;s decree is to be examined by Scripture, and the only supreme judge is the Spirit speaking in Scripture. That includes the Synod, and the Confession itself. (Text as in the 1646 Confession; 1.9 goes on: &ldquo;when there is a question about the true and full sense of any scripture&hellip; it [must] be searched and known by other places that speak more clearly.&rdquo;)<br>'
  '&rarr; They did not reject the Confession. They took it at its word. And the same book says more.</aside></section>')

A('<section class="slide"><div class=eyebrow>The same Confession</div>'
  '<div class=litany style="text-align:left;gap:3.4vmin;margin-top:1.4vmin;max-width:88vw">'
  '<div class="no frag"><b style="color:var(--gold)">20.2</b> &ldquo;<b>God alone is Lord of the conscience</b>, and hath left it free from the doctrines and commandments of men&hellip;&rdquo;</div>'
  '<div class="no frag"><b style="color:var(--gold)">31.3</b> &ldquo;All synods or councils since the apostles&rsquo; times, whether general or particular, <b>may err, and many have erred</b>; therefore they are not to be made the rule of faith or practice&hellip;&rdquo;</div>'
  '</div>'
  '<aside class=notes>Two clicks. Chapter 20, Of Christian Liberty and Liberty of Conscience; chapter 31, Of Synods and Councils (31.3 in the American text the Synod used; 31.4 in the 1646 original). 20.2 goes on: &ldquo;the requiring an implicit faith, and an absolute and blind obedience, is to destroy liberty of conscience, and reason also.&rdquo; 31.3 ends: &ldquo;but to be used as a help in both.&rdquo;<br>'
  '&rarr; The Synod of Kentucky was a synod. By its own Confession, it may err.</aside></section>')

A(CARD('These men were radical.<br>' + G('But they were also faithful.'),
  'Radical in what they did: walked out of a synod, tore up a salary, dissolved their own presbytery. Faithful in why.'))

A(CARD('They were not breaking with their tradition.<br>' + G('They were honoring its deepest impulses.'),
  'Scripture as the only infallible rule; God alone Lord of the conscience; councils may err. Every one is in the Westminster Confession. The Reformation&rsquo;s own principles, taken seriously: Luther at Worms, again. &rarr; And they pressed them further than the Synod would.'))

A('<section class="slide"><div class=eyebrow>The Synod sends a committee to win them back</div>'
  '<div class=litany>'
  '<div class="no frag">One of the committee, Matthew Houston, &ldquo;became convinced that the doctrine we preached was true, and <b>soon after united with us</b>.&rdquo;</div>'
  '<div class="no frag">Another, &ldquo;old father David Rice,&rdquo; argued &ldquo;that every departure from Calvinism was an advance to atheism&rdquo;:</div>'
  '<div class="no frag" style="color:var(--gold)">Calvinism &rarr; Arminianism &rarr; Pelagianism &rarr; deism &rarr; atheism</div>'
  '</div><div class=cite>' + STONE + '</div>'
  '<aside class=notes>Three clicks, and a smile. The committee sent to bring them back lost a member to them. Rice was the father of Kentucky Presbyterianism and Stone honors him (&ldquo;of precious memory&rdquo;), but his argument, Stone says, &ldquo;could have no effect on minds ardent in the search of truth.&rdquo; The logic: the creed is the only thing between you and atheism. Last week answered that.</aside></section>')

A(Q('&ldquo;We insisted that after we had orderly protested, and withdrawn, that the Synod had <b>no better right to suspend us, than the pope of Rome had to suspend Luther</b>, after he had done the same thing.&rdquo;', STONE, 'The suspension') +
  N('The Synod suspended them anyway and sent committees to read &ldquo;the Synod&rsquo;s bull of suspension&rdquo; in their pulpits and declare their churches vacant. &ldquo;Bull&rdquo; is the pope&rsquo;s word, on purpose. Luther again, from last week: Worms.'))

A(Q('&ldquo;&hellip;not only were churches divided, but families; those who before had lived in harmony and love, were now set in hostile array against each other. What scenes of confusion and distress! <b>not produced by the Bible; but by human authoritative creeds</b>&hellip;&rdquo;', STONE) +
  N('The cost to the people. The sentence goes on: &ldquo;My heart was sickened, and effectually turned against such creeds, as nuisances of religious society, and the very bane of Christian unity.&rdquo;',
    '&rarr; Then the cost to Stone.'))

# ---------- 2 THE COST ----------
A(Q('&ldquo;I called together my congregations, and informed them that I could no longer conscientiously preach to support the Presbyterian church&hellip; that I absolved them from all obligations in a pecuniary point of view, and then <b>in their presence tore up their salary obligation to me</b>&hellip;&rdquo;', STONE, 'Cane Ridge and Concord &middot; late 1803') +
  N('Mime it if you like. He kept preaching to them, &ldquo;but not in the relation that had previously existed between us.&rdquo; Of the people: &ldquo;Never have I found a more loving, kind, and orderly people in any country.&rdquo; Of the day: &ldquo;This was truly a day of sorrow, and the impressions of it are indelible.&rdquo;'))

A(Q('&ldquo;I preferred honesty and a good conscience to all these things. Having now no support from the congregations, and having emancipated my slaves, I turned my attention cheerfully, though awkwardly, to labor on my little farm&hellip; often on my return home, <b>I found the weeds were getting ahead of my corn</b>.&rdquo;', STONE) +
  N('He had already freed the people he had enslaved. Now no salary either. He preached almost every night and worked the field at night &ldquo;while others were asleep.&rdquo;',
    '&rarr; And here is the surprise: it worked.'))

# ---------- 3 IT WORKED, AND THE PROBLEM ----------
A('<section class="slide"><h2>It worked.</h2>'
  '<div class=litany>'
  '<div class="no frag">They form the <b>Springfield Presbytery</b> and publish the <i>Apology</i>: no authoritative creed but the Bible.</div>'
  '<div class="no frag">The pamphlets against them, &ldquo;full of misrepresentation and invective,&rdquo; <b>spread their views</b>.</div>'
  '<div class="no frag">People &ldquo;disgusted and offended&rdquo; by the attacks &ldquo;were driven from them, and <b>cleaved to us</b>.&rdquo;</div>'
  '</div><div class=cite>' + STONE + '</div>'
  '<aside class=notes>Three clicks. The Methodists in Virginia reprinted the <i>Apology</i>, &ldquo;except our remarks upon creeds.&rdquo; Churches planted, preachers multiplied.<br>&rarr; Which is exactly when the problem began.</aside></section>')

A(Q('&ldquo;&hellip;they endeavored to cultivate a spirit of love and unity with all Christians; but found it extremely difficult to suppress the idea that they themselves were a party separate from others. <b>This difficulty increased in proportion to their success.</b>&rdquo;', WIT, 'Why they did it') +
  N('The witnesses who signed the will, explaining it. They left a party because it fenced Christians apart. Now people saw them as a party, and they began to feel like one. Stone: &ldquo;we had not worn our name more than one year, before we saw it savored of a party spirit.&rdquo;'))

A(CARD('Success was making them<br>' + G('the thing they had protested.'),
  'Say it once. Failure would have been easy to read; success was the danger.'))

A(Q('&ldquo;We will, that our weak brethren, who may have been <b>wishing to make the Presbytery of Springfield their king</b>, and wot not what is now become of it, betake themselves to the Rock of Ages, and follow Jesus for the future.&rdquo;', WILL, 'From the will') +
  N('Their own people. Gentle, and a little funny: &ldquo;wot not what is now become of it.&rdquo; The presbytery was being asked to stand where Christ stands.'))

A(Q('&ldquo;&hellip;they soon found that there was <b>neither precept nor example in the New Testament for such confederacies</b> as modern Church Sessions, Presbyteries, Synods, General Assemblies, etc.&rdquo;', WIT, 'Writing a book on church government') +
  N('At their last meeting they set out to write <i>Observations on Church Government</i>. The research convicted the researchers: their own presbytery was one of these confederacies. &ldquo;While they continued in the connection in which they then stood, they were off the foundation of the Apostles and Prophets.&rdquo; (The book never appeared.)'))

A(CARD('They caught their own presbytery<br>' + G('being handed a job only Christ can do.'),
  'Last week&rsquo;s thesis, lived five years before it was written: anything asked to do a job only Christ can do will fail. They did not wait for it to fail. &rarr; So they let it die.'))

# ---------- 4 THE READING OF THE WILL ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg househbg"></div></div>'
  '<div class=credit>Cane Ridge Meeting House &middot; HABS, Theodore Webb, 1934</div>'
  '<div class=eyebrow>Cane Ridge &middot; June 28, 1804</div>'
  '<h2>The reading of the will.</h2>'
  '<aside class=notes>Back to the room of Chapter 1. Three years earlier, thousands came through the mud to an open table here. The will is dated &ldquo;sitting at Cane Ridge,&rdquo; by tradition in this meetinghouse. Signed by six: the five from the garden and David Purviance.</aside></section>')

A(Q('&ldquo;For where a testament is, there must of necessity be <b>the death of the testator</b>&hellip; Verily, verily I say unto you, except a corn of wheat fall into the ground and die, it abideth alone; but <b>if it die, it bringeth forth much fruit</b>.&rdquo;', 'The will&rsquo;s epigraph &middot; Hebrews 9:16; John 12:24', 'At the top of the page') +
  N('They put the theology at the top. A will has no force while the testator lives. The inheritance can only pass when the presbytery is gone.'))

A('<section class="slide breath"><h2 style="max-width:none;font-size:clamp(48px,10vmin,128px);line-height:1.1">&ldquo;&hellip;it is appointed for<br>all delegated bodies<br>' + G('once to die.') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + WILL + '</div>'
  '<aside class=notes>From the preamble, after &ldquo;more than ordinary bodily health.&rdquo; Hebrews 9:27, &ldquo;it is appointed unto men once to die,&rdquo; applied to institutions. Every presbytery, synod, board and program is a delegated body: it holds authority on loan. It is mortal by design.</aside></section>')

A(Q('&ldquo;Imprimis. We will, that this body <b>die, be dissolved, and sink into union with the Body of Christ at large</b>; for there is but one body, and one spirit, even as we are called in one hope of our calling.&rdquo;', WILL, 'First bequest') +
  N('The line we opened with; now the room knows how they got here. &ldquo;Imprimis&rdquo;: in the first place, the legal word. Ephesians 4:4. The presbytery does not dissolve into nothing; it sinks into the whole church. The heir is the Body of Christ at large.'))

A(IDEA(2))

A(Q('&ldquo;We will, that our name of distinction, with its Reverend title, <b>be forgotten</b>, that there be but one Lord over God&rsquo;s heritage, and his name one.&rdquo;', WILL, 'Their name') +
  N('A will gives things away; this one gives away everything a church body has, starting with its name and its titles. They took the name Christian (Rice Haggard&rsquo;s pamphlet).'))

A(Q('&ldquo;We will, that our power of making laws for the government of the church, and executing them by delegated authority, <b>forever cease</b>; that the people may have free course to the Bible&hellip;&rdquo;', WILL, 'Their power') +
  N('Not abolished: bequeathed. The power to make law for the church goes back to where they think it belongs. The sentence ends: &ldquo;and adopt the law of the spirit of life in Christ Jesus.&rdquo;'))

A(Q('&ldquo;We will, that the church of Christ assume her <b>native right of internal government</b>&hellip; and admit no other proof of their authority, but Christ speaking in them.&rdquo;', WILL, 'To the church') +
  N('&ldquo;Native&rdquo;: it was always hers. The church will &ldquo;try her candidates for the ministry, as to their soundness in the faith, acquaintance with experimental religion, gravity and aptness to teach.&rdquo; What the Synod did to McNemar, the congregation now does, and the only credential is &ldquo;Christ speaking in them.&rdquo;'))

A(Q('&ldquo;We will, that each particular church, as a body&hellip; <b>choose her own preacher</b>, and support him by a free will offering&hellip; admit members &mdash; remove offences; and <b>never henceforth delegate her right of government to any man or set of men whatever</b>.&rdquo;', WILL, 'To every congregation') +
  N('The biggest bequest. Everything the Synod did to them (try preachers, admit, exclude) is handed to the congregation. The priesthood of all believers, as polity.',
    '&rarr; Hold this one. Next week, at Brush Run, a congregation will use exactly this right.'))

A(IDEA(3))

A(Q('&ldquo;We will, that preachers and people, cultivate a spirit of mutual forbearance; <b>pray more and dispute less</b>; and while they behold the signs of the times, look up, and confidently expect that redemption draweth nigh.&rdquo;', WILL, 'To preachers and people') +
  N('A church that has given away its courts has nothing left to settle its quarrels but forbearance and prayer, and the will says so in the same breath. Then: look up; redemption draweth nigh. They died expecting the future.'))

A(IDEA(4))

# ---------- 5 WHY ----------
A(Q('&ldquo;&hellip;from its first existence it was knit together in love, lived in peace and concord, and <b>died a voluntary and happy death</b>.&rdquo;', WIT, 'The witnesses') +
  N('Not a split, not a failure, not a scandal. A happy death.'))

A(Q('&ldquo;&hellip;from a principle of love to Christians of every name, the precious cause of Jesus, and <b>dying sinners who are kept from the Lord by the existence of sects and parties</b> in the church, they have cheerfully consented to retire from the din and fury of conflicting parties &mdash; sink out of the view of fleshly minds, and die the death.&rdquo;', WIT, 'Why') +
  N('The three reasons: love of Christians of every name; the cause of Jesus; and the people outside, kept from the Lord by our divisions.'))

A(Q('&ldquo;&hellip;we became a by-word and laughing stock to the sects around; all prophesying our speedy annihilation. Yet <b>from this period I date the commencement of that reformation</b>, which has progressed to this day.&rdquo;', STONE) +
  N('Stone does not date the movement from Cane Ridge in 1801, or from the garden in 1803. He dates it from here: the giving up of the party.'))

A(CARD('A will only takes effect<br>when someone dies.<br>' + G('The heir was the whole church of Christ.'),
  'Let it sit before the room.'))

# ---------- OUR TABLE ----------
A('<section class="slide room"><div class=eyebrow>Our table</div>'
  '<h2>What in our church is &ldquo;in more than ordinary bodily health&rdquo;?</h2>'
  '<div class="sub frag">Would we be willing to let it die?</div>'
  '<aside class=notes>Discussion, eight minutes. Not what is failing: what is thriving. A program, a name, a building, a way of doing things, a reputation. Which of them is starting to stand where only Christ should stand? Leave it open.</aside></section>')
A(BLACK)

# ---------- IDEAS ----------
DISCUSS = re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): What do we keep alive mostly because it is ours? Who in our congregation holds authority that belongs to the gathered church? If our own church were thriving, could we let some part of it die for the sake of unity?<br>If the room is slow: &ldquo;What would you put in our will?&rdquo;</aside>',
                 w3b.pick('&#9670; for discussion', 0), flags=re.S)
A(DISCUSS)
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A('<section class="slide room"><div class=eyebrow>Ideas</div>'
  '<div class="litany ideasum" style="text-align:left;gap:1.2vmin;margin-top:2.6vmin">'
  + ''.join('<div class=no><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (k, plain(h)) for k, (h, _) in enumerate(IDEAS, 1)) +
  '</div><aside class=notes>All four at once, before the discussion.</aside></section>')
A(DISCUSS)
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Both of tonight&rsquo;s sources are there in full: the <i>Last Will and Testament</i> with the Witnesses&rsquo; Address, and Stone&rsquo;s <i>Biography</i>. Say &ldquo;sources and other information are on the site,&rdquo; and leave it there.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S))
A('<section class="slide"><h2>Next week: wherever two or three are gathered.</h2>'
  '<div class="sub frag">The will gave every congregation the right to choose its own ministers. At Brush Run, one will.</div>'
  '<aside class=notes>Chapter 5, the Brush Run ordination: the Campbells&rsquo; side, 1811. Rebuffed by the Presbyterians, they ordain their own, and find that in the New Testament authority inheres in the congregation.</aside></section>')
A(BLACK)

# ---------- ADDENDUM ----------
A(C('Addendum', 'Reference material; not part of the telling.'))
A('<section class="slide"><div class=eyebrow>What they left</div>'
  '<div class=litany>'
  '<div class="no frag">Their name, and the Reverend title: &ldquo;<b>be forgotten</b>, that there be but one Lord over God&rsquo;s heritage, and his name one.&rdquo;</div>'
  '<div class="no frag">Their power of making laws for the church: &ldquo;<b>forever cease</b>; that the people may have free course to the Bible.&rdquo;</div>'
  '<div class="no frag">To the people: &ldquo;the Bible as the <b>only sure guide to heaven</b>.&rdquo;</div>'
  '</div><div class=cite>' + WILL + '</div>'
  '<aside class=notes>The bequests in one list (the telling gives each its own slide). On the Bible item, the joke: those offended by other books &ldquo;may cast them into the fire if they choose: for it is better to enter into life having one book, than having many to be cast into hell.&rdquo;</aside></section>')
A('<section class="slide ideasmap"><div class=eyebrow>What this week touched</div>'
  '<div class=wmap><div class="r ms-christ"><span class="th on">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class="th key">UNITY</span><span class="th key">PRIESTHOOD</span><span class="th on">FUTURE</span></div>'
  '<div class="r ms-sec"><span class=th>HOMECOMING</span><span class="th key">SELF-SACRIFICE</span><span class="th on">FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class="th on">MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class="th on">the Table</span><span class=th>Baptism</span><span class="th on">Scripture</span><span class=th>Singing</span><span class="th key">Congregation</span></div></div>'
  '<div class=small>Bright: the spine of this week. Dim: touched in passing. Unlit: still ahead of us.</div>'
  '<aside class=notes>The values board from Week 2. New light this week: Self-Sacrifice and Congregation. Future: &ldquo;redemption draweth nigh.&rdquo;</aside></section>')
