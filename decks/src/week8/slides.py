# -*- coding: utf-8 -*-
# Chapter 8: The Handshake at Lexington (the Stone-Campbell union, 1831-1835).
# The story as Micah told it (week8.md, "Story spine v3", 2026-11-19): recap (unity, freedom, priesthood, refused on
# every side); two movements in 1831; Lexington and every historic division at one table; Marburg; the proposition
# to unite on the Bible; the handshake; not agreement on interpretation; Campbell's circle; it took three years;
# it worked; the quiz again (No creed but... Christ or the Bible), Scott, and Williams's "their only Leader".
# Build:  python3 decks/src/week8map/build.py   ->  decks/chapter8.html
# Quotations: every quote slide carries data-chk=<source key>; python3 decks/src/week8/check_quotes.py.
import base64, importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
w4 = _load('w4slides', 'week4/slides.py')
R = _load('resources', 'resources.py')
w3 = w3b.w3
C, CARD, G, BLACK = w4.C, w4.CARD, w4.G, w4.BLACK
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS
Q, N = w3.Q, w3.N

def BIGQ(slide, size='clamp(30px,6.4vmin,80px)', width='40ch'):
    return re.sub(r'<p class="bigquote( long| xlong)?">', lambda m: '<p class="bigquote%s" style="font-size:%s;max-width:%s;line-height:1.22">' % (m.group(1) or '', size, width), slide, 1)
def K(slide, key):
    return slide.replace('<section class="slide', '<section data-chk="%s" class="slide' % key, 1)
def DS(slide, doc):   # route the slide's document view (press Z) to a document
    return slide.replace('<section ', '<section data-src="%s" ' % doc, 1)
def QK(quote, cite, eyebrow, key, *notes, size=None, width=None, doc=None):
    s = Q(quote, cite, eyebrow)
    if size: s = BIGQ(s, size, width or '40ch')
    s = K(s, key) + N(*notes)
    return DS(s, doc) if doc else s
def LIST(eyebrow, title, items, note, size='clamp(26px,4.6vmin,58px)', gap='1.6vmin'):
    lis = ''.join('<div class="no frag" style="font-size:%s">%s</div>' % (size, it) for it in items)
    return ('<section class="slide"><div class=eyebrow>%s</div><h2 style="max-width:none">%s</h2>'
            '<div class=litany style="text-align:left;gap:%s;max-width:90vw">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, title, gap, lis, note))
def D(y, t): return '<b>%s</b> &nbsp;%s' % (y, t)
def IMG(img, eyebrow, cite, note, h='72vh'):
    p = os.path.join(_H, 'images', img)
    src = 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    return ('<section class="slide"><div class=eyebrow>%s</div>'
            '<img src="%s" alt="" style="max-height:%s;max-width:88vw;height:auto;border:1px solid rgba(201,162,74,.55);box-shadow:0 6px 24px rgba(0,0,0,.6)">'
            '<div class=cite style="margin-top:2vmin">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, src, h, cite, note))

WIL = 'J. A. Williams, <i>Life of Elder John Smith</i> (1870)'
CM = 'Stone and Johnson, <i>Christian Messenger</i>'
SMITH = '&ldquo;Raccoon&rdquo; John Smith, at Lexington'
STONE = 'Barton W. Stone, at Lexington'

IDEAS = [
    ('They united around the Bible,<br>' + G('not their readings of it.'), 'Smith: &ldquo;one in faith, and not in opinion.&rdquo; Stone and Johnson: &ldquo;we do not know, nor are we concerned to know.&rdquo;'),
    ('Every historic division<br>' + G('came to one table.'), 'God, authority, the sacraments: what had divided Christendom since Nicaea was in the room at Hill Street.'),
    ('Unity was not a moment.<br>' + G('It was worked out.'), 'Three years in Lexington; person by person, congregation by congregation elsewhere.'),
    ('No creed but Christ;<br>' + G('the Bible as our manual.'), 'Scott, 1832: the Bible &ldquo;her only manual,&rdquo; &ldquo;Jesus Christ is the Son of God&rdquo; her creed. Williams: each had &ldquo;already taken Jesus the Christ as their only Leader.&rdquo;'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>' % (k, len(IDEAS), h, n))
def IDEASUM(note):
    return ('<section class="slide room"><div class=eyebrow>Today&rsquo;s ideas</div>'
            '<div class="litany ideasum" style="text-align:left;gap:1vmin;margin-top:2vmin">'
            + ''.join('<div class=no style="font-size:clamp(30px,6vmin,74px)"><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (n, h.replace('<br>', ' ')) for n, (h, _) in enumerate(IDEAS, 1))
            + '</div><aside class=notes>%s</aside></section>' % note)

S = []
A = S.append

# ---------- OPENING ----------
A(w3b.S[0])   # the class title
A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none;font-size:clamp(60px,13vmin,160px)">No creed but&hellip;</h2>'
  '<aside class=notes>Let them answer aloud. Expect both &ldquo;Christ&rdquo; and &ldquo;the Bible.&rdquo; Don&rsquo;t resolve it: note who said which. We come back to it at the end (&ldquo;No creed but&hellip;, again&rdquo;).</aside></section>')
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 8</div>'
  '<h1>The Handshake<br>at Lexington</h1><div class=table-line></div>'
  '<div class=sub>Stone&rsquo;s Christians and Campbell&rsquo;s Disciples &middot; 1831&ndash;1835</div>'
  '<aside class=notes>Chapter 8. Last week: the <i>Millennial Harbinger</i>, a movement living toward God&rsquo;s future. This morning: can they unite with anyone, even each other?</aside></section>')

# ---------- I. RECAP ----------
A(LIST('Where we are', 'What they were reaching for',
  ['<b>Unity:</b> Cane Ridge&rsquo;s open table; the <i>Declaration and Address</i>',
   '<b>Freedom:</b> conscience, and the people, over every outside authority',
   '<b>Laying down their own authority:</b> the Springfield Presbytery dies (1804); Mahoning dissolves itself (1830)',
   '<b>The priesthood of all:</b> Brush Run ordains by the choice of the people (1812)'],
  'Four clicks, one breath each. Unity, freedom, priesthood, and a willingness to dissolve their own bodies rather than stand in the way.',
  size='clamp(26px,4.8vmin,60px)', gap='2vmin'))
A(R.ASSOC_SUMMARY.replace('<div class=eyebrow>From the Evangelical Society on</div>', '<div class=eyebrow>And on every side</div>', 1)
   .replace('<h2 style="max-width:none">Joined, refused, dissolved</h2>', '<h2 style="max-width:none">They were refused</h2>', 1))
for _x in R.associations(): A(_x)   # side path: the whole timeline of joining and refusal
A(CARD('Because they would not<br>' + G('draw the lines where others drew them.'),
  'The Synod of Pittsburg (1810), the Baptist associations (1820s&ndash;1830), the Presbyterians (Stone, 1803). Every time: they reached for the widest fellowship, and refused any body that made a creed the test.'))
A(CARD('Can they achieve unity<br>' + G('with anyone?'), 'Hold the question.'))

# ---------- II. TWO MOVEMENTS ----------
A(C('1831: two movements', 'Our predecessors, the movement that led to us, and in 1831 still two.', '1831'))
A('<section class="slide"><div class=eyebrow>Two names</div>'
  '<div class=litany style="gap:3vmin;max-width:88vw">'
  '<div class=no style="font-size:clamp(34px,6.8vmin,86px)">Stone&rsquo;s people: <span style="color:var(--gold)">Christians</span>, only.</div>'
  '<div class="no frag" style="font-size:clamp(34px,6.8vmin,86px)">Campbell&rsquo;s people: <span style="color:var(--gold)">Disciples</span>, only.</div>'
  '<div class="no frag" style="font-size:clamp(28px,5vmin,62px);color:var(--bone-dim)">No creed. No authority but Scripture.</div></div>'
  '<aside class=notes>Two clicks. Stone&rsquo;s churches in Kentucky and Ohio since 1804; Campbell&rsquo;s &ldquo;Reformers,&rdquo; put out of the Baptist associations by 1830. Both had rejected creeds and every authority but Scripture. In Georgetown, in the autumn of 1831, the two began to worship together.</aside></section>')
A(QK('&ldquo;We saw no reason why <b>we should not be the same family</b>.&rdquo;',
     CM + ', January 1832', 'Georgetown, autumn 1831', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, p. 6. Stone and J. T. Johnson, in Georgetown: &ldquo;the Reforming Baptists, (known invidiously, by the name of Campbellites,) and the Christians, in Georgetown and the neighborhood, agreed to meet and worship together. We soon found that we were indeed in the same spirit, on the same foundation, the New Testament, and wore the same name, Christian.&rdquo;',
     size='clamp(40px,8.6vmin,108px)', width='26ch', doc='lex'))

# ---------- III. LEXINGTON: THE DIFFERENCES ----------
A(IMG('bower-1955-hill-street-meetinghouse.jpg', 'Hill Street, Lexington', 'The Hill Street meetinghouse of the Christians, painted by William Clayton Bower (1955)',
  'Saturday, December 31, 1831: a four-day meeting over New Year&rsquo;s, after another at Georgetown over Christmas. Williams: &ldquo;a multitude of anxious brethren began, at an early hour, to crowd the old meeting-house of the Christians, on Hill Street, in Lexington. There were Stone, and Johnson, and Smith, and Rogers, and Elley, and Creath&hellip;&rdquo; (p. 450). Hill Street is now High Street; the building was demolished in the 1970s. Image: therestorationmovement.com (class use).', h='62vh'))
A(QK('&ldquo;It was not a meeting of Elders or Preachers only, but <b>a popular assembly</b>&hellip;&rdquo;',
     WIL + ', p. 450', 'A mass meeting', 'wil',
     'Williams goes on: &ldquo;&mdash;a mass meeting of the brethren.&rdquo; They came &ldquo;to talk over, once more, and finally, the points of difference between them, to ascertain whether the proposed union were practicable.&rdquo; Williams wrote in 1870, from Smith&rsquo;s papers and memory.', doc='wil32'))
A(DS(LIST('&ldquo;Honest doubts respecting the doctrine of the others&rdquo;', 'What divided them',
  ['<b>Christ:</b> &ldquo;Some Reformers still looked upon the Christians as Arians&rdquo;',
   '<b>The Spirit:</b> the Reformers &ldquo;denied the influence of the Spirit&rdquo;',
   '<b>Baptism:</b> not all held &ldquo;in the same sense that baptism was for the remission of sins&rdquo;',
   '<b>The table, how open:</b> &ldquo;free or restricted communion&rdquo;',
   '<b>The table, how often:</b> weekly, or now and then',
   '<b>Clergy:</b> who may serve the table',
   '<b>The name:</b> Christian, or Disciple'],
  'Seven clicks. All from Williams, p. 450, except the last three: weekly communion (Stone: the Reformers &ldquo;insisted also upon weekly communion, which we had neglected,&rdquo; <i>Biography</i>); clergy (Stone, 1830: &ldquo;the church may elect, but not ordain&rdquo;; and see February 1832, below); the name (&ldquo;the Christians still refused to give up their name&rdquo;). The Spirit: some Christians feared the Reformers &ldquo;denied the influence of the Spirit, and attached undue importance to baptism&rdquo;: the Spirit&rsquo;s work in conversion, not his place in the Trinity. The Trinity charge ran the other way: Christ.',
  size='clamp(24px,4.3vmin,54px)', gap='1.3vmin'), 'wil32'))

# ---------- IV. EVERY HISTORIC DIVISION AT ONE TABLE ----------
A('<section class="slide"><div class=eyebrow>Two thousand years of division</div>'
  '<div class=litany style="text-align:left;gap:2.6vmin;max-width:88vw">'
  '<div class="no frag" style="font-size:clamp(32px,6.2vmin,78px)"><span style="color:var(--gold)">God</span> &nbsp;the Trinity &middot; Nicaea, 325</div>'
  '<div class="no frag" style="font-size:clamp(32px,6.2vmin,78px)"><span style="color:var(--gold)">Authority</span> &nbsp;who governs, who is clergy &middot; 1054, 1517</div>'
  '<div class="no frag" style="font-size:clamp(32px,6.2vmin,78px)"><span style="color:var(--gold)">The sacraments</span> &nbsp;baptism, the table &middot; 1529</div></div>'
  '<aside class=notes>Three clicks. The same three heads as the list just shown: Christ and the Spirit; clergy; baptism and the table. They recapitulate the whole history of Christian division. (Chapter 3&rsquo;s river of division, 325&ndash;1806, can be shown here: decks/elements/christendom-divisions.html.)</aside></section>')
A([_s for _s in w3.S if 'marburgbg' in _s][0])   # Chapter 3's Marburg slide (Noack's painting)
A(QK('&ldquo;To-day the Landgrave is making every effort to unite us, or at least to make us consider each other brethren and members of Christ&rsquo;s body&hellip; But <b>although we object to be brethren</b>, we wish to live at peace and on good terms.&rdquo;',
     'Martin Luther to Katharina, Marburg, October 4, 1529 (trans. Currie, 1908)', 'Luther, from Marburg', 'none',
     'Checked in the research database (<i>Who May Ordain / Churches Refusing Each Other&rsquo;s Orders</i>, A.2; Currie, <i>The Letters of Martin Luther</i>, p. 197). The Lutherans&rsquo; decision, per Brenz: the Zwinglians to be acknowledged &ldquo;as friends, but not as brothers and members of the church of Christ&rdquo; (WA 30 III, p. 155). Luther would not take the offered hand.', doc='lex'))
A(CARD('Every one of these divisions<br>' + G('was in the room at Lexington.'),
  'All Christendom had failed to unite across them. Can two small movements in Kentucky?'))

# ---------- V. THE PROPOSITION ----------
A(C('The proposition', 'Saturday, December 31, 1831. One speaker from each side: Smith for the Disciples, Stone for the Christians.'))
A(QK('&ldquo;God has but one people on the earth. <b>He has given to them but one Book</b>, and therein exhorts and commands them to be one family.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith rises first', 'wil',
     'Stone had asked: &ldquo;What is your choice, my brother? Will you speak first, or last?&rdquo; Smith: &ldquo;Brother Stone, I have no choice.&rdquo; Williams: &ldquo;Every eye turned upon him, and every ear leaned to catch the slightest tones of his voice.&rdquo;', doc='wil32'))
A(QK('&ldquo;But an amalgamation of sects is not such a union as Christ prayed for, and God enjoins.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Not an amalgamation', 'none',
     'Checked on the page scan (the OCR scrambles &ldquo;prayed for&rdquo;). Next: &ldquo;To agree to be one upon any system of human invention would be contrary to his will.&rdquo;', doc='wil32'))
A(QK('&ldquo;While there is but one faith, there may be ten thousand opinions; and hence, if Christians are ever to be one, <b>they must be one in faith, and not in opinion</b>.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 453', 'One faith', 'wil',
     'Just before, on the Trinity and the atonement: &ldquo;If I come to the passage, &lsquo;My Father is greater than I,&rsquo; I will quote it, but will not stop to speculate upon the inferiority of the Son.&rdquo; He will speak of such things &ldquo;only in the words which the Lord has given.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))
A(QK('&ldquo;Let us, then, my brethren, be no longer Campbellites or Stoneites&hellip; but <b>let us all come to the Bible, and to the Bible alone</b>, as the only book in the world that can give us all the Light we need.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 454', 'The proposition', 'wil',
     'The words cut: &ldquo;New Lights or Old Lights, or any other kind of lights.&rdquo; He sat down.', doc='wil32'))
A(QK('&ldquo;&hellip;the controversies of the Church sufficiently prove that <b>Christians never can be one in their speculations</b> upon those mysterious and sublime subjects&hellip;&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 454', 'Stone answers', 'wil',
     'Stone: &ldquo;I will not attempt to introduce any new topic.&rdquo; Of his own sermons on the Trinity, forced by opposition: &ldquo;I never preached a sermon of that kind that once feasted my heart; I always felt a barrenness of soul afterwards.&rdquo;', doc='wil32'))
A(QK('&ldquo;I have not one objection to the ground laid down by him as the true scriptural basis of union among the people of God; and <b>I am willing to give him, now and here, my hand</b>.&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 455', 'His hand', 'none',
     'Checked on the page scan (the OCR interleaves two lines here). Williams: &ldquo;He turned as he spoke, and offered to Smith a hand trembling with rapture and brotherly love, and it was grasped by a hand full of the honest pledges of fellowship.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))
A(IMG('cane-ridge-window-lexington-handshake.jpg', 'The handshake', 'Stained-glass window, Cane Ridge Meeting House (photograph: therestorationmovement.com)',
  'Over an open Bible on the pulpit; the communion table before them, two plates and two cups. Set it against Marburg: Luther would not take the hand; Stone offered his. Maker and date of the window: unknown (to find). Class use only.', h='70vh'))
A(DS(QK('&ldquo;A song arose, and brethren and sisters, with many tearful greetings, ratified and confirmed the union. <b>On Lord&rsquo;s day, they broke the loaf together</b>&hellip;&rdquo;',
     WIL + ', p. 455', 'The song and the loaf', 'wil',
     'Before: &ldquo;elders and teachers hastened forward, and joined their hands and hearts in joyful accord.&rdquo; After: &ldquo;and in that sweet and solemn communion, again pledged to each other their brotherly love.&rdquo; Sunday, January 1, 1832. Williams is the only source for the communion that day; Smith&rsquo;s own letter (February 1832) confirms they broke the loaf together in the weeks after.'), 'wil32'))

# ---------- VI. NOT AGREEMENT ON INTERPRETATION ----------
A(CARD('They did not agree<br>' + G('on how to read it.'), 'Uniting around the Bible was not agreeing on its interpretation: Christ, the Spirit, baptism, the table, the clergy were all still open.'))
A(QK('&ldquo;It may be asked, is there no difference of opinion among you? We answer, <b>we do not know, nor are we concerned to know</b>.&rdquo;',
     CM + ', January 1832', 'The statement', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, p. 6&ndash;8. Next: &ldquo;We have never asked them what were their opinions, nor have they asked us. If they have opinions different from ours, they are welcome to have them, provided they do not endeavor to impose them on us as articles of faith.&rdquo; And the creed: &ldquo;We have a perfect one&hellip; we mean the New Testament.&rdquo;',
     size='clamp(32px,6.8vmin,86px)', doc='lex'))
for _x in R.circle(): A(_x)   # Campbell's circle, January 2, 1832 (two slides)

# ---------- VII. IT TOOK THREE YEARS ----------
A(C('It took three years', 'The differences mattered in practice. They worked them out.'))
A(QK('&ldquo;For they believe that <b>no person but a preacher</b> has a right to administer the ordinances&mdash;such as the breaking of the loaf &amp;c. and become very much alarmed at the idea of <b>us common folks</b> receiving the name of kings and priests to the Lord&hellip;&rdquo;',
     'H. C. C., a Disciple in Lexington, to Campbell, <i>Millennial Harbinger</i> 1832, p. 192', 'Lexington, February 1832', 'mh1832',
     'The two Lexington congregations pledged to &ldquo;unite upon the New Testament&rdquo; (Feb. 12), broke the loaf together (Feb. 19), and dissolved the pledge (Feb. 25), over choosing an elder and who may serve the table. &ldquo;us common folks&rdquo;: read on the page scan. His verdict: &ldquo;It is the Clergy&mdash;the hireling system&mdash;the called and sent&mdash;the rulers&mdash;that keep us apart.&rdquo; Side path: <i>Who keeps the table</i>.', doc='lex'))
for _x in R.table(): A(_x)   # side path: who keeps the table
A(DS(QK('&ldquo;Nor was a union between the two congregations finally and formally effected <b>till in July, 1835</b>&hellip;&rdquo;',
     WIL + ', p. 460', 'Lexington, 1835', 'wil',
     'When Thomas M. Allen, preaching to the Lexington Christians, proposed it again; they &ldquo;waived all prejudice and differences of opinion on the subject of order and clerical privilege&rdquo; and &ldquo;not only consented to the union, but nobly proposed it to the Disciples.&rdquo; Williams is the only source for 1835 found so far.',
     size='clamp(36px,7.6vmin,96px)'), 'lex'))
A(LIST('Beyond Lexington', 'Person by person, congregation by congregation',
  [D('1832', 'Smith (a Disciple) and Rogers (a Christian) ride together to every church'),
   D('1832', 'Smith defends himself to his own alarmed Reformers'),
   D('1834', 'Jacksonville, Illinois: Stone joins neither church until they unite'),
   D('1835', 'Lexington, at last')],
  'Four clicks. Stone at Jacksonville: &ldquo;I refused to unite with either until they united together, and labored to effect it. It was effected&rdquo; (<i>Biography</i>, p. 79). Where it was slow, Stone blamed &ldquo;a few ignorant, headstrong bigots on both sides.&rdquo; (The map of the spreading union goes here once the gazetteer is in.)',
  size='clamp(28px,5.2vmin,66px)', gap='1.8vmin'))
A(CARD('No magic moment.<br>' + G('It was worked out.'),
  'Visible unity came over years, with patience and forbearance, exploring together. Smith called it &ldquo;the best act of his life&rdquo; (Williams, p. 456); Stone, &ldquo;the noblest act of my life&rdquo; (<i>Biography</i>, p. 79).'))

# ---------- VIII. AND IT WORKED ----------
A(CARD('And it worked:<br>' + G('one movement, one history.'), 'We look back on it as shared history. Today it is one movement, in three streams.'))
A(CARD('Are we more Stone,<br>' + G('or more Campbell?'),
  'For discussion. Weekly communion (Campbell); the open table (Stone); baptism for remission (Campbell); elders and preachers; the name; revival and the Spirit (Stone). It gets confusing, and that is the point.', 'For discussion'))

# ---------- IX. NO CREED BUT..., AGAIN ----------
A('<section class="slide"><div class=eyebrow>The quiz, again</div>'
  '<h2 style="max-width:none;font-size:clamp(60px,13vmin,160px)">No creed but&hellip;</h2>'
  '<div class="litany" style="gap:2vmin;margin-top:3vmin">'
  '<div class="no frag" style="font-size:clamp(34px,7vmin,88px);color:var(--gold)">&hellip;Christ.</div>'
  '<div class="no frag" style="font-size:clamp(34px,7vmin,88px);color:var(--gold)">&hellip;the Bible.</div></div>'
  '<aside class=notes>Two clicks: the room&rsquo;s two answers. &ldquo;No creed but the Bible&rdquo; is Stone&rsquo;s own phrase (1828, 1832); &ldquo;No creed but Christ&rdquo; grows out of Walter Scott&rsquo;s creed and is a slogan by the 1900s. Side path: <i>No creed but&hellip;</i>.</aside></section>')
A(QK('&ldquo;&hellip;to state the anomaly as boldly as possible, the movement is at one and the same time <b>Christocentric and bibliocentric</b>.&rdquo;',
     'Dwight E. Stevenson, Disciples Panel of Scholars (1963)', 'Two proposals?', 'enc',
     'As quoted in the <i>Encyclopedia of the Stone-Campbell Movement</i>, &ldquo;Faith.&rdquo; Paul Blowers summarizes him: the two slogans are &ldquo;very different proposals, as different as allegiance to Christ and allegiance to the strict letter of the scriptural text.&rdquo;'))
A(DS(QK('&ldquo;&hellip;her only manual was, &lsquo;<b>The Bible</b>.&rsquo; And her all comprehensive creed for the binding of the faithful; &lsquo;<b>Jesus Christ is the Son of God</b>.&rsquo;&rdquo;',
     'Walter Scott, <i>The Evangelist</i> (1832), &ldquo;Primitive Sufferings,&rdquo; p. 32', 'Scott, the year of Lexington', 'ev32',
     'Of the first church. &ldquo;On this faith and this volume she gathered her children thick as the leaves in Autumn.&rdquo; The Bible the manual; Christ the creed. Both of the room&rsquo;s answers, in one sentence. Side path follows.',
     size='clamp(30px,6.4vmin,82px)', width='34ch'), 'crd'))
for _x in R.creed(): A(_x)   # side path: No creed but...
A(CARD('Different proposals,<br>' + G('only if we forget what they meant.'),
  'Micah, in his own voice: he prefers &ldquo;No creed but Christ.&rdquo; Uniting on the Bible was never uniting on opinions about the Bible. Smith, the same morning: &ldquo;no deduction or inference from them, however logical or true, forms any part of the Gospel of Jesus Christ&rdquo; (Williams, p. 453).'))
A(DS(QK('&ldquo;The brethren of Stone did not join Alexander Campbell as their leader, nor did the brethren of Campbell join Barton W. Stone as their leader; but each, <b>having already taken Jesus the Christ as their only Leader</b>, in love and liberty became one body&hellip;&rdquo;',
     WIL + ', p. 456', 'Their only Leader', 'wil',
     'Williams&rsquo;s summary of what the handshake meant (1870). It goes on: &ldquo;not Stoneites, or Campbellites; not Christians, or Disciples, distinctively as such; but Christians, Disciples, saints, brethren, and children of the same Father.&rdquo; Before it: &ldquo;an equal and mutual pledge and resolution to meet on the Bible as on common ground, and to preach the Gospel rather than to propagate opinions.&rdquo;'), 'wil32'))
A(CARD('A shared practice:<br>' + G('coming to Scripture to meet Christ.'),
  'What that looked like, person by person and congregation by congregation, could be as far apart as all the historic streams of Christianity. And still they held that it could bring them together.'))

# ---------- CLOSE ----------
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A(IDEASUM('All four at once, before the discussion.'))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): What do we still require of each other before we will eat together? What would it take to keep eating together while we disagree? Which division from the list would be hardest for us?</aside>',
         w3b.pick('&#9670; for discussion', 0), flags=re.S).replace('&#9670; for discussion', '&#9670; for discussion &middot; Chapter 8', 1))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Today&rsquo;s sources: Williams&rsquo;s <i>Life of Elder John Smith</i>, Stone&rsquo;s <i>Christian Messenger</i>, the <i>Millennial Harbinger</i>, Scott&rsquo;s <i>Evangelist</i>.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S).replace('<h2 class=url>stone-campbell.micahredding.com</h2>',
          '<h2 class=url style="letter-spacing:.02em"><span style="color:var(--gold)">stone-campbell</span><span style="color:#ede4d3;opacity:.75">.micahredding.com</span></h2>', 1))
A(BLACK)
