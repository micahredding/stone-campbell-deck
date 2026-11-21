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
UM = _load('unionmap', 'week8/unionmap.py')
DV = _load('division', 'week8/division.py')
RC = _load('recap', 'week8/recap.py')
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
    ('Scripture, like the table,<br>' + G('is shared by all.'), 'Not doctrines to agree on: a shared table, a shared conversation, a shared way to meet Christ. Scott, 1832: the Bible &ldquo;her only manual,&rdquo; &ldquo;Jesus Christ is the Son of God&rdquo; her creed.'),
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

# ---------- I. RECAP: the story so far ----------

A(C('Story so far&hellip;', 'Seven pictures, one breath each, in the order we told them (the <i>Last Will</i>, 1804, was Chapter 4, after the <i>Declaration</i>).'))
for _x in RC.slides(): A(_x)   # the recap in pictures (Micah, 2026-11-21: one image slide per point; the eight-line list removed)

# ---------- II. OUR MOVEMENT, TWO MOVEMENTS, SO MUCH IN COMMON ----------

A(C('Our movement, our tradition', 'This is the movement that led to us. Until 1832, it was two.', 'Until 1832'))

A('<section class="slide twomv" style="padding:4vmin 4vw 4vmin;justify-content:flex-start;padding-top:9vh"><div class=twobg style="position:absolute;inset:0;display:flex;gap:.5vmin;background:#0e0b09;z-index:0"><div style="flex:1;overflow:hidden"><img src="' + RC._b64('stone-biography-1847.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:sepia(.35) brightness(.5)"></div><div style="flex:1;overflow:hidden"><img src="' + RC._b64('acold-engraving-oval.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 25%;filter:sepia(.2) brightness(.5)"></div></div><div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.55) 0%,rgba(14,11,9,.15) 70%)"></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;width:88vw;margin:0 0 3.5vmin"><div style="text-align:right;font-family:\'IM Fell English\',Georgia,serif;color:var(--gold);font-size:clamp(36px,7vmin,88px);text-shadow:0 2px 14px #000">Stone&rsquo;s Christians</div><div style="text-align:left;font-family:\'IM Fell English\',Georgia,serif;color:var(--gold);font-size:clamp(36px,7vmin,88px);text-shadow:0 2px 14px #000">Campbell&rsquo;s Reformers</div></div><div class=litany style="gap:1.2vmin;width:88vw;max-width:none"><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right"><b style="color:var(--gold)">&ldquo;Christians&rdquo;</b></div><div style="text-align:left"><b style="color:var(--gold)">&ldquo;Disciples&rdquo;</b></div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Unity in freedom</div><div style="text-align:left">Unity in freedom</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Open table</div><div style="text-align:left">Open table</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">No creed</div><div style="text-align:left">No creed</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Priesthood of all</div><div style="text-align:left">Priesthood of all</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Radical future</div><div style="text-align:left">Radical future</div></div></div><style>.twomv>*:not(.twobg):not(aside){position:relative;z-index:1}.twomv .litany>div{text-shadow:0 2px 12px #000,0 0 4px #000}</style><aside class=notes>Six clicks, one row each. What the two shared (Micah, 2026-11-20): unity within freedom and diversity of thought; an open table to Christians of every name (Stone; and Campbell: &ldquo;the only bond of union&rdquo; is the confession that Jesus is the Christ); creeds laid down as tests of fellowship; the priesthood of all, with governance in the people (the <i>Last Will</i>; Brush Run); and a radical future, the kingdom breaking in, calling for religious and social reform (Stone&rsquo;s premillennial hope; the <i>Harbinger</i>). So much in common: seeking unity with all Christians, surely they could find it with each other. So they began to look for a way to embody that unity in practice.</aside></section>')


A(QK('&ldquo;We saw no reason why <b>we should not be the same family</b>.&rdquo;',
     CM + ', January 1832', 'Georgetown, autumn 1831', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, p. 6. Stone and J. T. Johnson, in Georgetown: &ldquo;the Reforming Baptists, (known invidiously, by the name of Campbellites,) and the Christians, in Georgetown and the neighborhood, agreed to meet and worship together. We soon found that we were indeed in the same spirit, on the same foundation, the New Testament, and wore the same name, Christian.&rdquo;',
     size='clamp(40px,8.6vmin,108px)', width='26ch', doc='lex'))

# ---------- III. LEXINGTON: THE PEOPLE, AND THEIR DIVISIONS ----------

A(IMG('bower-1955-hill-street-meetinghouse.jpg', 'Hill Street, Lexington', 'The Hill Street meetinghouse of the Christians, painted by William Clayton Bower (1955)',
  'Saturday, December 31, 1831: a four-day meeting over New Year&rsquo;s, after another at Georgetown over Christmas. Williams: &ldquo;a multitude of anxious brethren began, at an early hour, to crowd the old meeting-house of the Christians, on Hill Street, in Lexington. There were Stone, and Johnson, and Smith, and Rogers, and Elley, and Creath&hellip;&rdquo; (p. 450). Hill Street is now High Street; the building was demolished in the 1970s. Image: therestorationmovement.com (class use).', h='62vh'))

A(QK('&ldquo;It was not a meeting of Elders or Preachers only, but <b>a popular assembly</b>&hellip;&rdquo;',
     WIL + ', p. 450', 'A mass meeting', 'wil',
     'Williams goes on: &ldquo;&mdash;a mass meeting of the brethren.&rdquo; They came &ldquo;to talk over, once more, and finally, the points of difference between them, to ascertain whether the proposed union were practicable.&rdquo; Williams wrote in 1870, from Smith&rsquo;s papers and memory.', doc='wil32'))

A('<section class="slide" style="padding:3vmin 4vw 6vmin"><div class=eyebrow>Points of contention</div><div class=litany style="gap:1.6vmin;text-align:left"><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Godhead:</b> Christ, Spirit</div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Clergy</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Table</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Baptism</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Future</b></div></div><aside class=notes>Five clicks, one line each. Side by side, as we tell it: Godhead, Christ: the Christians kept to Scripture&rsquo;s words, and to the Reformers looked &ldquo;Arian&rdquo;; the Reformers held the Trinitarian faith. Godhead, the Spirit: the Christians, that he works directly, in conversion and revival (the camp meeting, the anxious seat); the Reformers, that he works through the word (believe the gospel facts, confess, be immersed). Clergy: ordained elders and preachers serve the ordinances, or any disciple may, the church appointing. Table: free communion or restricted to the immersed; now and then, or every Lord&rsquo;s day. Baptism: immersion, but not &ldquo;for the remission of sins,&rdquo; or immersion for the remission of sins. Future: Christ comes first, to judge, or the gospel brings the millennium. Williams, p. 450: &ldquo;some of each party still cherished honest doubts respecting the doctrine of the others.&rdquo; Christ and the Spirit, Williams, p. 450: &ldquo;Some Reformers still looked upon the Christians as Arians; and some Christians were adverse to the union, in the belief that the Reformers denied the influence of the Spirit, and attached undue importance to baptism.&rdquo; The Spirit here is his work in conversion (Campbell: the Spirit works through the word), not his place in the Trinity. Baptism: &ldquo;all did not hold in the same sense that baptism was for the remission of sins.&rdquo; Most Christians had come to immerse; Stone: the Reformers &ldquo;preached baptism for the remission of sins to believing penitents.&rdquo; The table: &ldquo;they still differed on the question of free or restricted communion&rdquo;; Stone: the Reformers &ldquo;insisted also upon weekly communion, which we had neglected&rdquo; (<i>Biography</i>). Clergy: Stone, 1830: &ldquo;the church may elect, but not ordain&rdquo;; Campbell: any disciple may break the loaf; the Lexington churches split on exactly this in February 1832. Conversion: Stone&rsquo;s revival culture (Cane Ridge) against Scott&rsquo;s plan of salvation (believe, repent, be baptized, receive). The future: Stone premillennial by 1832&ndash;33; Campbell postmillennial (Chapter 7). These are generalizations: people on both sides held both views on several points.</aside></section>')

# ---------- IV. THE WHOLE HISTORY OF DIVISION ----------

for _x in DV.slides(): A(_x)   # the egg replayed; God, authority and clergy, the sacraments, each answered at Lexington

A(CARD('Every division of eighteen centuries<br>' + G('in one room.'),
  'The Trinity, the clergy, the sacraments: what had divided Christendom since Nicaea. Will it be unity, or division, like every effort before?'))

# ---------- V. THE HANDSHAKE ----------

A(C('The proposition', 'Saturday, December 31, 1831. One speaker from each side: Smith for the Disciples, Stone for the Christians.'))

A(IMG('smith-sartain-1870.jpg', '&ldquo;Raccoon&rdquo; John Smith, 1784&ndash;1868', 'Frontispiece engraving by John Sartain, in J. A. Williams, <i>Life of Elder John Smith</i> (1870)',
  'Who he was: born 1784 in East Tennessee (&ldquo;a native of the State of Franklin,&rdquo; the short-lived breakaway frontier state, Williams p. 13) to a Regular Baptist family, raised in Stockton&rsquo;s Valley on the Kentucky frontier, &ldquo;never had more than six months of schooling&rdquo; (<i>Encyclopedia</i>). January 1815, near Huntsville, Alabama: his cabin burned and two of his children died; his wife died soon after. Riding home, the Calvinist preacher could not comfort her: &ldquo;If I tell her that our babies are glorified, the thought that possibly they were of the non-elect will only aggravate her woe&rdquo;; his faith in that doctrine &ldquo;yielded up its strength forever&rdquo; (Williams, p. 103). The nickname means backwoodsman: at Crab Orchard in 1815 he introduced himself as from the hills of the Cumberland, where &ldquo;saltpeter caves abound, and raccoons make their homes&rdquo; (p. 115), and people spoke of &ldquo;the man that had been raised among the raccoons&rdquo; (p. 117). Later Philip Fall posted notices in Frankfort that &ldquo;Raccoon John Smith would preach&rdquo;; ever after, &ldquo;some knew me as &lsquo;Raccoon John Smith, of Montgomery&rsquo;&rdquo; (p. 278), a title he &ldquo;disliked but tolerated.&rdquo; 1828, to his wife: &ldquo;I have baptized seven hundred sinners and capsized fifteen hundred Baptists&rdquo; (p. 258). &ldquo;A civil Campbellite&rdquo; (Williams, pp. 478&ndash;479, read on the page scan): on a journey south, a woman serving him breakfast had heard of &ldquo;a strange sort of people up there in Kentucky called Campbellites&rdquo;; she was told they &ldquo;even chased after people, and ran them down,&rdquo; and once ran a poor fellow &ldquo;five miles before they caught him.&rdquo; Smith: &ldquo;That was a very long-winded fellow, ma&rsquo;am.&rdquo; She imagined &ldquo;a sort of wild, fierce, fanatical look.&rdquo; Smith, setting down his knife and fork: &ldquo;look right at me, and you will see one! But don&rsquo;t be afraid&hellip; I am a <i>civil</i> Campbellite, and will not chase <i>you</i> into the water.&rdquo;', h='74vh'))
# Raccoon John Smith, for flavor (Micah, 2026-11-21: "I want all this")
A(DS(LIST('&ldquo;Raccoon&rdquo; John Smith', 'Who he was',
  [D('1784', 'Born in the &ldquo;State of Franklin,&rdquo; the breakaway frontier state'),
   D('Boyhood', 'Stockton&rsquo;s Valley, Kentucky; six months of school'),
   D('1815', 'Two children die in a cabin fire; his Calvinism breaks'),
   D('1815', 'Crab Orchard: the preacher &ldquo;raised among the raccoons&rdquo;'),
   D('1828', 'Thirty baptisms a week')],
  'Five clicks. Born October 15, 1784, in Sullivan County, East Tennessee, while the State of Franklin was forming (Williams, p. 13). Raised on the Kentucky frontier; &ldquo;never had more than six months of schooling&rdquo; (<i>Encyclopedia</i>). A Regular Baptist preacher from 1808; a farmer all his life, since the Baptists did not pay their preachers. The fire: January 1815, near Huntsville, Alabama; his wife Anna died soon after. The name meant backwoodsman. In 1828 he averaged thirty or more baptisms a week for months.',
  size='clamp(26px,4.8vmin,60px)', gap='1.8vmin'), 'lex'))
A(DS(QK('&ldquo;If I tell her that our babies are glorified, <b>the thought that possibly they were of the non-elect will only aggravate her woe</b>.&rdquo;',
     'Smith, riding home to his wife, January 1815 &middot; ' + WIL + ', p. 103', 'The fire', 'wil',
     'The messenger: &ldquo;Your house took fire last night, and every thing is lost. Two of the children were burned to death&rdquo; (p. 102). Williams: &ldquo;his faith in that harsh doctrine of his Church yielded up its strength forever.&rdquo; The man who would say &ldquo;one in faith, and not in opinion&rdquo; lost a doctrine before he lost a creed.'), 'lex'))
A(DS(QK('&ldquo;I am John Smith, from Stockton&rsquo;s Valley&hellip; Down there, saltpeter caves abound, and <b>raccoons make their homes</b>. On that wild frontier we never had good schools, nor many books; consequently, I stand before you to-day a man without an education.&rdquo;',
     'Smith at Crab Orchard, Kentucky, 1815 &middot; ' + WIL + ', p. 115', 'Where the name came from', 'none',
     'Read on the page scan (the OCR scrambles it). He came back from Alabama ragged and grieving, and introduced himself so to a Baptist association. It goes on: &ldquo;But, my brethren, even in that ill-favored region, the Lord, in good time, found me.&rdquo; The crowd wanted to hear again &ldquo;the man that had been raised among the raccoons&rdquo; (p. 117). Years later, at Frankfort, Philip Fall&rsquo;s notices read &ldquo;Raccoon John Smith would preach&rdquo;; he &ldquo;disliked but tolerated&rdquo; the name.'), 'lex'))
A(DS(QK('&ldquo;I have baptized seven hundred sinners and <b>capsized fifteen hundred Baptists</b>.&rdquo;',
     'Smith to his wife, 1828 &middot; ' + WIL + ', p. 258', 'The preacher', 'none',
     '&ldquo;Nancy,&rdquo; said he: checked; the OCR runs &ldquo;sinners and&rdquo; together. &ldquo;Capsized&rdquo; is a boat joke beside &ldquo;baptized&rdquo;: he turned Baptists over, out of the Calvinist Baptist creed and into the Reformation. Not rebaptism: they were already immersed, and the Reformers did not rebaptize Baptists. Seven hundred new converts baptized; fifteen hundred Baptists won over, whole churches with them. He went on: &ldquo;so we have made two great mistakes&rdquo;: he had told her at the start of the year that the Reformation would not prevail in his lifetime, and he had braced for persecution, yet within six months &ldquo;it was already established in the hearts of the people&rdquo; (Williams, pp. 258&ndash;259).', size='clamp(40px,8.4vmin,104px)', width='26ch'), 'lex'))
A(DS(QK('&ldquo;Look right at me, and you will see one! But don&rsquo;t be afraid&hellip; <b>I am a civil Campbellite, and will not chase you into the water</b>.&rdquo;',
     'Smith, to a woman at breakfast &middot; ' + WIL + ', p. 479', 'A civil Campbellite', 'none',
     'Read on the page scan. On a journey south, the woman of the house had heard of &ldquo;a strange sort of people up there in Kentucky called Campbellites&rdquo; who &ldquo;even chased after people, and ran them down,&rdquo; once a poor fellow &ldquo;five miles before they caught him.&rdquo; Smith: &ldquo;That was a very long-winded fellow, ma&rsquo;am.&rdquo; She imagined &ldquo;a sort of wild, fierce, fanatical look.&rdquo; Then he sat her down, told her what they believed, and invited her to hear him preach.', size='clamp(36px,7.6vmin,96px)', width='28ch'), 'lex'))
A(QK('&ldquo;God has but one people on the earth. <b>He has given to them but one Book</b>, and therein exhorts and commands them to be one family.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith rises first', 'wil',
     'Stone had asked: &ldquo;What is your choice, my brother? Will you speak first, or last?&rdquo; Smith: &ldquo;Brother Stone, I have no choice.&rdquo; Williams: &ldquo;Every eye turned upon him, and every ear leaned to catch the slightest tones of his voice.&rdquo;', doc='wil32'))

A(QK('&ldquo;While there is but one faith, there may be ten thousand opinions; and hence, if Christians are ever to be one, <b>they must be one in faith, and not in opinion</b>.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 453', 'One faith', 'wil',
     'Just before, on the Trinity and the atonement: &ldquo;If I come to the passage, &lsquo;My Father is greater than I,&rsquo; I will quote it, but will not stop to speculate upon the inferiority of the Son.&rdquo; He will speak of such things &ldquo;only in the words which the Lord has given.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))

A(QK('&ldquo;&hellip;the controversies of the Church sufficiently prove that <b>Christians never can be one in their speculations</b> upon those mysterious and sublime subjects&hellip;&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 454', 'Stone answers', 'wil',
     'Stone: &ldquo;I will not attempt to introduce any new topic.&rdquo; Of his own sermons on the Trinity, forced by opposition: &ldquo;I never preached a sermon of that kind that once feasted my heart; I always felt a barrenness of soul afterwards.&rdquo;', doc='wil32'))

A(QK('&ldquo;I have not one objection to the ground laid down by him as the true scriptural basis of union among the people of God; and <b>I am willing to give him, now and here, my hand</b>.&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 455', 'His hand', 'none',
     'Checked on the page scan (the OCR interleaves two lines here). Williams: &ldquo;He turned as he spoke, and offered to Smith a hand trembling with rapture and brotherly love, and it was grasped by a hand full of the honest pledges of fellowship.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))

A(CARD('Not agreement of opinion:<br>' + G('agreement of faith.'),
  'Smith: &ldquo;one in faith, and not in opinion.&rdquo; Williams: &ldquo;who taught that opinions were no part of the faith delivered to the saints&rdquo; (p. 455).'))

A(QK('&ldquo;It may be asked, is there no difference of opinion among you? We answer, <b>we do not know, nor are we concerned to know</b>.&rdquo;',
     CM + ', January 1832', 'The statement', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, p. 6&ndash;8. Next: &ldquo;We have never asked them what were their opinions, nor have they asked us. If they have opinions different from ours, they are welcome to have them, provided they do not endeavor to impose them on us as articles of faith.&rdquo; And the creed: &ldquo;We have a perfect one&hellip; we mean the New Testament.&rdquo;',
     size='clamp(32px,6.8vmin,86px)', doc='lex'))

A(IMG('cane-ridge-window-lexington-handshake.jpg', 'The handshake', 'Stained-glass window, Cane Ridge Meeting House (photograph: therestorationmovement.com)',
  'Over an open Bible on the pulpit; the communion table before them, two plates and two cups. Set it against Marburg: Luther would not take the hand; Stone offered his. Maker and date of the window: unknown (to find). Class use only.', h='70vh'))

A(DS(QK('&ldquo;A song arose, and brethren and sisters, with many tearful greetings, ratified and confirmed the union. <b>On Lord&rsquo;s day, they broke the loaf together</b>&hellip;&rdquo;',
     WIL + ', p. 455', 'The song and the loaf', 'wil',
     'Before: &ldquo;elders and teachers hastened forward, and joined their hands and hearts in joyful accord.&rdquo; After: &ldquo;and in that sweet and solemn communion, again pledged to each other their brotherly love.&rdquo; Sunday, January 1, 1832. Williams is the only source for the communion that day; Smith&rsquo;s own letter (February 1832) confirms they broke the loaf together in the weeks after.'), 'wil32'))

# ---------- VI. IT TOOK SEVERAL YEARS ----------

A(C('It took years', 'The honest truth: the differences mattered in practice: how to keep the Supper, how to think of their clergy. They worked it out, congregation by congregation.'))

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
  'Four clicks. Stone at Jacksonville: &ldquo;I refused to unite with either until they united together, and labored to effect it. It was effected&rdquo; (<i>Biography</i>, p. 79). Where it was slow, Stone blamed &ldquo;a few ignorant, headstrong bigots on both sides.&rdquo;',
  size='clamp(28px,5.2vmin,66px)', gap='1.8vmin'))

A(UM.slide())   # the union spreading, in waves (Micah, 2026-11-19)

A(CARD('No magic moment.<br>' + G('It was worked out.'),
  'Visible unity came over years, with patience and forbearance, exploring together. Smith called it &ldquo;the best act of his life&rdquo; (Williams, p. 456); Stone, &ldquo;the noblest act of my life&rdquo; (<i>Biography</i>, p. 79).'))

# ---------- VII. IT WORKED ----------

A(CARD('And it worked:<br>' + G('one movement, one history.'), 'Today we do not speak of a Stone movement and a Campbell movement, but of the Stone-Campbell movement, the Restoration movement. (If time: are we more Stone or more Campbell? Weekly communion and baptism for remission, Campbell; the open table and revival, Stone. It gets confusing, and that is the point.)'))

# ---------- VIII. UNITING ON THE BIBLE: WHAT THEY MEANT ----------

A(C('Uniting on the Bible', 'We put this off. Now: what did they mean by it?'))

A(CARD('Not uniting on opinions<br>' + G('about the Bible.'), 'Not doctrines to agree on, not interpretations: they explicitly rejected that.'))

A('<section class="slide"><div class=eyebrow>The quiz, again</div>'
  '<h2 style="max-width:none;font-size:clamp(60px,13vmin,160px)">No creed but&hellip;</h2>'
  '<div class="litany" style="gap:2vmin;margin-top:3vmin">'
  '<div class="no frag" style="font-size:clamp(34px,7vmin,88px);color:var(--gold)">&hellip;Christ.</div>'
  '<div class="no frag" style="font-size:clamp(34px,7vmin,88px);color:var(--gold)">&hellip;the Bible.</div></div>'
  '<aside class=notes>Two clicks: the room&rsquo;s two answers. &ldquo;No creed but the Bible&rdquo; is Stone&rsquo;s own phrase (1828, 1832); &ldquo;No creed but Christ&rdquo; grows out of Walter Scott&rsquo;s creed and is a slogan by the 1900s. Side path: <i>No creed but&hellip;</i>.</aside></section>')

A(DS(QK('&ldquo;&hellip;has not this been <b>the only bond of union</b> which the &lsquo;Christian Baptist&rsquo; ever advocated? And what is it but a sincere and hearty conviction, expressed or confessed by the lips, <b>that Jesus is the Christ</b>&hellip;&rdquo;',
     'Alexander Campbell, <i>Christian Baptist</i> (1826), &ldquo;To an Independent Baptist,&rdquo; p. 201', 'Christ alone', 'cb3',
     'Campbell defending himself: he is in &ldquo;full communion&rdquo; with the Baptists because the confession is the only bond of union. It goes on: &ldquo;and this belief, exhibited by an overt act of obedience&hellip; qualifies him, if you please, to be saluted as a brother.&rdquo;'), 'lex'))

A(DS(QK('&ldquo;The belief of this one fact, and submission to one institution expressive of it, <b>is all that is required of Heaven to admission into the church</b>.&rdquo;',
     'Alexander Campbell, <i>The Christian System</i>, &ldquo;Foundation of Christian Union,&rdquo; p. 128', 'One fact', 'cs',
     'Next: &ldquo;The one fact is expressed in a single proposition&mdash;that Jesus the Nazarene is the Messiah.&rdquo; The one institution: baptism. The confession, not a system, is the foundation of union.'), 'lex'))

A(DS(QK('&ldquo;&hellip;her only manual was, &lsquo;<b>The Bible</b>.&rsquo; And her all comprehensive creed for the binding of the faithful; &lsquo;<b>Jesus Christ is the Son of God</b>.&rsquo;&rdquo;',
     'Walter Scott, <i>The Evangelist</i> (1832), &ldquo;Primitive Sufferings,&rdquo; p. 32', 'Scott, the year of Lexington', 'ev32',
     'Of the first church. &ldquo;On this faith and this volume she gathered her children thick as the leaves in Autumn.&rdquo; The Bible the manual; Christ the creed. Both of the room&rsquo;s answers, in one sentence. Side path follows.',
     size='clamp(30px,6.4vmin,82px)', width='34ch'), 'crd'))

for _x in R.creed(): A(_x)   # side path: No creed but...

A(DS(QK('&ldquo;&hellip;consisting of all those in every place that profess their faith in Christ and obedience to him in all things <b>according to the Scriptures</b>&hellip;&rdquo;',
     'Thomas Campbell, <i>Declaration and Address</i> (1809), Proposition 1', 'And the Scriptures', 'dna',
     'Proposition 1 opens: &ldquo;That the Church of Christ upon earth is essentially, intentionally, and constitutionally one.&rdquo; Faith in Christ, and then: according to the Scriptures. Eric, a few weeks ago: he wishes Thomas had left that out. Micah: so do I; it would have saved confusion. But it matters what they meant by it.'), 'lex'))

A(QK('&ldquo;Let us, then, my brethren, be no longer Campbellites or Stoneites&hellip; but <b>let us all come to the Bible, and to the Bible alone</b>, as the only book in the world that can give us all the Light we need.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 454', 'Smith, at Lexington', 'wil',
     'The words cut: &ldquo;New Lights or Old Lights, or any other kind of lights.&rdquo; He sat down.', doc='wil32'))

A(QK('&ldquo;&hellip;to state the anomaly as boldly as possible, the movement is at one and the same time <b>Christocentric and bibliocentric</b>.&rdquo;',
     'Dwight E. Stevenson, Disciples Panel of Scholars (1963)', 'Two proposals?', 'enc',
     'As quoted in the <i>Encyclopedia of the Stone-Campbell Movement</i>, &ldquo;Faith.&rdquo; Paul Blowers summarizes him: the two slogans are &ldquo;very different proposals, as different as allegiance to Christ and allegiance to the strict letter of the scriptural text.&rdquo;'))

A(DS(QK('&ldquo;&hellip;inferences and deductions from Scripture premises&hellip; <b>are they not formally binding upon the consciences of Christians farther than they perceive the connection</b>&hellip;&rdquo;',
     'Thomas Campbell, <i>Declaration and Address</i> (1809), Proposition 6', 'Not our readings', 'dna',
     'In full: &ldquo;although inferences and deductions from Scripture premises, when fairly inferred, may be truly called the doctrine of God&rsquo;s holy word, yet are they not formally binding upon the consciences of Christians farther than they perceive the connection, and evidently see that they are so&hellip; Therefore, no such deductions can be made terms of communion.&rdquo; Our readings of Scripture are not the bond.'), 'lex'))

A(DS(QK('&ldquo;&hellip;<b>no deduction or inference from them, however logical or true, forms any part of the Gospel</b> of Jesus Christ.&rdquo;',
     '&ldquo;Raccoon&rdquo; John Smith, at Lexington &middot; ' + WIL + ', p. 453', 'Smith, the same morning', 'wil',
     'Before it: &ldquo;the Gospel is a system of facts, commands, and promises.&rdquo; After: &ldquo;No heaven is promised to those who hold them, and no hell is threatened to those who deny them.&rdquo;'), 'wil32'))

A(CARD('Different proposals,<br>' + G('only if we forget what they meant.'),
  'Micah, in his own voice: he prefers &ldquo;No creed but Christ.&rdquo; Uniting on the Bible was never uniting on opinions about the Bible. Smith, the same morning: &ldquo;no deduction or inference from them, however logical or true, forms any part of the Gospel of Jesus Christ&rdquo; (Williams, p. 453).'))

for _x in R.circle(): A(_x)   # Campbell's circle, January 2, 1832 (two slides)

A(DS(QK('&ldquo;The brethren of Stone did not join Alexander Campbell as their leader, nor did the brethren of Campbell join Barton W. Stone as their leader; but each, <b>having already taken Jesus the Christ as their only Leader</b>, in love and liberty became one body&hellip;&rdquo;',
     WIL + ', p. 456', 'Their only Leader', 'wil',
     'Williams&rsquo;s summary of what the handshake meant (1870). It goes on: &ldquo;not Stoneites, or Campbellites; not Christians, or Disciples, distinctively as such; but Christians, Disciples, saints, brethren, and children of the same Father.&rdquo; Before it: &ldquo;an equal and mutual pledge and resolution to meet on the Bible as on common ground, and to preach the Gospel rather than to propagate opinions.&rdquo;'), 'wil32'))

A(CARD('Scripture, like the table:<br>' + G('shared by all.'),
  'Not a set of doctrines to agree on, but a shared table to come to: a shared basis for conversation and dialogue, and a shared way to meet Christ himself. We know this in our own congregation: we can argue about Scripture all day, hold every interpretation there is, and still it brings us together, and back to Christ. Like the communion table, Scripture is the common property of all: unity in our dialogue, in our diversity. (More on how they read the Bible in the weeks ahead.)'))

# ---------- CLOSE ----------
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A(IDEASUM('All four at once, before the discussion.'))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): What do we still require of each other before we will eat together? What would it take to keep eating together while we disagree? Which division from the list would be hardest for us?</aside>',
         w3b.pick('&#9670; for discussion', 0), flags=re.S).replace('&#9670; for discussion', '&#9670; for discussion &middot; Chapter 8', 1))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Today&rsquo;s sources: Williams&rsquo;s <i>Life of Elder John Smith</i>, Stone&rsquo;s <i>Christian Messenger</i>, the <i>Millennial Harbinger</i>, Scott&rsquo;s <i>Evangelist</i>.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S).replace('<h2 class=url>stone-campbell.micahredding.com</h2>',
          '<h2 class=url style="letter-spacing:.02em"><span style="color:var(--gold)">stone-campbell</span><span style="color:#ede4d3;opacity:.75">.micahredding.com</span></h2>', 1))
A(BLACK)
