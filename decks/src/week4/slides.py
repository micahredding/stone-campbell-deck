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
WIT = 'The Witnesses&rsquo; Address, appended to the Last Will and Testament, 1804'
STONE = 'Barton W. Stone, <i>Biography</i> (1847)'

IDEAS = [
    ('Unity:<br>' + G('institutional self-sacrifice.'),
     'Not just rejecting other religious authorities for the sake of unity, but dissolving even their own: &ldquo;We will, that this body die, be dissolved, and sink into union with the Body of Christ at large.&rdquo; The presbytery was thriving, and they let it die.'),
    ('Freedom of conscience:<br>' + G('claimed for ourselves, extended to others.'),
     'Claimed: &ldquo;We chose to hearken to God, rather than men.&rdquo; Paid for: Stone tears up his salary obligation in front of his congregations, and goes back to the farm. Extended: they would not excommunicate their judges: &ldquo;we will admit to communion as formerly, and desire to be admitted.&rdquo; Campbell, five years later, the same.'),
    ('Priesthood:<br>' + G('authority belongs to gathered believers.'),
     'Each church, &ldquo;actuated by the same spirit,&rdquo; to &ldquo;choose her own preacher&hellip; admit members&hellip; remove offences; and never henceforth delegate her right of government to any man or set of men whatever.&rdquo; No proof of a minister&rsquo;s authority &ldquo;but Christ speaking in them.&rdquo; &rarr; Next week, at Brush Run, a congregation uses exactly this right.'),
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
  '<h2 style="max-width:none">Which of the following is a Restoration Movement publication?</h2>'
  '<div class="litany" style="text-align:left;gap:1.6vmin;margin-top:4vmin">'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">A.</span><i>Christianity Today</i></div>'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">B.</span><i>Contending for the Faith</i><span class=frag style="color:var(--gold);margin-left:.5em">&larr;</span></div>'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">C.</span><i>Charisma</i> Magazine</div>'
  '</div>'
  '<aside class=notes>One click points to the answer. Let the room answer first.<br>&bull; B: <i>Contending for the Faith</i>, a conservative Churches of Christ paper (Ira Y. Rice Jr., from 1970).<br>&bull; <i>Christianity Today</i> is the evangelical magazine Billy Graham founded (1956); <i>Charisma</i> is Pentecostal and charismatic (1975).</aside></section>')

# ---------- THE HOOK ----------
A('<section class="slide breath"><h2 style="max-width:none;font-size:clamp(48px,10vmin,128px);line-height:1.1">&ldquo;We will, that this body die,</h2>'
  '<h2 style="max-width:none;font-size:clamp(48px,10vmin,128px);line-height:1.1;margin-top:1vmin">' + G('be dissolved, and sink into union<br>with the Body of Christ at large&hellip;') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + WILL + '</div>'
  '<aside class=notes>The cold open. No clicks. Read the first line and stop; let &ldquo;die&rdquo; sit before you read on. The sentence goes on: &ldquo;for there is but one body, and one spirit, even as we are called in one hope of our calling&rdquo; (Ephesians 4:4).<br>'
  '&rarr; Then last week&rsquo;s ideas, and then name it: the title.</aside></section>')

_sum = [x for x in w3b.S if 'class="litany ideasum"' in x and '<div class=eyebrow>Ideas</div>' in x]
assert len(_sum) == 1
A(re.sub(r'<div class=no><span[^>]*>5\.</span>.*?</div>', '', _sum[0], flags=re.S).replace('Christ builds his body.', 'Christ has built his body.').replace('<div class=eyebrow>Ideas</div>', '<div class=eyebrow>Last week&rsquo;s ideas</div>')
  .replace('All five at once, before the discussion.', 'Four of last week&rsquo;s ideas, all at once. Read them, or let the room read them; do not re-teach.<br>&rarr; &ldquo;Tonight, five years earlier: men who acted on idea three before Campbell wrote it down.&rdquo;'))

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 4</div>'
  '<h1>The Last Will<br>and Testament</h1><div class=table-line></div>'
  '<div class=sub>Cane Ridge, Kentucky &middot; June 28, 1804</div>'
  '<aside class=notes>Two documents set the course of our movement: the <i>Declaration and Address</i> (the last few weeks) and this one. This one is five years older. Then the recap: Cane Ridge; Thomas Campbell&rsquo;s fight for unity, carried from Ireland to America; communion for Christians outside his sect; his trial. Unity and freedom of conscience, all along, as one question.<br>The frame for the hour is a will-reading: who died, of what, what they left, and to whom.<br>'
  'The hour: the will&rsquo;s opening 3 &middot; the trial and the garden 10 &middot; the cost 4 &middot; it worked, and the problem 8 &middot; the reading of the will 12 &middot; our table 8 &middot; close 5.</aside></section>')

# ---------- 1 THE TRIAL ----------
A('<section class="slide breath sect"><h2>A few years after Cane Ridge&hellip;</h2><div class=table-line></div>'
  '<div class=sub>Kentucky and Ohio &middot; 1803</div>'
  '<aside class=notes>Setup. Cane Ridge was August 1801; the revival kept spreading, and by 1803 five Presbyterian ministers were preaching in its strain.</aside></section>')

A(Q('&ldquo;There were at this time <b>five preachers</b> in the Presbyterian connection, who were in the same strain of preaching, and <b>whose doctrine was different from that taught in the Confession of Faith</b> of that body. Their names were, Richard McNemar, John Thompson, John Dunlavy, Robert Marshall, and myself&hellip;&rdquo;', STONE, 'Five preachers') +
  N('The revival has kept going since Cane Ridge, and Stone is one of five ministers preaching in its strain. The sentence goes on: &ldquo;the three former lived in Ohio, the two latter in Kentucky.&rdquo; David Purviance, then a candidate for the ministry, &ldquo;was of the same faith.&rdquo;',
    '&rarr; Here is what they preached.'))

A(Q('&ldquo;The distinguishing doctrine preached by us was, that <b>God loved the world &mdash; the whole world</b>, and sent his Son to save them&hellip; that the gospel was the means of salvation&hellip; that God required us to believe in his Son, and had given us sufficient evidence in his Word to produce faith in us&hellip; that <b>sinners were capable of understanding and believing this testimony</b>, and of acting upon it by coming to the Saviour and obeying him, and from him obtaining salvation and the Holy Spirit.&rdquo;', STONE, 'What the five preached') +
  N('Clipped from the slide: &ldquo;on condition that they believed in him&rdquo; (after &ldquo;save them&rdquo;); &ldquo;but that this means would never be effectual to this end, until believed and obeyed by us&rdquo; (after &ldquo;the means of salvation&rdquo;); and &ldquo;if attended to by us&rdquo; (after &ldquo;faith in us&rdquo;).',
    'Their distinctive teaching.',
    'Against Westminster: Christ died for the elect only, and the sinner can do nothing until God first regenerates him. Here: the whole world, and the sinner is able to believe.'))

A(Q('&ldquo;We urged upon the sinner to <b>believe now</b>, and receive salvation&hellip; that God was as willing to save them now, as he ever was, or ever would be&mdash; that <b>no previous qualification was required</b>, or necessary in order to believe in Jesus, and come to him&hellip; that <b>Jesus died for all</b>, and that all things were now ready.&rdquo;', STONE) +
  N('Clipped from the slide, after &ldquo;receive salvation&rdquo;: &ldquo;that in vain they looked for the Spirit to be given them, while they remained in unbelief &mdash; they must believe before the Spirit or salvation would be given them.&rdquo; And after &ldquo;come to him&rdquo;: &ldquo;that if they were sinners, this was their divine warrant to believe in him, and to come to him for salvation.&rdquo;',
    'The same paragraph, continued. &ldquo;No previous qualification&rdquo; is the open table again, as doctrine: nothing stands between the sinner and Christ.',
    'Stone says this is the doctrine of their <i>Apology</i>, and that he later dissented from its account of the Atonement.'))

A(Q('&ldquo;When we began first to preach these things, the people appeared as just awakened from the sleep of ages &mdash; <b>they seemed to see for the first time that they were responsible beings</b>&hellip;&rdquo;', STONE) +
  N('The sentence goes on: &ldquo;and that a refusal to use the means appointed, was a damning sin.&rdquo;',
    '&rarr; Grandmother: the mining camp, the Church of Christ, agency.',
    'Then the reaction: &ldquo;The sticklers for orthodoxy amongst us writhed under these doctrines&rdquo;; they &ldquo;painfully saw their Confession of Faith neglected.&rdquo;'))


A(Q('&ldquo;When we neglected it [the Westminster Confession] and followed the Spirit of God, in his word, our minds were enlightened, and our souls were quickened. But when we compared this light, with the confession, they would not agree. We could not withstand God. <b>We chose to hearken to God, rather than men</b>&hellip;&rdquo;', 'Springfield Presbytery, <i>Apology</i> (1804)', 'Obey God rather than men') +
  N('Acts 5:29. From the <i>Apology</i> they published the next year, on the Confession; the sentence before: &ldquo;That book never helped, but hindered our faith.&rdquo; The sentence ends: &ldquo;and therefore, have taken our leave of that book.&rdquo;',
    '&rarr; It flourished, and it drew enough ire that the first one they went after was McNemar.'))
A(C('The Trial', 'Lexington, September 1803.'))

A('<section class="slide"><div class=eyebrow>The Synod of Kentucky &middot; Lexington, September 1803</div>'
  '<h2>Richard McNemar is on trial.</h2>'
  '<div class=sub>Four other ministers are watching.<br>They preach what he preaches.</div>'
  '<aside class=notes>The four: Robert Marshall, John Dunlavy, John Thompson, and Barton Stone, the minister of Cane Ridge. Same machinery as Chapter 2, on the other side of the mountains.</aside></section>')

A(Q('&ldquo;&hellip;first took McNemar through their <b>fiery ordeal</b>, for preaching these anti-calvinistic doctrines.&rdquo;', STONE, 'Richard McNemar, 1770&ndash;1839') +
  N('McNemar, a revival preacher in Ohio. His crime: preaching what the revival preached, that the gospel offer is open to everyone and anyone may respond. That is not what the Westminster Confession says, and every Presbyterian minister had sworn to the Confession.',
    'The &ldquo;ordeal&rdquo; was his own presbytery, the Washington Presbytery (Stone&rsquo;s sentence calls it &ldquo;the Presbytery of Springfield, in Ohio&rdquo;; the records say Washington, and the name would only confuse here). The Synod of Kentucky censured that presbytery for not dealing with him, and his case came up to the Synod at Lexington, September 1803.'))

A('<section class="slide plateslide tight"><figure class="plate short"><img src="IMG_STONE" alt="" style="max-height:58vh"><figcaption>Barton W. Stone, 1772&ndash;1844 &middot; minister of Cane Ridge and Concord</figcaption></figure>'
  '<p class="bigquote long" style="margin-top:2vmin"><span class=q>&ldquo;It was plainly hinted to us, that <b>we would not be forgotten</b> by the Synod.&rdquo;</span></p>'
  '<aside class=notes>Stone, whom the room met at Cane Ridge in Chapter 1. &ldquo;We waited anxiously for the issue, till we plainly saw it would be adverse to him, and consequently to us all.&rdquo;<br>&rarr; So, in a recess of the Synod&hellip;</aside></section>')

A(Q('&ldquo;In a short recess of Synod, we five withdrew to a private garden, where, after prayer for direction, and a free conversation, with a perfect unanimity we drew up a protest&hellip; and a declaration of our independence, and of our <b>withdrawal from their jurisdiction, but not from their communion</b>.&rdquo;', STONE, 'The garden') +
  N('Five men, a recess, a garden, prayer. &ldquo;A declaration of our independence&rdquo;: his words, twenty-seven years after the other one. The protest is dated 10 September 1803.'))

A(Q('&ldquo;This protest we immediately presented to the Synod, through their Moderator &mdash; it was altogether unexpected by them, and produced very unpleasant feelings; and <b>a profound silence for a few minutes ensued</b>.&rdquo;', STONE) +
  N('Let the room have a few seconds of silence of its own.'))

A(CARD('They did not withdraw communion.',
  'Make the Campbell connection here, out loud. The cue, from the <i>Declaration and Address</i> (1809, Appendix): &ldquo;no man can relinquish his opinions or practices till once convinced that they are wrong&hellip; One thing, however, he may do: when not bound by an express command, he need not impose them upon others, by anywise requiring their approbation.&rdquo; Luther claimed conscience for himself; Campbell extended it to his brother. The Synod could keep communion on its terms; he only asked to keep it on his.'))

A(Q('&ldquo;We do not desire, nor do we consider ourselves to be separated from the Presbyterian church, as Christians, whether ministers or people; we still wish to continue united to them in the bonds of love: <b>we will admit to communion as formerly, and desire to be admitted</b>. It is not our design to form a party.&rdquo;', 'The five, letter to their congregations, September 1803 &middot; in Stone, <i>Biography</i> (1847)', 'Exit without excommunication') +
  N('Their circular letter, written right after the protest. They withdrew from the Synod&rsquo;s jurisdiction, and in the same breath kept the table open both ways: they would still give communion to the men putting them out, and still ask to receive it from them.',
    '&rarr; They left the court. They did not leave the table.'))

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
  '<p class="bigquote"><span class=q>One of the committee, Matthew Houston, &ldquo;became convinced that the doctrine we preached was true, and <b>soon after united with us</b>.&rdquo;</span></p>'
  '<div class=cite>' + STONE + '</div>'
  '<aside class=notes>A smile. The committee sent to bring them back lost a member to them.</aside></section>')

A('<section class="slide"><div class=eyebrow>Another of the committee</div>'
  '<div class=litany>'
  '<div class=no>&ldquo;Old father David Rice&rdquo; argued &ldquo;that every departure from Calvinism was an advance to atheism&rdquo;:</div>'
  '<div class="no frag" style="color:var(--gold)">Calvinism &rarr; Arminianism &rarr; Pelagianism &rarr; deism &rarr; atheism</div>'
  '</div><div class=cite>' + STONE + '</div>'
  '<aside class=notes>One click. Rice was the father of Kentucky Presbyterianism and Stone honors him (&ldquo;of precious memory&rdquo;), but his argument, Stone says, &ldquo;could have no effect on minds ardent in the search of truth.&rdquo; The logic: the creed is the only thing between you and atheism. Last week answered that.<br>&rarr; Then the Synod suspended them anyway, and sent committees to read &ldquo;the Synod&rsquo;s bull of suspension&rdquo; in their pulpits and declare their churches vacant.</aside></section>')

# ---------- 2 THE COST ----------
A(Q('&ldquo;I called together my congregations, and informed them that I could no longer conscientiously preach to support the Presbyterian church&hellip; that I absolved them from all obligations in a pecuniary point of view, and then <b>in their presence tore up their salary obligation to me</b>&hellip;&rdquo;', STONE, 'Cane Ridge and Concord &middot; late 1803') +
  N('Mime it if you like. He kept preaching to them, &ldquo;but not in the relation that had previously existed between us.&rdquo; Of the people: &ldquo;Never have I found a more loving, kind, and orderly people in any country.&rdquo; Of the day: &ldquo;This was truly a day of sorrow, and the impressions of it are indelible.&rdquo;'))

A(Q('&ldquo;I preferred honesty and a good conscience to all these things. Having now no support from the congregations, and having emancipated my slaves, I turned my attention cheerfully, though awkwardly, to labor on my little farm&hellip; often on my return home, <b>I found the weeds were getting ahead of my corn</b>.&rdquo;', STONE) +
  N('He had already freed the people he had enslaved. Now no salary either. He preached almost every night and worked the field at night &ldquo;while others were asleep.&rdquo;',
    '&rarr; And here is the surprise: they flourished.'))


# ---------- 3 FORMED AND FLOURISHING ----------
A(C('The Rise of the Springfield Presbytery', 'Late 1803 to 1804.'))

A('<section class="slide">'
  '<div class=litany>'
  '<div class="no">They form the <b>Springfield Presbytery</b> and publish the <i>Apology</i>.</div>'
  '<div class="no frag">The <i>Apology</i> &ldquo;was quickly <b>republished by the Methodists</b> in Virginia&hellip;&rdquo;</div>'
  '<div class="no frag">Pamphlets against them, &ldquo;full of misrepresentation and invective,&rdquo; <b>spread their views</b>.</div>'
  '<div class="no frag">People &ldquo;disgusted and offended&rdquo; by the attacks &ldquo;were driven from them, and <b>cleaved to us</b>.&rdquo;</div>'
  '</div><div class=cite>' + STONE + '</div>'
  '<aside class=notes>Three clicks. The Methodists reprinted it &ldquo;except our remarks upon creeds.&rdquo; Stone: &ldquo;This book produced a great effect in the Christian community.&rdquo;</aside></section>')

A(CARD('The Springfield Presbytery<br>' + G('flourished.'),
  'Churches planted, preachers multiplied. &rarr; Which is exactly when the problem began.'))

# ---------- 4 CHURCH GOVERNMENT ----------
# ---------- 5 WHY THEY DISSOLVED ----------
A(Q('&ldquo;&hellip;they endeavored to cultivate a spirit of love and unity with all Christians; but found it extremely difficult to suppress the idea that they themselves were a party separate from others. <b>This difficulty increased in proportion to their success in the ministry.</b> <b>Jealousies were excited in the minds of other denominations</b>&hellip;&rdquo;', WIT, 'Why they did it') +
  N('The witnesses who signed the will, explaining it. They left a party because it fenced Christians apart. Now people saw them as a party, and they began to feel like one. Stone: &ldquo;we had not worn our name more than one year, before we saw it savored of a party spirit.&rdquo;'))

A(CARD('Success was making them<br>' + G('the thing they had protested.'),
  'Say it once. Failure would have been easy to read; success was the danger.'))

A(CARD('They caught their own presbytery<br>' + G('being handed a job only Christ can do.'),
  'Last week&rsquo;s thesis, lived five years before it was written: anything asked to do a job only Christ can do will fail. They did not wait for it to fail.'))

A(Q('&ldquo;Therefore, from a principle of love to Christians of every name, the precious cause of Jesus, and <b>dying sinners who are kept from the Lord by the existence of sects and parties</b> in the church, they have cheerfully consented to retire from the din and fury of conflicting parties &mdash; sink out of the view of fleshly minds, and die the death.&rdquo;', WIT, 'Why') +
  N('The three reasons: love of Christians of every name; the cause of Jesus; and the people outside, kept from the Lord by our divisions. &rarr; So they wrote their will.'))

# ---------- 4 THE READING OF THE WILL ----------
A('<section class="slide room"><h2 style="max-width:none">How do we claim the unity of the body of Christ?</h2>'
  '<h2 class=frag style="max-width:none;margin-top:3vmin">How do we live that now?</h2>'
  '<h2 class=frag style="max-width:none;margin-top:3vmin;color:var(--gold)">And what does it ask of our conscience?</h2>'
  '<aside class=notes>Two clicks. For them these were not two questions but one. What does unity compel conscience to do: to extend, to give up. &rarr; &ldquo;Here is how far they were willing to take it.&rdquo;</aside></section>')

A(C('The Last Will &amp; Testament', 'Cane Ridge, June 28, 1804.'))

A('<section class="slide bleed"><div class=bg><div class="bgimg househbg"></div></div>'
  '<div class=credit>Cane Ridge Meeting House &middot; HABS, Theodore Webb, 1934</div>'
  '<div class=eyebrow>Cane Ridge &middot; June 28, 1804</div>'
  '<h2>The reading of the will.</h2>'
  '<aside class=notes>Back to the room of Chapter 1. Three years earlier, thousands came through the mud to an open table here. The will is dated &ldquo;sitting at Cane Ridge,&rdquo; by tradition in this meetinghouse. Signed by six: the five from the garden and David Purviance.</aside></section>')

A(Q('&ldquo;For where a testament is, there must of necessity be <b>the death of the testator</b>&hellip; Verily, verily I say unto you, except a corn of wheat fall into the ground and die, it abideth alone; but <b>if it die, it bringeth forth much fruit</b>.&rdquo;', 'The will&rsquo;s epigraph &middot; Hebrews 9:16; John 12:24', 'At the top of the page') +
  N('They put the theology at the top. A will has no force while the testator lives. The inheritance can only pass when the presbytery is gone.'))

A(Q('&ldquo;The Presbytery of Springfield, sitting at Cane Ridge&hellip; being, through a gracious Providence, <b>in more than ordinary bodily health, growing in strength and size daily</b>, and in perfect soundness and composure of mind; but knowing that it is appointed for all delegated bodies once to die&hellip; do make and ordain this our Last Will and Testament&hellip;&rdquo;', WILL, 'June 28, 1804') +
  N('The will&rsquo;s opening, in the legal form of a real will. Read it slowly; the joke is in &ldquo;more than ordinary bodily health.&rdquo; Nobody makes a will because they are growing in strength and size daily.',
    '&rarr; This church body was nine months old, and thriving.'))

A('<section class="slide breath"><h2 style="max-width:none;font-size:clamp(48px,10vmin,128px);line-height:1.1">&ldquo;&hellip;it is appointed for<br>all delegated bodies<br>' + G('once to die.') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + WILL + '</div>'
  '<aside class=notes>From the preamble, after &ldquo;more than ordinary bodily health.&rdquo; Hebrews 9:27, &ldquo;it is appointed unto men once to die,&rdquo; applied to institutions. Every presbytery, synod, board and program is a delegated body: it holds authority on loan. It is mortal by design.</aside></section>')

A(Q('&ldquo;Imprimis. We will, that this body <b>die, be dissolved, and sink into union with the Body of Christ at large</b>; for there is but one body, and one spirit, even as we are called in one hope of our calling.&rdquo;', WILL, 'First bequest') +
  N('The line we opened with; now the room knows how they got here. &ldquo;Imprimis&rdquo;: in the first place, the legal word. Ephesians 4:4. The presbytery does not dissolve into nothing; it sinks into the whole church. The heir is the Body of Christ at large.'))


A(Q('&ldquo;We will, that our name of distinction, with its Reverend title, <b>be forgotten</b>, that there be but one Lord over God&rsquo;s heritage, and his name one.&rdquo;', WILL, 'Their name') +
  N('A will gives things away; this one gives away everything a church body has, starting with its name and its titles. They took the name Christian (Rice Haggard&rsquo;s pamphlet).'))

A(Q('&ldquo;We will, that preachers and people, cultivate a spirit of mutual forbearance; <b>pray more and dispute less</b>; and while they behold the signs of the times, look up, and confidently expect that redemption draweth nigh.&rdquo;', WILL, 'To preachers and people') +
  N('A church that has given away its courts has nothing left to settle its quarrels but forbearance and prayer, and the will says so in the same breath. Then: look up; redemption draweth nigh. They died expecting the future.'))


A(Q('&ldquo;We will, that our weak brethren, who may have been <b>wishing to make the Presbytery of Springfield their king</b>, and wot not what is now become of it, betake themselves to the Rock of Ages, and follow Jesus for the future.&rdquo;', WILL, 'Their weak brethren') +
  N('Their own people. Gentle, and a little funny: &ldquo;wot not what is now become of it.&rdquo; The presbytery was being asked to stand where Christ stands.'))
A(Q('&ldquo;&hellip;from its first existence it [the Springfield Presbytery] was knit together in love, lived in peace and concord, and <b>died a voluntary and happy death</b>.&rdquo;', WIT, 'The witnesses to the will') +
  N('Not a split, not a failure, not a scandal. A happy death.'))


A(Q('&ldquo;We heartily unite with our <b>Christian brethren of every name</b>, in thanksgiving to God for the display of his goodness in the glorious work he is carrying on&hellip; which we hope will terminate in <b>the universal spread of the Gospel, and the unity of the church</b>.&rdquo;', WIT, 'The last words') +
  N('The closing sentence of the whole pamphlet, just before &ldquo;The End.&rdquo; The cut is &ldquo;in our Western country.&rdquo; Cane Ridge is still the background: the glorious work is the revival.'))
A(Q('&ldquo;Having divested ourselves of all party creeds, and party names, and trusting alone in God, and the word of his grace, we became a by-word and laughing stock to the sects around; all prophesying our speedy annihilation. Yet <b>from this period I date the commencement of that reformation</b>, which has progressed to this day.&rdquo;', STONE, 'After the will') +
  N('&ldquo;Party names&rdquo; is the name Springfield Presbytery. Just before this: &ldquo;we had not worn our name more than one year, before we saw it savored of a party spirit. With the man-made creeds we threw it overboard, and took the name Christian.&rdquo;',
    'Stone does not date the movement from Cane Ridge in 1801, or from the garden in 1803. He dates it from here: the giving up of the party.'))

A(CARD('A will only takes effect<br>when someone dies.<br>' + G('The heir was the whole church of Christ.'),
  'Let it sit before the room.'))

# ---------- 7 THE BEQUEST ----------
A(C('The Bequest', 'On church government: what the heir received.'))

A(Q('&ldquo;&hellip;<i>Observations on Church Government</i>, in which the world will see <b>the beautiful simplicity of Christian church government, stript of human inventions and lordly traditions</b>.&rdquo;', WIT, 'Writing a book on church government') +
  N('Back to their last meeting before the will: they set out to write a book on church government. What they found was not only an absence. The authority Christ gave belongs to the gathered church; the will says so: &ldquo;native right of internal government&rdquo;, &ldquo;Christ speaking in them.&rdquo; Your reading, and say it as yours: Matthew 18:20, where two or three are gathered (next week&rsquo;s title); every believer a priest. Every other institution answers to that.',
    'At their last meeting they set out to write <i>Observations on Church Government</i>. The next sentence: &ldquo;As they proceeded in the investigation of that subject, they soon found that there was neither precept nor example in the New Testament for such confederacies as modern Church Sessions, Presbyteries, Synods, General Assemblies, etc.&rdquo; The research convicted the researchers: their own presbytery was one of these confederacies. &ldquo;While they continued in the connection in which they then stood, they were off the foundation of the Apostles and Prophets.&rdquo; (The book never appeared.)'))

A(Q('&ldquo;We will, that our power of making laws for the government of the church, and executing them by delegated authority, <b>forever cease</b>; that the people may have free course to the Bible, and adopt <b>the law of the spirit of life in Christ Jesus</b>.&rdquo;', WILL, 'Their power') +
  N('Not abolished: bequeathed. The power to make law for the church goes back to where they think it belongs.'))

A(Q('&ldquo;We will, that the church of Christ assume her <b>native right of internal government</b>&hellip; and admit no other proof of their authority, but Christ speaking in them.&rdquo;', WILL, 'To the church') +
  N('&ldquo;Native&rdquo;: it was always hers. The church will &ldquo;try her candidates for the ministry, as to their soundness in the faith, acquaintance with experimental religion, gravity and aptness to teach.&rdquo; What the Synod did to McNemar, the congregation now does, and the only credential is &ldquo;Christ speaking in them.&rdquo;'))

A(Q('&ldquo;We will, that each particular church, as a body, <b>actuated by the same spirit</b>, choose her own preacher, and support him by a free will offering&hellip; admit members &mdash; remove offences; and <b>never henceforth delegate her right of government to any man or set of men whatever</b>.&rdquo;', WILL, 'To every congregation') +
  N('The biggest bequest. Everything the Synod did to them (try preachers, admit, exclude) is handed to the congregation. The priesthood of all believers, as polity.',
    '&rarr; Hold this one. Next week, at Brush Run, a congregation will use exactly this right.'))

A(Q('&ldquo;We will, that candidates for the Gospel ministry henceforth study the holy scriptures with fervent prayer, and <b>obtain license from God to preach the simple Gospel, with the Holy Ghost sent down from heaven</b>, without any mixture of philosophy, vain deceit, traditions of men, or the rudiments of the world.&rdquo;', WILL, 'To the ministers') +
  N('No presbytery to license a preacher now. The license comes from God, and the Spirit is the credential.'))

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
  '</div><aside class=notes>All three at once, before the discussion.</aside></section>')
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
