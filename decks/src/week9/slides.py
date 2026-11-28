# -*- coding: utf-8 -*-
# Chapter 9: Tale of a Young Universalist (Aylett Raines, Walter Scott and the Campbells, 1828), then N. T. Wright.
# The story as Micah ordered it (2026-11-24; decks/src/week9/RAINES_STORY.md): the geography;
# (the Universalism backstory is hidden, 2026-11-25); Windham and the conversion (how Scott made the Scriptures come alive); the road with Thomas Campbell;
# the trial at Warren and Thomas Campbell's intervention; Alexander Campbell's proposal; then the question,
# what way of reading makes Scripture come alive?, and the turn to Wright.
# Build:  python3 decks/src/week9map/build.py   ->  decks/chapter9.html
# Quotations: every quote slide carries data-chk=<source key>; python3 decks/src/week9/check_quotes.py.
import base64, importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w8 = _load('w8slides', 'week8/slides.py')
w7 = _load('w7slides', 'week7/slides.py')
w3b, w4 = w8.w3b, w8.w4
C, CARD, G, BLACK, Q, N = w4.C, w4.CARD, w4.G, w4.BLACK, w8.Q, w8.N
PATDEFS, CHRISTENDOM_CSS = w8.PATDEFS, w8.CHRISTENDOM_CSS
QK, LIST, DS, K, BIGQ = w8.QK, w8.LIST, w8.DS, w8.K, w8.BIGQ

def img_path(name):
    for d in ('week9/images', 'week8/images'):
        p = os.path.join(_H, '..', d, name)
        if os.path.exists(p): return p
    return None
def b64(name):
    p = img_path(name)
    mime = 'image/png' if name.endswith('.png') else 'image/jpeg'
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())
def have(name): return img_path(name) is not None

def SVG(name, note):
    svg = open(os.path.join(_H, 'images', name)).read()
    return '<section class="slide" style="padding:0;background:#0e0b09">' + svg + '<aside class=notes>%s</aside></section>' % note

def PORTRAIT(img, name, line, note, eyebrow='', h='74vh'):
    # a portrait at the left, the name and one line at the right
    if not have(img):
        return C(name, note + ' [Portrait to come: %s]' % img, eyebrow)
    e = '<div class=eyebrow style="text-align:left">%s</div>' % eyebrow if eyebrow else ''
    return ('<section class="slide" style="flex-direction:row;gap:5vw;align-items:center;justify-content:center">'
            '<img src="%s" alt="" style="max-height:%s;max-width:38vw;height:auto;border:1px solid rgba(201,162,74,.55);box-shadow:0 6px 24px rgba(0,0,0,.6);filter:sepia(.2)">'
            '<div style="text-align:left;max-width:44vw">%s<h2 style="max-width:none;text-align:left">%s</h2>'
            '<div class=sub style="text-align:left;margin-top:2vmin">%s</div></div>'
            '<aside class=notes>%s</aside></section>' % (b64(img), h, e, name, line, note))

def WITHBG(slide, img, dim=.28, pos='center'):
    return w8.WITHBG(slide, img, dim, pos) if have(img) and os.path.dirname(img_path(img)).endswith('week8/images') else (
        _withbg9(slide, img, dim, pos) if have(img) else slide)
def _withbg9(slide, img, dim, pos):
    i = slide.index('<section'); j = slide.index('>', i); tag = slide[i:j]
    tag = tag.replace('class="slide', 'class="slide withbg', 1) if 'class="slide' in tag else tag.replace('class=slide', 'class="slide withbg"', 1)
    layer = ('<img class=bgl src="%s" alt="" style="position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;object-position:%s;filter:sepia(.3) brightness(%s);z-index:0">'
             '<div class=bgl style="position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse at center,rgba(14,11,9,.6) 0%%,rgba(14,11,9,.15) 75%%)"></div>'
             '<style>.withbg>*:not(.bgl):not(aside){position:relative;z-index:1}.withbg{text-shadow:0 2px 14px #000}</style>') % (b64(img), pos, dim)
    return slide[:i] + tag + slide[j:j + 1] + layer + slide[j + 1:]

def TALK(eyebrow, lines, note, size='clamp(30px,5.6vmin,70px)'):
    # a conversation, one line per click: (speaker, words)
    rows = ''.join('<div class="no frag" style="font-size:%s;line-height:1.3"><span style="color:var(--gold);font-style:italic">%s:</span> %s</div>' % (size, s, w) for s, w in lines)
    return ('<section class="slide"><div class=eyebrow>%s</div>'
            '<div class=litany style="text-align:left;gap:2.2vmin;max-width:84vw">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, rows, note))

def SCENE(img, eyebrow, title, cite, note, h='60vh'):
    # a period print, framed, with a title above it
    if not have(img): return C(title, note, eyebrow)
    return ('<section class="slide"><div class=eyebrow>%s</div><h2 style="max-width:none;margin-bottom:2vmin">%s</h2>'
            '<img src="%s" alt="" style="max-height:%s;max-width:86vw;height:auto;border:1px solid rgba(201,162,74,.55);box-shadow:0 6px 24px rgba(0,0,0,.6);filter:sepia(.35) brightness(.92)">'
            '<div class=cite style="margin-top:1.6vmin">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, title, b64(img), h, cite, note))

HAY = 'A. S. Hayden, <i>Early History of the Disciples in the Western Reserve</i> (1875)'
RAINES = 'Aylett Raines, recalling it in 1868 &middot; ' + HAY
RICH = 'Robert Richardson, <i>Memoirs of Alexander Campbell</i>, vol. 2 (1870)'
MH30 = '<i>Millennial Harbinger</i> (1830), &ldquo;Millennium.&mdash;No. II&rdquo;'
AC = 'Alexander Campbell'
NTW = 'N. T. Wright'
BAX = 'William Baxter, <i>Life of Elder Walter Scott</i> (1874)'
W18 = NTW + ', &ldquo;The Meanings of History,&rdquo; <i>Journal of Analytic Theology</i> 6 (2018)'
LAING = NTW + ', &ldquo;How Can the Bible Be Authoritative?&rdquo; (Laing Lecture, 1989), <i>Vox Evangelica</i> 21 (1991)'

IDEAS = [
    ('Read whole,<br>' + G('the Bible came alive.'), 'Scott read whole chapters &ldquo;connectedly&rdquo;; Raines had used a verse as a proof-text and made &ldquo;a chaos&rdquo; of the covenants.'),
    ('Faith rests on testimony.<br>' + G('Opinion is private property.'), '&ldquo;No testimony, no faith.&rdquo; Where Scripture gives no testimony, there is only opinion, and opinion is no test of fellowship.'),
    ('Kindness, not coercion,<br>' + G('changes minds.'), 'Raines: &ldquo;Had they attempted to brow-beat me I might have been ruined forever. But treating me kindly&hellip; redeemed me.&rdquo;'),
    ('Scripture is a story,<br>' + G('and we are in it.'), 'Wright: earlier acts keep the authority of earlier acts; the church improvises the last act, in character.'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>' % (k, len(IDEAS), h, n))
def IDEASUM(note):
    return ('<section class="slide room"><div class=eyebrow>Today&rsquo;s ideas</div>'
            '<div class="litany ideasum" style="text-align:left;gap:1vmin;margin-top:2vmin">'
            + ''.join('<div class=no style="font-size:clamp(30px,6vmin,74px)"><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (n, h.replace('<br>', ' ')) for n, (h, _) in enumerate(IDEAS, 1))
            + '</div><aside class=notes>%s</aside></section>' % note)

# The escalating questions (Micah, 2026-11-26): each card shows the ones before it, dimmed.
QUESTIONS = [
    'What made Scott&rsquo;s preaching <span style="color:var(--gold)">so compelling?</span>',
    'How could Campbell <span style="color:var(--gold)">embrace a Universalist?</span>',
    'What was Campbell&rsquo;s <span style="color:var(--gold)">Bible method?</span>',
    'What are these people all <span style="color:var(--gold)">doing with the Bible?</span>',
    'How could a whole movement <span style="color:var(--gold)">unite on the Bible?</span>',
    'Why is Wright <span style="color:var(--gold)">popular among us?</span>',
]
def ASK(k, note, eyebrow='The question'):
    # k = 1..6: questions 1..k-1 small and dim, question k large; k = 0: all of them, even
    rows = []
    for n, q in enumerate(QUESTIONS, 1):
        if k and n > k: break
        if k and n < k: st = 'font-size:clamp(20px,3.3vmin,40px);opacity:.42'
        elif k: st = 'font-size:clamp(40px,7.6vmin,96px);margin-top:1.4vmin'
        else: st = 'font-size:clamp(30px,6.2vmin,78px)'
        rows.append('<div class=no style="%s"><span style="color:var(--gold);display:inline-block;width:1.5em">%d.</span>%s</div>' % (st, n, q))
    return ('<section class="slide room"><div class=eyebrow>%s</div>'
            '<div class=litany style="text-align:left;gap:1.2vmin;max-width:90vw">%s</div>'
            '<aside class=notes>%s</aside></section>' % (eyebrow, ''.join(rows), note))

def PAIR(eyebrow, wq, wcite, wkey, cq, ccite, ckey, note, size='clamp(28px,5.4vmin,66px)'):
    # Wright on the left; one click brings Campbell in on the right. Each quotation carries its own data-chk.
    def col(who, q, cite, key, frag):
        return ('<div class="%s" style="flex:1;text-align:left">'
                '<div class=eyebrow style="text-align:left;margin-bottom:1.2vmin">%s</div>'
                '<p class=bigquote style="font-size:%s;line-height:1.25;max-width:none;text-align:left"><span class=q data-chk="%s">%s</span></p>'
                '<div class=cite style="text-align:left">%s</div></div>') % ('frag' if frag else '', who, size, key, q, cite)
    return ('<section class="slide"><div class=eyebrow>%s</div>'
            '<div style="display:flex;gap:4.5vw;align-items:flex-start;max-width:92vw;margin-top:2vmin">%s%s</div>'
            '<aside class=notes>%s</aside></section>') % (eyebrow, col('Wright', wq, wcite, wkey, False), col('Campbell', cq, ccite, ckey, True), note)

S = []
A = S.append
def HIDE(slide): pass

# ---------- OPENING ----------
A(w3b.S[0])   # the class title

A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none;font-size:clamp(48px,10vmin,128px)">&ldquo;We speak where the Bible speaks&hellip;&rdquo;</h2>'
  '<div class="sub frag" style="font-size:clamp(30px,6vmin,76px);color:var(--gold)">&hellip;and we are silent where the Bible is silent.</div>'
  '<aside class=notes>From <code>quizzes.md</code>. Let them finish it; one click shows the rest. Thomas Campbell, Washington, Pa., 1809. Hold the question in the air: <i>where</i> does the Bible speak, to whom, and how do you know? We come back to it at the end.</aside></section>')

A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 9</div>'
  '<h1>Tale of a<br>Young Universalist</h1><div class=table-line></div>'
  '<div class=sub>Aylett Raines, Walter Scott and the Campbells &middot; 1828</div>'
  '<aside class=notes>Chapter 9. Last week: Lexington, where they united on the Bible and not on their readings of it. This morning: how did they read it? A story about a man who came to argue and could not.</aside></section>')

A(PORTRAIT('cane-ridge-window-lexington-handshake.jpg', 'How did they unite<br>' + G('around the Bible?'),
  'Lexington, New Year&rsquo;s Eve, 1831.<br><span style="font-size:.7em;opacity:.75">The handshake: stained glass, Cane Ridge Meeting House</span>',
  'Recap. Stone&rsquo;s Christians and Campbell&rsquo;s Disciples, disagreeing on nearly everything, united on the Bible, not on their readings of it. Smith: &ldquo;While there is but one faith, there may be ten thousand opinions.&rdquo; Stone took his hand. The answer, next slide. Window: photograph from therestorationmovement.com (Chapter 8 images, SOURCES.md); maker and date unknown.', eyebrow='Recap'))
A(CARD('Scripture, like the table:<br>' + G('shared by all.'),
  'Last week&rsquo;s last idea. They came to Scripture as to a table: not a set of agreed readings, but a shared inheritance. This morning: what kind of reading made it live?', 'Last week'))
A(CARD('A young<br>' + G('Universalist.'),
  'This time: a Universalist preacher comes to heckle Walter Scott, and stays. Aylett Raines, the Western Reserve, 1828.', 'This time'))

# ---------- I. UNIVERSALISM (hidden: Micah, 2026-11-25, "we don't need the backstory on universalism") ----------
HIDE(C('A movement of its own', 'Before the story, the man&rsquo;s church. In 1828 Universalism was not a stray opinion. It was a denomination: preachers, conventions, papers, a confession of faith, and growing fast on the Western Reserve.', 'Universalism'))
HIDE(LIST('Universalism in America', 'A denomination, not a stray opinion',
  ['<b>1770</b> &nbsp;John Murray lands; Gloucester, Mass., 1779.',
   '<b>1788</b> &nbsp;Elhanan Winchester, <i>Dialogues on the Universal Restoration</i>.',
   '<b>1803</b> &nbsp;The Winchester Profession: a confession of faith.',
   '<b>1805</b> &nbsp;Hosea Ballou, <i>A Treatise on Atonement</i>.',
   '<b>1821</b> &nbsp;The Northern Ohio Universalian Association, Portage County.'],
  'Five clicks. Sources: Richard Eddy, <i>Universalism in America</i> (1884&ndash;86), vol. 1 p. 137 (Murray&rsquo;s first American sermon, Good Luck, N.J., 30 Sept. 1770), vol. 2 pp. 48&ndash;50 (the Profession), p. 393 (Ohio). By 1836, about 317 preachers and 653 societies (Hayward, <i>Religious Creeds and Statistics</i>, 1836, p. 151; approximate). The 1821 association met at Palmyra, Portage County: eleven churches and sixteen societies.',
  size='clamp(30px,5.6vmin,70px)', gap='1.8vmin'))
if have('murray.jpg') and have('ballou.jpg'):
    HIDE('<section class="slide" style="flex-direction:row;gap:4vw;align-items:flex-end;justify-content:center">'
      + ''.join('<div style="text-align:center"><img src="%s" alt="" style="height:62vh;width:auto;border:1px solid rgba(201,162,74,.55);filter:sepia(.25)"><div class=cite style="margin-top:1.5vmin">%s</div></div>' % (b64(f), t)
                for f, t in (('murray.jpg', 'John Murray (1741&ndash;1815)'), ('winchester-portrait.jpg' if have('winchester-portrait.jpg') else 'murray.jpg', 'Elhanan Winchester (1751&ndash;1797)'), ('ballou.jpg', 'Hosea Ballou (1771&ndash;1852)')))
      + '<aside class=notes>Three founders. Murray, the English preacher who landed in New Jersey; Winchester, the Baptist preacher in Philadelphia whose <i>Dialogues</i> made Raines a Restorationist; Ballou, who by 1817 taught no punishment after death at all.</aside></section>')
HIDE(QK('&ldquo;We believe that there is one God, whose nature is Love, revealed in one Lord Jesus Christ, by one Holy Spirit of Grace, <b>who will finally restore the whole family of mankind to holiness and happiness</b>.&rdquo;',
     'The Winchester Profession (1803), Article II &middot; in Eddy, <i>Universalism in America</i>, vol. 2, p. 49', 'Their confession', 'eddy2',
     'Adopted at Winchester, N.H., by the General Association of Universalists of the New England States. Its plan of union, on the next page, has a line Campbell could have written: &ldquo;where the brethren cannot see alike, they may agree to differ&rdquo; (p. 50).'))
HIDE(SCENE('winchester-dialogues-title.jpg', 'The book that converted Raines', 'Winchester&rsquo;s <i>Dialogues</i>', 'Elhanan Winchester, <i>The Universal Restoration, Exhibited in Four Dialogues</i>, 2nd ed. (Philadelphia, 1792)', 'First published in London, 1788. Dialogues between a Minister and a Friend who raises the objections. Raines read it teaching school near Fredonia, Indiana; it &ldquo;completed the work&rdquo; (Hayden p. 151).', h='64vh'))
HIDE(QK('&ldquo;Christ is <b>the great attracting loadstone</b>, that shall finally draw all things to him.&rdquo;',
     'Elhanan Winchester, <i>Dialogues on the Universal Restoration</i> (1831 ed.)', 'The book that converted Raines', 'winc31',
     'The book Raines read in Indiana: it &ldquo;completed the work&rdquo; (Hayden p. 151). Winchester wrote it as dialogues between a Minister and a Friend who objects. His Minister, on his own manner: &ldquo;I have always made it a rule never to press the belief of my sentiments upon my friends&rdquo; (pp. 53&ndash;54). Keep that in mind for Warren.', size='clamp(40px,8.6vmin,110px)', width='26ch'))
HIDE(LIST('Two kinds of Universalist', 'After death, then what?',
  ['<b>Restorationists</b> (Winchester; Raines): real punishment after death, and then all restored.',
   '<b>&ldquo;Ultra&rdquo; Universalists</b> (Ballou, from 1817): no punishment after death. Opponents called it &ldquo;death and glory.&rdquo;'],
  'Two clicks. The quarrel split the movement: in 1831 the Restorationists formed their own Massachusetts association at Mendon (Paul Dean, Adin Ballou and others), resolving that &ldquo;No-Future accountability&rdquo; was &ldquo;subversive of the best interests of society&rdquo; (Eddy II, 331). Raines kept the distinction all his life: &ldquo;I make a distinction between Restorationism and Universalism&rdquo; (Hayden p. 170).',
  size='clamp(32px,6.2vmin,78px)', gap='3.4vmin'))
HIDE(QK('&ldquo;&hellip;your whole number, seven years ago, who believed in the universal love of God, did not exceed twenty; and at this time, on the same ground, <b>your numbers are more than fifteen hundred</b>.&rdquo;',
     'Timothy Bigelow, to the Northern Ohio Universalian Association, 1821 &middot; in Whittemore, <i>Modern History of Universalism</i> (1830), p. 428', 'On the Western Reserve', 'whit',
     'New Englanders carried it west: Bigelow came from Winchester, N.H., in 1814, because his former neighbors wanted &ldquo;a Universalist Minister to break up the ground&rdquo; (Eddy II, 126). At this 1821 meeting the association ordained Ebenezer Williams of Ravenna &ldquo;minister at large.&rdquo; Remember the name. Hayden, of 1828: &ldquo;Restorationists, who were numerous&rdquo; (p. 130).'))
HIDE(QK('&ldquo;One grand objection that is very generally made against the doctrine of the Restoration, is, that <b>it tends to licentiousness</b>.&rdquo;',
     'The objector in Winchester&rsquo;s <i>Dialogues</i> (1831 ed.), p. 147', 'Why the orthodox shunned them', 'winc31',
     'The charge everyone knew: no hell, no restraint, no social order (<i>Encyclopedia</i>, &ldquo;Universalism&rdquo;). For a Baptist association to receive a Universalist preacher was unheard of.'))

# ---------- II. RAINES, AND WHERE ----------
A(PORTRAIT('aylett-raines.jpg', 'Aylett Raines', 'Born in Virginia, 1797 or 1798. Five years a Universalist preacher.',
  'Restorationist: a Universalist who held there is punishment after death, and then all are restored (Winchester&rsquo;s <i>Dialogues</i>, the book that converted him). Hayden: born near Fredericksburg, Spotsylvania County (p. 150, &ldquo;1797&rdquo;; his gravestone, as reported online, 22 Jan. 1798: to check). Christened at four in the Episcopal church, &ldquo;amidst many tears,&rdquo; tears &ldquo;of fear and apprehension&rdquo; (Hayden&rsquo;s words). Skeptical in his teens, after contradictory preaching and Paine&rsquo;s <i>Age of Reason</i>. Teaching school near Fredonia, Indiana, his employers were Universalists; he lost the arguments, and Winchester &ldquo;completed the work.&rdquo; Died at Eminence, Kentucky, 1881 (to check); fifty years a preacher of the gospel in Ohio and Kentucky.', 'Our man', h='56vh'))
A(SVG('map-road.svg', 'His road: Virginia; at fourteen, Jefferson County, Kentucky; teaching near Fredonia, Indiana, where he became a Universalist; then two years preaching &ldquo;at large,&rdquo; which brought him to the Western Reserve in 1828. Map drawn for the class from U.S. Census boundaries; the Reserve is shaded by today&rsquo;s counties.'))
A(QK('&ldquo;I got religion. <b>The sky appeared to be bluer, the leaves looked greener, and the birds sang more sweetly than ever before.</b>&rdquo;',
     RAINES + ', p. 151', 'Raines, on becoming a Universalist', 'hay',
     'He goes on: &ldquo;I underwent a great moral change. There was much of the love of God in it. Shrouded as I was in error, yet there were apertures through which the love of God passed into my heart, and made me inexpressibly happy.&rdquo; Then: &ldquo;I now commenced the study of the Scriptures in good earnest, and after two years commenced preaching.&rdquo; He preached Restorationism &ldquo;five years.&rdquo; A real conversion, in his own telling, to a faith he would later leave.'))
A(QK('&ldquo;In these, one sectarianism was arrayed against another; and those that came plunging and crashing against mine <b>seemed so very frail, and made so feeble a defense, as rather to confirm me in my errors</b>.&rdquo;',
     RAINES + ', p. 151', 'His debates', 'hay',
     'Five years a Universalist preacher, two of them traveling &ldquo;at large&rdquo;: &ldquo;This, of course, provoked great opposition, and I had a number of debates.&rdquo; Argument only confirmed him. Hold that against what Scott does.'))
A(SVG('map-reserve.svg', 'The Western Reserve: Connecticut&rsquo;s strip of northeast Ohio, kept when it ceded its western claims (1786), sold in 1795, surveyed in 1796, and settled by New Englanders, who brought Universalism with them. Everything in this story happens within about thirty miles: Windham, Ravenna, Shalersville, Sandy Lake, Austintown, Warren. New Lisbon, where Walter Scott first preached the &ldquo;ancient gospel&rdquo; (November 1827), lies south of the Reserve; Bethany, the Campbells&rsquo; home, seventy miles south. The Mahoning Baptist Association had made Scott its evangelist in 1827; by August 1828 nearly a thousand had been added to its churches (Richardson II, p. 244).'))
A(QK('&ldquo;Misrepresentations&hellip; <b>were as numerous as blackbirds in August</b>&hellip;&rdquo;',
     RAINES + ', p. 152', 'The Reserve in 1828', 'hay',
     'In full: &ldquo;Hundreds were being baptized. Much interest had been awakened in behalf of the gospel, and bitter was the opposition which had been enlisted against it. Misrepresentations &mdash; not to use a harsher term &mdash; were as numerous as blackbirds in August, and these too, very often by those who professed to be &lsquo;embassadors for Christ&rsquo;&rdquo;. The rumor about Scott&rsquo;s preaching: &ldquo;Just say you believe, and let a preacher dip you&rdquo;.', size='clamp(40px,8.6vmin,110px)', width='26ch'))

# ---------- III. WINDHAM ----------
A(PORTRAIT('walter-scott.jpg', 'Walter Scott', 'The evangelist of the Mahoning Association, 1827&ndash;30.',
  'Scott (1796&ndash;1861): Scottish-born, a schoolmaster in Pittsburgh, the Association&rsquo;s evangelist from August 1827. His plan of the gospel in &ldquo;six points&rdquo; (later counted on five fingers): faith, repentance, baptism, remission of sins, the gift of the Holy Spirit, eternal life. He was known to call for objections at the end of a sermon.', 'Windham, 1828'))
A(QK('&ldquo;&hellip;I had been told that he was a very bold man, and at the close of his discourses he challenged objectors to make known their objections. Here, thought I, will be a good opportunity for me! and hence <b>I let a number of my brethren know that I intended to oppose him</b>.&rdquo;',
     RAINES + ', p. 152', 'He came to argue', 'hay',
     'At Samuel Robbins&rsquo;s house, in the town of Windham, at night. Richardson (II, p. 220): Raines &ldquo;did not believe in water baptism, but in the baptism of fire and the Holy Ghost,&rdquo; and &ldquo;expected to have a discussion with him.&rdquo;'))
A(QK('&ldquo;&hellip;when he called for objections I was confounded. <b>I could see the heads of my brethren moving to the right and left, in the crowd, expecting to see me rise to my feet. But they didn&rsquo;t see me rise!</b>&rdquo;',
     RAINES + ', p. 152', 'The first night', 'hay',
     'Scott read 1 Corinthians 1 and &ldquo;preached it through, not forgetting to state and defend what he styled the six points of the gospel. I was greatly surprised.&rdquo; Why he kept his seat: &ldquo;I felt certain that if I opposed Bro. Scott I would expose myself. His discourse appeared to me, at every point, invulnerable.&rdquo; Richardson: he was even asked to close the meeting in prayer, and slipped in his favorite petition, for &ldquo;a Pentecostean season&rdquo; and the baptism &ldquo;with fire&rdquo; (II, p. 220).'))
A(QK('&ldquo;<b>I felt certain that if I opposed Bro. Scott I would expose myself.</b> His discourse appeared to me, at every point, invulnerable.&rdquo;',
     RAINES + ', pp. 152&ndash;153', 'Why he kept his seat', 'hay',
     'Scott had not argued with him. He read a chapter and preached it through.'))
A(QK('&ldquo;&hellip;when called upon to close the meeting, made an excellent prayer, desiring that all might have a spirit of obedience, etc., but <b>taking care to introduce his favorite petition that they might have a Pentecostean season and be baptized with the Holy Ghost and with fire</b>.&rdquo;',
     RICH + ', p. 220', 'Asked to close in prayer', 'rich2',
     'Richardson&rsquo;s telling, not Raines&rsquo;s own words. The heckler, asked to pray, got his objection in anyway: the Universalists held to the baptism of fire and the Spirit, not of water. Next day he went back, &ldquo;hoping that he would now be more successful in detecting errors&rdquo; (p. 220).'))
A(TALK('Outside, in the yard', [
    ('His brethren', '&ldquo;Bro. Raines, what do you think of the discourse?&rdquo;'),
    ('Raines', '&ldquo;I can do nothing against the gospel as preached by Bro. Scott; unless I should live to disgrace it; which may our gracious Lord forbid!&rdquo;')],
  'Two clicks. Raines, 1868, Hayden p. 153. He adds: &ldquo;Hence I have no sympathy with those who say they can not understand the preachers of the reformation. I understood the first I ever heard a great deal better than I desired.&rdquo; (That line next.)'))
A(QK('&ldquo;I understood the first I ever heard <b>a great deal better than I desired</b>.&rdquo;',
     RAINES + ', p. 153', 'Raines', 'hay', 'The laugh line. Then he went back the next night.', size='clamp(44px,9.6vmin,124px)', width='22ch'))
A(LIST('Four nights', 'He kept coming back',
  ['<b>1 Corinthians 1:</b> the points of the gospel.',
   '<b>1 Corinthians 15:</b> the resurrection.',
   '<b>The two covenants:</b> the old and the new.',
   '<b>Hebrews 11:</b> the story of faith.'],
  'Four clicks. Each is a whole chapter or a whole sweep of Scripture, not a verse. Richardson: Scott &ldquo;was accustomed to take the Scriptures connectedly&rdquo; (II, p. 221).', size='clamp(36px,7vmin,88px)', gap='2.4vmin'))
A(CARD('&ldquo;As in Adam all die, even so in Christ<br>' + G('shall all be made alive.') + '&rdquo;',
  '1 Corinthians 15:22, Raines&rsquo;s own proof-text. Raines: &ldquo;I deemed a passage of cardinal importance, and the whole chapter very good in its place; but as I did not understand it, of course I saw none of its beauties, and was superlatively ignorant of the meaning of the scrap just referred to, which was one of the proof-texts by which I attempted to prove the ultimate holiness and happiness of all men&rdquo; (Hayden p. 153). Richardson: Universalist preachers had little use for the chapter &ldquo;with the exception of a single sentence in it&rdquo; (II, p. 221).', 'His proof-text'))
A(QK('&ldquo;<b>Germs of truth, and beauties and glories sprang from the bosom of that chapter</b> under the handling of Bro Scott, of which before I had scarcely any conception.&rdquo;',
     RAINES + ', p. 153', 'The second night: the resurrection', 'hay',
     'The same chapter he had quoted for years, read whole. Richardson: under Scott, the chapter &ldquo;soon presented itself to Mr. Raines as a thing of life, and made to him a revelation of such lofty trains of thought and unspeakable glories that his heart was touched&rdquo; (II, p. 221).'))
A(QK('&ldquo;&hellip;although I had been a preacher five years, I certainly did not know the difference between the old covenant and the new. I obtained from them a sort of hotch-potch; or rather <b>I made of them a chaos, and preached the darkness that was on the face of the deep!</b>&rdquo;',
     RAINES + ', p. 153', 'The third night: the two covenants', 'hay',
     'Genesis 1:2, turned on himself. The old covenant and the new as two acts of one story, told in order. Keep this line: it comes back with Wright.'))
A(QK('&ldquo;<b>Here I virtually surrendered</b> &mdash; not that I was convinced that all men would not be finally saved.&rdquo;',
     RAINES + ', p. 154', 'The fourth night: Hebrews 11', 'hay',
     'Scott &ldquo;still bore himself aloft in all the grandeur of the gospel, and in the captivating intelligence of the truth as it is in Jesus.&rdquo; Note what did not happen: Scott did not argue him out of his Universalism. Next slide.'))
A(QK('&ldquo;Bro. Scott said nothing on this subject, only that <b>it was a philosophy, as was Calvinism, Arminianism, etc., and no part of Christianity</b>.&rdquo;',
     RAINES + ', p. 154', 'What Scott said about his Universalism', 'hay',
     'Raines goes on: &ldquo;He convinced me that I ought to lay my philosophy aside, and preach the gospel as the apostles preached&hellip; This was, so far, a capital conquest, for it terminated in due time in the conviction, in my mind, that Restorationism itself&hellip; is founded in error.&rdquo; Scott set the opinion to one side and preached the story.'))
A(QK('&ldquo;<b>He convinced me that I ought to lay my philosophy aside, and preach the gospel as the apostles preached</b>, making their discourses a model to be accurately copied by me in all my ministrations.&rdquo;',
     RAINES + ', p. 154', 'Lay it aside', 'hay',
     'Then: &ldquo;This was, so far, a capital conquest, for it terminated in due time in the conviction, in my mind, that Restorationism itself, as much as I had formerly idolized it, is founded in error.&rdquo; Not argued out of the opinion: asked to set it aside, and the opinion faded on its own.'))
A(QK('&ldquo;<b>I resolved that I would preach as Bro. Scott had done</b>, and as I believed the apostles did, and that <b>at the close of each discourse I would call for objections</b>.&rdquo;',
     RAINES + ', p. 154', 'The heckler invites hecklers', 'hay',
     'He had his own preaching tour to finish. &ldquo;And I told my old brethren that I threw myself on their mercy; in other words, that if they believed me to be going astray, in mercy to set me right. This attempt was often made within this tour, but it only served to convince me more satisfactorily that I was right.&rdquo; Richardson: their arguments &ldquo;were so feeble that he became only the more convinced&rdquo; (II, p. 221).'))
A(QK('&ldquo;My friends, I find myself in a strait; I am shut up in a dilemma; and <b>I can see no way out, with the Word of God in my hand, but through the obedience of faith in baptism.</b> If any of you can see any other, I implore you in the name of my Master to show it to me.&rdquo;',
     'Raines at Austintown, April (1828) &middot; as Hayden reports it, p. 131', 'He tells his own people', 'hay',
     'He kept his old appointments, and told them so: &ldquo;I threw myself on their mercy; in other words, that if they believed me to be going astray, in mercy to set me right&rdquo; (p. 154). At Austintown, word had gone round that he would preach his renunciation of Universalism; the house was full. Hayden: the Universalists &ldquo;jerked up their chairs, started over the benches, and hurried to their homes.&rdquo; (Hayden gives &ldquo;April,&rdquo; no year; 1828 by the order of events.)'))
A(SCENE('bg-ravenna-1846.jpg', 'Ebenezer Williams&rsquo;s town', 'Ravenna', 'View in Ravenna &middot; Henry Howe, <i>Historical Collections of Ohio</i> (1847)', 'Howe&rsquo;s view of Ravenna in the 1840s; by the image researcher&rsquo;s reading of Howe&rsquo;s text, the church shown is the Universalist church (to confirm). Williams: born at Warwick, Mass., 1793; settled in Ravenna in 1815; ordained &ldquo;minister at large&rdquo; by the Universalian Association in 1821; preaching at Shalersville a quarter of his time &ldquo;at one hundred dollars.&rdquo; In May 1828 he preached there against baptism, from Acts 2, and rode home unhappy: &ldquo;My text&hellip; were constantly occupying my mind&rdquo; (Hayden pp. 155&ndash;156). Then Raines appeared at his door.'))
A(WITHBG(QK('&ldquo;&hellip;<b>taking hold of each other&rsquo;s hands, we walked into the water. I baptized him; he in turn baptized me.</b> I think they were all Universalists who witnessed the scene. Some cried, some scolded.&rdquo;',
     'Ebenezer Williams, Universalist preacher of Ravenna &middot; in Hayden, p. 157', 'Sandy Lake, May 1828', 'hay',
     'Williams, the minister ordained by the Universalian Association in 1821, had just preached against baptism at Shalersville and could not sleep. Then: &ldquo;a child came and informed me that Bro. Raines was at the house&hellip; Bro. Raines said he had been hearing Walter Scott; that he had got into trouble, and wanted me to help him out&rdquo; (p. 156). Sandy Lake: &ldquo;a beautiful pond in the corners of Brimfield and Rootstown.&rdquo; It cost Williams his salary: &ldquo;Thus I turned my back on the four hundred a year.&rdquo; Raines: &ldquo;within five weeks I immersed fifty persons, three of them, counting Bro. Williams, talented [Universalist] preachers&rdquo; (p. 154).'), 'bg-baptism.jpg', .26))

A(ASK(1, 'The end of the Windham story. Hold the question. The answer comes at the end: he let the story do the work. Each new question widens the circle: one preacher, one leader, one method, a whole people, a movement, and us.'))
# ---------- IV. THOMAS CAMPBELL ----------
A(PORTRAIT('tcampbell-oval.jpg', 'Thomas Campbell', 'Sixty-five, a Calvinist all his life.',
  'The author of the <i>Declaration and Address</i> (1809), now on the Western Reserve helping the work. Hayden: &ldquo;probably no man within the reformation who possessed such authority of personal influence; of noble mien and manly form; grave and serene of countenance&rdquo; (p. 149).', 'On the road, summer 1828'))
A(QK('&ldquo;He interested himself in my favor, and had me travel and preach with him several months&hellip; <b>By day and by night, publicly and from house to house, he was my teacher.</b>&rdquo;',
     RAINES + ', pp. 149&ndash;150', 'Raines, on Thomas Campbell', 'hay',
     'Before: &ldquo;Not long after this period I made the acquaintance of Bro. Thomas Campbell.&rdquo; &ldquo;This I view as a merciful interposition of my Heavenly Father.&rdquo;'))
A(QK('&ldquo;Often have I seen him, when he had no reason to believe that any eye saw him but that eye before which all things are naked and open, in his closet, <b>prostrate on his face, pouring out his soul in prayer to God</b>.&rdquo;',
     RAINES + ', p. 150', 'What Raines saw', 'hay',
     '&ldquo;Not only by word, but by example, he deeply impressed my warm and susceptible heart. He was, emphatically, a godly man.&rdquo;'))
A(CARD('A Calvinist and a Universalist,<br>' + G('on the road together.'),
  'An old Calvinist and a young Universalist, travelling and preaching for months. They disagreed about the end of all things, and Thomas never set out to argue him out of it. Thomas, in Raines&rsquo;s memory: &ldquo;we have mutually unbosomed ourselves to each other.&rdquo;'))

# ---------- V. WARREN ----------
A(SCENE('bg-warren-1846.jpg', 'The trial', 'Warren, August 1828', 'Public Square, Warren &middot; Henry Howe, <i>Historical Collections of Ohio</i> (1847)', 'The Mahoning Association met at Warren, the seat of Trumbull County, in the last week of August 1828 (exact days to check). Hayden was there &ldquo;from first to last&rdquo; (p. 161). A triumphant meeting: Methodists, Baptists, Universalists, now one body: &ldquo;a grand demonstration of the possibility of the union of Christians on original Bible ground&rdquo; (p. 162). And a worry. Engraving from Howe&rsquo;s drawings of the 1840s, the nearest view we have to the town of 1828.'))
# Stacy and Person (Eddy II, 7-8): hidden until Micah places it (2026-11-25). Candidates: before 'The worry' (here), at Sandy Lake, or before Alexander's proposal.
HIDE(QK('&ldquo;He had, therefore, offered to receive it by the hands of both Baptist and Methodist, but <b>neither would baptize him unless he would renounce his faith in Universal Salvation.</b>&rdquo;',
     'Nathaniel Stacy, on Cornelius G. Person, New York, 1817 &middot; in Eddy, <i>Universalism in America</i>, vol. 2, p. 7', 'Elsewhere, a Universalist asks to be immersed', 'eddy2',
     'Person, a Universalist preacher in Greenfield, N.Y., came to believe he should be immersed; he &ldquo;considered all who named the name of Christ as Christians.&rdquo; Refused by both, he asked Stacy, a fellow Universalist, who came the next February: &ldquo;we had a hole cut in the ice, and I baptized him&rdquo; (Eddy II, 8). The contrast with Warren: the Baptists and Methodists asked him to give up the opinion first; the Mahoning Association, itself still a Baptist association in 1828, received Raines with his opinion kept as private property.'))
A(QK('&ldquo;It was feared that they were, after all, <b>merely baptized Universalists</b>. If this was all, it was nothing.&rdquo;',
     HAY + ', p. 158', 'The worry', 'hay',
     'Hayden goes on: &ldquo;Baptized Universalism is Universalism still; not the gospel.&rdquo; There were &ldquo;out-of-door discussions touching the prudence of such a loose proceeding&rdquo; (p. 163). Richardson: some &ldquo;doubted whether under such circumstances Mr. Raines could be received&rdquo; (II, p. 244).'))
A(QK('&ldquo;I went to that association expecting trouble&hellip; <b>But I resolved to breast the storm.</b>&rdquo;',
     RAINES + ', p. 167', 'Raines', 'hay',
     'In full: &ldquo;for, although I did not preach my [Universalist] opinions, yet I sometimes told such persons as approached me becomingly, that it was still my opinion that all men would, ultimately, in some distant period of eternity, be saved. Out of this the trouble was to grow.&rdquo;', size='clamp(40px,8.6vmin,110px)', width='26ch'))
A(QK('&ldquo;Him that is weak in the faith receive ye, <b>but without regard to differences of opinion</b>.&rdquo;',
     'Romans 14:1, in Campbell&rsquo;s translation &middot; Alexander Campbell&rsquo;s text at Warren, Friday', 'Friday: the opening sermon', 'hay',
     'Raines heard Alexander Campbell that day for the first time. &ldquo;Bro. Campbell dilated lucidly, showing the difference between faith and opinion&hellip; I felt very much strengthened and comforted, knowing, if my case came up in the association, I would have at least Bro. Campbell on my side&rdquo; (Hayden p. 167). Richardson: &ldquo;As Mr. Campbell was aware of this state of feeling, he took as the subject of his introductory discourse the fourteenth chapter of Romans&rdquo; (II, p. 244). The sermon&rsquo;s substance comes back in a moment.', size='clamp(40px,8.6vmin,110px)', width='26ch'))
A(TALK('Saturday morning, in the street', [
    ('Dr. Wright', '&ldquo;I understand that you sometimes tell people that you still believe that all men will finally become holy and happy.&rdquo;'),
    ('Raines', '&ldquo;I do, sir.&rdquo;'),
    ('Dr. Wright', '&ldquo;What then will you do with this passage: <i>These shall go away into everlasting punishment</i>&hellip;?&rdquo;'),
    ('Raines', '&ldquo;I will not do any thing with it. If I argue with you in defense of my opinions I shall make myself a factionist&hellip; and if you get up an argument with me, be careful, you will make yourself a factionist.&rdquo;')],
  'Four clicks. Raines, 1868, Hayden pp. 167&ndash;168. Matthew 25:46. Raines will not trade proof-texts: to press an opinion is to make a faction. The doctor&rsquo;s name was Wright. Remember it.', size='clamp(26px,4.8vmin,60px)'))
A(TALK('Saturday morning, in the street', [
    ('Dr. Wright', '&ldquo;Well, sir, I&rsquo;ll see whether this association will fellowship men of your views.&rdquo;'),
    ('Raines', '&ldquo;I will show you that I will have Thomas Campbell, A. Campbell, Walter Scott, Bentley, and a number of others on my side.&rdquo;'),
    ('Dr. Wright', '&ldquo;It is impossible.&rdquo;'),
    ('Raines', '&ldquo;Well, try it.&rdquo;')],
  'Four clicks. Hayden p. 168. Raines (paraphrasing the first line): &ldquo;the Doctor, seeing that I was not in his trap, became excited.&rdquo;'))
A(CARD('Saturday afternoon:<br>' + G('the case is called.'),
  'Not Dr. Wright but Jacob Osborne, &ldquo;very lugubriously&rdquo; (Raines), brought it before the Association. Hayden calls him &ldquo;the careful and judicious Osborne,&rdquo; pressed by others to have the matter settled. Some were for rejecting Raines, many in doubt, &ldquo;the greater number&rdquo; for him (p. 166).'))
A(WITHBG(QK('&ldquo;<b>The devil has brought this question into this association</b> to sow discord among brethren.&rdquo;',
     'Thomas Campbell, as Raines remembered it &middot; Hayden, p. 168', 'Thomas Campbell rises first', 'hay',
     'Raines (1868): &ldquo;Bro. Thomas Campbell first responded, as nearly as I can recollect, in words following.&rdquo; Richardson, more decorously: &ldquo;such a question was only calculated to create discord among the brethren&rdquo; (II, p. 245). Alexander Campbell&rsquo;s own account (1830) does not give the speech.', size='clamp(40px,8.6vmin,110px)', width='26ch'), 'tcampbell-oval.jpg', .22, 'center 30%'))
A(WITHBG(QK('&ldquo;Bro. Raines and I have been much together for the last several months, and we have mutually unbosomed ourselves to each other. I am a Calvinist, and he a [Universalist]; and, although I am a Calvinist, <b>I would put my right arm into the fire and have it burnt off before I would raise my hand against him.</b>&rdquo;',
     'Thomas Campbell, as Raines remembered it &middot; Hayden, p. 168', 'Thomas Campbell', 'none',
     'Checked by eye: the scan splits &ldquo;Calvin ist&rdquo; across a line. Richardson&rsquo;s version: &ldquo;He is philosophically a [Universalist] and I am a Calvinist, but notwithstanding this difference of opinion between us, I would put my right hand into the fire and have it burnt off before I would hold up my hands against him&rdquo; (II, p. 245). &ldquo;Raise my hand&rdquo;: they voted by show of hands.'), 'tcampbell-oval.jpg', .22, 'center 30%'))
A(WITHBG(QK('&ldquo;And if I were Paul, <b>I would have Bro. Raines in preference to any other young man&hellip; to be my Timothy</b>.&rdquo;',
     'Thomas Campbell, as Raines remembered it &middot; Hayden, p. 168', 'Thomas Campbell', 'hay',
     'Raines answered him two years later, in a letter (coming up): &ldquo;if I were Timothy, father Campbell should, in preference to any man, be my Paul.&rdquo;', size='clamp(38px,8vmin,104px)', width='28ch'), 'tcampbell-oval.jpg', .22, 'center 30%'))
A(QK('&ldquo;I think&hellip; that Bro. Raines has been very badly treated, and <b>I fear that when he speaks he will speak with too much severity</b>.&rdquo;',
     'Walter Scott, as Raines remembered it &middot; Hayden, p. 168', 'Walter Scott', 'hay',
     'Scott: he &ldquo;concurred with the preceding speakers, and would not have said any thing on the occasion but to give me time for reflection.&rdquo; Scott buying him a minute to cool down.'))

# ---------- VI. ALEXANDER'S PROPOSAL ----------
A(PORTRAIT('acyoung-oval.jpg', 'Alexander Campbell', 'Forty years old. His proposal.',
  'Then Alexander rose, and &ldquo;substantially repeated what he had said in his introductory discourse, on the difference between faith and opinion&rdquo; (Raines, Hayden p. 168). What was that discourse?', 'Saturday afternoon'))
A(LIST('The Friday sermon, as Hayden heard it', 'Three kinds of thing',
  ['<b>Knowledge:</b> what one has seen and heard for oneself. The apostles knew Jesus.',
   '<b>Faith:</b> the facts reported to us, received on their testimony.',
   '<b>Opinion:</b> everything else. &ldquo;The fruitful source of all the schism.&rdquo;'],
  'Three clicks. Hayden&rsquo;s summary of Campbell&rsquo;s sermon on Romans 14:1, pp. 164&ndash;165: &ldquo;1st. Matters of knowledge &mdash; personal knowledge; 2d. The things of faith, the facts reported to us, which we accept on testimony; 3d. Matters of opinion.&rdquo; &ldquo;The apostles knew the gospel to be true, and none but they stood on this high ground of knowledge.&rdquo; &ldquo;As the facts of the gospel are always one and invariable&hellip; the faith of all persons is a unit. The important conclusion was thus reached, that Christians are not divided on the faith.&rdquo; Opinion &ldquo;was the fruitful source of all the schism which checkers, disgraces, and weakens the Christian profession.&rdquo;',
  size='clamp(32px,6.2vmin,78px)', gap='3vmin'))
A(QK('&ldquo;Faith stands on testimony. <b>No testimony, no faith.</b>&rdquo;',
     'Campbell&rsquo;s Friday sermon, in Hayden&rsquo;s summary, p. 164', 'The rule', 'hay',
     'Hayden goes on: &ldquo;Testimony is delivered by witnesses. Christ&rsquo;s apostles are his witnesses&hellip; Our faith in Christ is founded on the testimony of his witnesses&hellip; &lsquo;Faith comes by hearing, and hearing by the word of God&rsquo;; Rom. x: 17.&rdquo; Hayden&rsquo;s words, summarizing; not Campbell verbatim.', size='clamp(50px,11vmin,140px)', width='18ch'))
A(QK('&ldquo;&hellip;<b>It could never be considered a matter of belief, since there was no testimony to render it such.</b>&rdquo;',
     RICH + ', p. 245 (summarizing Campbell at Warren)', 'Applied to Raines', 'rich2',
     'Richardson: Raines&rsquo; view &ldquo;could be regarded as nothing but an opinion, since there was not a passage anywhere in the writings of prophets or apostles affirming it.&rdquo; Campbell then proposed that Raines &ldquo;should express his willingness to preach the gospel as the apostles preached it, and to retain his opinions as private property in harmony with the principles of the Reformation.&rdquo;'))
A(QK('&ldquo;If a person say such is his private opinion, let him have it as his private opinion; but lay no stress upon it; and <b>if it be a wrong private opinion, it will die a natural death much sooner than if you attempt to kill it</b>.&rdquo;',
     AC + ', ' + MH30 + ', p. 147', 'Alexander Campbell, in his own words', 'mh1830',
     'Written in 1830, telling this very story. Before it: &ldquo;And will you receive a Universalist too? No; not as a Universalist. If a man, professing Universalist opinions, should apply for admission, we will receive him, if he will consent to use and apply all the Bible phrases in their plain reference to the future state of men and angels.&rdquo; And of the essay&rsquo;s whole argument: &ldquo;We do not ask them to give up their opinions&mdash;we ask them only not to impose them upon others&rdquo; (p. 145).'))
A(QK('&ldquo;&hellip;Bro. Campbell requested me <b>to stand upon a bench</b>, and proclaim to the large concourse present, my own views of my obligations as a Christian and as a preacher of the gospel.&rdquo;',
     RAINES + ', p. 168', 'On the bench', 'hay',
     'Hayden&rsquo;s footnote: &ldquo;The better to be heard, the house being very full.&rdquo; What Raines said: &ldquo;That my Restorationism was a philosophy. That I would neither preach it nor contend for it, but would preach the whole gospel, and teach the whole truth of Christianity according to my best ability.&rdquo;'))
A(TALK('The question', [
    ('Alexander Campbell', '&ldquo;Whether there was any law of Christ by which I could be condemned?&rdquo;'),
    ('The Association', '&ldquo;The vote was in the negative, and in my favor <b>by an overwhelming majority</b>.&rdquo;')],
  'Two clicks. Raines, Hayden p. 169. Richardson: &ldquo;Whether there was any law of Christ by which a brother could be condemned who deported himself as Mr. Raines proposed to do?&rdquo; decided &ldquo;by a very large majority&rdquo; (II, p. 246). Raines: &ldquo;This I took to be quite a triumph; but the end was not yet.&rdquo;', size='clamp(34px,6.4vmin,80px)'))
A(TALK('Sunday, the sunrise prayer meeting', [
    ('An old brother', '&ldquo;Brethren, I understand there are certain persons in the fellowship of this association who deny that sinners are saved by grace&hellip; I move that such persons be disfellowshiped.&rdquo;'),
    ('Raines', '&ldquo;I second that motion; for <i>by grace are ye saved through faith</i>&hellip; Now, if any member of this association holds any doctrine contradictory to the teaching of this passage, I move that he be immediately disfellowshiped.&rdquo;'),
    ('Raines', '&ldquo;The old Brother who had put the motion, <b>struck a direct line for the door</b>, and the congregation followed him; and there my association troubles ended.&rdquo;')],
  'Three clicks. Hayden p. 169. &ldquo;In a twinkling I was on my feet.&rdquo; Ephesians 2:8&ndash;9. Raines: &ldquo;Affairs, however, would probably have taken a very different turn, had somebody else than myself seconded the old man&rsquo;s motion.&rdquo;', size='clamp(25px,4.5vmin,56px)'))
A(ASK(2, 'After the vote and the sunrise motion. The stakes were real: Baptists and Methodists elsewhere would not even immerse a Universalist (Stacy and Person, New York, 1817). Hold it: the answer is the same as the first.'))
A(CARD('The rest<br>' + G('of the story.'),
  'In Raines&rsquo;s own words, forty years on and two years on.', 'Raines'))
A(QK('&ldquo;<b>Had they attempted to brow-beat me I might have been ruined forever.</b> But treating me kindly, at the same time that they convinced me that my opinion, whether true or false, dwindled into nothingness in comparison with the faith of the gospel, <b>redeemed me</b>.&rdquo;',
     RAINES + ', p. 169', 'Forty years later', 'hay',
     'Before it: &ldquo;I was dealt with, and my case managed, by Bro. Campbell and all the chief brethren in very great kindness and wisdom.&rdquo; After: &ldquo;I became a day and night preacher of the gospel, and my mind becoming absorbed in this vast work, the opinion faded, and in ten months was numbered with all my former errors&rdquo; (pp. 169&ndash;170; a page break falls in that sentence).'))
A(QK('&ldquo;<b>The facts of the New Testament will conquer the world. They have conquered me</b>, and are now conquering thousands of others.&rdquo;',
     'Aylett Raines, letter to Campbell, Cincinnati, April 13, 1830 &middot; ' + MH30 + ', p. 149', 'Two years later', 'none',
     'Checked by eye in the scan (&ldquo;con quered&rdquo; split across a line). The letter: &ldquo;I wish to inform you that my &lsquo;Restorationist&rsquo; sentiments have been slowly and imperceptibly erased from my mind, by the ministry of Paul and Peter&hellip; After my immersion, I brought my mind, as much as I possibly could, like a blank surface, to the ministry of the New Institution&rdquo; (pp. 148&ndash;149). And: &ldquo;My former associates persecute me, I would say, most cruelly.&rdquo;', size='clamp(38px,8vmin,104px)', width='28ch'))
A(QK('&ldquo;I am strongly disposed to reciprocate the kindness of that beloved brother, by declaring, that, <b>if I were Timothy, father Campbell should, in preference to any man, be my Paul</b>.&rdquo;',
     'Aylett Raines, letter, 1830 &middot; ' + MH30 + ', p. 149', 'To Thomas Campbell', 'mh1830',
     '&ldquo;You will not call this flattery. It is a warm sentimental effusion of my heart.&rdquo; Campbell printed the letter as proof of &ldquo;the wisdom of the course pursued.&rdquo; His own comment on his reasoning at Warren: &ldquo;I urged this course from the conviction that, if these opinions were not agitated nor discussed, the ancient gospel would cause them to wither away. This was my philosophy then&rdquo; (p. 148).'))
A(QK('&ldquo;Reason and experience unite their testimony in assuring us that, <b>in the same proportion as individuals labor to be of one opinion, they disagree</b>.&rdquo;',
     AC + ', ' + MH30 + ', p. 149', 'Campbell&rsquo;s lesson', 'mh1830',
     'He goes on: &ldquo;The greater the emphasis laid upon opinions, the more rapidly they generate. The nearest approaches to a unity of opinion which I have ever witnessed, have appeared in those societies in which no effort was made to be of one opinion; in which they allowed the greatest liberty of opinion, and in which they talked more and boasted more of the glory and majesty of the great facts, the wonderful works of God&rsquo;s loving kindness.&rdquo; Honest notes: the terms were that Raines not teach his opinion; a minority nearly split the Association, and some would-be members walked away (Richardson II, p. 246).'))

# ---------- VII. THE HINGE ----------
A(LIST('Two ways of reading', 'Raines, before and after',
  ['<b>Before:</b> a verse as proof. &ldquo;The scrap.&rdquo; The covenants a &ldquo;hotch-potch,&rdquo; &ldquo;a chaos.&rdquo;',
   '<b>Scott:</b> the whole chapter. The covenants in order. The story of faith.'],
  'Two clicks. Same Bible, same man. What changed was the unit of reading: not the verse, the story.', size='clamp(36px,7vmin,88px)', gap='3.4vmin'))
A(QK('&ldquo;The words and sentences of the Bible are to be translated, interpreted, and understood according to <b>the same code of laws and principles of interpretation by which other ancient writings are translated and understood</b>&hellip;&rdquo;',
     AC + ', <i>The Christian System</i> (1839), &ldquo;Rules of Interpretation,&rdquo; p. 16', 'Like any other book', 'cs',
     'He goes on: &ldquo;for when God spoke to man in his own language, he spoke as one person converses with another.&rdquo; Rule 1: &ldquo;consider first the historical circumstances of the book&rdquo;: the order, title, author, date, place and occasion. Rule 2: &ldquo;observe who it is that speaks, and under what dispensation he officiates.&rdquo;'))
A(QK('&ldquo;In reading the historical and epistolary parts of the sacred writings, begin at the beginning and <b>follow the writer in the train of his own thoughts</b> and reasonings to the end of the subject on which he writes, <b>irrespective of chapters and verses</b>.&rdquo;',
     AC + ', <i>Millennial Harbinger</i> (1846), &ldquo;Tracts for the People,&rdquo; No. III, p. 22', 'Campbell&rsquo;s rule', 'mh1846',
     'On the same page: dividing the Bible into chapters and verses has given it &ldquo;the appearance of a book of proverbs.&rdquo; Rule 2 of his rules of interpretation: &ldquo;observe who it is that speaks, and under what dispensation he officiates. Is he a Patriarch, a Jew, or a Christian?&rdquo; (<i>Christian System</i>, p. 16).'))
A(QK('&ldquo;The Bible is a book of facts, not of opinions, theories, abstract generalities, nor of verbal definitions&hellip; <b>History is therefore the plan pursued in both Testaments</b>&hellip;&rdquo;',
     AC + ', <i>The Christian System</i> (1839), p. 19', 'Campbell: a book of facts', 'cs',
     'In full: &ldquo;It is a book of awful facts, grand and sublime beyond description. These facts reveal God and man&hellip; The meaning of the Bible facts is the true biblical doctrine. History is therefore the plan pursued in both Testaments; for testimony has primarily to do with faith, and reasoning with the understanding.&rdquo; History and prophecy &ldquo;make up exactly four-fifths of all the volumes of inspiration.&rdquo; And: &ldquo;Fact means something done&rdquo; (p. 115). A book of deeds, a story; and its facts are received on testimony. That is the Warren sermon.'))
A(ASK(3, 'A rule, a book of facts. But what was the method, really, that made a Universalist preacher see the Bible for the first time? Hold it.'))
A(QK('&ldquo;His main object was to convince the people <b>that God meant what he said</b> in his Word, which caused great excitement&hellip; <b>many sitting up all night reading the Scriptures to see if they meant what they said</b>&hellip;&rdquo;',
     'Samuel Robbins&rsquo;s diary, Braceville Ridge, February 23, 1828 &middot; ' + HAY + ', p. 143', 'Up all night', 'hay',
     'Scott preaching, the winter before Warren; the excitement ran through &ldquo;Braceville and Windham.&rdquo; Robbins goes on: Scott held up his left hand and counted the five items on his fingers, &ldquo;then contrast it with the five points of Calvinism; and thus he made the Scripture order of the gospel so plain, that little boys could carry it home.&rdquo;'))
A(QK('&ldquo;They got their Bibles, and went to reading and searching for the truth. <b>No word fell on the floor, or hit the wall&mdash;all was eagerly caught and tried by the book.</b>&rdquo;',
     'J. G. Mitchell, on Scott at Warren, 1828 &middot; ' + HAY + ', p. 97', 'Tried by the book', 'hay',
     'The hearers checked the preacher against their own Bibles. Mitchell goes on: &ldquo;They could do nothing against it; it was the simple gospel of Christ in its facts, and commands, and promises.&rdquo; Elsewhere on the Reserve: &ldquo;The Bibles were looked up, the dust brushed off, and the people began to read&rdquo; (Hayden, p. 121).'))
A(QK('&ldquo;I also discovered that I had never read the Scriptures, to form sentiments for myself. <b>My religion consisted in opinions, rather than faith.</b> I had been acting upon the credit system, and I was determined to abandon it at once.&rdquo;',
     'Jonas Hartzel, a farmer of Deerfield, in his own account &middot; ' + HAY + ', p. 315', 'Opinions, rather than faith', 'hay',
     'A hearer using Campbell&rsquo;s distinction for himself. Next: &ldquo;We now began to read the Bible as we had never read it before.&rdquo; Their study group of every sect: &ldquo;No doctrinal standard was appealed to. All human authorities were ignored. The Bible was our book; Jesus Christ and his apostles were our umpire&rdquo; (pp. 318&ndash;319).'))
A(QK('&ldquo;It was easily perceived <b>the book was to be read like other books</b>&hellip; From that time the Bible was studied as a new book, and oh, what a change it made! It is better remembered and felt than told.&rdquo;',
     'William Hayden, in his own words &middot; ' + BAX + ', pp. 198&ndash;199', 'A new book', 'bax',
     'At a preachers&rsquo; meeting in New Lisbon, on &ldquo;the true principles of interpretation&rdquo;: &ldquo;first, find who speaks, who it is spoken to, what is the subject, what is the object, and what is the context.&rdquo; Then: &ldquo;every diligent student of it could be a self-taught disciple.&rdquo; Campbell&rsquo;s method, in a lay preacher&rsquo;s mouth.'))
A(ASK(4, 'Not Campbell now: the farmers, the diarists, the lay preachers. Their own words.'))
A(ASK(5, 'Last week&rsquo;s question, sharpened: not how did they unite, but how could they? Leave it open. To answer it, a detour, through a Wright.'))
A(CARD('The accuser at Warren was a<br>' + G('Dr. Wright.'),
  'A small joke on the way. Two centuries later, another Wright is read all over the Churches of Christ, and here, and he reads the Bible the way Scott read it to Raines: as a story, in acts.', 'Another Wright'))

# ---------- VIII. N. T. WRIGHT, AND CAMPBELL (paired slides, Micah, 2026-11-27) ----------
A(C('N. T. Wright', 'Bishop of Durham (2003&ndash;2010); New Testament scholar at St Andrews and Oxford. Read across the Churches of Christ, and here at Otter Creek. Held over from Chapter 7: how Wright reads Scripture.', 'Two centuries later'))

# 1. A historian, reading a story
A(CARD('Wright is a historian.<br>' + G('He reads the Bible as a story.'), 'The first of four things Wright does that Campbell did. Each pair: Wright, then one click for Campbell.', '1 of 4'))
A(PAIR('What God has done',
  '&ldquo;The historian has to plunge into the real world&hellip; in order to find out <b>what it is in fact that God has sovereignly done</b>&hellip;&rdquo;', W18 + ', p. 22', 'w18',
  '&ldquo;<b>Fact means something done.</b>&rdquo;', AC + ', <i>The Christian System</i> (1839), p. 115', 'cs',
  'Wright&rsquo;s history and Campbell&rsquo;s fact are the same thing: what God did. Campbell goes on: &ldquo;The work of redemption is a system of works, or deeds, on the part of Heaven&hellip; the most splendid series of moral facts which man or angel ever saw&rdquo; (p. 116). Raines: Scott preached Hebrews 11, faith as a story of deeds, and &ldquo;here I virtually surrendered.&rdquo;'))
A(QK('&ldquo;Suppose there exists a Shakespeare play <b>whose fifth act had been lost</b>.&rdquo;',
     LAING + ', p. 18', 'Wright&rsquo;s parable', 'hcba',
     'He goes on: the first four acts are so rich that the play ought to be staged; rather than write a fifth act once for all, give the parts to experienced actors &ldquo;who would immerse themselves in the first four acts, and in the language and culture of Shakespeare and his time, and who would then be told to work out a fifth act for themselves.&rdquo; &ldquo;The first four acts, existing as they did, would be the undoubted &lsquo;authority&rsquo; for the task in hand.&rdquo;', size='clamp(44px,9.6vmin,124px)', width='22ch'))
A(LIST('The five acts', 'Wright&rsquo;s play',
  ['<b>1.</b> Creation', '<b>2.</b> Fall', '<b>3.</b> Israel', '<b>4.</b> Jesus',
   '<b>5.</b> The church: the New Testament its first scene, and we are on stage.'],
  'Five clicks. Laing Lecture, p. 19: &ldquo;the possibility of seeing the five acts as follows: (1) Creation; (2) Fall; (3) Israel; (4) Jesus. The New Testament would then form the first scene in the fifth act, giving hints as well (Rom 8; 1 Cor 15; parts of the Apocalypse) of how the play is supposed to end.&rdquo; Note 1 Corinthians 15: Raines&rsquo;s chapter. Campbell&rsquo;s acts: the Patriarchal, the Jewish, the Christian ages (<i>Sermon on the Law</i>, 1816; &ldquo;the star-light&hellip; the moonlight&hellip; the sun-light of the moral world,&rdquo; <i>Christian Baptist</i>, 1828).',
  size='clamp(36px,7vmin,88px)', gap='1.6vmin'))
A(PAIR('In acts',
  '&ldquo;<b>The Old Testament has the authority that an earlier act of the play would have, no more, no less.</b>&rdquo;', LAING + ', p. 19', 'hcba',
  '&ldquo;<b>The first act of the great drama closes with the Deluge.</b>&rdquo;', 'Alexander Campbell&rsquo;s <i>Christian Baptist</i> 6 (Dec. 1, 1828), &ldquo;The Patriarchal Age.&mdash;No. V,&rdquo; p. 118 (unsigned)', 'cb6',
  'Raines&rsquo;s third night: &ldquo;I certainly did not know the difference between the old covenant and the new&hellip; I made of them a chaos.&rdquo; Scott put the acts in order. Campbell&rsquo;s serial on the ages ran in his paper the very months of the Raines story; Babel closes the second act, Abraham begins &ldquo;a new chapter.&rdquo; Rule 2: &ldquo;Is he a Patriarch, a Jew, or a Christian?&rdquo;'))

# 2. Creeds
A(CARD('He pushes back on the creeds:<br>' + G('they divorce us from the text.'), 'Not that they are false. They are incomplete as narrative.', '2 of 4'))
A(PAIR('Distilled',
  '&ldquo;&hellip;some of Christianity&rsquo;s Great Traditions have <b>slipped their moorings and floated off into the blue sky of speculation</b>&hellip;&rdquo;', W18 + ', p. 20', 'w18',
  '&ldquo;Some of those dogmas <b>may be metaphysically true, but they are distilled truths.</b> They have come from the Calvinistic or Arminian distillery.&rdquo;', AC + ', <i>Christian Baptist</i> 2 (March 7, 1825), p. 151', 'cb2',
  'Neither says the creeds are false: Campbell, &ldquo;may be metaphysically true&rdquo;; Wright&rsquo;s example is Chalcedon, whose abstract terms &ldquo;do not do justice to the vivid figure of the four Gospels&rdquo; (Chadwick, quoted p. 20). Wright also: the Bible is not &ldquo;creeds&mdash;lists of things to be believed&rdquo; (Laing Lecture, p. 9). Raines: Scott said his Universalism &ldquo;was a philosophy, as was Calvinism, Arminianism, etc., and no part of Christianity.&rdquo;'))

# 3. Atonement theories
A(CARD('He pushes back on atonement theories<br>' + G('that leave the story behind.'), 'Wright, then Campbell on his own first great sermon.', '3 of 4'))
A(PAIR('The atonement',
  '&ldquo;<b>Theories of atonement do not need to be superimposed on an abstract narrative about Jesus</b>, as has so often been attempted. They grow out of the real-life Jesus stories we already have.&rdquo;', NTW + ', <i>The Day the Revolution Began</i> (2016), p. 193', 'none',
  '&ldquo;It was rather a youthful performance&hellip; <b>Its views of the atonement are rather commercial than evangelical.</b>&rdquo;', AC + ', <i>Millennial Harbinger</i> (1846), on his <i>Sermon on the Law</i> (1816), p. 493', 'mh1846',
  'Wright&rsquo;s line: checked in Micah&rsquo;s ebook (2026-11-04), not yet against a text in the database; recheck before class. Campbell reprinted the 1816 sermon thirty years on, unchanged, and flagged its atonement as a transaction (commercial) rather than the gospel (evangelical). That sermon got him tried for heresy by the Redstone Baptists: the young Campbell had his own Warren.'))

# 4. Renewal, and living in the story
A(CARD('He points us to the renewal of all things,<br>' + G('and invites us to live in that story.'), 'The last of the four.', '4 of 4'))
A(PAIR('The renewal of all things',
  '&ldquo;<b>The point about new creation is that it is the renewal of this world</b>, not the substitution of another one.&rdquo;', W18 + ', p. 19', 'w18',
  '&ldquo;It shall have for its object the developement, and introduction of that political and religious order of society called <b>THE MILLENNIUM</b>&hellip;&rdquo;', AC + ', <i>Millennial Harbinger</i> 1 (1830), prospectus', 'mh1830',
  'The Harbinger began in January 1830, the year of Raines&rsquo;s letter. The prospectus goes on: &ldquo;which will be the consummation of that ultimate amelioration of society proposed in the Christian Scriptures.&rdquo; Chapter 7&rsquo;s theme: God&rsquo;s future, lived now.'))
A(PAIR('Living in the story',
  '&ldquo;The church would then live under the &lsquo;authority&rsquo; of the extant story, being required to offer <b>something between an improvisation and an actual performance of the final act</b>.&rdquo;', LAING + ', p. 19', 'hcba',
  '&ldquo;<b>The fact, or the thing said to be done, produces the change</b> in the frame of mind.&rdquo;', AC + ', <i>The Christian System</i> (1839), p. 122', 'cs',
  'Wright goes on: &ldquo;And that is the task of the whole church. Need I say, not merely of the professional caste within it&rdquo; (p. 27). Campbell&rsquo;s chain: &ldquo;fact, testimony, faith, and feeling&rdquo; (p. 122), then action; the facts are &ldquo;a moral seal or archetype&rdquo; that draws God&rsquo;s image on the soul (p. 116). Raines, 1830: &ldquo;The facts of the New Testament will conquer the world. They have conquered me.&rdquo;'))

A(ASK(6, 'The sub-question, asked after the pairs, and the storytelling trick: answer this one, and it frames the answer to the others. Answer, next slide. Otter Creek reads Wright: the sermons, the classes, the books on the shelf. [Micah: examples from Otter Creek.] Four things he does, and Campbell beside each.'))
A(CARD('Both point us to<br>' + G('the power of the story.'),
  'The answer to question 6. We are drawn to Wright because he points where Campbell pointed: the story of Scripture, read whole, read as history, with power of its own to change us. Historian and story; past the creeds; past the atonement theories; into the renewal of all things. Campbell&rsquo;s heirs kept his rules and lost his story; Wright gives it back.', 'Why Wright is popular among us'))

# Hidden in the reshape (2026-11-26), kept for reference
HIDE(QK('&ldquo;<b>The Old Testament has the authority that an earlier act of the play would have, no more, no less.</b>&rdquo;',
     LAING + ', p. 19', 'The two covenants', 'hcba',
     'Raines&rsquo;s third night: he &ldquo;did not know the difference between the old covenant and the new&rdquo; and &ldquo;made of them a chaos.&rdquo; Wright: earlier acts are &ldquo;not at all appropriate to be picked up and hurled forward into Act 5 without more ado.&rdquo; Campbell, Rule 2: &ldquo;observe who it is that speaks, and under what dispensation.&rdquo;', size='clamp(40px,8.6vmin,110px)', width='26ch'))
HIDE(LIST('Campbell and Wright', 'Where they meet, where they part',
  ['<b>Both:</b> the Bible is mostly story, God&rsquo;s deeds; doctrine follows the facts.',
   '<b>Both:</b> read in acts; earlier acts are not today&rsquo;s script.',
   '<b>Campbell:</b> facts are plain; the same rules give the same conclusions.',
   '<b>Wright:</b> facts come inside a story; we improvise the last act.'],
  'Four clicks. Campbell hoped &ldquo;all who work by the same rules, come to the same conclusions&rdquo; (MH 1846, p. 13). Lexington, February 1832, proved otherwise: pledged to &ldquo;the New Testament alone,&rdquo; they split within a week over who may serve the loaf. Wright: &ldquo;the more that you insist that you are based on the Bible, the more fissiparous you become&rdquo; (Laing, p. 13). Our summary: Wright is a restorationist with a better epistemology; Campbell was a narrative theologian with a Baconian one. And Raines: what changed him was not a rule but a story read whole, and two old men who treated him kindly.',
  size='clamp(30px,5.8vmin,72px)', gap='2.4vmin'))
HIDE(CARD('How Wright-pilled<br>' + G('are we?'),
  'Held over from Chapter 7. Otter Creek reads Wright: Josh Graves, the sermons, the classes, the books on the shelf. Why are we drawn to him? Maybe because he gives back the half of Campbell his heirs dropped: the story. [Micah: examples from Otter Creek.]', 'An observation'))
# Displaced by the paired slides (2026-11-27)
HIDE(w7.NEXT_WEEK[1])   # "Story authority"
HIDE(w7.NEXT_WEEK[0])   # "Most of the Bible does not consist of rules... Nor does it consist of creeds"
HIDE(w7.NEXT_WEEK[3])   # "not merely of the professional caste"
HIDE(QK('&ldquo;The church would then live under the &lsquo;authority&rsquo; of the extant story, being required to offer <b>something between an improvisation and an actual performance of the final act</b>.&rdquo;',
     LAING + ', p. 19', 'Our part', 'hcba',
     '&ldquo;Appeal could always be made to the inconsistency of what was being offered with a major theme or characterization in the earlier material.&rdquo; Faithful improvisation: not repeating earlier scenes, not making up a new play.'))
HIDE(QK('&ldquo;&hellip;some of Christianity&rsquo;s Great Traditions have <b>slipped their moorings and floated off into the blue sky of speculation</b>&hellip;&rdquo;',
     W18 + ', p. 20', 'Wright, on the creeds', 'w18',
     'His example is Chalcedon, through Henry Chadwick: &ldquo;Abstract terms do not do justice to the vivid figure of the four Gospels.&rdquo; And: &ldquo;the ways we have perceived and re-expressed it have indeed introduced mistakes, precisely by not attending to the historical setting and meaning&rdquo; (p. 19). Dogma, tradition and piety &ldquo;all need to submit&hellip; to the original meaning of scripture itself.&rdquo;'))
HIDE(QK('&ldquo;<b>The historian has to plunge into the real world</b>, to follow the Jesus of Philippians 2 into the messy and risky sphere of history itself&hellip; in order to find out what it is in fact that God has sovereignly done&hellip;&rdquo;',
     W18 + ', p. 22', 'Wright, the historian', 'w18',
     'Then: &ldquo;We do not know this in advance. The first disciples didn&rsquo;t know it in advance.&rdquo; Campbell&rsquo;s word for what God has done is a fact: &ldquo;Fact means something done.&rdquo;'))

# ---------- CLOSE ----------
A('<section class="slide"><div class=eyebrow>The quiz, again</div>'
  '<h2 style="max-width:none;font-size:clamp(40px,8vmin,104px)">&ldquo;We speak where the Bible speaks&hellip;&rdquo;</h2>'
  '<div class="sub frag" style="font-size:clamp(26px,5vmin,62px);color:var(--gold)">To whom? In which act? Read whole?</div>'
  '<aside class=notes>One click. Raines had a verse where the Bible spoke, and it spoke wrong until he heard the chapter. Where the Bible is silent (the end of all things, in Raines&rsquo;s case), Campbell&rsquo;s answer was: keep your opinion as private property, and preach the story.</aside></section>')
A(ASK(0, 'All six, together. One answer serves them.', 'Our questions'))
# One idea, three ramifications (Micah, 2026-11-26). The four earlier ideas (IDEAS, above) are no longer shown.
A('<section class="slide idea room"><div class=eyebrow>Today&rsquo;s idea</div>'
  '<h2 style="max-width:none">The story ' + G('does the work.') + '</h2>'
  '<div class=litany style="text-align:left;gap:2.6vmin;max-width:90vw;margin-top:3vmin">'
  + ''.join('<div class="no frag" style="font-size:clamp(30px,5.6vmin,70px)">%s</div>' % t for t in (
    'This is how <b>Walter Scott</b> can be so compelling.',
    'This is how <b>Alexander Campbell</b> can embrace a Universalist.',
    'This is how <b>Stone-Campbell</b> can unite on the Bible.'))
  + '</div><aside class=notes>One idea, three clicks for its ramifications. '
  '<b>Scott:</b> four nights of whole chapters (1 Cor 1, 1 Cor 15, the two covenants, Hebrews 11); the story converted a man no argument could. Robbins: he convinced them &ldquo;that God meant what he said.&rdquo; '
  '<b>Campbell:</b> faith rests on the testimony of the story, &ldquo;No testimony, no faith&rdquo;; Raines&rsquo;s Universalism was an opinion about what the story had not told, so it could be held &ldquo;as private property.&rdquo; And it was held kindly: Raines, &ldquo;Had they attempted to brow-beat me I might have been ruined forever. But treating me kindly&hellip; redeemed me.&rdquo; '
  '<b>Stone-Campbell:</b> Lexington, 1832, united on the story itself and left the readings free. Wright: the story is still going, and the whole church is in it.</aside></section>')
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): Where do we still read the Bible as a book of proverbs, a verse at a time? What opinions do we hold as tests of fellowship? Who has been our Thomas Campbell, kind while we were wrong?</aside>',
         w3b.pick('&#9670; for discussion', 0), flags=re.S).replace('&#9670; for discussion', '&#9670; for discussion &middot; Chapter 9', 1))
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Today&rsquo;s sources: Hayden, <i>Early History of the Disciples in the Western Reserve</i> (1875), with Raines&rsquo;s own recollections; Richardson&rsquo;s <i>Memoirs</i>; Campbell, &ldquo;Millennium.&mdash;No. II&rdquo; (1830); Eddy, <i>Universalism in America</i>; Wright&rsquo;s Laing Lecture.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S).replace('<h2 class=url>stone-campbell.micahredding.com</h2>',
          '<h2 class=url style="letter-spacing:.02em"><span style="color:var(--gold)">stone-campbell</span><span style="color:#ede4d3;opacity:.75">.micahredding.com</span></h2>', 1))
A(BLACK)
