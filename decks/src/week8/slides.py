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
SP = _load('spreadmap', 'week8/spreadmap.py')
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
def BGIMG(img, title, cite, note, pos='66%', h=None):
    # the picture behind the words (Micah, 2026-11-21): large, dimmed, its edges feathered into the dark
    src = RC._b64(img)
    return ('<section class="slide" style="padding:0;background:#0e0b09">'
            '<img src="%s" alt="" style="position:absolute;top:-4vh;height:118vh;left:%s;transform:translateX(-50%%);'
            'filter:none;'
            '-webkit-mask-image:radial-gradient(ellipse 50%% 50%% at 50%% 42%%,#000 60%%,transparent 100%%);mask-image:radial-gradient(ellipse 50%% 50%% at 50%% 42%%,#000 60%%,transparent 100%%)">'
            '<div style="position:absolute;inset:0;background:linear-gradient(to right,rgba(14,11,9,.9) 0%%,rgba(14,11,9,.4) 45%%,rgba(14,11,9,0) 70%%)"></div>'
            '<div style="position:absolute;left:6vw;top:50%%;transform:translateY(-50%%);max-width:52vw;text-align:left;text-shadow:0 2px 16px #000">'
            '<div style="font-family:\'IM Fell English\',Georgia,serif;color:var(--bone);font-size:clamp(44px,9vmin,116px);line-height:1.05">%s</div>'
            '<div style="font-family:Spectral,Georgia,serif;color:var(--bone-dim);font-size:clamp(14px,2.2vmin,26px);margin-top:3vmin;max-width:40vw">%s</div></div>'
            '<aside class=notes>%s</aside></section>' % (src, pos, title, cite, note))

def BGCARD(img, eyebrow, html, note, pos='center'):
    # a statement over a darkened full-bleed picture (Micah, 2026-11-22)
    return ('<section class="slide" style="padding:0">'
            '<img src="%s" alt="" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:%s;filter:sepia(.3) brightness(.3)">'
            '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.55) 0%%,rgba(14,11,9,.1) 75%%)"></div>'
            '<div style="position:relative;z-index:1;text-align:center;text-shadow:0 2px 16px #000">'
            '<div class=eyebrow>%s</div><h2 style="max-width:none">%s</h2></div>'
            '<aside class=notes>%s</aside></section>' % (RC._b64(img), pos, eyebrow, html, note))

def WITHBG(slide, img, dim=.3, pos='center'):
    # put a darkened picture behind an existing slide (Micah, 2026-11-22: the inn behind the whole breakfast story)
    i = slide.index('<section'); j = slide.index('>', i)
    tag = slide[i:j]
    tag = tag.replace('class="slide', 'class="slide withbg', 1) if 'class="slide' in tag else tag.replace('class=slide', 'class="slide withbg"', 1)
    layer = ('<img class=bgl src="%s" alt="" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:%s;filter:sepia(.3) brightness(%s);z-index:0">'
             '<div class=bgl style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.6) 0%%,rgba(14,11,9,.15) 75%%)"></div>'
             '<style>.withbg>*:not(.bgl):not(aside){position:relative;z-index:1}.withbg{text-shadow:0 2px 14px #000}</style>') % (RC._b64(img), pos, dim)
    return slide[:i] + tag + slide[j:j + 1] + layer + slide[j + 1:]

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
    ('Every historic division<br>' + G('came to one table.'), 'God, authority, the sacraments: what had divided Christendom since Nicaea was in the room at Hill Street.'),
    ('They united around the Bible,<br>' + G('not their readings of it.'), 'Smith: &ldquo;one in faith, and not in opinion.&rdquo; Stone and Johnson: &ldquo;we do not know, nor are we concerned to know.&rdquo;'),
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
def HIDE(slide): pass   # a hidden slide: kept here, left out of the deck (change HIDE back to A to show it)

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

A('<section class="slide twomv" style="padding:4vmin 4vw 4vmin;justify-content:flex-start;padding-top:9vh"><div class=twobg style="position:absolute;inset:0;display:flex;gap:.5vmin;background:#0e0b09;z-index:0"><div style="flex:1;overflow:hidden"><img src="' + RC._b64('stone-biography-1847.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:sepia(.35) brightness(.5)"></div><div style="flex:1;overflow:hidden"><img src="' + RC._b64('acold-engraving-oval.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 25%;filter:sepia(.2) brightness(.5)"></div></div><div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.55) 0%,rgba(14,11,9,.15) 70%)"></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;width:88vw;margin:0 0 3.5vmin"><div style="text-align:right;font-family:\'IM Fell English\',Georgia,serif;color:var(--gold);font-size:clamp(36px,7vmin,88px);text-shadow:0 2px 14px #000">Stone&rsquo;s Christians</div><div style="text-align:left;font-family:\'IM Fell English\',Georgia,serif;color:var(--gold);font-size:clamp(36px,7vmin,88px);text-shadow:0 2px 14px #000">Campbell&rsquo;s Reformers</div></div><div class=litany style="gap:1.2vmin;width:88vw;max-width:none"><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right"><b style="color:var(--gold)">&ldquo;Christians&rdquo;</b></div><div style="text-align:left"><b style="color:var(--gold)">&ldquo;Disciples&rdquo;</b></div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Unity in freedom</div><div style="text-align:left">Unity in freedom</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Open table</div><div style="text-align:left">Open table</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">No creed</div><div style="text-align:left">No creed</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Priesthood of all</div><div style="text-align:left">Priesthood of all</div></div><div class="no frag" style="display:grid;grid-template-columns:1fr 1fr;gap:4vw;font-size:clamp(32px,6.4vmin,80px);line-height:1.18"><div style="text-align:right">Future</div><div style="text-align:left">Future</div></div></div><style>.twomv>*:not(.twobg):not(aside){position:relative;z-index:1}.twomv .litany>div{text-shadow:0 2px 12px #000,0 0 4px #000}</style><aside class=notes>Six clicks, one row each. What the two shared (Micah, 2026-11-20): unity within freedom and diversity of thought; an open table to Christians of every name (Stone; and Campbell: &ldquo;the only bond of union&rdquo; is the confession that Jesus is the Christ); creeds laid down as tests of fellowship; the priesthood of all, with governance in the people (the <i>Last Will</i>; Brush Run); and a radical future, the kingdom breaking in, calling for religious and social reform (Stone&rsquo;s premillennial hope; the <i>Harbinger</i>). So much in common: seeking unity with all Christians, surely they could find it with each other. So they began to look for a way to embody that unity in practice.</aside></section>')


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

A('<section class="slide twomv" style="padding:3vmin 4vw 6vmin"><div class=twobg style="position:absolute;inset:0;display:flex;gap:.5vmin;background:#0e0b09;z-index:0"><div style="flex:1;overflow:hidden"><img src="' + RC._b64('stone-biography-1847.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:sepia(.35) brightness(.5)"></div><div style="flex:1;overflow:hidden"><img src="' + RC._b64('acold-engraving-oval.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 25%;filter:sepia(.2) brightness(.5)"></div></div><div style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.55) 0%,rgba(14,11,9,.15) 70%)"></div><div class=eyebrow>Points of contention</div><div class=litany style="gap:1.6vmin;text-align:center;align-items:center"><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Trinity</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Atonement</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Clergy</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Communion</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Baptism</b></div><div class="no frag" style="font-size:clamp(34px,7vmin,88px);line-height:1.15"><b style="color:var(--gold)">Future</b></div></div><style>.twomv>*:not(.twobg):not(aside){position:relative;z-index:1}.twomv .litany>div{text-shadow:0 2px 12px #000,0 0 4px #000}</style><aside class=notes>Six clicks, one line each. Atonement: how Christ saves (Stone rejected the substitutionary &ldquo;satisfaction&rdquo; view; Smith at Lexington names &ldquo;the Ground and Nature of the Atonement&rdquo; with the Trinity). Side by side, as we tell it: Trinity, Christ: the Christians kept to Scripture&rsquo;s words, and to the Reformers looked &ldquo;Arian&rdquo;; the Reformers held the Trinitarian faith. Trinity, the Spirit: the Christians, that he works directly, in conversion and revival (the camp meeting, the anxious seat); the Reformers, that he works through the word (believe the gospel facts, confess, be immersed). Clergy: ordained elders and preachers serve the ordinances, or any disciple may, the church appointing. Table: free communion or restricted to the immersed; now and then, or every Lord&rsquo;s day. Baptism: immersion, but not &ldquo;for the remission of sins,&rdquo; or immersion for the remission of sins. Future: Christ comes first, to judge, or the gospel brings the millennium. Williams, p. 450: &ldquo;some of each party still cherished honest doubts respecting the doctrine of the others.&rdquo; Christ and the Spirit, Williams, p. 450: &ldquo;Some Reformers still looked upon the Christians as Arians; and some Christians were adverse to the union, in the belief that the Reformers denied the influence of the Spirit, and attached undue importance to baptism.&rdquo; The Spirit here is his work in conversion (Campbell: the Spirit works through the word), not his place in the Trinity. Baptism: &ldquo;all did not hold in the same sense that baptism was for the remission of sins.&rdquo; Most Christians had come to immerse; Stone: the Reformers &ldquo;preached baptism for the remission of sins to believing penitents.&rdquo; The table: &ldquo;they still differed on the question of free or restricted communion&rdquo;; Stone: the Reformers &ldquo;insisted also upon weekly communion, which we had neglected&rdquo; (<i>Biography</i>). Clergy: Stone, 1830: &ldquo;the church may elect, but not ordain&rdquo;; Campbell: any disciple may break the loaf; the Lexington churches split on exactly this in February 1832. Conversion: Stone&rsquo;s revival culture (Cane Ridge) against Scott&rsquo;s plan of salvation (believe, repent, be baptized, receive). The future: Stone premillennial by 1832&ndash;33; Campbell postmillennial (Chapter 7). These are generalizations: people on both sides held both views on several points.</aside></section>')

# ---------- IV. THE WHOLE HISTORY OF DIVISION ----------

for _x in DV.slides(): A(_x)   # the egg replayed; God, authority and clergy, the sacraments, each answered at Lexington

A(CARD('Every division of eighteen centuries<br>' + G('in one room.'),
  'The Trinity, the clergy, the sacraments: what had divided Christendom since Nicaea. Will it be unity, or division, like every effort before?'))

# ---------- V. THE HANDSHAKE ----------

A(CARD('How could they possibly<br>' + G('come together?'),
  'Every division of eighteen centuries in one room, as wide as any division Christianity had ever known. Before we get to the answer, we have to meet somebody: &ldquo;Raccoon&rdquo; John Smith.'))
A(CARD('<span style="font-size:2.2em;color:var(--gold)">&hellip;</span>',
  'A pause. Before we get to the answer, we have to meet somebody.'))

A(BGIMG('smith-sartain-bg.jpg', '&ldquo;Raccoon&rdquo;<br>John Smith<div style="font-size:.42em;color:var(--gold);margin-top:1.5vmin;letter-spacing:.06em">1784&ndash;1868</div>', 'Frontispiece engraving by John Sartain, in J. A. Williams, <i>Life of Elder John Smith</i> (1870)',
  'Who he was: born 1784 in East Tennessee (&ldquo;a native of the State of Franklin,&rdquo; the short-lived breakaway frontier state, Williams p. 17) to a Regular Baptist family, raised in Stockton&rsquo;s Valley on the Kentucky frontier, &ldquo;never had more than six months of schooling&rdquo; (<i>Encyclopedia</i>). January 1815, near Huntsville, Alabama: his cabin burned and two of his children died; his wife died soon after. Riding home, the Calvinist preacher could not comfort her: &ldquo;If I tell her that our babies are glorified, the thought that possibly they were of the non-elect will only aggravate her woe&rdquo;; his faith in that doctrine &ldquo;yielded up its strength forever&rdquo; (Williams, p. 103). The nickname means backwoodsman: at Crab Orchard in 1815 he introduced himself as from the hills of the Cumberland, where &ldquo;saltpeter caves abound, and raccoons make their homes&rdquo; (p. 115), and people spoke of &ldquo;the man that had been raised among the raccoons&rdquo; (p. 117). Later Philip Fall posted notices in Frankfort that &ldquo;Raccoon John Smith would preach&rdquo;; ever after, &ldquo;some knew me as &lsquo;Raccoon John Smith, of Montgomery&rsquo;&rdquo; (p. 278), a title he &ldquo;disliked but tolerated.&rdquo; 1828, to his wife: &ldquo;I have baptized seven hundred sinners and capsized fifteen hundred Baptists&rdquo; (p. 258). &ldquo;A civil Campbellite&rdquo; (Williams, pp. 478&ndash;479, read on the page scan): on a journey south, a woman serving him breakfast had heard of &ldquo;a strange sort of people up there in Kentucky called Campbellites&rdquo;; she was told they &ldquo;even chased after people, and ran them down,&rdquo; and once ran a poor fellow &ldquo;five miles before they caught him.&rdquo; Smith: &ldquo;That was a very long-winded fellow, ma&rsquo;am.&rdquo; She imagined &ldquo;a sort of wild, fierce, fanatical look.&rdquo; Smith, setting down his knife and fork: &ldquo;look right at me, and you will see one! But don&rsquo;t be afraid&hellip; I am a <i>civil</i> Campbellite, and will not chase <i>you</i> into the water.&rdquo;', h='74vh'))
# Raccoon John Smith, for flavor (Micah, 2026-11-21: "I want all this")
A('<section class="slide" style="padding:0;background:#0e0b09">' + _load('franklin_svg', 'week8/franklin_svg.py').SVG + '<aside class=notes>Where Smith came from. Williams: &ldquo;Elder John Smith was born on the 15th of October, 1784, in Sullivan County, East Tennessee&rdquo; (p. 15); &ldquo;he was a native of the State of Franklin, an unacknowledged, though duly organized commonwealth of the olden time&rdquo; (p. 17). Franklin: the counties west of the mountains that North Carolina ceded to Congress in 1784 organized their own state (Jonesborough, then Greeneville, its capital; John Sevier its governor), petitioned Congress for admission, and never got it; its leaders even sounded out Spain, and North Carolina arrested Sevier (1788); by 1788&ndash;89 it had collapsed back into North Carolina, and the land became part of Tennessee in 1796. The Smiths moved on to Stockton&rsquo;s Valley, on the Kentucky frontier. He &ldquo;never had more than six months of schooling&rdquo; (<i>Encyclopedia</i>). A Regular Baptist preacher from 1808, and a farmer all his life, since the Baptists did not pay their preachers. The shading follows today&rsquo;s counties, an approximation: Franklin&rsquo;s western line was never settled. Map drawn for the class from U.S. Census boundaries (us-atlas).</aside></section>')
A(DS(QK('&ldquo;Smith was urged to preach that night, for every body wished to hear again <b>the man that had been raised among the raccoons</b>.&rdquo;',
     WIL + ', p. 117', 'Raised among the raccoons', 'none',
     'Williams narrating, Crab Orchard, 1815; read on the page scan (the OCR interleaves the lines). He would not preach that night: he &ldquo;rather shrank from the attentions that were now pressed upon him.&rdquo; On the way home, &ldquo;they smiled when told how he looked that day on the stand, as he declared his origin among the raccoons and caves of the rocky frontier.&rdquo; The nickname means backwoodsman. Earlier that day (p. 115), he had introduced himself: &ldquo;I am John Smith, from Stockton&rsquo;s Valley&hellip; Down there, saltpeter caves abound, and raccoons make their homes. On that wild frontier we never had good schools, nor many books; consequently, I stand before you to-day a man without an education.&rdquo;'), 'lex'))
A(CARD('<i style="color:var(--gold);font-size:1.7em">The Fire</i>',
  'January 1815, near Huntsville, Alabama, while Smith was away preaching. The messenger: &ldquo;Your house took fire last night, and every thing is lost. Two of the children were burned to death&rdquo; (Williams, p. 102). His wife Anna died soon after.'))
A(DS(QK('&ldquo;If I tell her that our babies are glorified, <b>the thought that possibly they were of the non-elect will only aggravate her woe</b>.&rdquo;',
     'Smith, riding home to his wife, January 1815 &middot; ' + WIL + ', p. 103', 'The fire', 'wil',
     'The messenger: &ldquo;Your house took fire last night, and every thing is lost. Two of the children were burned to death&rdquo; (p. 102). Williams: &ldquo;his faith in that harsh doctrine of his Church yielded up its strength forever.&rdquo; The man who would say &ldquo;one in faith, and not in opinion&rdquo; lost a doctrine before he lost a creed.'), 'lex'))
A(DS(QK('&ldquo;I know nothing about the man; but, be he saint or devil, <b>he has thrown more light on that epistle, and on the whole Scriptures</b>, than I have received in all the sermons that I have ever heard before.&rdquo;',
     '&ldquo;Raccoon&rdquo; John Smith, on first hearing Alexander Campbell, Flemingsburg, Kentucky, spring 1824 &middot; ' + WIL + ', p. 164', '1824: Smith meets Campbell', 'wil',
     'Read on the page scan. Smith rode twenty miles alone to meet him; his Baptist brethren, prejudiced by Campbell&rsquo;s essays, would not go. In town he asked Elder William Vaughn, who had heard Campbell for eight days: &ldquo;Is he a Calvinist or an Arminian, an Arian or a Trinitarian?&rdquo; Vaughn: &ldquo;I do not know; he has nothing to do with any of these things&rdquo; (p. 162, read on the scan). Campbell preached on the allegory of Hagar and Sarah (Galatians 4), leaning on his cane; Smith sat on the platform at his feet, &ldquo;determined now to find out the theory of religion he held to.&rdquo; Afterward: &ldquo;Is it not hard, brother Billy, to ride twenty miles, as I have done, just to hear a man preach thirty minutes?&rdquo; It had been two and a half hours. &ldquo;Did you find out, brother John, whether he was a Calvinist or an Arminian?&rdquo; Then this (pp. 163&ndash;164). Campbell, on meeting him: &ldquo;I know brother Smith very well, though I have never seen him before.&rdquo;', size='clamp(30px,6.4vmin,82px)'), 'wil32'))
A(CARD('By 1828,<br>' + G('he joins the Reformers.'),
  'Gradually. 1824: Flemingsburg. 1826: he reads Campbell&rsquo;s New Testament translation and begins preaching &ldquo;the Ancient Gospel&rdquo; in Baptist pulpits. July 1827: charges at the North District Association, laid over a year in the hope that &ldquo;the heresy of Campbellism would be forgotten, and Smith would return to the faith of his fathers&rdquo; (Williams, ch. XVII). By 1828 he is leading the Reformation in Montgomery County; the reforming congregations separate from the Baptist associations about 1829&ndash;30.'))
A(CARD('1828, Montgomery County:<br>' + G('thirty baptisms a week.'),
  'Williams: &ldquo;Revivals&hellip; were now of frequent occurrence. In fact, for several months in succession, he immersed about thirty persons every week&rdquo; (p. 212; read on the page scan). Where: his own country, Montgomery County, Kentucky, around Mount Sterling and Grassy Lick, spring 1828. James Mason, an elder at Grassy Lick, April 19, 1828: &ldquo;At our last meeting, thirty-six were immersed and added to our church. On last Lord&rsquo;s Day, at Mount Sterling, thirty-seven were immersed&rdquo; (p. 211). &ldquo;These results did not fail to alarm the orthodox.&rdquo;'))
A(DS(QK('&ldquo;I have <i>baptized</i> seven hundred sinners, and <b><i>capsized</i> fifteen hundred Baptists</b>&hellip;&rdquo;',
     'Smith to his wife, 1828 &middot; ' + WIL + ', p. 258', 'The preacher', 'none',
     'Read on the page scan (pp. 258&ndash;259). The context: he kept no journal, but for a while in 1828 he noted the results of each week; one evening at home, mid-1828, reviewing the past few months, he announced the result to his wife. He went on: &ldquo;so we have made two great mistakes&rdquo;: &ldquo;He had said to her, at the beginning of the year, that the Reformation would not prevail in his lifetime; yet six months only had passed by, and it was already established in the hearts of the people. He had counted up the sacrifices, too, that he would have to make, and had talked of the persecutions that he would have to endure; but now he felt that the struggle was over.&rdquo; &ldquo;Nancy,&rdquo; said he: checked; the OCR runs &ldquo;sinners and&rdquo; together. &ldquo;Capsized&rdquo; is a boat joke beside &ldquo;baptized&rdquo;: he turned Baptists over, out of the Calvinist Baptist creed and into the Reformation. Not rebaptism: they were already immersed, and the Reformers did not rebaptize Baptists. Seven hundred new converts baptized; fifteen hundred Baptists won over, whole churches with them. He went on: &ldquo;so we have made two great mistakes&rdquo;: he had told her at the start of the year that the Reformation would not prevail in his lifetime, and he had braced for persecution, yet within six months &ldquo;it was already established in the hearts of the people&rdquo; (Williams, pp. 258&ndash;259).', size='clamp(40px,8.4vmin,104px)', width='26ch'), 'lex'))
A(BGCARD('krimmel_village_politicians_1819.jpg', 'about 1834', 'On the road to Alabama:<br>' + G('breakfast at a roadside inn.'),
  'Williams, pp. 477&ndash;478: riding through Tennessee one hot summer morning, nearly twenty-five miles already, Smith stopped at an inn on the roadside, not far from Sparta, and called for his breakfast. The landlady was alone that day (the young people of the family had gone to a social gathering), so she served him herself. Learning he was from Montgomery County, Kentucky, she put down her coffee-pot&hellip; Picture: John Lewis Krimmel, <i>The Village Politicians</i> (c. 1819; Crystal Bridges Museum of American Art; Wikimedia Commons, public domain), an American tavern of the time, not Smith&rsquo;s inn.'))
A(WITHBG(CARD('<i style="color:var(--gold);font-size:1.7em">&ldquo;A strange sort of people&hellip;&rdquo;</i>',
  'On a journey south, at breakfast, the lady of the house heard he was from Montgomery County, Kentucky: &ldquo;Travelers tell me that there is a strange sort of people up there in Kentucky called Campbellites&rdquo; (Williams, p. 478).'), 'krimmel_village_politicians_1819.jpg'))
A(WITHBG(DS(QK('&ldquo;One man told me that they would sometimes take people by force, and drag them down into the water; that they even chased after people, and ran them down; that they once took a fancy to a poor fellow, and <b>ran him five miles before they caught him</b>&hellip;&rdquo;',
     'The lady of the house, to Smith at breakfast &middot; ' + WIL + ', p. 478', 'At breakfast', 'none',
     'Read on the page scan. About 1834, on one of his trips to Alabama: riding through Tennessee one hot summer morning, nearly twenty-five miles already, he stopped at a roadside inn not far from Sparta and called for breakfast; the landlady was alone, the young people gone to a social gathering (Williams, pp. 477&ndash;478). Back home, the church at Albany in Stockton&rsquo;s Valley had just been organized. Hearing he was from Montgomery County, Kentucky, she put down her coffee-pot: &ldquo;Travelers tell me that there is a strange sort of people up there in Kentucky called Campbellites.&rdquo; Smith: &ldquo;Yes, madam&hellip; but they don&rsquo;t like that name.&rdquo; She: &ldquo;I&rsquo;d give more to see one of those people than any show.&rdquo; After the five miles, Smith: &ldquo;That was a very long-winded fellow, ma&rsquo;am, to run five miles before the Campbellites caught him.&rdquo; Then he asked how a Campbellite would look. She: &ldquo;I imagine they have a sort of wild, fierce, fanatical look about them.&rdquo; Smith: &ldquo;I think I can manage for you to see one.&rdquo;'), 'lex'), 'krimmel_village_politicians_1819.jpg'))
A(WITHBG(DS(QK('&ldquo;I imagine they have <b>a sort of wild, fierce, fanatical look</b> about them.&rdquo;',
     'The lady of the house &middot; ' + WIL + ', p. 479', 'How would a Campbellite look?', 'none',
     'Read on the page scan. Smith, &ldquo;after breaking his fast a little&rdquo;: &ldquo;How do you think a Campbellite would look?&rdquo; Then her answer. Smith: &ldquo;I think I can manage for you to see one,&rdquo; as he received his second cup from her hands. She: &ldquo;I&rsquo;d give any thing almost, if you would, sir.&rdquo;', size='clamp(36px,7.4vmin,94px)'), 'lex'), 'krimmel_village_politicians_1819.jpg'))
A(WITHBG(DS(QK('&ldquo;I would really like to see one, so much,&rdquo; said she, musingly; &ldquo;<b>I&rsquo;d give more to see one of those people than any show</b>.&rdquo;',
     'The lady of the house &middot; ' + WIL + ', p. 478', 'She would love to see one', 'none',
     'Read on the page scan. She says it twice; later, &ldquo;I don&rsquo;t know what I wouldn&rsquo;t give to see one of them&rdquo;; and after Smith&rsquo;s &ldquo;I think I can manage for you to see one&rdquo;: &ldquo;I&rsquo;d give any thing almost, if you would, sir&rdquo; (pp. 478&ndash;479).', size='clamp(34px,7.2vmin,92px)'), 'lex'), 'krimmel_village_politicians_1819.jpg'))
A(BGIMG('smith-sartain-bg.jpg', '<span style="font-size:.62em;line-height:1.2;display:block">&ldquo;Madam&hellip; look right at me, and you will see one! But don&rsquo;t be afraid&hellip; I am a <i>civil</i> Campbellite, and <span style="color:var(--gold)">will not chase <i>you</i> into the water</span>.&rdquo;<span style="display:block;margin-top:1.2em;color:var(--gold)">&mdash; Raccoon John Smith</span></span>',
  WIL + ', p. 479',
  'Read on the page scan. Williams: &ldquo;said he, laying down the knife and fork which he had plied with more than usual assiduity, and raising his bland, good-natured face upon her&rdquo;; she started, &ldquo;and then blush[ed] with confusion.&rdquo; Afterward he told her what they believed and preached, &ldquo;and corrected all the wicked stories that had been told against them,&rdquo; and invited her to hear him preach at Sparta.', pos='74%'))
A(C('Lexington<div style="font-size:.42em;color:var(--gold);margin-top:2vmin;letter-spacing:.04em">Saturday, December 31, 1831</div>',
  'The four-day meeting at the Christians&rsquo; Hill Street meetinghouse, Saturday, December 31, 1831, to Tuesday, January 3, 1832 (Williams, pp. 450&ndash;455). One speaker from each side: Smith for the Disciples, Stone for the Christians.'))
A('<section class="slide" style="padding:0"><div style="position:absolute;inset:0;display:flex;gap:.5vmin;background:#0e0b09"><div style="flex:1;position:relative;overflow:hidden"><img src="' + RC._b64('smith-sartain-bg.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 20%;filter:brightness(.85)"><div style="position:absolute;left:0;right:0;bottom:7vh;text-align:center;text-shadow:0 2px 16px #000"><div style="font-family:\'IM Fell English\',Georgia,serif;color:var(--bone);font-size:clamp(30px,6vmin,76px);line-height:1.05">&ldquo;Raccoon&rdquo; John Smith</div><div style="font-family:\'IM Fell English\',Georgia,serif;font-style:italic;color:var(--gold);font-size:clamp(18px,3.4vmin,42px);margin-top:1vmin">for the Disciples</div></div></div><div style="flex:1;position:relative;overflow:hidden"><img src="' + RC._b64('stone-1847-bg.jpg') + '" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center 25%;filter:brightness(.85)"><div style="position:absolute;left:0;right:0;bottom:7vh;text-align:center;text-shadow:0 2px 16px #000"><div style="font-family:\'IM Fell English\',Georgia,serif;color:var(--bone);font-size:clamp(30px,6vmin,76px);line-height:1.05">Barton W. Stone</div><div style="font-family:\'IM Fell English\',Georgia,serif;font-style:italic;color:var(--gold);font-size:clamp(18px,3.4vmin,42px);margin-top:1vmin">for the Christians</div></div></div></div><aside class=notes>One speaker for each side. Smith was chosen by the Disciples; Stone by the Christians. Stone: &ldquo;What is your choice, my brother? Will you speak first, or last?&rdquo; Smith: &ldquo;Brother Stone, I have no choice&rdquo; (Williams, p. 452). Portraits: Sartain&rsquo;s engraving of Smith (Williams, 1870); Stone, frontispiece of his <i>Biography</i> (1847).</aside></section>')
A(BGIMG('smith-sartain-bg.jpg', '&ldquo;Raccoon&rdquo;<br>John Smith<div style="font-size:.42em;color:var(--gold);margin-top:1.5vmin;letter-spacing:.04em">rises to speak for the Disciples</div>',
  'Lexington, Saturday, December 31, 1831',
  'Williams: &ldquo;Every eye turned upon him, and every ear leaned to catch the slightest tones of his voice&rdquo; (p. 452). Stone had asked: &ldquo;What is your choice, my brother? Will you speak first, or last?&rdquo; Smith: &ldquo;Brother Stone, I have no choice.&rdquo; A single wrong word, Williams says, &ldquo;might arouse suspicion and prejudice, and blast the hope of union in the very moment when it was budding with so many promises.&rdquo;'))
A(QK('&ldquo;God has but one people on the earth. <b>He has given to them but one Book</b>, and therein exhorts and commands them to be one family.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith rises first', 'wil',
     'The Disciples had chosen Smith to speak for them; the Christians chose Stone. Stone had asked: &ldquo;What is your choice, my brother? Will you speak first, or last?&rdquo; Smith: &ldquo;Brother Stone, I have no choice.&rdquo; Williams: &ldquo;Every eye turned upon him, and every ear leaned to catch the slightest tones of his voice.&rdquo;', doc='wil32'))
A(DS(QK('&ldquo;A union, such as we plead for&mdash;a union of God&rsquo;s people on that one Book&mdash;<b>must, then, be practicable</b>.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith, continuing', 'wil',
     'Read on the page scan. Next: &ldquo;Every Christian desires to stand complete in the whole will of God. The prayer of the Savior, and the whole tenor of his teaching, clearly show that it is God&rsquo;s will that his children should be united. To the Christian, then, such a union must be desirable. But an amalgamation of sects is not such a union as Christ prayed for, and God enjoins.&rdquo;', size='clamp(36px,7.6vmin,96px)'), 'wil32'))
A(DS(QK('&ldquo;The prayer of the Savior, and the whole tenor of his teaching, clearly show that <b>it is God&rsquo;s will that his children should be united</b>. To the Christian, then, such a union must be desirable.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith', 'wil',
     'Read on the page scan. Just before: &ldquo;Every Christian desires to stand complete in the whole will of God.&rdquo; The prayer is John 17: &ldquo;that they all may be one.&rdquo; Next: &ldquo;But an amalgamation of sects is not such a union as Christ prayed for, and God enjoins.&rdquo;', size='clamp(32px,6.8vmin,86px)'), 'wil32'))
A(DS(QK('&ldquo;But an amalgamation of sects is not such a union as Christ prayed for, and God enjoins. To agree to be <i>one</i> upon any system of human invention would be contrary to his will, and could never be a blessing to the Church or the world; therefore <b>the only union practicable or desirable must be based on the Word of God</b>&hellip;&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 452', 'Smith', 'wil',
     'Read on the page scan. The sentence ends: &ldquo;as the only rule of faith and practice.&rdquo; Next: &ldquo;There are certain abstruse or speculative matters&hellip;&rdquo;', size='clamp(28px,5.8vmin,74px)'), 'wil32'))
A(DS(QK('&ldquo;There are certain&hellip; speculative matters&mdash;such as the mode of the <i>Divine Existence</i>, and the <i>Ground and Nature of the Atonement</i>&mdash;that have, for centuries, been themes of discussion among Christians. <b>These questions are as far from being settled now as they were in the beginning of the controversy.</b>&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 453', 'Never settled', 'wil',
     'Read on the page scan. Smith&rsquo;s first move: the very questions that split Christendom (who God is; how Christ saves) have never been settled, and will not be settled at Lexington either. Before it: &ldquo;the only union practicable or desirable must be based on the Word of God, as the only rule of faith and practice&rdquo; (p. 452).', size='clamp(28px,5.8vmin,74px)'), 'wil32'))

A(QK('&ldquo;While there is but one faith, there may be ten thousand opinions; and hence, if Christians are ever to be one, <b>they must be one in faith, and not in opinion</b>.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 453', 'One faith', 'wil',
     'Just before, on the Trinity and the atonement: &ldquo;If I come to the passage, &lsquo;My Father is greater than I,&rsquo; I will quote it, but will not stop to speculate upon the inferiority of the Son.&rdquo; He will speak of such things &ldquo;only in the words which the Lord has given.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))
A(DS(QK('&ldquo;Let us, then, my brethren, be no longer Campbellites or Stoneites, New Lights or Old Lights, or any other kind of lights, but <b>let us all come to the Bible, and to the Bible alone</b>, as the only book in the world that can give us all the Light we need.&rdquo;',
     SMITH + ' &middot; ' + WIL + ', p. 454', 'Smith, closing', 'wil',
     'Read on the page scan. His last words before he sat down; then &ldquo;Stone arose, his heart glowing with love, and every pulse bounding with hope.&rdquo; Just before: &ldquo;For several years past, I have stood pledged to meet the religious world, or any part of it, on the ancient Gospel and order of things, as presented in the words of the Book.&rdquo;', size='clamp(30px,6.2vmin,80px)'), 'wil32'))

A(BGIMG('stone-1847-bg.jpg', 'Barton W. Stone<div style="font-size:.42em;color:var(--gold);margin-top:1.5vmin;letter-spacing:.04em">answers for the Christians</div>',
  'Lexington, Saturday, December 31, 1831',
  'Williams: &ldquo;He sat down, and Stone arose, his heart glowing with love, and every pulse bounding with hope&rdquo; (p. 454). Stone: &ldquo;I will not attempt to introduce any new topic, but will say a few things on the same subjects already presented by my beloved brother.&rdquo; Portrait: frontispiece of his <i>Biography</i> (1847), toned.'))
A(QK('&ldquo;&hellip;the controversies of the Church sufficiently prove that <b>Christians never can be one in their speculations</b> upon those mysterious and sublime subjects&hellip;&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 454', 'Stone answers', 'wil',
     'Stone rises knowing every historic division is in the room: the wrong word could split it down the middle. Stone: &ldquo;I will not attempt to introduce any new topic.&rdquo; Of his own sermons on the Trinity, forced by opposition: &ldquo;I never preached a sermon of that kind that once feasted my heart; I always felt a barrenness of soul afterwards.&rdquo;', doc='wil32'))
HIDE(DS(QK('&ldquo;&hellip;by force of circumstances, I was led to deliver some speculative discourses upon those subjects. But <b>I never preached a sermon of that kind that once feasted my heart</b>; I always felt a barrenness of soul afterwards.&rdquo;',
     STONE + ' &middot; ' + WIL + ', pp. 454&ndash;455', 'Stone', 'wil',
     'Read on the page scan. Before it: &ldquo;After we had given up all creeds and taken the Bible, and the Bible alone, as our rule of faith and practice, we met with so much opposition, that, by force of circumstances&hellip;&rdquo; Stone had been accused of Arianism for years; he knew what these arguments cost.', size='clamp(30px,6.4vmin,82px)'), 'wil32'))
A(DS(QK('&ldquo;I perfectly accord with Brother Smith that <b>those speculations should never be taken into the pulpit</b>; but that when compelled to speak of them at all, we should do so in the words of inspiration.&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 455', 'Stone', 'wil',
     'Read on the page scan. Then, at once: &ldquo;I have not one objection to the ground laid down by him&hellip;&rdquo;', size='clamp(30px,6.4vmin,82px)'), 'wil32'))

A(QK('&ldquo;I have not one objection to the ground laid down by him as the&hellip; basis of union among the people of God; and <b>I am willing to give him, now and here, my hand</b>.&rdquo;',
     STONE + ' &middot; ' + WIL + ', p. 455', 'His hand', 'none',
     'Checked on the page scan (the OCR interleaves two lines here). Williams: &ldquo;He turned as he spoke, and offered to Smith a hand trembling with rapture and brotherly love, and it was grasped by a hand full of the honest pledges of fellowship.&rdquo;',
     size='clamp(32px,6.6vmin,84px)', doc='wil32'))



A(IMG('cane-ridge-window-lexington-handshake.jpg', 'The handshake', 'Stained-glass window, Cane Ridge Meeting House (photograph: therestorationmovement.com)',
  'Over an open Bible on the pulpit; the communion table before them, two plates and two cups. Set it against Marburg: Luther would not take the hand; Stone offered his. Maker and date of the window: unknown (to find). Class use only.', h='70vh'))

A(DS(QK('&ldquo;It was now proposed that <b>all who felt willing to unite on these principles</b>, should express that willingness by giving one another the hand of fellowship; and elders and teachers hastened forward, and joined their hands and hearts in joyful accord.&rdquo;',
     WIL + ', p. 455', 'Everyone ratifies', 'wil',
     'Read on the page scan. They were not delegates; no one there had authority to enact a union for anyone else. So the handshake was offered to the whole room, and the room itself ratified it, hand by hand.', size='clamp(30px,6.4vmin,82px)'), 'wil32'))
A(DS(QK('&ldquo;A song arose, and brethren and sisters, with many tearful greetings, ratified and confirmed the union. <b>On Lord&rsquo;s day, they broke the loaf together</b>&hellip;&rdquo;',
     WIL + ', p. 455', 'The song and the loaf', 'wil',
     'Before: &ldquo;elders and teachers hastened forward, and joined their hands and hearts in joyful accord.&rdquo; After: &ldquo;and in that sweet and solemn communion, again pledged to each other their brotherly love.&rdquo; Sunday, January 1, 1832. Williams is the only source for the communion that day; Smith&rsquo;s own letter (February 1832) confirms they broke the loaf together in the weeks after.'), 'wil32'))
A(CARD('Not agreement of opinion:<br>' + G('agreement of faith.'),
  'Smith: &ldquo;one in faith, and not in opinion.&rdquo; Williams: &ldquo;who taught that opinions were no part of the faith delivered to the saints&rdquo; (p. 455). So this was the proposition before the room: unite on faith, not opinion.', 'The proposition'))
A(QK('&ldquo;It may be asked, is there no difference of opinion among you? We answer, <b>we do not know, nor are we concerned to know</b>.&rdquo;',
     CM + ', January 1832', 'The statement', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, p. 6&ndash;8. Next: &ldquo;We have never asked them what were their opinions, nor have they asked us. If they have opinions different from ours, they are welcome to have them, provided they do not endeavor to impose them on us as articles of faith.&rdquo; And the creed: &ldquo;We have a perfect one&hellip; we mean the New Testament.&rdquo;',
     size='clamp(32px,6.8vmin,86px)', doc='lex'))
A(DS(QK('&ldquo;If they have opinions different from ours, they are welcome to have them, <b>provided they do not endeavor to impose them on us as articles of faith</b>. They say the same of us.&rdquo;',
     CM + ', January 1832', 'The statement, continued', 'cm6',
     '&ldquo;Union of Christians,&rdquo; <i>CM</i> 6, pp. 6&ndash;8. Just before: &ldquo;We have never asked them what were their opinions, nor have they asked us.&rdquo; After: &ldquo;We hear each other preach; and are mutually pleased and edified.&rdquo;', size='clamp(34px,7vmin,88px)'), 'lex'))
A(DS(QK('&ldquo;This union of the Christians and the Disciples was not a surrender of the one party to the other; it was an agreement of such as already recognized and loved each other as brethren, <b>to work and to worship together</b>.&rdquo;',
     WIL + ', p. 455', 'What the union was', 'wil',
     'Williams&rsquo;s summary (1870), read on the page scans. The first cut: &ldquo;who accepted the facts, commands, and promises as set forth in the Bible&rdquo;. The second: &ldquo;but that when compelled to speak on controverted subjects, they would adopt the style and language of the Holy Spirit.&rdquo; Then: &ldquo;each, having already taken Jesus the Christ as their only Leader, in love and liberty became one body.&rdquo; New Union Christian Church, Faywood (dropped from the slides): Micah and Emily were told it was founded in 1834 and named for this union.', size='clamp(30px,6.2vmin,80px)'), 'wil32'))
A(DS(QK('&ldquo;It was a union of those who held&hellip; the necessity of implicit faith&hellip; <b>who conceded the right of private judgment to all; who taught that opinions were no part of the faith delivered to the saints</b>; and who were now pledged that no speculative matters should ever be debated to the disturbance of the peace and harmony of the Church&hellip;&rdquo;',
     WIL + ', pp. 455&ndash;456', 'What the union was', 'wil',
     'Read on the page scan. In full: &ldquo;who held alike the necessity of implicit faith and of unreserved obedience; who accepted the facts, commands, and promises as set forth in the Bible;&rdquo;. The second: &ldquo;but that when compelled to speak on controverted subjects, they would adopt the style and language of the Holy Spirit.&rdquo;', size='clamp(26px,5.2vmin,66px)'), 'wil32'))
A(DS(QK('&ldquo;It was an equal and mutual pledge and resolution <b>to meet on the Bible as on common ground</b>&hellip;&rdquo;',
     WIL + ', p. 456', 'What the union was', 'wil',
     'The sentence ends: &ldquo;and to preach the Gospel rather than to propagate opinions.&rdquo; Next: &ldquo;The brethren of Stone did not join Alexander Campbell as their leader, nor did the brethren of Campbell join Barton W. Stone as their leader; but each, having already taken Jesus the Christ as their only Leader, in love and liberty became one body.&rdquo;', size='clamp(32px,6.8vmin,86px)'), 'wil32'))
A('<section class="slide"><div class=litany style="gap:2vmin;text-align:center;align-items:center"><div class="no frag" style="font-size:clamp(36px,8vmin,100px);line-height:1.2">Handshake by handshake</div><div class="no frag" style="font-size:clamp(36px,8vmin,100px);line-height:1.2">Person by person</div><div class="no frag" style="font-size:clamp(36px,8vmin,100px);line-height:1.2"><span style="color:var(--gold)">Congregation by congregation</span></div></div><aside class=notes>Three clicks. Then the maps. As it spread: 1832, Smith (a Disciple) and Rogers (a Christian) ride together to every church; 1832, Smith defends himself to his own alarmed Reformers; 1834, Jacksonville, Illinois: Stone joins neither church until they unite; 1835, Lexington, at last. Stone at Jacksonville: &ldquo;I refused to unite with either until they united together, and labored to effect it. It was effected&rdquo; (<i>Biography</i>, p. 79). Where it was slow, Stone blamed &ldquo;a few ignorant, headstrong bigots on both sides.&rdquo;</aside></section>')
A(UM.slide())
A(SP.slide())   # the one movement spreading, 1836-1860 (Micah, 2026-11-21)
A(SP.today_slide())   # and today: every congregation, 2020   # the union spreading, in waves (Micah, 2026-11-19)

# ---------- VI. IT TOOK SEVERAL YEARS ----------

A(C('It took years', 'The honest truth: the differences mattered in practice: how to keep the Supper, how to think of their clergy. They worked it out, congregation by congregation. Lexington, February 1832: the two congregations pledged union, broke the loaf together on Feb. 19, and dissolved it on Feb. 25, because many of the Christians held that &ldquo;no person but a preacher has a right to administer the ordinances&rdquo; and were &ldquo;alarmed at the idea of us common folks receiving the name of kings and priests to the Lord&rdquo; (H. C. C., MH 1832, p. 192). Side path: <i>Who keeps the table</i>.'))


for _x in R.table(): A(_x)   # side path: who keeps the table

A(DS(QK('&ldquo;Nor was a union between the two congregations finally and formally effected <b>till in July, 1835</b>&hellip;&rdquo;',
     WIL + ', p. 460', 'Lexington, 1835', 'wil',
     'When Thomas M. Allen, preaching to the Lexington Christians, proposed it again; they &ldquo;waived all prejudice and differences of opinion on the subject of order and clerical privilege&rdquo; and &ldquo;not only consented to the union, but nobly proposed it to the Disciples.&rdquo; Williams is the only source for 1835 found so far.',
     size='clamp(36px,7.6vmin,96px)'), 'lex'))
A(CARD('No magic moment.<br>' + G('It was worked out.'),
  'Visible unity came over years, with patience and forbearance, exploring together. Smith called it &ldquo;the best act of his life&rdquo; (Williams, p. 456); Stone, &ldquo;the noblest act of my life&rdquo; (<i>Biography</i>, p. 79).'))
A(CARD('And it worked:<br>' + G('one movement, one history.'), 'Today we do not speak of a Stone movement and a Campbell movement, but of the Stone-Campbell movement, the Restoration movement. No Stone church, no Campbell church: every church that traces its roots to this story sees itself as heir of both, and our practices come from both sides of that room, inextricably. The churches descended from it have divided over other things; none has renounced the handshake. (If time: are we more Stone or more Campbell? Weekly communion and baptism for remission, Campbell; the open table and revival, Stone. It gets confusing, and that is the point.)'))
A(CARD('Still working it out:<br>' + G('one handshake at a time.'),
  'With all the divisions we have, maybe we are still working it out. And maybe, like the church at Lexington, we can keep working it out: one handshake, one person, one congregation at a time.'))




# ---------- VII. IT WORKED ----------


# ---------- VIII. CHRIST... OR THE BIBLE? (Micah, 2026-11-21) ----------

A(C('Christ&hellip; or the Bible?', 'The quiz, again: no creed but&hellip; Christ, or the Bible? The room gave both answers. So did they.'))

A(CARD('<i style="color:var(--gold);font-size:1.7em">Christ</i>',
  'First: what they said was required of a Christian, and for union. Each of them answers: faith in Jesus as the Christ.'))
A(DS(QK('&ldquo;[The church&rsquo;s] all comprehensive creed for the binding of the faithful; &lsquo;<b>Jesus Christ is the Son of God</b>.&rsquo;&rdquo;',
     'Walter Scott, <i>The Evangelist</i> (1832), &ldquo;Primitive Sufferings,&rdquo; p. 32', 'Walter Scott, on the first church', 'ev32',
     'Of the primitive church: &ldquo;Alike unacquainted with the creeds of the Reformation and the idolatrous manuals of the Apostacy; her only manual was, &lsquo;The Bible.&rsquo; And her all comprehensive creed for the binding of the faithful; &lsquo;Jesus Christ is the Son of God.&rsquo;&rdquo; The other half of the sentence comes back under &ldquo;&hellip;and the Bible.&rdquo;', size='clamp(36px,7.6vmin,96px)', width='28ch'), 'crd'))
A(DS(QK('&ldquo;&hellip;has not this been <b>the only bond of union</b> which the &lsquo;Christian Baptist&rsquo; ever advocated? And what is it but a sincere and hearty conviction, expressed or confessed by the lips, <b>that Jesus is the Christ</b>&hellip;&rdquo;',
     'Alexander Campbell, <i>Christian Baptist</i> (1826), &ldquo;To an Independent Baptist,&rdquo; p. 201', 'Alexander Campbell', 'cb3',
     'Campbell defending himself: he is in &ldquo;full communion&rdquo; with the Baptists because the confession is the only bond of union. It goes on: &ldquo;and this belief, exhibited by an overt act of obedience&hellip; qualifies him, if you please, to be saluted as a brother.&rdquo; Also, <i>The Christian System</i>, &ldquo;Foundation of Christian Union,&rdquo; p. 128: &ldquo;The belief of this one fact, and submission to one institution expressive of it, is all that is required of Heaven to admission into the church.&rdquo;'), 'lex'))
A(QK('&ldquo;[T]he Church of Christ upon earth is essentially, intentionally, and constitutionally one; consisting of all those in every place that <b>profess their faith in Christ</b>&hellip;&rdquo;',
     'Thomas Campbell, <i>Declaration and Address</i> (1809), Proposition 1', 'Thomas Campbell', 'dna',
     'Proposition 1, stopped at Christ; its fuller form comes back in &ldquo;&hellip;and the Bible.&rdquo; Proposition 8 says the same of what is required: &ldquo;their having a due measure of Scriptural self-knowledge&hellip; and of the way of salvation through Jesus Christ, accompanied with a profession of their faith in and obedience to him, in all things, according to his word, is all that is absolutely necessary to qualify them for admission into his Church.&rdquo; Proposition 8 opens with what is not required: &ldquo;That as it is not necessary that persons should have a particular knowledge or distinct apprehension of all Divinely revealed truths in order to entitle them to a place in the Church; neither should they, for this purpose, be required to make a profession more extensive than their knowledge&rdquo;. The cut: &ldquo;by nature and practice&rdquo;. Elsewhere in the Address: &ldquo;the first and foundation truth of our Christianity is union with him, and the very next to it in order, union with each other in him.&rdquo; In full: &ldquo;That as it is not necessary that persons should have a particular knowledge or distinct apprehension of all Divinely revealed truths in order to entitle them to a place in the Church; neither should they, for this purpose, be required to make a profession more extensive than their knowledge; but that, on the contrary, their having a due measure of Scriptural self-knowledge respecting their lost and perishing condition by nature and practice, and of the way of salvation through Jesus Christ, accompanied with a profession of their faith in and obedience to him, in all things, according to his word, is all that is absolutely necessary to qualify them for admission into his Church.&rdquo;'))
A(QK('&ldquo;&hellip;they all stand ultimately upon this one Oracle, &lsquo;<b>Jesus is the Christ</b>.&rsquo; The person who affectionately admits this into the chambers of his soul, and reforms, <b>may be admitted into our churches</b>&hellip;&rdquo;',
     'Walter Scott, <i>The Evangelist</i> (1832), p. 4', 'Walter Scott', 'ev32',
     'Before it: &ldquo;Perhaps it is none of the least of all those things which distinguish the Reformation Churches, that they all stand ultimately upon this one Oracle&rdquo;. After: &ldquo;and if he continues to do honor to his own confession, he may ever remain in our churches&rdquo;. The year of Lexington. Alexander Campbell, <i>The Christian System</i>: &ldquo;The belief of this one fact, and submission to one institution expressive of it, is all that is required of Heaven to admission into the church&rdquo; (<i>The Christian System</i>, p. 128).'))
A(DS(QK('&ldquo;&hellip;this grand fact, that <b>Jesus is the Christ</b>, the Son of the living God&hellip; the belief of this one fact with the heart, <b>is the only prerequisite to Christian baptism and Church membership</b>&hellip;&rdquo;',
     'Stone&rsquo;s <i>Christian Messenger</i> (May 1828), &ldquo;The Spirit of Orthodoxy, No. II,&rdquo; p. 146', 'Barton W. Stone', 'cm2',
     'The lead article of Stone&rsquo;s paper, unsigned (Stone was its editor), stating what the Christians hold: &ldquo;to meet the christian world upon the language which the Holy Spirit teaches, unconnected with any opinions or speculations&rdquo;; &ldquo;all agree that Jesus is the Christ&rdquo;; and on this foundation all Christians &ldquo;will ultimately settle and unite.&rdquo; Williams, of Lexington: each side, &ldquo;having already taken Jesus the Christ as their only Leader, in love and liberty became one body&rdquo; (p. 456). Full sentence on the slide: &ldquo;this grand fact, that Jesus is the Christ, the Son of the living God, and Saviour of men, is the foundation on which the Saviour has built his Church&rdquo;.', size='clamp(30px,6.2vmin,80px)'), 'lex'))
for _x in R.circle(): A(_x)   # side path: Campbell's circle, January 2, 1832 (Christ the centre)

A(CARD('<i style="color:var(--gold);font-size:1.7em">&hellip;and the Bible</i>',
  'Second: what they said of the Bible. The same people, often in the same breath.'))
A(DS(QK('&ldquo;We determined that we would own no name but Christian&hellip; and that we would <b>subscribe to no creed but the Bible</b>&hellip;&rdquo;',
     'Barton W. Stone, <i>Christian Messenger</i> (1828), p. 231', 'Barton W. Stone', 'cm3',
     'In full: &ldquo;We determined that we would own no name but Christian, which we derive from our union with Christ; and that we would subscribe to no creed but the Bible&rdquo;. Of the Springfield Presbytery&rsquo;s choice in 1804.'), 'crd'))
A(DS(QK('&ldquo;[The church&rsquo;s] only manual was, &lsquo;<b>The Bible</b>.&rsquo;&rdquo;',
     'Walter Scott, <i>The Evangelist</i> (1832), &ldquo;Primitive Sufferings,&rdquo; p. 32', 'Walter Scott, on the first church', 'ev32',
     'Of the first church: the essay sets the primitive church, &ldquo;a sweet, innocent virgin attired in Godly simplicity,&rdquo; against the Apostasy and the Reformation, &ldquo;Alike unacquainted with the creeds of the Reformation and the idolatrous manuals of the Apostacy&rdquo;. It is printed right after George W. Elley&rsquo;s letter reporting the Lexington union. &ldquo;On this faith and this volume she gathered her children thick as the leaves in Autumn.&rdquo; The Bible the manual; Christ the creed. Both of the room&rsquo;s answers, in one sentence. Side path follows.',
     size='clamp(40px,9vmin,116px)', width='24ch'), 'crd'))
for _x in R.creed(): A(_x)   # side path: No creed but...

A(QK('&ldquo;<b>We have no authority but the Bible</b>; we wear no name but &lsquo;Christians;&rsquo; and <b>we have no creed but Christ</b>.&rdquo;',
     'T. W. Phillips, chairman, Centennial Convention, Pittsburgh (1909)', 'The Centennial, 1909', 'none',
     'The centennial of the <i>Declaration and Address</i>: the two answers, side by side, a century on. By then the full slogan ran: &ldquo;No creed but Christ, no book but the Bible, no law but love, no name but the divine&rdquo; (<i>Encyclopedia</i>, &ldquo;Slogans&rdquo;; no known author). The earliest uses in our corpus are 1909 and Garrison (1926). Then the scholars ask whether they are one proposal or two.'))
A(CARD('<i style="color:var(--gold);font-size:1.7em">The problem</i>',
  'Two answers, Christ and the Bible: are they the same proposal?'))
A(QK('&ldquo;&hellip;to state the anomaly as boldly as possible, the movement is at one and the same time <b>Christocentric and bibliocentric</b>.&rdquo;',
     'Dwight E. Stevenson, Disciples Panel of Scholars (1963)', 'Dwight Stevenson, 1963', 'enc',
     'As quoted in the <i>Encyclopedia of the Stone-Campbell Movement</i>, &ldquo;Faith.&rdquo; Paul Blowers summarizes him: the two slogans are &ldquo;very different proposals, as different as allegiance to Christ and allegiance to the strict letter of the scriptural text.&rdquo;'))
A(QK('&ldquo;[These are] <b>very different proposals</b>, as different as allegiance to Christ and allegiance to the strict letter of the scriptural text.&rdquo;',
     'Paul M. Blowers, <i>Encyclopedia of the Stone-Campbell Movement</i> (2004), &ldquo;Faith&rdquo;', 'Paul Blowers, 2004', 'enc',
     'Blowers, summarizing the two slogans, &ldquo;No creed but Christ&rdquo; and &ldquo;No book but the Bible&rdquo;, after Stevenson. Micah: I disagree with Blowers here. For these first reformers it was not a call to the strict letter, not a new legalism: not our interpretation of Scripture, but Scripture itself; not our opinions about the Bible, but the Bible.'))

A(CARD('<i style="color:var(--gold);font-size:1.7em">But</i>',
  'Uniting on the Bible was never uniting on opinions about the Bible. They said so, plainly.'))
A(DS(QK('&ldquo;&hellip;inferences and deductions from Scripture premises&hellip; <b>are they not formally binding upon the consciences of Christians farther than they perceive the connection</b>&hellip;&rdquo;',
     'Thomas Campbell, <i>Declaration and Address</i> (1809), Proposition 6', 'Not our readings', 'dna',
     'In full: &ldquo;although inferences and deductions from Scripture premises, when fairly inferred, may be truly called the doctrine of God&rsquo;s holy word, yet are they not formally binding upon the consciences of Christians farther than they perceive the connection, and evidently see that they are so&hellip; Therefore, no such deductions can be made terms of communion.&rdquo; Our readings of Scripture are not the bond.'), 'lex'))
A(DS(QK('&ldquo;If they have opinions different from ours, they are welcome to have them, <b>provided they do not endeavor to impose them on us as articles of faith</b>.&rdquo;',
     'Stone and Johnson, <i>Christian Messenger</i>, January 1832, &ldquo;Union of Christians,&rdquo; pp. 6&ndash;8', 'Stone and Johnson', 'cm6',
     'Of the Reformers, just after Lexington. Before it: &ldquo;We have never asked them what were their opinions, nor have they asked us.&rdquo; After: &ldquo;They say the same of us. We hear each other preach; and are mutually pleased.&rdquo;'), 'lex'))

A('<section class="slide breath"><div class=litany style="gap:3vmin;text-align:center;align-items:center"><div class="no frag" style="font-size:clamp(34px,6.8vmin,88px);line-height:1.2;margin:1.6vmin 0">Sacramentally:<br><span style="color:var(--gold)">formed by its words and its story.</span></div><div class="no frag" style="font-size:clamp(34px,6.8vmin,88px);line-height:1.2;margin:1.6vmin 0">Liturgically:<br><span style="color:var(--gold)">immersed in Scripture&rsquo;s words.</span></div></div><aside class=notes>Two clicks. Sacramentally: They came to the Bible as a text that forms us: not through our interpretation of it, but through the encounter with its words and its story. Like the table: we do not have to agree on what happens there to be fed by it, together.<br><br>Liturgically: In practice they spoke in the Bible&rsquo;s own words, and left their theories unspoken. Smith at Lexington (Williams p. 453, read on the scan): &ldquo;For several years past I have tried to speak on such subjects only in the language of inspiration; for it can offend no one to say about those things just what the Lord himself has said. In this scriptural style of speech all Christians should be agreed.&rdquo; Stone: &ldquo;when compelled to speak of them at all, we should do so in the words of inspiration&rdquo; (p. 455). It is what the liturgical churches have long done: the service itself is an immersion in Scripture, its psalms, readings, canticles and prayers in the Bible&rsquo;s own words. Unity in the words we share, not in our theories about them. (The Book of Common Prayer: read and recite Scripture together, without much speculation upon the words, and let the words do the work they are meant to do.)</aside></section>')
A(CARD('<i style="color:var(--gold);font-size:1.7em">We do this here.</i>',
  'Our congregation: we read it together, sing it, pray it, argue about it, hold every interpretation there is, and still it brings us together, and back to Christ. Wednesday nights: Christians with very different opinions argue these things and leave with different opinions, and Scripture still brings us together: a shared touchstone, not because it irons out our differences, but because it gives us a way to be one in spite of them.'))
A(CARD('Scripture, like the table:<br>' + G('shared by all.'),
  'The summary. As far apart as east from west, they could still recognize Scripture as a shared inheritance, something all of them cherished, and come together around it as around a table. Not a set of doctrines to agree on, but a shared table to come to: a shared basis for conversation and dialogue, and a shared way to meet Christ himself. Like the communion table, Scripture is the common property of all: unity in our dialogue, in our diversity. (More on how they read the Bible in the weeks ahead.)'))

# ---------- CLOSE ----------
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A(IDEASUM('All four at once, before the discussion.'))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): What do we still require of each other before we will eat together? What would it take to keep eating together while we disagree? Which division from the list would be hardest for us?</aside>',
         w3b.pick('&#9670; for discussion', 0), flags=re.S).replace('&#9670; for discussion', '&#9670; for discussion &middot; Chapter 8', 1))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Today&rsquo;s sources: Williams&rsquo;s <i>Life of Elder John Smith</i>, Stone&rsquo;s <i>Christian Messenger</i>, the <i>Millennial Harbinger</i>, Scott&rsquo;s <i>Evangelist</i>.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S).replace('<h2 class=url>stone-campbell.micahredding.com</h2>',
          '<h2 class=url style="letter-spacing:.02em"><span style="color:var(--gold)">stone-campbell</span><span style="color:#ede4d3;opacity:.75">.micahredding.com</span></h2>', 1))
A(BLACK)
