# -*- coding: utf-8 -*-
# Chapter 5 — Wherever Two or Three Are Gathered: the Brush Run ordination (1810–1812), with Alexander
# Campbell's shipwreck leading up to it, tied back to the Declaration and Address and the Last Will.
# Built as a map deck:  python3 decks/src/week5map/build.py   (runs the Chapter 3 engine with PART=5)
# Sources: Robert Richardson, Memoirs of Alexander Campbell, vol. 1 (1868), which quotes the Synod of
# Pittsburg's minutes, Alexander's reply, his sermon notes and his ordination certificate; excerpts in
# decks/src/week5map/sources/. The Declaration and Address and the Last Will from the class site's full texts.
# Notes are a cue card: fact / source / your line. "→" marks a line that is Micah's to say.
import importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
w4 = _load('w4slides', 'week4/slides.py')
R = _load('resources', 'resources.py')       # shared side paths and documents (decks/src/resources.py)
w3 = w3b.w3
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS

C, CARD, G, plain, BLACK = w4.C, w4.CARD, w4.G, w4.plain, w4.BLACK
Q, N = w3.Q, w3.N
def DIM(slide, bg, credit=''):   # a slide over a darkened picture
    cr = '<div class=credit>%s</div>' % credit if credit else ''
    return slide.replace('<section class="slide', '<section class="slide bleed midbleed dimbg', 1).replace(
        '<div class=bg><div class="bgimg lutherbg"></div></div>', '', 1).replace(
        '">', '">%s<div class=bg><div class="bgimg %s"></div></div>' % (cr, bg), 1)
def BIGQ(slide, size='clamp(30px,6.4vmin,80px)', width='40ch'):   # a quote set larger than Q's default
    return re.sub(r'<p class="bigquote( long| xlong)?">', lambda m: '<p class="bigquote%s" style="font-size:%s;max-width:%s;line-height:1.22">' % (m.group(1) or '', size, width), slide, 1)

RICH = 'Robert Richardson, <i>Memoirs of Alexander Campbell</i> (1868)'
AC = 'Alexander Campbell'
MIN = 'Minutes of the Synod of Pittsburg, October 1810 &middot; in Richardson, <i>Memoirs</i>'
DA = 'Thomas Campbell, <i>Declaration and Address</i> (1809)'
WILL = w4.WILL

IDEAS = [
    ('The priesthood of all believers<br>' + G('is real authority.'),
     'It inheres in every Christian and in the gathered church, not in an order above them. &ldquo;The clergy are the opposite to the laity&hellip; Trace them to their origin and we find no difference.&rdquo; Our movement embraces this deeply: no clergy-laity line, any brother may preside at the table.'),
    ('The power to ordain<br>' + G('belongs to the people.'),
     '&ldquo;It is not the persons called bishops who have the power, but the people.&rdquo; Ordination does not confer authority; it testifies to it. Cane Ridge willed it in 1804; Brush Run did it in 1812.'),
    ('The table is a taste of<br>' + G('the age to come.'),
     'At the first Lord&rsquo;s Supper at Brush Run: &ldquo;an emblem of the millennial state of the Church&rdquo;, men of different names sitting down together in the kingdom of God. Not a memorial only: God&rsquo;s future, arriving early. That is why the fences around it had to come down. &rarr; Next week: the Millennial Harbinger.'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>'
            % (k, len(IDEAS), h, n))

S = []
A = S.append
def HIDE(slide): pass   # a hidden slide: kept here, left out of the deck (change HIDE back to A to show it)

# ---------- OPENING ----------
A(w3b.S[0])                                     # the class title

A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none">Which is the preferred title for our preacher?</h2>'
  '<div class="litany" style="text-align:left;gap:1.6vmin;margin-top:4vmin">'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">A.</span>Pastor</div>'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">B.</span>Reverend</div>'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">C.</span>Brother<span class=frag style="color:var(--gold);margin-left:.5em">&larr;</span></div>'
  '<div class=no style="position:relative"><span style="color:var(--gold);display:inline-block;width:1.6em">D.</span>None of the above</div>'
  '</div>'
  '<aside class=notes>One click points to C. Let the room argue first; &ldquo;none of the above&rdquo; (minister, evangelist, preacher) is a fair answer too.<br>&bull; Not &ldquo;Reverend&rdquo;: the Last Will willed that title &ldquo;be forgotten&rdquo; (last week). Not &ldquo;Pastor&rdquo;: in the New Testament the pastors are the elders.</aside></section>')

# ---------- THE HOOK ----------
A('<section class="slide breath"><div class=eyebrow>Why the Synod would not have them</div>'
  '<h2 style="max-width:22ch;font-size:clamp(44px,8.6vmin,112px);line-height:1.12">&ldquo;for encouraging or countenancing his son to preach the gospel ' + G('without any regular authority') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + MIN + '</div>'
  '<aside class=notes>The cold open. No clicks. Thomas Campbell asked the Presbyterian Synod to take him in, October 1810. One of their reasons for refusing was his son.<br>&rarr; &ldquo;Who gave him authority? That is tonight&rsquo;s question.&rdquo;</aside></section>')

_last = [x for x in w4.S if 'class="litany ideasum"' in x and '<div class=eyebrow>Ideas</div>' in x]
assert len(_last) == 1
A(_last[0].replace('<div class=eyebrow>Ideas</div>', '<div class=eyebrow>Last week&rsquo;s ideas</div>')
  .replace('All three at once, before the discussion.', 'Last week&rsquo;s three, all at once. Read them, or let the room read them.<br>&rarr; &ldquo;Idea three: Stone&rsquo;s side willed it in 1804. Tonight, the Campbells&rsquo; side does it.&rdquo;'))

A('<section class="slide room"><h2 style="max-width:16ch;font-size:clamp(44px,11vmin,130px);line-height:1.12">Who has authority?</h2>'
  '<aside class=notes>Alexander&rsquo;s own question, when he was asked why he preached without it (we will get to his answer). Who can make someone a minister? A bishop? A presbytery? The congregation? &rarr; &ldquo;Hold that.&rdquo;</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 5</div>'
  '<h1>Wherever Two or Three<br>Are Gathered</h1><div class=table-line></div>'
  '<div class=sub>Brush Run, Pennsylvania &middot; 1811&ndash;1812</div>'
  '<aside class=notes>Matthew 18:20, and the <i>Declaration and Address</i> quotes it (we will see where). The Campbells&rsquo; side of the story, picking up where Chapter 2 left Alexander: off the coast of Scotland.<br>'
  'The hour: the sea 6 &middot; the first sermon 4 &middot; the Synod 8 &middot; Alexander answers 6 &middot; Brush Run 10 &middot; the ordination 10 &middot; tying back 5 &middot; close 10.</aside></section>')

# ---------- ALEXANDER AND THE SEA ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg5"></div></div>'
  '<div class=credit>Philippe-Jacques de Loutherbourg, <i>A Shipwreck off a Rocky Coast</i> &middot; not the Hibernia</div>'
  '<div class=eyebrow>Islay, Scotland &middot; October 7, 1808</div>'
  '<h2>Alexander and the Sea</h2>'
  '<aside class=notes>Recap from Chapter 2, quickly. His father is in America, already on trial before the Seceders. Alexander, twenty, sails with his mother and the children on the Hibernia. It drags its anchors in a gale and strikes a rock off Islay at night. They cut away the masts.</aside></section>')

A(DIM(Q('&ldquo;It was then in that solemn hour, that he gave himself up wholly to God, and resolved that, if saved from the present peril, <b>he would certainly spend his entire life in the ministry of the gospel</b>.&rdquo;', RICH, 'On the stump of the broken mast'), 'wreckbg5') +
  N('He sat on the stump of the broken mast and &ldquo;thought of his father&rsquo;s noble life.&rdquo; Everyone survived; the family wintered in Glasgow.',
    '&rarr; &ldquo;Hold the mast. It comes back at the ordination.&rdquo;'))

A('<section class="slide"><div class=eyebrow>Glasgow &middot; 1808&ndash;09 &middot; from Chapter 2</div>'
  '<div class="litany bigl">'
  '<div class="no frag">He heard other preachers, the thing his father was condemned for.</div>'
  '<div class="no frag">He heard of the Haldanes: <b>laymen who preached without ordination</b>.</div>'
  '<div class="no frag">He held a communion token, and <b>would not use it</b>.</div>'
  '</div><aside class=notes>Three clicks, one per line; quickly, the room has heard it. The Haldanes matter tonight: two Scottish laymen, preaching the gospel unordained, one of them arrested at the clergy&rsquo;s instigation.</aside></section>')

A(Q('&ldquo;&hellip;instead of fearing opposition from him to the views to which he had himself been definitely brought while in Glasgow, he found him already, though by a somewhat different method, <b>led practically to the very same conclusions</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:220', 'On the road, 1809') +
  N('He lands in the autumn of 1809, crosses the mountains, and meets his father on the road. Thomas has just written the <i>Declaration and Address</i>, and Alexander reads it in proof.',
    '&rarr; &ldquo;Father and son, an ocean apart, arrive at the same place.&rdquo;'))

# ---------- THE FIRST SERMON ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg grovebg5"></div></div>'
  '<div class=credit>An American forest, 19th-century painting &middot; not the Templeton farm</div>'
  '<div class=eyebrow>July 15, 1810 &middot; a grove on Major Templeton&rsquo;s farm</div>'
  '<h2>His first sermon</h2>'
  '<aside class=notes>Eight miles from Washington, Pennsylvania. He was twenty-one. His father had had him speak once, briefly, at a house meeting that spring; this was his first real sermon, written out and memorized.</aside></section>')

A(BIGQ(Q('&ldquo;When the hour arrived, he rose up with modest dignity, in the temporary stand erected for the occasion, in front of which the audience were seated <b>upon rough planks or upon the grass beneath the shady maples</b>&hellip;&rdquo;', RICH)) +
  N('His text: the close of the Sermon on the Mount, Matthew 7:24&ndash;27, the wise man who built his house upon a rock.',
    'No church building, no ordination, no license.'))

A(CARD('In his first year he preached<br>' + G('one hundred and six sermons.'),
  'Richardson: &ldquo;no less than one hundred and six sermons&rdquo;, at the crossroads, in Washington, at Buffalo, in houses, into Ohio. Nobody had ordained him. &rarr; &ldquo;Someone noticed.&rdquo;'))

# ---------- THE SYNOD ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg synodbg5"></div></div>'
  '<div class=credit>The Synod of Dort, 1618&ndash;19 &middot; painting attributed to Pouwels Weyts, c. 1621</div>'
  '<div class=eyebrow>Washington, Pennsylvania &middot; October 1810</div>'
  '<h2>The Synod of Pittsburg</h2>'
  '<aside class=notes>The Presbyterian synod, meeting in their own town. Thomas feared that the Christian Association was drifting into a new party, the one thing he did not want. A Presbyterian pastor (John Anderson of Upper Buffalo) urged him to apply. So he asked to be taken in, Association and all: &ldquo;Christian union upon Christian principles.&rdquo; Alexander disapproved and expected nothing, but did not oppose his father.<br>(The picture is the Synod of Dort, from last week.)</aside></section>')

A(DIM(BIGQ(Q('&ldquo;&hellip;the Synod unanimously resolved, that <b>however specious the plan</b> of the Christian Association and <b>however seducing its professions</b>&hellip; the Synod are constrained to disapprove the plan and its native effects.&rdquo;', MIN, 'October 4, 1810')), 'synodbg5') +
  N('The cut: &ldquo;as experience of the effects of similar projects in other parts has evinced their baleful tendency and destructive operations on the whole interests of religion by promoting divisions instead of union, by degrading the ministerial character&hellip;&rdquo;',
    'A plan for unity, refused for promoting division.'))

A(DIM(BIGQ(Q('&ldquo;&hellip;Mr. Campbell&rsquo;s request to be received into ministerial and Christian communion <b>cannot be granted</b>.&rdquo;', MIN), 'clamp(36px,8vmin,100px)', '30ch'), 'synodbg5') +
  N('&ldquo;For the above and many other important reasons.&rdquo; Thomas came back the next day and asked what the &ldquo;important reasons&rdquo; were.'))

A(DIM('<section class="slide"><div class=eyebrow>The &ldquo;important reasons,&rdquo; October 5</div>'
  '<div class=litany style="font-size:1.3em;max-width:88vw">'
  '<div class="no frag">&ldquo;for expressing his belief that there are some opinions taught in our Confession of Faith which are not founded in the Bible&rdquo;</div>'
  '<div class="no frag">&ldquo;for declaring that the administration of baptism to infants is not authorized by scriptural precept or example&rdquo;</div>'
  '<div class="no frag" style="color:var(--gold)">&ldquo;for encouraging or countenancing his son to preach the gospel without any regular authority&rdquo;</div>'
  '<div class="no frag">&ldquo;for opposing creeds and confessions as injurious to the interests of religion&rdquo;</div>'
  '</div><div class=cite>' + MIN + '</div>'
  '<aside class=notes>Four clicks. The third is the cold open. The list ends: &ldquo;because it is not consistent with the regulations of the Presbyterian Church that Synod should form a connection with any ministers, churches or associations.&rdquo; Thomas, reading it, said he felt &ldquo;quite relieved&rdquo;: it was not for any immorality.</aside></section>', 'synodbg5'))

# side path: the Confession against itself (shared resource), with the Synod of Pittsburg's case
for _x in R.westminster(extra=[
    Q('&ldquo;The Confession of Faith of the Synod declared the Bible to be the only rule of faith and practice, and yet when a respectable body of religious persons apply for admission, they are ruled out, <b>because they will have no other rule than the Bible</b>!&rdquo;', RICH, 'The Synod of Pittsburg, by its own Confession') +
    N('Richardson&rsquo;s comment on the Synod&rsquo;s refusal. He goes on: &ldquo;In the case of Thomas Campbell it was the &lsquo;Confession,&rsquo; and not the Bible, that was made the standard by which one of the best of men was denied religious fellowship.&rdquo;')]):
    A(_x)

A(CARD('Rejected by the Seceders in 1808.<br>' + G('Rejected by the Presbyterians in 1810.'),
  'Twice now, for the same thing: the Bible alone, and a table open to other Christians. &rarr; &ldquo;And the Synod had named the son. The son answered.&rdquo;'))

# ---------- ALEXANDER ANSWERS ----------
A(C('Alexander Answers', 'Washington, November 1, 1810: an address at a regular meeting of the Christian Association, defending it against the Synod. He was twenty-two. His father had promised in the <i>Declaration and Address</i> not to dispute in public; the son had promised nothing.'))

A(Q('&ldquo;It is again objected that it opens a door for <b>lay preaching</b>.&rdquo;', AC + ', reply to the Synod, November 1810') +
  N('He takes the Synod&rsquo;s charges one by one. This is the charge about him.',
    'His first answer: the Association&rsquo;s twelfth proposition asks for ministers &ldquo;duly and scripturally qualified.&rdquo; &ldquo;Are lay preachers the only persons &lsquo;duly and scripturally qualified?&rsquo; If they be, let us have a number of them.&rdquo;'))

A(BIGQ(Q('&ldquo;The clergy are the opposite to the laity. Both these terms are used in Scripture to denote <b>God&rsquo;s people</b>. Trace them to their origin and <b>we find no difference</b>.&rdquo;', AC + ', reply to the Synod, November 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('<i>Laos</i>, &ldquo;people&rdquo;: God&rsquo;s people. <i>Kleros</i>, &ldquo;lot, inheritance&rdquo;: also God&rsquo;s people (1 Peter 5:3, &ldquo;not as lords over God&rsquo;s heritage&rdquo;). Both words name the whole church.',
    '&rarr; &ldquo;The line the Synod was guarding is not in the Bible.&rdquo;'))

A(BIGQ(Q('&ldquo;We would be obliged to some person of <b>exquisite keenness of distinction</b> to point out and define the difference between laical and clerical preachers.&rdquo;', AC + ', reply to the Synod, November 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('A smile. Twenty-two years old, answering a synod.'))

A('<section class="slide"><div class=eyebrow>Richardson&rsquo;s note</div>'
  '<p class="bigquote long"><span class=q>&ldquo;&hellip;there is not, in Scripture, the slightest ground for the distinction between clergy and laity. On the contrary, all the disciples collectively are denominated a <b>&lsquo;royal priesthood,&rsquo;</b>&hellip;&rdquo;</span></p>'
  '<div class=cite>' + RICH + ', footnote to the reply</div>'
  '<aside class=notes>Side path: Richardson&rsquo;s gloss, not Campbell&rsquo;s words. 1 Peter 2:9; Revelation 5:10, &ldquo;kings and priests to God.&rdquo; The priesthood of all believers, in a footnote.</aside></section>')

A(BIGQ(Q('&ldquo;I dare not be a party man for these reasons&hellip; <b>Because no party will receive into communion all whom God would receive into heaven.</b>&rdquo;', AC + ', 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('From an address after a sermon at Mr. Buchanan&rsquo;s, the same season. The next line: &ldquo;God loves his children more than our creeds, and man was not made for the Bible, but the Bible for man.&rdquo;',
    'Chapter 1&rsquo;s table and Chapter 2&rsquo;s trial, in one sentence.'))
for _x in R.campbell_reread(): A(_x)             # side path: Alexander Campbell, reread (shared resource)

# ---------- BRUSH RUN ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg brushbg"></div></div>'
  '<div class=credit>The Brush Run meeting house, reconstructed at Bethany &middot; courtesy of Bethany College</div>'
  '<div class=eyebrow>May 4, 1811</div>'
  '<h2>Brush Run</h2>'
  '<aside class=notes>A creek and a few farms, about eight miles from Washington. The meeting house was a plain frame building, never finished; it was later sold, moved, used as a blacksmith shop, a post office and a barn, and rebuilt at Bethany in 1909.</aside></section>')

A(BIGQ(Q('&ldquo;It was with <b>great reluctance</b> that he finally concluded to take this step, and to separate himself from those whom he desired to recognize as brethren.&rdquo;', RICH, 'Thomas Campbell, spring 1811')) +
  N('Every overture refused, Thomas concluded &ldquo;that the Christian Association should assume the character of an independent Church.&rdquo; The thing he had dreaded since 1809.'))

A(BIGQ(Q('&ldquo;This Society <b>by no means considers itself a Church</b>, nor does at all assume to itself the powers peculiar to such a society&hellip;&rdquo;', DA + ', Resolution IV')) +
  N('What they promised in 1809: &ldquo;merely as voluntary advocates for Church reformation.&rdquo; A society can preach; it cannot keep the Supper or ordain.',
    '&rarr; &ldquo;Now they would have to be one.&rdquo;'))

A(BIGQ(Q('&ldquo;Certainly, James Foster is a member, <b>having been with us from the beginning</b>, and his religious sentiments being perfectly well known to all.&rdquo;', 'Alexander Campbell, May 4, 1811 &middot; in Richardson, <i>Memoirs</i>', 'The test question')) +
  N('Thomas had each member answer a test question: &ldquo;What is the meritorious cause of a sinner&rsquo;s acceptance with God?&rdquo; Foster missed that meeting. Some said he was not a member. Alexander, &ldquo;not entirely convinced that there was any authority for such a test,&rdquo; stood up.',
    'Richardson: &ldquo;The test question, accordingly, was not propounded to him, nor to any one else afterward.&rdquo; No creed at the door, from the first day.'))

A(BIGQ(Q('&ldquo;At this meeting, <b>Thomas Campbell was appointed elder</b>, and <b>Alexander was licensed to preach the gospel</b>. Four deacons were also chosen&hellip;&rdquo;', RICH, 'May 4, 1811')) +
  N('The deacons: John Dawson, George Sharp, William Gilcrist, James Foster. About thirty members.',
    'No presbytery licensed him. The church did.'))

A(CARD('No bishop. No presbytery.<br>' + G('A congregation.'),
  'Let it sit. This is the thing the Synod could not imagine: a church that makes its own ministers.'))
for _x in R.governance(): A(_x)                   # side path: who governs the church (shared resource)

A('<section class="slide breath"><div class=eyebrow>What they sang &middot; Psalm 118, the Scottish metrical version</div>'
  '<div class=litany style="gap:.6vmin">'
  '<div class=no style="font-size:clamp(28px,5.4vmin,68px)">&ldquo;Thou sore hast thrust that I might fall;</div>'
  '<div class=no style="font-size:clamp(28px,5.4vmin,68px)">' + G('But my Lord helped me') + '&hellip;</div>'
  '<div class="no frag" style="font-size:clamp(28px,5.4vmin,68px);margin-top:2vmin">I shall not die, but live, and shall</div>'
  '<div class="no frag" style="font-size:clamp(28px,5.4vmin,68px)">' + G('The works of God discover') + '.&rdquo;</div>'
  '</div><div class=cite>' + RICH + '</div>'
  '<aside class=notes>One click. Verses 13 to 29, as they had sung them as Seceders. Richardson: &ldquo;these verses of the Psalm they sung had to them a peculiar significance.&rdquo; Rejected, and not dead.</aside></section>')

A('<section class="slide"><div class=eyebrow>The next day &middot; May 5, 1811 &middot; their first Lord&rsquo;s Supper</div>'
  '<p class="bigquote" style="font-size:clamp(30px,6.4vmin,80px);max-width:36ch;line-height:1.22"><span class=q>&ldquo;&hellip;in assembling there on that occasion, they furnished <b>an emblem of the millennial state of the Church</b>, nay, an emblem of the heavenly state, when men of different nations, and known by different names, <b>should sit down together in the kingdom of God</b>.&rdquo;</span></p>'
  '<div class=cite>Alexander Campbell&rsquo;s communion sermon &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>The high point of the hour. His text: John 6:48, &ldquo;I am that bread of life.&rdquo; Richardson is summarizing his sermon notes.<br>&rarr; &ldquo;The table is not only a memory. It is the future, arriving early: everyone who will be at the last table, at this one.&rdquo; Chapter 1&rsquo;s table, again.</aside></section>')

A(BIGQ(Q('&ldquo;&hellip;the Lord&rsquo;s Supper, which, according to the custom of the Independent churches in Scotland, <b>was now celebrated weekly</b>.&rdquo;', RICH, 'Every Lord&rsquo;s day')) +
  N('The Haldane churches again. At Cane Ridge the Supper came once or twice a year, after weeks of preparation and a token. At Brush Run, every Sunday, from the beginning. That is us.'))

A(BIGQ(Q('&ldquo;The reason being asked, Joseph Bryant replied, that <b>he did not consider himself authorized to partake</b>, as he had never been baptized.&rdquo;', RICH, 'Side path &middot; who was not at the table')) +
  N('Side path. Three members never baptized: Joseph Bryant, Margaret Fullerton, Abraham Altars. On July 4, 1811 Thomas Campbell immersed them in a deep pool of Buffalo Creek, standing on a root at the edge, unimmersed himself. The baptism question opens here; it gets its own chapter.'))

# ---------- THE ORDINATION ----------
A(C('The Ordination', 'Licensed in May 1811; ordained on January 1, 1812. He preached all over the region through 1811 and married Margaret Brown that March. At Christmas he sat down, as he did every year&rsquo;s end, to examine himself.', 'January 1, 1812'))

A('<section class="slide"><div class=eyebrow>December 25, 1811 &middot; his own list</div>'
  '<div class="litany" style="text-align:left;gap:1.4vmin">'
  '<div class=no style="font-size:clamp(24px,4.6vmin,58px)">&ldquo;Special instances of Divine power which I consider to bind me under obligations to be specially devoted to Him&hellip;</div>'
  '<div class="no frag" style="font-size:clamp(24px,4.6vmin,58px)">III. In resolving, when in imminent danger at sea, <b>to serve God in this way</b>, on two occasions of extraordinary deliverance&hellip;</div>'
  '<div class="no frag" style="font-size:clamp(24px,4.6vmin,58px)">XI. In giving me <b>a call from the Church</b> to preach the Gospel&hellip;</div>'
  '<div class="no frag" style="font-size:clamp(24px,4.6vmin,58px)">XII. In my desire to suffer hardships and reproach in that good work.&rdquo;</div>'
  '</div><div class=cite>' + AC + ' &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>Three clicks. Twelve reasons; three shown. The mast comes back: &ldquo;two occasions&rdquo; are the Hibernia off Islay in 1808, and the 1809 crossing on the Latonia, which sprang a leak and nearly went down in a squall.<br>Number XI: the call came from the church, not from a court.</aside></section>')

A(BIGQ(Q('&ldquo;You see that ordination is not a mere unmeaning thing, but <b>consists in the choice of the people</b>, which must be hearty&hellip;&rdquo;', AC + ', sermon on Titus 1:5 &middot; in Richardson, <i>Memoirs</i>'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('His notes for a sermon that winter. The sentence goes on: &ldquo;and that it might be evidenced, the elders or rulers impose their hands.&rdquo; The laying on of hands shows the choice; it does not make it.'))

A('<section class="slide breath"><p class="bigquote" style="font-size:clamp(38px,8.4vmin,108px);max-width:26ch;line-height:1.16"><span class=q>&ldquo;Why do we contend for uninterrupted succession in ordination, seeing it is <b>not the persons called bishops who have the power, but the people?</b>&rdquo;</span></p>'
  '<div class=cite>' + AC + ', sermon on Titus 1:5 &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>The second high point. No apostolic succession, no line of hands from Peter to now that makes a minister. The power is in the people.<br>Richardson: he did not regard ordination &ldquo;as conferring any authority, but as a public testimony that the persons ordained possessed the necessary authority.&rdquo;</aside></section>')

A('<section class="slide"><div class=eyebrow>Asked why he preached without authority</div>'
  '<div class=litany style="gap:1.2vmin">'
  '<div class=no style="font-size:clamp(30px,6vmin,76px)">&ldquo;<b>Who has authority?</b></div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to license men?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to make laws for the Church?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to decide religious matters by vote?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to choose ministers?&rdquo;</div>'
  '</div><div class=cite>' + AC + ' &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>Four clicks; the question keeps extending. The framing question of the hour, in his own mouth. He turns the Synod&rsquo;s charge around: the presbytery is the one without authority.</aside></section>')

A(BIGQ(Q('&ldquo;We do hereby certify that Alexander Campbell&hellip; was, <b>according to the principles of this Church</b> regularly chosen and ordained a minister thereof, upon the first day of January, one thousand eight hundred and twelve.&rdquo;', 'Certificate of ordination, recorded in the Brooke County court, December 1812 &middot; in Richardson, <i>Memoirs</i>')) +
  N('He needed it in court to be allowed to perform marriages. Signed at a church meeting at John Dawson&rsquo;s, September 1, 1812.',
    'The cut: &ldquo;after a due course of trials preparatory to the work of the holy ministry.&rdquo;'))

A('<section class="slide"><div class=eyebrow>Signed</div>'
  '<div class=litany style="gap:1vmin">'
  '<div class=no style="font-size:clamp(30px,5.8vmin,74px)">Thomas Campbell, senior minister</div>'
  '<div class="no frag" style="font-size:clamp(30px,5.8vmin,74px);color:var(--gold)">George Sharp &middot; William Gilcrist &middot; James Foster &middot; John Dawson, deacons</div>'
  '</div><div class=cite>The ordination certificate &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>One click. His father, and four farmers. One of them, James Foster, is the man nearly kept out by the test question. The man who would debate Robert Owen and the Catholic bishop of Cincinnati, and found a college, was ordained by a creekside congregation of about thirty.</aside></section>')
for _x in R.universals(): A(_x)                  # side path: the whole church remembers (shared resource)

# ---------- TYING BACK ----------
A(C('Two Wills, One Bequest', 'Tie it back. Kentucky, 1804, and Pennsylvania, 1811: neither side knew the other existed. Stone and Alexander Campbell would not meet until 1824.'))

A(BIGQ(Q('&ldquo;We will, that each particular church, as a body, actuated by the same spirit, <b>choose her own preacher</b>&hellip; and <b>never henceforth delegate her right of government to any man or set of men whatever</b>.&rdquo;', WILL, 'Cane Ridge, 1804')) +
  N('Last week: the bequest to every congregation. Seven years later and hundreds of miles away, a congregation that never heard of the will does exactly this.',
    'The ministers&rsquo; bequest, too: &ldquo;obtain license from God to preach the simple Gospel.&rdquo;'))

A(BIGQ(Q('&ldquo;&hellip;for where <b>two or three are gathered together in my name</b>, there am I in the midst of them.&rdquo;', DA + ', quoting Matthew 18:20'), 'clamp(36px,8vmin,100px)', '28ch') +
  N('The <i>Address</i>, to the friends of reform: &ldquo;Let not the paucity of your number in any given district, prove an insuperable discouragement.&rdquo; Thirty people at a creek. Christ in the midst of them.',
    '&rarr; The title of the hour.'))

A(CARD('The Springfield Presbytery died<br>so that congregations could choose.<br>' + G('Brush Run chose.'),
  'The two streams meet in 1832. They already agreed.'))

A(BLACK)

# ---------- CLOSE ----------
DISCUSS = re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): Who has authority in our congregation, and where did it come from? What would it mean to believe every member could be called? What does our table look like as a taste of the age to come?</aside>',
                 w3b.pick('&#9670; for discussion', 0), flags=re.S)
A(DISCUSS)
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A('<section class="slide room"><div class=eyebrow>Ideas</div>'
  '<div class="litany ideasum" style="text-align:left;gap:1.2vmin;margin-top:2.6vmin">'
  + ''.join('<div class=no><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (k, plain(h)) for k, (h, _) in enumerate(IDEAS, 1)) +
  '</div><aside class=notes>All three at once, before the discussion.</aside></section>')
A(DISCUSS)
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. The <i>Declaration and Address</i> and the <i>Last Will</i> are there in full; tonight&rsquo;s other source is Richardson&rsquo;s <i>Memoirs of Alexander Campbell</i> (1868).</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S))
A('<section class="slide"><h2>Next week: living into God&rsquo;s future.</h2>'
  '<div class="sub frag">&ldquo;An emblem of the millennial state of the Church.&rdquo; In 1830 he names a journal for it: the <i>Millennial Harbinger</i>.</div>'
  '<aside class=notes>Chapter 6. Alexander pivots from attack journalism to building for the age to come; eschatology as the movement&rsquo;s north star.</aside></section>')
A(BLACK)

# ---------- ADDENDUM ----------
A(C('Addendum', 'Reference material; not part of the telling.'))
A('<section class="slide"><div class=eyebrow>The year, in order</div>'
  '<div class="litany" style="text-align:left;gap:.8vmin">'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Oct 1808</b> &middot; the Hibernia wrecked off Islay; Glasgow for the winter</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Sep 1809</b> &middot; the <i>Declaration and Address</i>; Alexander lands, and reads it in proof</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Jul 15, 1810</b> &middot; first sermon, Templeton&rsquo;s grove</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Oct 4&ndash;5, 1810</b> &middot; the Synod of Pittsburg refuses Thomas Campbell</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Nov 1, 1810</b> &middot; Alexander&rsquo;s reply</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Mar 12, 1811</b> &middot; marries Margaret Brown</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>May 4&ndash;5, 1811</b> &middot; Brush Run constituted; first Lord&rsquo;s Supper</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Jul 4, 1811</b> &middot; the first immersions, in Buffalo Creek</div>'
  '<div class=no style="font-size:clamp(20px,3.6vmin,44px)"><b>Jan 1, 1812</b> &middot; Alexander ordained</div>'
  '</div><aside class=notes>All dates from Richardson, <i>Memoirs</i>, vol. 1.</aside></section>')
A('<section class="slide ideasmap"><div class=eyebrow>What this week touched</div>'
  '<div class=wmap><div class="r ms-christ"><span class="th on">CHRIST ALONE</span></div>'
  '<div class="r ms-pri"><span class="th on">UNITY</span><span class="th key">PRIESTHOOD</span><span class="th key">FUTURE</span></div>'
  '<div class="r ms-sec"><span class=th>HOMECOMING</span><span class=th>SELF-SACRIFICE</span><span class="th on">FREEDOM OF CONSCIENCE</span><span class=th>SCIENCE &amp; REASON</span><span class="th on">MINIMALISM</span></div>'
  '<div class="r ms-pra"><span class="th key">the Table</span><span class="th on">Baptism</span><span class="th on">Scripture</span><span class=th>Singing</span><span class="th key">Congregation</span></div></div>'
  '<div class=small>Bright: the spine of this week. Dim: touched in passing. Unlit: still ahead of us.</div>'
  '<aside class=notes>The values board. New light this week: Priesthood, Future (the millennial table), and Baptism, just glimpsed.</aside></section>')
