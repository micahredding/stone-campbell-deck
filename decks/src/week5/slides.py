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
    ('The priesthood of all believers<br>' + G('is real authority.'),
     'It inheres in every Christian and in the gathered church, not in an order above them. &ldquo;It is not the persons called bishops who have the power, but the people.&rdquo; No clergy-laity line.'),
    ('The priesthood of all believers<br>' + G('keeps the table.'),
     'Not only open to all: hosted by any. Campbell: the royal priesthood is &ldquo;consecrated to officiate&rdquo;; the one who gives thanks breaks the loaf &ldquo;not as the representative of the Lord, but after his example.&rdquo; Lipscomb: &ldquo;This is not officiating, for any disciple can do this.&rdquo;'),
    ('Authority lives where<br>' + G('two or three are gathered.'),
     'Matthew 18 gives the binding and loosing to the gathered church; Luther said the congregation&rsquo;s call confirms a minister; Cane Ridge willed each church to choose her own preacher; Brush Run licensed and ordained Alexander. And the table is a taste of the age to come: &ldquo;an emblem of the millennial state of the Church.&rdquo; &rarr; Next week: the Millennial Harbinger.'),
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
A('<section class="slide"><h2 style="max-width:none;color:var(--gold);font-size:clamp(34px,6.6vmin,84px);margin-bottom:1vmin">Unity movement</h2>'
  '<div style="display:flex;gap:6vw;justify-content:center;align-items:flex-start;margin-top:2vmin">'
  '<figure style="margin:0;text-align:center;flex:0 1 auto"><img src="IMG_STONE" alt="Barton W. Stone" style="height:50vh;width:auto;max-width:40vw;object-fit:contain;border-radius:.4vmin;box-shadow:0 1vmin 4vmin rgba(0,0,0,.6)"><figcaption style="margin-top:1.6vmin"><div style="font-family:\'IM Fell English SC\',Georgia,serif;letter-spacing:.12em;color:var(--smoke);font-size:clamp(14px,2.2vmin,26px)">Barton W. Stone</div><div style="font-family:Spectral,Georgia,serif;color:var(--gold);font-size:clamp(22px,3.8vmin,46px);line-height:1.2;max-width:34vw;margin:.6vmin auto 0">Unity in Communion</div></figcaption></figure>'
  '<figure style="margin:0;text-align:center;flex:0 1 auto"><img src="IMG_TCAMPBELL" alt="Thomas Campbell" style="height:50vh;width:auto;max-width:40vw;object-fit:contain;border-radius:.4vmin;box-shadow:0 1vmin 4vmin rgba(0,0,0,.6)"><figcaption style="margin-top:1.6vmin"><div style="font-family:\'IM Fell English SC\',Georgia,serif;letter-spacing:.12em;color:var(--smoke);font-size:clamp(14px,2.2vmin,26px)">Thomas Campbell</div><div style="font-family:Spectral,Georgia,serif;color:var(--gold);font-size:clamp(22px,3.8vmin,46px);line-height:1.2;max-width:34vw;margin:.6vmin auto 0">Unity in Communion</div></figcaption></figure>'
  '</div><aside class=notes>The recap, in two pictures. Stone at Cane Ridge, Thomas Campbell at Conemaugh: two men, a continent apart in sympathy if not in miles, who opened the Lord&rsquo;s table to Christians of other names.</aside></section>')

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

A('<section class="slide room"><div class="litany" style="gap:4vmin">'
  '<h2 class=no style="max-width:18ch;font-size:clamp(44px,10vmin,124px);line-height:1.12">Who has authority?</h2>'
  '<h2 class="no frag" style="max-width:18ch;font-size:clamp(44px,10vmin,124px);line-height:1.12">Who may serve the table?</h2></div>'
  '<aside class=notes>One click for the second question. Tonight&rsquo;s two points. Who can make someone a minister: a bishop, a presbytery, the congregation? And who may give thanks at the Lord&rsquo;s table? &rarr; &ldquo;Hold both.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 5</div>'
  '<h1>Wherever Two or Three<br>Are Gathered</h1><div class=table-line></div>'
  '<div class=sub>Brush Run, Pennsylvania &middot; 1811&ndash;1812</div>'
  '<aside class=notes>Matthew 18:20, and the <i>Declaration and Address</i> quotes it (we will see where). The Campbells&rsquo; side of the story, picking up where Chapter 2 left Alexander: off the coast of Scotland. Two points tonight: who serves the table, and where authority lives.<br>'
  'The hour: the sea 6 &middot; Glasgow 7 &middot; reunion 3 &middot; Brush Run 8 &middot; the ordination 8 &middot; who serves the table 7 &middot; two or three gathered 9 &middot; close 10.</aside></section>')
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
# ---------- GLASGOW ----------
A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">1 &middot; Article 4</span> &middot; Glasgow, winter 1808&ndash;09</div>'
  '<h2>He went to hear other preachers.</h2>'
  '<div class="sub frag">Above all <b>Greville Ewing</b>: fifteen hundred people in a converted circus.</div>'
  '<div class="sub frag">The very thing his father was tried for: <b><i>occasional hearing</i></b>.</div>'
  '<aside class=notes>Two clicks. The family wintered in Glasgow after the wreck; Alexander studied at the university. He found the Seceder minister &ldquo;a prosy speaker&rdquo; and went to hear others whenever he could, above all Ewing at the Tabernacle. Back in Pennsylvania his father had been condemned for saying Seceders might hear ministers of other churches.<br>&rarr; &ldquo;The son is doing every week what the father was condemned for.&rdquo;</aside></section>')

A('<section class="slide"><div class=eyebrow><span style="color:var(--gold)">2 &middot; Articles 2 &amp; 3</span> &middot; at Ewing&rsquo;s house</div>'
  '<h2>Ewing told him the story of the Haldanes.</h2>'
  '<div class="sub frag">Two Scottish <b>laymen</b> who began preaching the gospel without ordination.</div>'
  '<div class="sub frag">James Haldane was <b>arrested at the instigation of the clergy</b>.</div>'
  '<aside class=notes>Two clicks. Robert and James Haldane, wealthy ex-navy laymen; James preached for years before he was ordained. Ewing had left the Church of Scotland to join them, ran their Glasgow Tabernacle, and kept the Supper weekly. His father had also been condemned for letting elders, not ministers, pray and exhort. Richardson says this story, more than anything, changed Alexander&rsquo;s mind.</aside></section>')

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
A(BIGQ(Q('&ldquo;As many members of the Christian Association lived near Buffalo Creek, it was, about this time, <b>resolved to erect a house of worship there</b>.&rdquo;', RICH, '1810 &middot; a meeting house')) +
  N('A plot on William Gilchrist&rsquo;s farm, in the valley of Brush Run, two miles above Buffalo Creek. Joseph Bryant&rsquo;s family ran the saw-mill next door and sawed the lumber. A plain frame building, never finished.'))

A(BIGQ(Q('&ldquo;<b>Though thy beginning was small</b>, yet thy latter end should greatly increase.&rdquo;', 'Job 8:7 &middot; Alexander&rsquo;s text for the first sermon at the site &middot; in Richardson, <i>Memoirs</i>', 'Under a spreading tree'), 'clamp(40px,9vmin,116px)', '24ch') +
  N('Before the building went up, a temporary stand by the ground; Alexander gave the first discourse there. Richardson: &ldquo;singularly appropriate and prophetic.&rdquo;'))

A(BIGQ(Q('&ldquo;&hellip;as the Society was not a Church&hellip; most of its members&hellip; <b>were deprived of various privileges which belonged to the church relation</b>.&rdquo;', RICH, 'But a society is not a church')) +
  N('No Lord&rsquo;s Supper, no baptism, no ordination: a society can preach, but it cannot keep the table. Most members had drifted from their old congregations; some had never belonged to any.'))

A(BIGQ(Q('&ldquo;&hellip;the Society must obtain admission into some regularly organized religious body, or be itself compelled to change its attitude and <b>resolve itself into an independent Church</b> &mdash; an alternative which Thomas Campbell particularly desired to avoid.&rdquo;', RICH)) +
  N('So in October 1810 Thomas asked the Presbyterian Synod of Pittsburg to receive them. They refused (the whole story is in the reserve deck). Through the winter Alexander preached at Brush Run, Washington and in houses round about; in March 1811 he married Margaret Brown.'))

A(BIGQ(Q('&ldquo;It was with <b>great reluctance</b> that he finally concluded to take this step, and to separate himself from those whom he desired to recognize as brethren.&rdquo;', RICH, 'Thomas Campbell, spring 1811')) +
  N('Spring 1811. Every overture refused, Thomas concluded &ldquo;that the Christian Association should assume the character of an independent Church.&rdquo; The thing he had dreaded since 1809. &ldquo;At the next meeting of the Association, accordingly, the matter was duly considered and agreed to.&rdquo;'))
A(BIGQ(Q('&ldquo;At this meeting, <b>Thomas Campbell was appointed elder</b>, and <b>Alexander was licensed to preach the gospel</b>. Four deacons were also chosen&hellip;&rdquo;', RICH, 'May 4, 1811')) +
  N('The deacons: John Dawson, George Sharp, William Gilcrist, James Foster. About thirty members.',
    'No presbytery licensed him. The church did.'))
A(CARD('No bishop. No presbytery.<br>' + G('A congregation.'),
  'Let it sit. This is the thing no church court could imagine: a church that makes its own ministers.'))
for _x in R.governance(): A(_x)                   # side path: who governs the church (shared resource)
for _x in R.constitution(): A(_x)                # side path: confession or constitution (shared resource)
A('<section class="slide"><div class=eyebrow>The next day &middot; May 5, 1811 &middot; their first Lord&rsquo;s Supper</div>'
  '<p class="bigquote" style="font-size:clamp(30px,6.4vmin,80px);max-width:36ch;line-height:1.22"><span class=q>&ldquo;&hellip;in assembling there on that occasion, they furnished <b>an emblem of the millennial state of the Church</b>, nay, an emblem of the heavenly state, when men of different nations, and known by different names, <b>should sit down together in the kingdom of God</b>.&rdquo;</span></p>'
  '<div class=cite>Alexander Campbell&rsquo;s communion sermon &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>The high point of the hour. His text: John 6:48, &ldquo;I am that bread of life.&rdquo; Richardson is summarizing his sermon notes.<br>&rarr; &ldquo;The table is not only a memory. It is the future, arriving early: everyone who will be at the last table, at this one.&rdquo; Chapter 1&rsquo;s table, again.</aside></section>')
A(BIGQ(Q('&ldquo;&hellip;the Lord&rsquo;s Supper, which, according to the custom of the Independent churches in Scotland, <b>was now celebrated weekly</b>.&rdquo;', RICH, 'Every Lord&rsquo;s day')) +
  N('The Haldane churches again. At Cane Ridge the Supper came once or twice a year, after weeks of preparation and a token. At Brush Run, every Sunday, from the beginning. That is us.'))
for _x in R.weekly(): A(_x)                      # side path: the table every Lord's day (shared resource)
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
  N('His notes for a sermon that winter. The sentence goes on: &ldquo;and that it might be evidenced, the elders or rulers impose their hands.&rdquo; The laying on of hands shows the choice; it does not make it. Richardson: he regarded ordination not &ldquo;as conferring any authority, but as a public testimony that the persons ordained possessed the necessary authority.&rdquo; The authority is the congregation&rsquo;s.'))
A('<section class="slide breath"><div class=eyebrow>Against succession &middot; a side path</div><p class="bigquote" style="font-size:clamp(38px,8.4vmin,108px);max-width:26ch;line-height:1.16"><span class=q>&ldquo;Why do we contend for uninterrupted succession in ordination, seeing it is <b>not the persons called bishops who have the power, but the people?</b>&rdquo;</span></p>'
  '<div class=cite>' + AC + ', sermon on Titus 1:5 &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>Side path: the argument with the alternatives, for when the room asks. No apostolic succession, no line of hands from Peter to now that makes a minister. The power is in the people.<br>Richardson: he did not regard ordination &ldquo;as conferring any authority, but as a public testimony that the persons ordained possessed the necessary authority.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Asked why he preached without authority</div>'
  '<div class=litany style="gap:1.2vmin">'
  '<div class=no style="font-size:clamp(30px,6vmin,76px)">&ldquo;<b>Who has authority?</b></div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to license men?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to make laws for the Church?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to decide religious matters by vote?</div>'
  '<div class="no frag" style="font-size:clamp(26px,4.8vmin,60px)">Who gave the Presbytery authority to choose ministers?&rdquo;</div>'
  '</div><div class=cite>' + AC + ' &middot; in Richardson, <i>Memoirs</i></div>'
  '<aside class=notes>Four clicks; the question keeps extending. End of the side path. He turns the charge around: the presbytery is the one without authority.</aside></section>')
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
A(CARD('A minister, made by<br>' + G('the priesthood of all believers.'),
  'The meaning Brush Run attached to it: the authority to make a minister is in the congregation, because every member is a priest. Luther is a witness in &ldquo;The whole church remembers.&rdquo;'))
# ---------- POINT ONE: WHO SERVES THE TABLE? ----------
A(C('Who serves the table?', 'The first point. Brush Run kept the Supper every Lord&rsquo;s day, open to every Christian. Campbell&rsquo;s argument goes further: the table is kept by the priesthood of all believers.'))
A(SRC(BIGQ(Q('&ldquo;May they not, <b>without a human priest to consecrate the way for them</b>, approach the Lord&rsquo;s table, and <b>handle the loaf and cup</b>?&rdquo;', CS, 'The same priesthood keeps the table'), 'clamp(32px,7.2vmin,90px)', '34ch'), 'acr') +
  N('Later, in <i>The Christian System</i>. The sentence before: &ldquo;May not, then, holy and royal priests thank God for the Lord&rsquo;s table, its loaf, and cup of wine?&rdquo;',
    'He had already written, in the <i>Christian Baptist</i> (1827): &ldquo;&lsquo;The administration of ordinances&rsquo; is a popish phrase, and ought to be cashiered from the christian vocabulary.&rdquo;'))
A(SRC(BIGQ(Q('&ldquo;&hellip;the royal priesthood may approach the Lord&rsquo;s table without fear, inasmuch as they are <b>consecrated to officiate</b> by a blood&hellip;&rdquo;', CS), 'clamp(34px,7.6vmin,96px)', '30ch'), 'acr') +
  N('Consecrated to officiate: not by a bishop&rsquo;s hands, by Christ&rsquo;s blood. Every baptized member is ordained to the table.',
    'Against the clergyman who says &ldquo;Stand by, I am holier than thou&rdquo;: he &ldquo;desecrates the royal priesthood of Jesus Christ.&rdquo;'))
A(SRC(BIGQ(Q('&ldquo;&hellip;he that gives thanks for the loaf should break it <b>not as the representative of the Lord, but after his example</b>&hellip; And thus <b>they as priests feast upon his sacrifice</b>.&rdquo;', CS), 'clamp(32px,7.2vmin,90px)', '34ch'), 'acr') +
  N('Between the two halves: the disciples hand the loaf &ldquo;to one another,&rdquo; and the one who broke it eats with them. No one stands in for Christ; everyone serves everyone.',
    '&rarr; In our congregations the thanks at the table are given by members, not by the preacher. That is this, still.'))
A(BIGQ(Q('&ldquo;I dare not be a party man for these reasons&hellip; <b>Because no party will receive into communion all whom God would receive into heaven.</b>&rdquo;', AC + ', 1810', 'Throwback &middot; open communion'), 'clamp(32px,7.2vmin,90px)', '34ch') +
  N('Throwback to 1810, a year before Brush Run: an address after a sermon at Mr. Buchanan&rsquo;s. The next line: &ldquo;God loves his children more than our creeds, and man was not made for the Bible, but the Bible for man.&rdquo;',
    'Chapter 1&rsquo;s table and Chapter 2&rsquo;s trial, in one sentence.'))
A(BIGQ(Q('&ldquo;That division among the Christians is <b>a horrid evil, fraught with many evils</b>. It is antichristian, as it <b>destroys the visible unity of the body of Christ</b>&hellip;&rdquo;', DA + ', Proposition 10', 'Throwback &middot; Thomas Campbell, 1809')) +
  N('Chapter 3. The table is where that unity is shown, or denied: a fenced table divides the body at the very place it is meant to be one.'))
A(CARD('Open to all.<br>' + G('Hosted by any.'),
  'Brush Run&rsquo;s table was weekly and its fences were coming down. Campbell&rsquo;s argument goes further: the table is kept by the priesthood of all believers. Not only open; hosted by any.'))
for _x in R.table(): A(_x)                       # side path: who keeps the table (shared resource)
# ---------- POINT TWO: WHERE TWO OR THREE ARE GATHERED ----------
A(C('Where two or three are gathered', 'The second point. The authority to ordain, and to govern, inheres in the gathered church. Matthew 18, the Declaration and Address, the Last Will, Brush Run.'))
A(BIGQ(Q('&ldquo;&hellip;<b>tell it unto the church</b>&hellip; Verily I say unto you, <b>Whatsoever ye shall bind on earth shall be bound in heaven</b>&hellip;&rdquo;', 'Matthew 18:17&ndash;18 (KJV)', 'Where the keys are'), 'clamp(34px,7.6vmin,96px)', '30ch') +
  N('In Matthew 16 the keys go to Peter. In Matthew 18 the binding and loosing go to &ldquo;the church&rdquo;: the gathering that hears a brother&rsquo;s case. Two verses later, two or three gathered, and Christ in the midst.',
    'Thomas Campbell, in the <i>Declaration and Address</i>: this is &ldquo;the awful sanction of the Church&rsquo;s judgment.&rdquo;',
    '&rarr; A church that can bind and loose can surely choose its own minister.'))
for _x in R.ekklesia(): A(_x)                    # side path: the church as ekklesia, the assembly (shared resource)
A(BIGQ(Q('&ldquo;&hellip;for where <b>two or three are gathered together in my name</b>, there am I in the midst of them.&rdquo;', DA + ', quoting Matthew 18:20'), 'clamp(36px,8vmin,100px)', '28ch') +
  N('The <i>Address</i>, to the friends of reform: &ldquo;Let not the paucity of your number in any given district, prove an insuperable discouragement.&rdquo; Thirty people at a creek. Christ in the midst of them.',
    '&rarr; The title of the hour.'))
A(BIGQ(Q('&ldquo;We will, that each particular church, as a body, actuated by the same spirit, <b>choose her own preacher</b>&hellip; and <b>never henceforth delegate her right of government to any man or set of men whatever</b>.&rdquo;', WILL, 'Cane Ridge, 1804')) +
  N('Last week: the bequest to every congregation. Seven years later and hundreds of miles away, a congregation that never heard of the will does exactly this.',
    'Brush Run chose its own preacher, licensed him, and ordained him.'))
A(BIGQ(Q('&ldquo;We will, that candidates for the Gospel ministry henceforth study the holy scriptures with fervent prayer, and <b>obtain license from God</b> to preach the simple Gospel&hellip;&rdquo;', WILL, 'Cane Ridge, 1804')) +
  N('No presbytery&rsquo;s license. In May 1811 Brush Run licensed Alexander; in January 1812 it ordained him. The license from God, recognized by the congregation.'))
A(CARD('The Springfield Presbytery died<br>so that congregations could choose.<br>' + G('Brush Run chose.'),
  'The two streams meet in 1832. They already agreed.'))
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
