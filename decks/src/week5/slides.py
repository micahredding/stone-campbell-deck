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
CS = 'Alexander Campbell, <i>The Christian System</i> (1839), &ldquo;Breaking the Loaf&rdquo;'
def SRC(slide, key):   # check this slide's quotes against one shared document (resources.py: 'church', 'acr')
    return slide.replace('<section class="slide', '<section data-src=%s class="slide' % key, 1)

IDEAS = [
    ('The Lord&rsquo;s table<br>' + G('turns no Christian away.'),
     'Glasgow: the Haldanes&rsquo; church was formed to &ldquo;avoid that contracted spirit which would exclude&rdquo;; the Seceder table would not have had them. Alexander gave back the token. In 1810: no standard should &ldquo;reject those whom God has not rejected.&rdquo; Brush Run kept the table open to every Christian.'),
    ('The church can gather<br>' + G('for those who are shut out.'),
     'Brush Run became a church because its people were refused &ldquo;those privileges&hellip; which belong to the Church relation.&rdquo; No synod granted it; the people constituted it, with great reluctance, for each other&rsquo;s sake.'),
    ('The priesthood of all believers<br>' + G('makes its ministers.'),
     'Ordination &ldquo;consists in the choice of the people&rdquo;; the hands testify to an authority the church has already given. &ldquo;The community, the church, the multitude of the faithful, are the fountain of official power.&rdquo; No clergy-laity line. Side paths: who may ordain?; who may serve?; the whole church remembers.'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>'
            % (k, len(IDEAS), h, n))

S = []
A = S.append
def HIDE(slide): pass   # a hidden slide: kept here, left out of the deck (change HIDE back to A to show it)

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
A('<section data-src="fnd dna" class="slide" style="padding:0">'
  '<div style="position:absolute;inset:0;display:flex">'
'<div style="flex:1;position:relative;overflow:hidden;border-right:1px solid rgba(201,162,74,.35)">'
  '<div style="position:absolute;inset:0;background:url(IMG_STONE) center 20%/cover no-repeat;filter:brightness(.6) sepia(.25)"></div><div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(14,11,9,.25) 0%,rgba(14,11,9,.55) 40%,rgba(14,11,9,.85) 100%)"></div>'
  '<div style="position:relative;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;padding:12vh 3.5vw 7vh;text-align:center">'
  '<div class=q style="font-family:\'IM Fell English\',Georgia,serif;font-size:clamp(30px,5.8vmin,74px);line-height:1.18;color:var(--bone);text-shadow:0 1px 10px rgba(0,0,0,.95)">&ldquo;<b>Let the unity of Christians be our polar star.</b>&rdquo;</div>'
  '<div class=cite style="margin-top:2.4vmin;text-shadow:0 1px 8px #000">Barton W. Stone, <i>Christian Messenger</i>, 1832</div>'
  '</div></div>'
'<div style="flex:1;position:relative;overflow:hidden;border-right:1px solid rgba(201,162,74,.35)">'
  '<div style="position:absolute;inset:0;background:url(IMG_TCAMPBELL) center 20%/cover no-repeat;filter:brightness(.6) sepia(.25)"></div><div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(14,11,9,.25) 0%,rgba(14,11,9,.55) 40%,rgba(14,11,9,.85) 100%)"></div>'
  '<div style="position:relative;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;padding:12vh 3.5vw 7vh;text-align:center">'
  '<div class=q style="font-family:\'IM Fell English\',Georgia,serif;font-size:clamp(30px,5.8vmin,74px);line-height:1.18;color:var(--bone);text-shadow:0 1px 10px rgba(0,0,0,.95)">&ldquo;Resume <b>that precious, that dear-bought liberty</b>, wherewith Christ has made his people free&hellip;&rdquo;</div>'
  '<div class=cite style="margin-top:2.4vmin;text-shadow:0 1px 8px #000">Thomas Campbell, <i>Declaration and Address</i>, 1809</div>'
  '</div></div>'
  '</div>'
  '<h2 style="position:absolute;top:4.5vh;left:0;right:0;margin:0 auto;max-width:none;text-align:center;font-size:clamp(34px,6.6vmin,84px);color:var(--gold);text-shadow:0 1px 10px #000">Unity movement</h2>'
  '<aside class=notes>The recap, in two founders and their own words. Stone, &ldquo;An Address to the Churches of Christ&rdquo; (1832), urging his churches not to divide from Campbell&rsquo;s over the design of baptism; it goes on, &ldquo;that the world may believe, and be saved.&rdquo; In 1835: &ldquo;For 32 years of my ministry I have kept in view the unity of Christians as my polar star.&rdquo; Thomas Campbell, the Address (1809): &ldquo;Resume that precious, that dear-bought liberty, wherewith Christ has made his people free; a liberty from subjection to any authority but his own, in matters of religion.&rdquo; The same Address: &ldquo;With you all we desire to unite in the bonds of an entire Christian unity.&rdquo; Both opened the Lord&rsquo;s table to Christians of other names: Stone at Cane Ridge, Campbell at Conemaugh.</aside></section>')

A('<section data-src="dna will" class="slide" style="padding:0">'
  '<div style="position:absolute;inset:0;display:flex">'
'<div style="flex:1;position:relative;overflow:hidden;border-right:1px solid rgba(201,162,74,.35)">'
  '<div style="position:absolute;inset:0;background:url(IMG_DNA) center/cover no-repeat;filter:brightness(.55) sepia(.3)"></div><div style="position:absolute;inset:0;background:rgba(14,11,9,.62)"></div>'
  '<div style="position:relative;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:12vh 3.5vw 4vh;text-align:center">'
  '<div class=q style="font-family:\'IM Fell English\',Georgia,serif;font-size:clamp(30px,5.8vmin,74px);line-height:1.18;color:var(--bone);text-shadow:0 1px 10px rgba(0,0,0,.95)">&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>&hellip;&rdquo;</div>'
  '<div class=cite style="margin-top:2.4vmin;text-shadow:0 1px 8px #000">Thomas Campbell, <i>Declaration and Address</i>, 1809</div>'
  '<div style="font-family:Spectral,Georgia,serif;color:var(--gold);font-size:clamp(20px,3.4vmin,42px);line-height:1.25;margin-top:2vmin;text-shadow:0 1px 8px #000">Unity, extending freedom of conscience to all</div>'
  '</div></div>'
'<div style="flex:1;position:relative;overflow:hidden;border-right:1px solid rgba(201,162,74,.35)">'
  '<div style="position:absolute;inset:0;background:url(IMG_LWT) center/cover no-repeat;filter:brightness(.55) sepia(.3)"></div><div style="position:absolute;inset:0;background:rgba(14,11,9,.62)"></div>'
  '<div style="position:relative;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:12vh 3.5vw 4vh;text-align:center">'
  '<div class=q style="font-family:\'IM Fell English\',Georgia,serif;font-size:clamp(30px,5.8vmin,74px);line-height:1.18;color:var(--bone);text-shadow:0 1px 10px rgba(0,0,0,.95)">&ldquo;We will, that this body die, be dissolved, and <b>sink into union with the Body of Christ at large</b>&hellip;&rdquo;</div>'
  '<div class=cite style="margin-top:2.4vmin;text-shadow:0 1px 8px #000">The Last Will and Testament of the Springfield Presbytery, 1804</div>'
  '<div style="font-family:Spectral,Georgia,serif;color:var(--gold);font-size:clamp(20px,3.4vmin,42px);line-height:1.25;margin-top:2vmin;text-shadow:0 1px 8px #000">Unity, dissolving our own authority for all</div>'
  '</div></div>'
  '</div>'
  '<h2 style="position:absolute;top:4.5vh;left:0;right:0;margin:0 auto;max-width:none;text-align:center;font-size:clamp(34px,6.6vmin,84px);color:var(--gold);text-shadow:0 1px 10px #000">Unity movement</h2>'
  '<aside class=notes>Thomas Campbell claimed freedom of conscience and extended it to everyone; the Springfield Presbytery gave up its own authority so that every congregation could hold it.<br>&rarr; &ldquo;Stone&rsquo;s side willed it in 1804. Tonight, the Campbells&rsquo; side does it.&rdquo;</aside></section>')

HIDE('<section class="slide room"><div class="litany" style="gap:4vmin">'
  '<h2 class=no style="max-width:18ch;font-size:clamp(44px,10vmin,124px);line-height:1.12">Who has authority?</h2>'
  '<h2 class="no frag" style="max-width:18ch;font-size:clamp(44px,10vmin,124px);line-height:1.12">Who may serve the table?</h2></div>'
  '<aside class=notes>One click for the second question. Tonight&rsquo;s two points. Who can make someone a minister: a bishop, a presbytery, the congregation? And who may give thanks at the Lord&rsquo;s table? &rarr; &ldquo;Hold both.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 5</div>'
  '<h1>Wherever Two or Three<br>Are Gathered</h1><div class=table-line></div>'
  '<div class=sub>Brush Run, Pennsylvania &middot; 1811&ndash;1812</div>'
  '<aside class=notes>Matthew 18:20, and the <i>Declaration and Address</i> quotes it (we will see where). The Campbells&rsquo; side of the story, picking up where Chapter 2 left Alexander: off the coast of Scotland. Two points tonight: who serves the table, and where authority lives.<br>'
  'The hour: the sea 6 &middot; Glasgow 14 &middot; reunion 4 &middot; Brush Run 5 &middot; the first Supper 9 &middot; the ordination 4 &middot; why the people 7 &middot; close 10.</aside></section>')
# ---------- ALEXANDER AND THE SEA ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg5"></div></div>'
  '<div class=credit>Philippe-Jacques de Loutherbourg, <i>A Shipwreck off a Rocky Coast</i> &middot; not the Hibernia</div>'
  '<div class=eyebrow>Islay, Scotland &middot; October 7, 1808</div>'
  '<h2>Alexander and the Sea</h2>'
  '<aside class=notes>Chapter 2&rsquo;s last section, which we never reached. The son&rsquo;s story while the father&rsquo;s is still open: his father is in America, on trial before the Seceders; Alexander, twenty, has been left in charge of the family. In Glasgow he will do, one after another, three things his father was charged with.</aside></section>')
A('<section class="slide"><h2 style="max-width:none">October 1808: the family sails</h2>'
  '<div class=days style="font-size:clamp(22px,4.2vmin,52px);gap:2vmin">'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Sep 20</span><span>The family sets out for Londonderry. The <i>Hibernia</i> is not ready; they wait eight days.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 1</span><span>The <i>Hibernia</i> sails, firing her ten cannon in farewell.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 2</span><span>Out into the Atlantic, then anchored again off Inishowen.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 3</span><span>Contrary winds off Malin Head. They run before the gale all night.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 4</span><span>The coast of Scotland. They anchor in Loch Indaal, on Islay, and wait for wind.</span></div>'
  '<div class="d frag"><span class=dn style="flex:0 0 4.6em">Oct 7</span><span style="color:var(--gold)">Evening. Alexander wakes from a dream.</span></div>'
  '</div>'
  '<aside class=notes>Six clicks; brisk until the last. Thomas had sailed ahead in 1807; now the family follows. Oct 7: Alexander dozes while reading to his sister Dorothea, and wakes alarmed: he dreamed the ship struck a rock and the water rushed in. (Richardson 1:94&ndash;99.)</aside></section>')

A(Q('&ldquo;<b>I will not undress to-night.</b> I will lay my shoes within my reach, and be ready to rise at a moment&rsquo;s warning&hellip;&rdquo;', 'Alexander Campbell, after the dream &middot; in Richardson, <i>Memoirs</i>', 'October 7, evening') +
  N('He told the family, and had them make ready. Let it sit before you click.'))

A('<section class="slide bleed"><div class=bg><div class="bgimg wreckbg5"></div></div>'
  '<div class=credit>Philippe-Jacques de Loutherbourg, <i>A Shipwreck off a Rocky Coast</i> &middot; not the Hibernia</div>'
  '<h2>That night, a gale blew in.</h2>'
  '<aside class=notes>About ten o&rsquo;clock the gale turned into the bay. The ship dragged her anchors onto a sunken rock; the water came in; they cut away the masts. No help could reach them until morning. Meanwhile his father had been tried and condemned in America, and Alexander did not know.</aside></section>')

A(DIM(Q('&ldquo;<b>He thought of his father&rsquo;s noble life</b>, devoted to God and to the salvation of his fellow-beings, and felt that such a calling&hellip; was, indeed, <b>the highest and most worthy sphere of action</b> in which any human being could engage.&rdquo;', RICH, 'On the stump of the broken mast'), 'wreckbg5') +
  N('Night, the storm still on. He sat on the stump of the broken mast, expecting to die, and thought of his father.',
    '&rarr; His calling is born out of admiring his father. Within months, his conscience will lead him away from his father&rsquo;s church.'))
A(DIM(Q('&ldquo;It was then in that solemn hour, that he gave himself up wholly to God, and resolved that, if saved from the present peril, <b>he would certainly spend his entire life in the ministry of the gospel</b>.&rdquo;', RICH, 'On the stump of the broken mast'), 'wreckbg5') +
  N('The next sentence. Everyone survived; stranded ten months, the family wintered in Glasgow and Alexander studied at the university.',
    '&rarr; &ldquo;Hold the mast. It comes back at the ordination.&rdquo;'))
A('<section class="slide hard"><h2>He had just vowed his life to his father&rsquo;s calling.</h2>'
  '<div class="sub frag">In Glasgow, one by one, he did <b>the three things his father was tried for</b>.</div>'
  '<aside class=notes>One click. The irony of the winter: the son who admired his father above anyone does, without knowing it, everything the Seceders had just condemned Thomas for in Pennsylvania. Hearing other preachers; honoring laymen who preach; and, in the end, the table.</aside></section>')
# ---------- GLASGOW ----------
A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">1 &middot; Article 4</span> &middot; Glasgow, winter 1808&ndash;09</div>'
  '<h2>He went to hear other preachers.</h2>'
  '<div class="sub frag">Above all <b>Greville Ewing</b>: fifteen hundred people in a converted circus.</div>'
  '<div class="sub frag">The very thing his father was tried for: <b><i>occasional hearing</i></b>.</div>'
  '<aside class=notes>Two clicks. The family wintered in Glasgow after the wreck; Alexander studied at the university. He found the Seceder minister &ldquo;a prosy speaker&rdquo; and went to hear others whenever he could, above all Ewing at the Tabernacle. Back in Pennsylvania his father had been condemned for saying Seceders might hear ministers of other churches.<br>&rarr; &ldquo;The son is doing every week what the father was condemned for.&rdquo;</aside></section>')
A(Q('&ldquo;&hellip;an effect which was, doubtless, facilitated by the fact that <b>his revered father, to whose religious sentiments he was accustomed to pay the utmost deference</b>, was now separated from him by the wide Atlantic.&rdquo;', RICH, 'With his father an ocean away') +
  N('Richardson on what the hearing did: it released him &ldquo;from the denominational influences of his religious education.&rdquo; He could think for himself because his father was not in the room.'))

A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">2 &middot; Articles 2 &amp; 3</span> &middot; at Ewing&rsquo;s house</div>'
  '<h2>Ewing told him the story of the Haldanes.</h2>'
  '<div class="sub frag">Robert and James: two brothers, <b>sea captains turned laymen</b>, who gave their fortune and their lives to the gospel.</div>'
  '<aside class=notes>One click. Robert Haldane served in the navy, James commanded an East India ship; both came home to Scotland, were converted in the 1790s, and turned everything over to preaching. James preached for years before he was ordained. Ewing had left the Church of Scotland to join them, ran their Glasgow Tabernacle, and kept the Supper weekly. His father had also been condemned for letting elders, not ministers, pray and exhort. Richardson says this story, more than anything, changed Alexander&rsquo;s mind.</aside></section>')
A(BIGQ(Q('&ldquo;Christianity&hellip; <b>is everything or nothing</b>. If it be true, it warrants and commands every sacrifice to promote its influence. If it be not, then let us lay aside the hypocrisy of believing it.&rdquo;', 'Robert Haldane &middot; in Richardson, <i>Memoirs</i>', 'Robert Haldane, 1795')) +
  N('After his conversion. He resolved to give his life and his property to the gospel; his wife agreed.'))
A(BIGQ(Q('&ldquo;He accordingly determined to <b>sell his beautiful estate of Airthrey</b>&hellip; but, upon application to the East India Company for permission to establish the mission among the Hindoos, <b>this was positively and unexpectedly refused</b>.&rdquo;', RICH, 'A mission to India, 1797')) +
  N('Inspired by William Carey in Bengal. Robert would fund the whole party, Ewing and Dr. Innes among them, with a printing press. The Company refused; appeals failed; he had already sold the estate.'))
A(BIGQ(Q('&ldquo;&hellip;&lsquo;That it is the duty of Christians to send the gospel to the heathen world,&rsquo; this, after debate, <b>was voted down by a large majority</b> &mdash; a favorite argument of the opposing party being that <b>there was plenty of ignorance, unbelief and immorality at home</b>&hellip;&rdquo;', RICH, 'The Church of Scotland on missions, 1796')) +
  N('James Haldane was in the gallery for the debate. He knew the church was doing nothing about the unbelief at home either.'))
A(CARD('Plenty of heathen at home, the Assembly said.<br>' + G('So they preached at home.'),
  'From 1797 James Haldane, with lay friends, toured Scotland and the Orkneys preaching in the open air, in streets, barns and fields. Robert paid.'))
A(Q('&ldquo;Whether a man&hellip; declare those important truths <b>to two or two hundred</b>, he is, in our opinion <b>a preacher of the gospel</b>&hellip;&rdquo;', 'The Haldanes&rsquo; printed notice, 1797 &middot; in Richardson, <i>Memoirs</i>', 'Their right to preach') +
  N('They grounded it &ldquo;upon the indispensable duty of every Christian to warn sinners.&rdquo; Every Christian: the priesthood of all believers, in a Scottish handbill.'))
A(Q('&ldquo;The clergy, however, soon began to manifest <b>their hostility to lay-preaching</b>; and the parish minister took means to <b>deprive them of the house</b> in which the meetings were held.&rdquo;', RICH, 'The church&rsquo;s answer') +
  N('They moved to a loft, then a barn. In 1799 the General Assembly closed the Church of Scotland&rsquo;s pulpits to anyone not licensed by it.'))
A(BIGQ(Q('&ldquo;&hellip;preaching every day in the open air to large numbers. On this trip <b>they were held for some time under arrest by the Highland chiefs, at the instigation of the clergy</b>.&rdquo;', RICH, 'Kintyre, 1800')) +
  N('James Haldane and John Campbell (no relation), touring Ayr, Arran and Kintyre. Richardson: &ldquo;notwithstanding the opposition, great good was effected.&rdquo;',
    '&rarr; &ldquo;Refused India. Refused the pulpits. Arrested at home. For preaching.&rdquo;'))
A(BIGQ(Q('&ldquo;The avowed object in forming this church was&hellip; to <b>avoid that contracted spirit which would exclude</b> from the pulpit, or from occasional communion, <b>any faithful preacher of the gospel or sincere lover of Christ</b>.&rdquo;', RICH, 'Their own church, Edinburgh, 1799')) +
  N('Pushed out, the Haldanes formed a church whose first rule was not to push anyone out. Three hundred and ten joined at once. Ewing drew up its plan of government.',
    '&rarr; &ldquo;A church built on refusing to exclude. Alexander is sitting at that man&rsquo;s table.&rdquo;'))
A(Q('&ldquo;He was particularly impressed with <b>the persistent opposition of the clergy</b>&hellip; and <b>the disposition they constantly manifested to exercise the power which they possessed in an arbitrary manner</b>.&rdquo;', RICH, 'What he saw in the churches') +
  N('The same sentence: &ldquo;the unscrupulous methods they often resorted to to hinder the progress of the truths they refused to admit.&rdquo; The corruption he saw was the use of power to shut people out.'))
A(BIGQ(Q('&ldquo;<b>imbibed disgust at the popular schemes</b>, chiefly while a student at Glasgow.&rdquo;', AC + ', in after years &middot; in Richardson, <i>Memoirs</i>', 'Alexander, looking back'), 'clamp(40px,9vmin,110px)', '24ch') +
  N('Richardson sets it against &ldquo;the course which the clergy pursued under the influence of their narrow policies and bigoted sectarianism.&rdquo;'))
A('<section class="slide room"><div class="litany" style="gap:3vmin">'
  '<h2 class=no style="max-width:none;font-size:clamp(40px,8.6vmin,108px)">He was welcome at his church&rsquo;s table.</h2>'
  '<h2 class="no frag" style="max-width:none;font-size:clamp(40px,8.6vmin,108px)">Ewing was not.</h2>'
  '<h2 class="no frag" style="max-width:none;font-size:clamp(40px,8.6vmin,108px)">The Haldanes were not.</h2>'
  '</div><aside class=notes>Two clicks. The Seceder table was for Seceders in good standing, with a token. The men whose preaching and piety he most admired could not have sat at it.</aside></section>')
A('<section class="slide room"><h2 style="max-width:20ch;font-size:clamp(44px,10vmin,124px);line-height:1.12">Can you be included by a church that excludes?</h2>'
  '<aside class=notes>Ask the room, and wait. Then carry it into his struggle: what he came to want, and what held him.</aside></section>')

A(Q('&ldquo;&hellip;the principles of Congregationalism entertained by Mr. Ewing, which secured <b>an entire emancipation from the control of domineering Synods and General Assemblies</b>&hellip;&rdquo;', RICH, 'What he came to want') +
  N('&ldquo;&hellip;and which seemed to him much more accordant with primitive usage.&rdquo; The congregation free of the church courts: the seed of tonight.'))

A(Q('&ldquo;&hellip;he did not feel himself at liberty to abandon rashly the cherished religious sentiments of his youth, and <b>the Seceder Church to which his father and the family belonged</b>&hellip;&rdquo;', RICH, 'But it was his father&rsquo;s church') +
  N('The same page as &ldquo;domineering Synods.&rdquo; Everything pulled him toward Ewing&rsquo;s freedom; everything he loved held him to his father&rsquo;s church, where &ldquo;he had thought it his duty to be a regular communicant.&rdquo;',
    'Call back the mast: the boy who vowed his life to his father&rsquo;s ministry.'))

A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">3 &middot; The table</span> &middot; Glasgow, spring 1809</div>'
  '<h2>The communion season came. He was examined, and given the token.</h2>'
  '<div class="sub frag">Eight hundred communicants, eight or nine tables. <b>He waited for the last one.</b></div>'
  '<aside class=notes>One click. The Seceder church&rsquo;s spring communion. No letter from Ireland, so the elders examined him and gave him the lead token, his ticket to the table.</aside></section>')

A(Q('&ldquo;His conscientious misgivings as to the propriety of <b>sanctioning any longer, by participation</b>, a religious system which he disapproved, and, on the other hand, his sincere desire to comply with all his religious obligations, <b>created a serious conflict in his mind, from which he found it impossible to escape</b>.&rdquo;', RICH, 'Why he waited') +
  N('Taking part would put his stamp on the system; leaving would break with his father&rsquo;s church. He waited for the last table &ldquo;in hopes of being able to overcome his scruples.&rdquo; He wanted to stay.',
    'Hit the word <b>sanctioning</b>. His father, leaving the Seceders in America, would use the same word.'))

A(Q('&ldquo;&hellip;the ring of the token, falling upon the plate, announced the instant at which he renounced Presbyterianism for ever &mdash; <b>the leaden voucher becoming thus a token not of communion but of separation</b>.&rdquo;', RICH, '', 'slide hard') +
  N('When the plate came round he dropped the token on it, and when the bread and wine came down the table he &ldquo;declined to partake.&rdquo; He told no one.',
    '&rarr; Silence. Do not explain it.'))
A(CARD('Welcomed at a table that turned others away,<br>' + G('he gave back the token.'),
  'The answer to the question, in an act rather than a word. Richardson: he was &ldquo;unable any longer conscientiously to recognize the Seceder Church as the Church of Christ.&rdquo;'))

# ---------- FAMILY REUNION ----------
A(C('Family Reunion', 'October 1809. The family finally lands in Philadelphia and crosses the mountains.'))

A('<section class="slide"><div class=eyebrow>October 1809 &middot; the road into Washington, Pennsylvania</div>'
  '<h2>Thomas rode out to meet them.</h2>'
  '<div class="sub frag">On the ride back he told his son everything: the trial, the rebuke, and that <b>he had left the Seceders</b>.</div>'
  '<aside class=notes>One click. Apart two and a half years. Alexander had carried his decision alone for six months, and expected his father to oppose him.</aside></section>')
A(Q('&ldquo;&hellip;instead of fearing opposition from him to the views to which he had himself been definitely brought while in Glasgow, he found him already, though by a somewhat different method, <b>led practically to the very same conclusions</b>.&rdquo;', 'Richardson, <i>Memoirs</i> 1:220', 'On the road, 1809') +
  N('He lands in the autumn of 1809, crosses the mountains, and meets his father on the road. Thomas has just written the <i>Declaration and Address</i>, and Alexander reads it in proof.',
    '&rarr; &ldquo;Father and son, an ocean apart, arrive at the same place.&rdquo;'))
A('<section class="slide hard"><h2>The father opened the table to people who had no token.</h2>'
  '<div class="sub frag">The son held a valid token, and would not use it.</div>'
  '<div class="sub frag"><b>Neither knew.</b></div>'
  '<aside class=notes>Two clicks. Say it plain and stop.<br>The father had been tried for serving the Supper to Presbyterians of other kinds in 1807; the son had walked away from a fenced table in 1809.</aside></section>')

A(Q('&ldquo;The Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>; consisting of all those in every place that profess their faith in Christ&hellip;&rdquo;', DA, 'That fall they asked him to write down what they stood for') +
  N('Chapter 3: the <i>Declaration and Address</i>, which Alexander read in proof that autumn. Optional sting: the presbytery formally deposed Thomas on April 18, 1810, seven months after it was published.'))
# ---------- BRUSH RUN ----------
A('<section class="slide bleed"><div class=bg><div class="bgimg brushbg"></div></div>'
  '<div class=credit>The Brush Run meeting house, reconstructed at Bethany &middot; courtesy of Bethany College</div>'
  '<div class=eyebrow>1810&ndash;1811</div>'
  '<h2>Brush Run</h2>'
  '<aside class=notes>A creek and a few farms, about eight miles from Washington. The meeting house was a plain frame building, never finished; it was later sold, moved, used as a blacksmith shop, a post office and a barn, and rebuilt at Bethany in 1909.</aside></section>')
A(BIGQ(Q('&ldquo;This Society <b>by no means considers itself a Church</b>, nor does at all assume to itself the powers peculiar to such a society&hellip;&rdquo;', DA + ', Resolution IV')) +
  N('What they promised in 1809: &ldquo;merely as voluntary advocates for Church reformation.&rdquo; A society can preach; it cannot keep the Supper or ordain.',
    '&rarr; &ldquo;Now they would have to be one.&rdquo;'))
HIDE(BIGQ(Q('&ldquo;As many members of the Christian Association lived near Buffalo Creek, it was, about this time, <b>resolved to erect a house of worship there</b>.&rdquo;', RICH, '1810 &middot; a meeting house')) +
  N('A plot on William Gilchrist&rsquo;s farm, in the valley of Brush Run, two miles above Buffalo Creek. Joseph Bryant&rsquo;s family ran the saw-mill next door and sawed the lumber. A plain frame building, never finished.'))

HIDE(BIGQ(Q('&ldquo;<b>Though thy beginning was small</b>, yet thy latter end should greatly increase.&rdquo;', 'Job 8:7 &middot; Alexander&rsquo;s text for the first sermon at the site &middot; in Richardson, <i>Memoirs</i>', 'Under a spreading tree'), 'clamp(40px,9vmin,116px)', '24ch') +
  N('Before the building went up, a temporary stand by the ground; Alexander gave the first discourse there. Richardson: &ldquo;singularly appropriate and prophetic.&rdquo;'))

A(BIGQ(Q('&ldquo;&hellip;as the Society was not a Church&hellip; most of its members&hellip; <b>were deprived of various privileges which belonged to the church relation</b>.&rdquo;', RICH, 'But a society is not a church')) +
  N('No Lord&rsquo;s Supper, no baptism, no ordination: a society can preach, but it cannot keep the table. Most members had drifted from their old congregations; some had never belonged to any.'))

A(BIGQ(Q('&ldquo;&hellip;the Society must obtain admission into some regularly organized religious body, or be itself compelled to change its attitude and <b>resolve itself into an independent Church</b> &mdash; an alternative which Thomas Campbell particularly desired to avoid.&rdquo;', RICH)) +
  N('The Society&rsquo;s first plan was not to become a church at all. In October 1810 Thomas asked the Presbyterian Synod of Pittsburg, a body other than the Seceders who had tried him, to receive him and the Association.'))
A('<section class="slide breath"><div class=eyebrow>Alexander, 1810</div><h2 style="max-width:none">Who may come?</h2>'
  '<aside class=notes>Alexander&rsquo;s case for an open table, from his addresses of 1810: the creeds as gates, Gabriel, the &ldquo;party man&rdquo; address, and the gates as wide as heaven. Then the Synod&rsquo;s answer to it all.</aside></section>')
A(BIGQ(Q('&ldquo;That standards had been lifted up which <b>narrowed the gates of Zion</b>&hellip; and there were none of them but would <b>reject those whom God has not rejected</b>, and deny admission to those whom God had admitted.&rdquo;', AC + ', address to the Christian Association, November 1810 &middot; in Richardson, <i>Memoirs</i>', 'The creeds as gates')) +
  N('&ldquo;Standards&rdquo; are the confessions used as tests of admission. His text was Isaiah 62:10, &ldquo;go through the gates.&rdquo;'))
A(BIGQ(Q('&ldquo;All are defective. <b>The apostle Paul, the angel Gabriel in human form, could not be admitted</b> on the principles of these standards.&rdquo;', AC + ', November 1810 &middot; in Richardson, <i>Memoirs</i>'), 'clamp(40px,9vmin,110px)', '26ch') +
  N('Let the room laugh. Then: the Seceder table he walked away from in Glasgow would not have had the apostle, and neither would the Synod of Pittsburg.'))
A(BIGQ(Q('&ldquo;I dare not be a party man for these reasons&hellip; <b>Because no party will receive into communion all whom God would receive into heaven.</b>&rdquo;', AC + ', 1810 &middot; in Richardson, <i>Memoirs</i>', 'Why he would join no party'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('The same year: an address after a sermon at Mr. Buchanan&rsquo;s. The next line: &ldquo;God loves his children more than our creeds, and man was not made for the Bible, but the Bible for man.&rdquo;',
    'Chapter 1&rsquo;s table and Chapter 2&rsquo;s trial, in one sentence.'))
A(BIGQ(Q('&ldquo;We have decided, therefore,&hellip; <b>to open the gates of admission into the Church as wide as the gates of heaven</b>.&rdquo;', AC + ', November 1810 &middot; in Richardson, <i>Memoirs</i>', 'The gates of admission'), 'clamp(38px,8.4vmin,106px)', '26ch') +
  N('In full: &ldquo;to lift it up as a standard for the Church,&rdquo; the New Testament as the only test of admission. The same address: the Society&rsquo;s first work was &ldquo;to remove the stumbling-block of making the private opinions of men a term of communion.&rdquo;'))
A('<section class="slide breath"><div class=eyebrow>Side path &middot; creeds as tests</div><h2 style="max-width:none">Creeds may teach. May they exclude?</h2>'
  '<aside class=notes>Side path. The Campbells did not reject creeds as teaching; they rejected them as tests of fellowship, because a test shuts out people God has not shut out. Thomas Campbell, 1809.</aside></section>')
A(BIGQ(Q('&ldquo;That although doctrinal exhibitions of the great system of Divine truths, and defensive testimonies in opposition to prevailing errors, <b>be highly expedient</b>, and the more full and explicit they be for those purposes, the better; yet&hellip; <b>they ought not to be made terms of Christian communion</b>&hellip;&rdquo;', DA, 'Proposition 7')) +
  N('Confessions are good teaching. They are human reasoning, full of &ldquo;inferential truths,&rdquo; so they cannot be the door.'))
A(BIGQ(Q('&ldquo;&hellip;unless we suppose, what is contrary to fact, that none have a right to the communion of the Church, but such as possess a very clear and decisive judgment&hellip; whereas <b>the Church from the beginning did, and ever will, consist of little children and young men, as well as fathers</b>.&rdquo;', DA, 'Proposition 7, continued')) +
  N('The reason: a test of doctrine excludes the young in faith, whom God has not excluded. 1 John 2:12&ndash;14.'))
A(BIGQ(Q('&ldquo;&hellip;yet are they not formally binding upon the consciences of Christians farther than they perceive the connection&hellip; Therefore, <b>no such deductions can be made terms of communion</b>, but do properly belong to the after and progressive edification of the Church.&rdquo;', DA, 'Proposition 6')) +
  N('Inferences belong to teaching, &ldquo;the after and progressive edification of the Church,&rdquo; not to admission.'))
A(CARD('Creeds may teach.<br>' + G('They may not fence the table.'),
  'Back to the spine: the Synod of Pittsburg'Back to the spine: Alexander&rsquo;s &ldquo;party man&rdquo; address.'rsquo;s answer.'))
A(BIGQ(Q('&ldquo;&hellip;Mr. Campbell&rsquo;s request to be received into ministerial and Christian communion <b>cannot be granted</b>.&rdquo;', MIN, 'The Synod of Pittsburg, October 1810'), 'clamp(40px,9vmin,110px)', '24ch') +
  N('Unanimous. Among its reasons: Thomas&rsquo;s &ldquo;opposing creeds and confessions as injurious to the interests of religion.&rdquo; Alexander&rsquo;s November address was his public reply. The reasons, and more of the reply, are in the reserve deck.'))
# ---------- BRUSH RUN BECOMES A CHURCH ----------
A(BIGQ(Q('&ldquo;&hellip;on account of <b>the continued hostility of the different parties</b>, it was necessary that the Christian Association should assume the character of an independent Church, <b>in order to the enjoyment of those privileges and the performance of those duties which belong to the Church relation</b>.&rdquo;', RICH, 'Why a church')) +
  N('The pastoral need. Its members had been shut out or had drifted from their old congregations: no Supper, no baptism for their children, no one to marry or bury them. '))
A(BIGQ(Q('&ldquo;It was with <b>great reluctance</b> that he finally concluded to take this step, and to separate himself from those whom he desired to recognize as brethren.&rdquo;', RICH, 'Thomas Campbell, spring 1811')) +
  N('Spring 1811. Every overture refused, Thomas concluded &ldquo;that the Christian Association should assume the character of an independent Church.&rdquo; The thing he had dreaded since 1809. &ldquo;At the next meeting of the Association, accordingly, the matter was duly considered and agreed to.&rdquo;'))
A('<section class="slide breath"><h2 style="max-width:none">Two ways not to become a sect</h2>'
  '<aside class=notes>The pattern to highlight. Both sides feared becoming one more party. Stone&rsquo;s presbytery solved it by dissolving itself. The Campbells tried to solve it by joining a body that already existed, and kept trying.</aside></section>')
A('<section data-src="will rich" class="slide"><div style="display:grid;grid-template-columns:1fr 1fr;gap:5vw;max-width:92vw;align-items:start">'
  '<div><div class=eyebrow>Stone&rsquo;s side, 1804 &middot; dissolve our own body</div><p class=bigquote style="font-size:clamp(30px,6vmin,76px);line-height:1.2;max-width:none">&ldquo;We will, that this body <b>die, be dissolved, and sink into union with the Body of Christ at large</b>&hellip;&rdquo;</p><div class=cite>The Last Will and Testament</div></div>'
  '<div class=frag><div class=eyebrow>The Campbells&rsquo; side, 1810 &middot; join an existing one</div><p class=bigquote style="font-size:clamp(30px,6vmin,76px);line-height:1.2;max-width:none">&ldquo;&hellip;the Society must <b>obtain admission into some regularly organized religious body</b>&hellip;&rdquo;</p><div class=cite>Richardson, <i>Memoirs</i></div></div>'
  '</div><aside class=notes>One click. The same fear, opposite remedies. Thomas left the Seceders, then asked the Presbyterians; when they refused, he formed a church only with great reluctance. And even then they kept looking for a body to join.</aside></section>')
A(BIGQ(Q('&ldquo;&hellip;expressing a willingness, upon certain conditions, to co-operate or to unite with that Association, <b>provided always that we should be allowed to teach and preach whatever we learned from the Holy Scriptures, regardless of any creed or formula in Christendom</b>.&rdquo;', AC + ', <i>Millennial Harbinger</i> 1848 &middot; in Richardson, <i>Memoirs</i>', 'Side path &middot; becoming Baptists &middot; Brush Run&rsquo;s overture, fall 1813')) +
  N('Side path, two years ahead. After the Campbells were immersed in 1812, Baptist congregations for sixty miles around asked Alexander to preach and &ldquo;all pressed us to join their Redstone Association.&rdquo; Brush Run&rsquo;s answer: eight or ten pages, &ldquo;exhibiting our remonstrance against all human creeds as bonds of communion.&rdquo; The Association voted, &ldquo;by a considerable majority,&rdquo; to receive them: &ldquo;Thus a union was formed.&rdquo;'))
A(BIGQ(Q('&ldquo;As the reformers were, however, <b>at this time identified with the Baptists</b>, it was thought expedient, in order to avoid offending religious prejudice&hellip; to make this concession so far as the name of the paper was concerned, qualifying &ldquo;Baptist&rdquo; by the word &ldquo;Christian.&rdquo;&rdquo;', 'Richardson, <i>Memoirs</i>, vol. 2', 'The name of his paper, 1823')) +
  N('<i>The Christian Baptist</i>, 1823&ndash;1830. Richardson calls it a concession; it was also simply true: the reformers were Baptists. He had debated as the Baptist champion against John Walker (1820) and W. L. Maccalla (1823).',
    'In 1829 he dropped the name because &ldquo;he feared that the name Christian Baptists would be given to the advocates of the Reformation.&rdquo; The 1848 memory was written from the far side of that break.'))
A(CARD('Refused by the Presbyterians,<br>' + G('they became Baptists.'),
  'For most of the next two decades the Campbells&rsquo; churches belonged to Baptist associations: Redstone from 1813, Alexander&rsquo;s Wellsburg church in the Mahoning Association from 1823. His paper (1823&ndash;1830) was called <i>The Christian Baptist</i>. The separation came around 1830.<br>&rarr; &ldquo;Stone gave up his institution. The Campbells kept looking for one to belong to.&rdquo;'))
A(C('Brush Run Church Formed', 'Saturday, May 4, 1811, at the Brush Run meeting house. About thirty members. They sang Psalm 118 in the old Scottish metrical version.', 'May 4, 1811'))
A(BIGQ(Q('&ldquo;At this meeting, <b>Thomas Campbell was appointed elder</b>, and <b>Alexander was licensed to preach the gospel</b>. Four deacons were also chosen&hellip;&rdquo;', RICH, 'May 4, 1811')) +
  N('The deacons: John Dawson, George Sharp, William Gilcrist, James Foster. About thirty members.',
    'No presbytery licensed him. The church did.'))
A(CARD('No bishop. No presbytery.<br>' + G('A congregation.'),
  'Let it sit. This is the thing no church court could imagine: a church that makes its own ministers.'))
A(C('The First Supper', 'The next day, May 5, 1811, the new church kept the Lord&rsquo;s Supper for the first time. Alexander preached.', 'Brush Run &middot; May 5, 1811'))
A(BIGQ(Q('&ldquo;<b>I am that bread of life.</b>&rdquo;', 'John 6:48 &middot; Alexander&rsquo;s text that morning &middot; in Richardson, <i>Memoirs</i>', 'His sermon'), 'clamp(48px,11vmin,140px)', '18ch') +
  N('And verse 58: &ldquo;He that eateth of this bread shall live for ever.&rdquo; Two years after he left a table with his token unused, he preaches at a table of his own.'))
A('<section class="slide"><div class=eyebrow>The sermon&rsquo;s close</div>'
  '<p class="bigquote" style="font-size:clamp(30px,6.4vmin,80px);max-width:36ch;line-height:1.22"><span class=q>&ldquo;&hellip;in assembling there on that occasion, they furnished <b>an emblem of the millennial state of the Church</b>, nay, an emblem of the heavenly state, when men of different nations, and known by different names, <b>should sit down together in the kingdom of God</b>.&rdquo;</span></p>'
  '<div class=cite>Alexander Campbell&rsquo;s communion sermon &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>The high point of the hour. His text: John 6:48, &ldquo;I am that bread of life.&rdquo; Richardson is summarizing his sermon notes.<br>&rarr; &ldquo;The table is not only a memory. It is the future, arriving early: everyone who will be at the last table, at this one.&rdquo; Chapter 1&rsquo;s table, again.</aside></section>')
A(BIGQ(Q('&ldquo;&hellip;the Lord&rsquo;s Supper, which, according to the custom of the Independent churches in Scotland, <b>was now celebrated weekly</b>.&rdquo;', RICH, 'Every Lord&rsquo;s day')) +
  N('The Haldane churches again. At Cane Ridge the Supper came once or twice a year, after weeks of preparation and a token. At Brush Run, every Sunday, from the beginning. That is us.'))
for _x in R.weekly(): A(_x)                      # side path: the table every Lord's day (shared resource)
# side path "Who may serve?": Campbell on the royal priesthood at the table, then the history (shared resource table())
A(C('Who serves the table?', 'Side path: who may serve? Brush Run kept the Supper every Lord&rsquo;s day, open to every Christian. Campbell&rsquo;s argument goes further: the table is kept by the priesthood of all believers.'))
A(SRC(BIGQ(Q('&ldquo;May they not, <b>without a human priest to consecrate the way for them</b>, approach the Lord&rsquo;s table, and <b>handle the loaf and cup</b>?&rdquo;', CS, 'The same priesthood keeps the table'), 'clamp(32px,7.2vmin,90px)', '34ch'), 'acr') +
  N('Later, in <i>The Christian System</i>. The sentence before: &ldquo;May not, then, holy and royal priests thank God for the Lord&rsquo;s table, its loaf, and cup of wine?&rdquo;',
    'He had already written, in the <i>Christian Baptist</i> (1827): &ldquo;&lsquo;The administration of ordinances&rsquo; is a popish phrase, and ought to be cashiered from the christian vocabulary.&rdquo;'))
A(SRC(BIGQ(Q('&ldquo;&hellip;the royal priesthood may approach the Lord&rsquo;s table without fear, inasmuch as they are <b>consecrated to officiate</b> by a blood&hellip;&rdquo;', CS), 'clamp(34px,7.6vmin,96px)', '30ch'), 'acr') +
  N('Consecrated to officiate: not by a bishop&rsquo;s hands, by Christ&rsquo;s blood. Every baptized member is ordained to the table.',
    'Against the clergyman who says &ldquo;Stand by, I am holier than thou&rdquo;: he &ldquo;desecrates the royal priesthood of Jesus Christ.&rdquo;'))
A(SRC(BIGQ(Q('&ldquo;&hellip;he that gives thanks for the loaf should break it <b>not as the representative of the Lord, but after his example</b>&hellip; And thus <b>they as priests feast upon his sacrifice</b>.&rdquo;', CS), 'clamp(32px,7.2vmin,90px)', '34ch'), 'acr') +
  N('Between the two halves: the disciples hand the loaf &ldquo;to one another,&rdquo; and the one who broke it eats with them. No one stands in for Christ; everyone serves everyone.',
    '&rarr; In our congregations the thanks at the table are given by members, not by the preacher. That is this, still.'))
A(BIGQ(Q('&ldquo;That division among the Christians is <b>a horrid evil, fraught with many evils</b>. It is antichristian, as it <b>destroys the visible unity of the body of Christ</b>&hellip;&rdquo;', DA + ', Proposition 10', 'Throwback &middot; Thomas Campbell, 1809')) +
  N('Chapter 3. The table is where that unity is shown, or denied: a fenced table divides the body at the very place it is meant to be one.'))
for _x in R.table()[1:-1]: A(_x)                 # its history, without its own title and closing card
A(CARD('Open to all.<br>' + G('Hosted by any.'),
  'Brush Run&rsquo;s table was weekly and its fences were coming down. Campbell&rsquo;s argument goes further: the table is kept by the priesthood of all believers. Not only open; hosted by any.'))
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
A(BIGQ(Q('&ldquo;We do hereby certify that Alexander Campbell&hellip; was, <b>according to the principles of this Church</b> regularly chosen and ordained a minister thereof, upon the first day of January, one thousand eight hundred and twelve.&rdquo;', 'Certificate of ordination, recorded in the Brooke County court, December 1812 &middot; in Richardson, <i>Memoirs</i>')) +
  N('He needed it in court to be allowed to perform marriages. Signed at a church meeting at John Dawson&rsquo;s, September 1, 1812.',
    'The cut: &ldquo;after a due course of trials preparatory to the work of the holy ministry.&rdquo;'))
A('<section class="slide"><div class=eyebrow>Signed</div>'
  '<div class=litany style="gap:1vmin">'
  '<div class=no style="font-size:clamp(30px,5.8vmin,74px)">Thomas Campbell, senior minister</div>'
  '<div class="no frag" style="font-size:clamp(30px,5.8vmin,74px);color:var(--gold)">George Sharp &middot; William Gilcrist &middot; James Foster &middot; John Dawson, deacons</div>'
  '</div><div class=cite>The ordination certificate &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>One click. His father, and four farmers. One of them, James Foster, is the man nearly kept out by the test question. The man who would debate Robert Owen and the Catholic bishop of Cincinnati, and found a college, was ordained by a creekside congregation of about thirty.</aside></section>')
# ---------- WHY THE PEOPLE? ----------
A(C('Why the people?', 'The theory behind the ordination: why Brush Run believed the authority to make a minister was its own.', 'The meaning of January 1, 1812'))
A(BIGQ(Q('&ldquo;You see that ordination is not a mere unmeaning thing, but <b>consists in the choice of the people</b>, which must be hearty&hellip;&rdquo;', AC + ', sermon on Titus 1:5 &middot; in Richardson, <i>Memoirs</i>'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('His notes for a sermon that winter. The sentence goes on: &ldquo;and that it might be evidenced, the elders or rulers impose their hands.&rdquo; The laying on of hands shows the choice; it does not make it. Richardson: he regarded ordination not &ldquo;as conferring any authority, but as a public testimony that the persons ordained possessed the necessary authority.&rdquo; The authority is the congregation&rsquo;s.'))
# side path "Who may ordain?": church government (shared resource), less what the spine already shows, with "Who gave the Presbytery authority?"
_gov = [x for x in R.governance() if 'As to the form or ceremony of ordination' not in x and 'The will&rsquo;s bequests on government' not in x]
for _x in _gov[:-1]: A(_x)
A(R.succession()[1])
A(_gov[-1])
A('<section data-src=will class="slide"><div class=eyebrow>The Springfield Presbytery, 1804 &middot; the court gives up its power</div>'
  '<div class=litany style="gap:4vmin;font-size:3.3em;max-width:90vw">'
  '<div class=no>&ldquo;We will, that <b>our power of making laws for the government of the church</b>, and executing them by delegated authority, <b>forever cease</b>&hellip;&rdquo;</div>'
  '<div class="no frag">&ldquo;We will, that candidates for the Gospel ministry&hellip; <b>obtain license from God</b> to preach the simple Gospel&hellip;&rdquo;</div>'
  '</div><div class=cite>The Last Will and Testament of the Springfield Presbytery</div>'
  '<aside class=notes>One click. Chapter 4, Cane Ridge: the presbytery dissolved itself. Two items about ministers: the presbytery will no longer license anyone; a minister&rsquo;s license comes from God.</aside></section>')
A('<section data-src=will class="slide"><div class=eyebrow>The Springfield Presbytery, 1804 &middot; the congregation takes it up</div>'
  '<div class=litany style="gap:4vmin;font-size:3em;max-width:92vw">'
  '<div class=no>&ldquo;We will, that the church of Christ assume <b>her native right of internal government</b>&mdash;<b>try her candidates for the ministry</b>&hellip; and admit no other proof of their authority, but Christ speaking in them.&rdquo;</div>'
  '<div class="no frag">&ldquo;We will, that each particular church, as a body&hellip; <b>choose her own preacher</b>&hellip; and <b>never henceforth delegate her right of government to any man or set of men whatever</b>.&rdquo;</div>'
  '</div><div class=cite>The Last Will and Testament of the Springfield Presbytery</div>'
  '<aside class=notes>One click. Where the authority goes: to each congregation. Seven years later and hundreds of miles away, a congregation that never heard of the will tried its own candidate, licensed him in May 1811 and ordained him in January 1812.</aside></section>')
A(CARD('The Springfield Presbytery died<br>so that congregations could choose.<br>' + G('Brush Run chose.'),
  'Neither side knew the other existed. The two streams meet in 1832; they already agreed.'))
A(BIGQ(Q('&ldquo;Each church was independent, and had <b>the exclusive authority to select its own officials</b>, who were, when approved, to be set apart by a formal ordination.&rdquo;', RICH, 'His views, 1811')) +
  N('Richardson: &ldquo;These views he continued to maintain unchanged through life.&rdquo;'))
A(BIGQ(Q('&ldquo;As to the form or ceremony of ordination, he did not regard it as <b>conferring any authority</b>, but as <b>a public testimony that the persons ordained possessed the necessary authority</b>.&rdquo;', RICH, 'What the hands do')) +
  N('The hands do not give the authority; they testify to it. The church already gave it, by choosing. Hence, Richardson goes on, he &ldquo;utterly repudiated the claim of apostolic succession.&rdquo;'))
A(BIGQ(Q('&ldquo;The clergy are the opposite to the laity. Both these terms are used in Scripture to denote <b>God&rsquo;s people</b>. Trace them to their origin and <b>we find no difference</b>.&rdquo;', AC + ', reply to the Synod, November 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('Clergy from <i>kl&ecirc;ros</i>, the Lord&rsquo;s lot or inheritance; laity from <i>laos</i>, the people of God. Both words name the whole church.'))
A(SRC(BIGQ(Q('&ldquo;<b>The community, the church, the multitude of the faithful, are the fountain of official power.</b> This power descends from the body itself &mdash; not from its servants. Servants made by servants are servants of servants&hellip;&rdquo;', 'Alexander Campbell, <i>The Christian System</i> (1839)', 'Alexander, later'), 'clamp(32px,6.8vmin,86px)', '32ch'), 'ekk') +
  N('The theory of Brush Run, written down twenty-seven years later. It goes on: authority &ldquo;thus derived from Christ the head, immediately through his body,&rdquo; is surer than one &ldquo;derived through a long, doubtful, corrupt dynasty of bishops or pontiffs.&rdquo;'))
for _x in R.universals(): A(_x)                  # side path: the whole church remembers (shared resource)
for _x in R.ekklesia():                           # side path: the church as ekklesia (shared resource), less the fountain already on the spine
    if 'fountain of official power' not in _x and 'Servants made by servants' not in _x: A(_x)
for _x in R.constitution(): A(_x)                # side path: confession or constitution (shared resource)
A(CARD('A minister, made by<br>' + G('the priesthood of all believers.'),
  'The meaning Brush Run attached to it: the authority to make a minister is in the congregation, because every member is a priest. Luther is a witness in &ldquo;The whole church remembers.&rdquo;'))
A(BLACK)

# ---------- CLOSE ----------
DISCUSS = re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): Who gives thanks at our table, and why that person? Who has authority in our congregation, and where did it come from? What would it mean to believe every member could be called?</aside>',
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


# ---------- RESERVE: the Synod's refusal and Alexander's reply ----------
# Not in Chapter 5. Kept for another day as its own deck: decks/src/reserve5/build.py (RES below).
RES = []
RS = RES.append
RS('<section class="slide bleed"><div class=bg><div class="bgimg grovebg5"></div></div>'
  '<div class=credit>An American forest, 19th-century painting &middot; not the Templeton farm</div>'
  '<div class=eyebrow>July 15, 1810 &middot; a grove on Major Templeton&rsquo;s farm</div>'
  '<h2>His first sermon</h2>'
  '<aside class=notes>Eight miles from Washington, Pennsylvania. He was twenty-one. His father had had him speak once, briefly, at a house meeting that spring; this was his first real sermon, written out and memorized.</aside></section>')
RS(BIGQ(Q('&ldquo;When the hour arrived, he rose up with modest dignity, in the temporary stand erected for the occasion, in front of which the audience were seated <b>upon rough planks or upon the grass beneath the shady maples</b>&hellip;&rdquo;', RICH)) +
  N('His text: the close of the Sermon on the Mount, Matthew 7:24&ndash;27, the wise man who built his house upon a rock.',
    'No church building, no ordination, no license.'))
RS(CARD('In his first year he preached<br>' + G('one hundred and six sermons.'),
  'Richardson: &ldquo;no less than one hundred and six sermons&rdquo;, at the crossroads, in Washington, at Buffalo, in houses, into Ohio. Nobody had ordained him. &rarr; &ldquo;Someone noticed.&rdquo;'))
# ---------- THE SYNOD ----------
RS('<section class="slide breath"><div class=eyebrow>October 1810 &middot; why the Synod would not have Thomas Campbell</div>'
  '<h2 style="max-width:22ch;font-size:clamp(44px,8.6vmin,112px);line-height:1.12">&ldquo;for encouraging or countenancing his son to preach the gospel ' + G('without any regular authority') + '&rdquo;</h2>'
  '<div class=cite style="margin-top:3vmin">' + MIN + '</div>'
  '<aside class=notes>No clicks. In October 1810 Thomas Campbell asked the Presbyterian Synod of Pittsburg to receive him. Among their reasons for refusing: his son. Alexander was doing what his father was charged with countenancing, preaching with no presbytery&rsquo;s license.<br>&rarr; &ldquo;Who gave him authority? Hold that; Brush Run answers it.&rdquo;</aside></section>')

RS('<section class="slide bleed"><div class=bg><div class="bgimg synodbg5"></div></div>'
  '<div class=credit>The Synod of Dort, 1618&ndash;19 &middot; painting attributed to Pouwels Weyts, c. 1621</div>'
  '<div class=eyebrow>Washington, Pennsylvania &middot; October 1810</div>'
  '<h2>The Synod of Pittsburg</h2>'
  '<aside class=notes>The Presbyterian synod, meeting in their own town. Thomas feared that the Christian Association was drifting into a new party, the one thing he did not want. A Presbyterian pastor (John Anderson of Upper Buffalo) urged him to apply. So he asked to be taken in, Association and all: &ldquo;Christian union upon Christian principles.&rdquo; Alexander disapproved and expected nothing, but did not oppose his father.<br>(The picture is the Synod of Dort, from last week.)</aside></section>')
RS(DIM(BIGQ(Q('&ldquo;&hellip;the Synod unanimously resolved, that <b>however specious the plan</b> of the Christian Association and <b>however seducing its professions</b>&hellip; the Synod are constrained to disapprove the plan and its native effects.&rdquo;', MIN, 'October 4, 1810')), 'synodbg5') +
  N('The cut: &ldquo;as experience of the effects of similar projects in other parts has evinced their baleful tendency and destructive operations on the whole interests of religion by promoting divisions instead of union, by degrading the ministerial character&hellip;&rdquo;',
    'A plan for unity, refused for promoting division.'))
RS(DIM(BIGQ(Q('&ldquo;&hellip;Mr. Campbell&rsquo;s request to be received into ministerial and Christian communion <b>cannot be granted</b>.&rdquo;', MIN), 'clamp(36px,8vmin,100px)', '30ch'), 'synodbg5') +
  N('&ldquo;For the above and many other important reasons.&rdquo; Thomas came back the next day and asked what the &ldquo;important reasons&rdquo; were.'))
RS(DIM('<section class="slide"><div class=eyebrow>The &ldquo;important reasons,&rdquo; October 5</div>'
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
    RS(_x)
RS(CARD('Rejected by the Seceders in 1808.<br>' + G('Rejected by the Presbyterians in 1810.'),
  'Twice now, for the same thing: the Bible alone, and a table open to other Christians. &rarr; &ldquo;And the Synod had named the son. The son answered.&rdquo;'))
# ---------- ALEXANDER ANSWERS ----------
RS(C('Alexander Answers', 'Washington, November 1, 1810: an address at a regular meeting of the Christian Association, defending it against the Synod. He was twenty-two. His father had promised in the <i>Declaration and Address</i> not to dispute in public; the son had promised nothing.'))
RS(Q('&ldquo;It is again objected that it opens a door for <b>lay preaching</b>.&rdquo;', AC + ', reply to the Synod, November 1810') +
  N('He takes the Synod&rsquo;s charges one by one. This is the charge about him.',
    'His first answer: the Association&rsquo;s twelfth proposition asks for ministers &ldquo;duly and scripturally qualified.&rdquo; &ldquo;Are lay preachers the only persons &lsquo;duly and scripturally qualified?&rsquo; If they be, let us have a number of them.&rdquo;'))
RS(BIGQ(Q('&ldquo;The clergy are the opposite to the laity. Both these terms are used in Scripture to denote <b>God&rsquo;s people</b>. Trace them to their origin and <b>we find no difference</b>.&rdquo;', AC + ', reply to the Synod, November 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('<i>Laos</i>, &ldquo;people&rdquo;: God&rsquo;s people. <i>Kleros</i>, &ldquo;lot, inheritance&rdquo;: also God&rsquo;s people (1 Peter 5:3, &ldquo;not as lords over God&rsquo;s heritage&rdquo;). Both words name the whole church.',
    '&rarr; &ldquo;The line the Synod was guarding is not in the Bible.&rdquo;'))
RS(BIGQ(Q('&ldquo;We would be obliged to some person of <b>exquisite keenness of distinction</b> to point out and define the difference between laical and clerical preachers.&rdquo;', AC + ', reply to the Synod, November 1810'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('A smile. Twenty-two years old, answering a synod.'))
RS('<section class="slide"><div class=eyebrow>Richardson&rsquo;s note</div>'
  '<p class="bigquote long"><span class=q>&ldquo;&hellip;there is not, in Scripture, the slightest ground for the distinction between clergy and laity. On the contrary, all the disciples collectively are denominated a <b>&lsquo;royal priesthood,&rsquo;</b>&hellip;&rdquo;</span></p>'
  '<div class=cite>' + RICH + ', footnote to the reply</div>'
  '<aside class=notes>Side path: Richardson&rsquo;s gloss, not Campbell&rsquo;s words. 1 Peter 2:9; Revelation 5:10, &ldquo;kings and priests to God.&rdquo; The priesthood of all believers, in a footnote.</aside></section>')
RS('<section class="slide breath"><div class=eyebrow>What they sang &middot; Psalm 118, the Scottish metrical version</div>'
  '<div class=litany style="gap:.6vmin">'
  '<div class=no style="font-size:clamp(28px,5.4vmin,68px)">&ldquo;Thou sore hast thrust that I might fall;</div>'
  '<div class=no style="font-size:clamp(28px,5.4vmin,68px)">' + G('But my Lord helped me') + '&hellip;</div>'
  '<div class="no frag" style="font-size:clamp(28px,5.4vmin,68px);margin-top:2vmin">I shall not die, but live, and shall</div>'
  '<div class="no frag" style="font-size:clamp(28px,5.4vmin,68px)">' + G('The works of God discover') + '.&rdquo;</div>'
  '</div><div class=cite>' + RICH + '</div>'
  '<aside class=notes>One click. Verses 13 to 29, as they had sung them as Seceders. Richardson: &ldquo;these verses of the Psalm they sung had to them a peculiar significance.&rdquo; Rejected, and not dead.</aside></section>')
RS(C('Two Wills, One Bequest', 'Tie it back. Kentucky, 1804, and Pennsylvania, 1811: neither side knew the other existed. Stone and Alexander Campbell would not meet until 1824.'))
