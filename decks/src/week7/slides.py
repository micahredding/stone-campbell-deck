# -*- coding: utf-8 -*-
# Chapter 7: Living into God's Future (the Millennial Harbinger). Sunday, November 15, 2026.
# The story as Micah will tell it (week7.md, "Narrative: the story as we'll tell it", 2026-11-13):
# recap; still seeking fellowship (the Baptists); the Christian Baptist; the eternal pattern; the pivot to the
# Millennial Harbinger; how they spoke about the future; unity, conscience and the priesthood as the coming
# church; not a particular eschatology but the future itself; N. T. Wright beside Campbell.
# Build:  python3 decks/src/week7map/build.py   ->  decks/chapter7.html   (runs the Chapter 3 engine with PART=7)
# Every on-screen quotation carries data-chk=<source key>; decks/src/week7/check_quotes.py runs the quote
# standard's checker (agent-framework/tools/quote_check.py) against the research database for each one.
# Notes are a cue card: fact / source / your line.
import importlib.util, os, re

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, '..', rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
w4 = _load('w4slides', 'week4/slides.py')
R = _load('resources', 'resources.py')
w3 = w3b.w3
PATDEFS, CHRISTENDOM_CSS = w3b.PATDEFS, w3b.CHRISTENDOM_CSS
C, CARD, G, BLACK = w4.C, w4.CARD, w4.G, w4.BLACK
Q, N = w3.Q, w3.N

def BIGQ(slide, size='clamp(30px,6.4vmin,80px)', width='40ch'):   # a quote set larger than Q's default
    return re.sub(r'<p class="bigquote( long| xlong)?">', lambda m: '<p class="bigquote%s" style="font-size:%s;max-width:%s;line-height:1.22">' % (m.group(1) or '', size, width), slide, 1)
def K(slide, key):   # tag a quote slide with its source key for check_quotes.py ('none' = checked elsewhere; see notes)
    return slide.replace('<section class="slide', '<section data-chk="%s" class="slide' % key, 1)
def QK(quote, cite, eyebrow, key, *notes, size=None, width=None):
    s = Q(quote, cite, eyebrow)
    if size: s = BIGQ(s, size, width or '40ch')
    return K(s, key) + N(*notes)
def LIST(eyebrow, title, items, note, size='clamp(26px,4.6vmin,58px)', gap='1.6vmin'):   # dated or parallel items, one per click
    lis = ''.join('<div class="no frag" style="font-size:%s">%s</div>' % (size, it) for it in items)
    return ('<section class="slide"><div class=eyebrow>%s</div><h2 style="max-width:none">%s</h2>'
            '<div class=litany style="text-align:left;gap:%s;max-width:90vw">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, title, gap, lis, note))
def D(y, t): return '<b>%s</b> &nbsp;%s' % (y, t)

AC = 'Alexander Campbell'
MH = '<i>Millennial Harbinger</i>'
CB = '<i>Christian Baptist</i>'
CS = 'Alexander Campbell, <i>The Christian System</i>'
DA = 'Thomas Campbell, <i>Declaration and Address</i> (1809)'
CM = 'Barton W. Stone, <i>Christian Messenger</i>'
NTW = 'N. T. Wright'

IDEAS = [   # the three ideas Micah drafted, then the three added 2026-11-10 (all six kept: Micah, "add, don't replace")
    ('We live as a microcosm<br>' + G('of the age to come.'), 'Brush Run&rsquo;s table, &ldquo;an emblem of the millennial state of the Church&rdquo;; Wright&rsquo;s &ldquo;small working model of new creation.&rdquo;'),
    ('Eschatology<br>' + G('is our tradition.'), 'Not a borrowed idea: the movement named its flagship for the future. Cane Ridge, the <i>Last Will</i>, Brush Run, the <i>Harbinger</i>.'),
    ('Eschatology drives us in various ways,<br>' + G('which may look very different.'), 'Campbell&rsquo;s colleges and missionary society; Stone&rsquo;s and Lipscomb&rsquo;s withdrawal from government and war. The same hope, different &ldquo;therefores.&rdquo;'),
    ('The church&rsquo;s life now<br>' + G('is a taste of God&rsquo;s future.'), 'The table, the Lord&rsquo;s day that &ldquo;anticipates the morning of the resurrection,&rdquo; every member a king and priest.'),
    ('Its unity is founded on Christ alone,<br>' + G('so it needs freedom of conscience.'), 'Unity on anything else (creed, party, sword, state) is not the real unity. &ldquo;We do not ask them to give up their opinions&mdash;We ask them only not to impose them upon others.&rdquo; (1830)'),
    ('Our practices are ways<br>' + G('of living that future now.'), 'The pattern as testimony, not legalism: how do we best embody the unity, the priesthood, the future that is coming?'),
]
def IDEA(k):
    h, n = IDEAS[k - 1]
    return ('<section class="slide idea room"><div class=eyebrow>Idea %d of %d</div><h2 style="max-width:none">%s</h2><aside class=notes>%s</aside></section>' % (k, len(IDEAS), h, n))
def IDEASUM(note):
    return ('<section class="slide room"><div class=eyebrow>Today&rsquo;s ideas</div>'
            '<div class="litany ideasum" style="text-align:left;gap:1vmin;margin-top:2vmin">'
            + ''.join('<div class=no style="font-size:clamp(24px,4.6vmin,58px)"><span style="color:var(--gold);display:inline-block;width:1.6em">%d.</span>%s</div>' % (n, h.replace('<br>', ' ')) for n, (h, _) in enumerate(IDEAS, 1))
            + '</div><aside class=notes>%s</aside></section>' % note)

S = []
A = S.append
def HIDE(slide): pass

# ---------- OPENING ----------
A(w3b.S[0])   # the class title
A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:24ch">Finish the song:<br><i>&ldquo;This world is not my home, I&rsquo;m just a-passing through. My treasures are laid up&hellip;&rdquo;</i></h2>'
  '<div class="sub frag" style="font-size:clamp(30px,6vmin,76px);margin-top:3vmin">&hellip;somewhere beyond the blue.</div>'
  '<aside class=notes>One click for the answer. Extra points if anyone sings the next line (&ldquo;The angels beckon me from heaven&rsquo;s open door&rdquo;). Let them sing. Don&rsquo;t comment yet: we come back to this song when we get to &ldquo;a new earth out of this earth.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Quiz</div>'
  '<h2 style="max-width:none">When do we celebrate Easter?</h2>'
  '<div class="sub frag" style="font-size:clamp(34px,7vmin,88px);margin-top:3vmin">Every Sunday.</div>'
  '<aside class=notes>One click. We come back to this too: Campbell, 1834, the Lord&rsquo;s day &ldquo;anticipates the morning of the resurrection.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 7</div>'
  '<h1>Living into<br>God&rsquo;s Future</h1><div class=table-line></div>'
  '<div class=sub>The <i>Millennial Harbinger</i> &middot; 1830&ndash;1870</div>'
  '<aside class=notes>Chapter 7. Last week: Brush Run ordains Alexander by the choice of the people. This morning: what they were reaching for.</aside></section>')

# ---------- 1. RECAP ----------
A(LIST('Where we are', 'From Ireland to Brush Run',
  [D('1808', 'Shipwrecked off Islay; a winter in Glasgow'), D('1809', 'The family reunited in Pennsylvania; the <i>Declaration and Address</i>'),
   D('1810', 'The Synod of Pittsburg refuses them'), D('May 1811', 'Brush Run constituted; the first Supper'), D('Jan. 1812', 'Alexander ordained by the choice of the people')],
  'Five clicks. One breath each. The ordination was last week.'))

# ---------- 2. STILL SEEKING FELLOWSHIP: THE BAPTISTS ----------
A(C('Still seeking<br>a larger fellowship', 'Thomas and Alexander kept looking for an institutional home. It ended with the Baptists.'))
A(R.ASSOC_SUMMARY)
for _x in R.associations(): A(_x)   # side path: the whole timeline, off the summary
A(LIST('Among the Baptists', 'Redstone and Mahoning',
  [D('1812', 'The family immersed; Baptist preachers press them to join'),
   D('Fall 1813', 'Brush Run joins the Redstone Baptist Association, on its own written terms: no creed'),
   D('1816', 'The &ldquo;Sermon on the Law&rdquo;; Redstone turns against him'),
   D('1823', 'The Wellsburg church joins the Mahoning Association'),
   D('1824&ndash;26', 'Redstone disfellowships Brush Run and four more churches'),
   D('1827', 'Mahoning sends out Walter Scott'),
   D('Aug. 1830', 'Mahoning dissolves itself')],
  'Seven clicks. Redstone: Campbell calls it &ldquo;a conditional union with the Redstone Association during the fall of 1813&rdquo; (<i>MH</i> 1848, p. 344, in Richardson, <i>Memoirs</i> I). Mahoning dissolved at Austintown, Ohio, in August 1830, judging it had no scriptural standing.',
  size='clamp(22px,4vmin,50px)', gap='1.2vmin'))
A(QK('&ldquo;I and the church with which I am connected are in <b>full communion with the Mahoning Baptist Association, and through them with the whole Baptist society</b>.&rdquo;',
     CB + ', 1826, &ldquo;To an Independent Baptist,&rdquo; p. 200', 'He cared about the connection', 'cb3',
     'Campbell quoting his own earlier declaration, which &ldquo;An Independent Baptist&rdquo; had attacked as inconsistent.',
     'His defense (pp. 201&ndash;202): the only bond of union the paper ever advocated is the confession &ldquo;that Jesus is the Christ.&rdquo; He would be the inconsistent one, he says, &ldquo;If I had refused communion with the whole Baptist society.&rdquo;'))

# ---------- 3. THE CHRISTIAN BAPTIST ----------
A(C('The <i>Christian Baptist</i>', '1823&ndash;1830. Seven years of attack journalism against the clergy, creeds and &ldquo;the kingdom of the clergy.&rdquo;', '1823&ndash;1830'))
A(QK('&ldquo;Style no man on earth your Father: for he alone is your Father who is in heaven; and <b>all ye are brethren</b>. Assume not the title of Rabbi; for ye have only One Teacher: neither assume the title of Leader; for ye have only One Leader&mdash;the Messiah.&rdquo;',
     'Matthew 23:8&ndash;10, on the title page of the <i>Christian Baptist</i>', 'Its masthead', 'cb1',
     'Last week&rsquo;s list: no titles, no &ldquo;Reverend&rdquo;; the preacher is &ldquo;Brother.&rdquo; Here it is on the masthead, in Campbell&rsquo;s own rendering of Matthew 23.',
     'Also on the title page: &ldquo;Prove all things: hold fast that which is good,&rdquo; and Benson: &ldquo;May all Christians use this liberty of judging for themselves in matters of religion, and allow it to one another.&rdquo; (Read in the 1827 edition, reprinted 1955.)'))

# ---------- 4. THE ETERNAL PATTERN ----------
A('<section class="slide breath"><div class=eyebrow>The eternal pattern</div>'
  '<div class=litany style="gap:3vmin;max-width:86vw">'
  '<div class=no style="font-size:clamp(36px,7.2vmin,92px)">They want the fellowship.</div>'
  '<div class="no frag" style="font-size:clamp(36px,7.2vmin,92px);color:var(--gold)">They won&rsquo;t accept the fence.</div></div>'
  '<aside class=notes>One click. The Seceders, the Synod of Pittsburg, Redstone, and by 1827&ndash;30 the Baptists at large, whose associations expelled the &ldquo;Reformers.&rdquo; Every time: they reach for the widest fellowship there is, and refuse any body that makes a creed the test.</aside></section>')

# ---------- 5. THE PIVOT ----------
A(C('The pivot', 'January 1830. Campbell starts a new paper; by July he closes the old one.', '1830'))
A(QK('&ldquo;It shall have for its object the developement, and introduction of that political and religious order of society called <b>THE MILLENNIUM</b>, which will be the consummation of that ultimate amelioration of society proposed in the Christian Scriptures.&rdquo;',
     'Prospectus, ' + MH + ', vol. 1, no. 1 (dated 1829), p. 1', 'The <i>Millennial Harbinger</i>', 'mh1830',
     '&ldquo;developement&rdquo; is the original spelling.',
     'The rest of the Prospectus lists real work in the real world: the end of sectarianism, education, injustice in government, &ldquo;the treatment of African slaves, as preparatory to their emancipation.&rdquo;'))
A(LIST('The flagship', 'The <i>Millennial Harbinger</i>',
  ['Published for four decades, 1830&ndash;1870', 'Campbell editing to 1864; then W. K. Pendleton', 'The movement&rsquo;s most influential editorial voice', 'Read for generations after'],
  'Four clicks.'))
A(CARD('What do you notice<br>' + G('about the name?'),
  '&rarr; Besides the fact that <i>Millennial Harbinger</i> is the most badass name for a religious journal ever. Let them talk.', 'For discussion'))
A('<section class="slide breath"><div class=litany style="gap:2.4vmin;max-width:86vw">'
  '<div class="no" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Restoration Quarterly</i>.</div>'
  '<div class="no frag" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Primitivist Paper</i>.</div>'
  '<div class="no frag" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Old Ways Digest</i>.</div></div>'
  '<aside class=notes>Two clicks. It&rsquo;s not about the past at all.</aside></section>')
A(CARD('It&rsquo;s about<br>' + G('the future.'), 'From Cane Ridge to Brush Run&rsquo;s first Supper: they saw what was happening as a sign that the Spirit was on the move, that God&rsquo;s future could be glimpsed now, and that their job was to get on board.'))

# ---------- 6. HOW THEY SPOKE ABOUT THE FUTURE ----------
A(C('How they spoke<br>about the future', 'Not escape from the world: a world made new. And the church&rsquo;s unity first, so that the world may believe.'))
A(LIST('What was distinctive', 'Campbell&rsquo;s eschatology',
       ['<b>New creation,</b> not just heaven: this earth made new.',
        '<b>Brought by the gospel,</b> not the sword: the church&rsquo;s unity comes first, &ldquo;that the world may believe.&rdquo;',
        '<b>The church as its foretaste:</b> living God&rsquo;s future now.',
        '<b>The future as the test:</b> judge a doctrine by its effects, measured against what God&rsquo;s future promises.'],
       'Three marks, one per click; the next three sections take them in turn. (1) Not escape to heaven but a world made new (MH 1830, 1855). (2) How it comes: by the gospel, peacefully and gradually, with the church&rsquo;s unity as the prerequisite for the world&rsquo;s conversion (John 17, the D&amp;A, the <i>Christian System</i>). This is what made him postmillennial, and it is what put unity at the center. (3) So the church&rsquo;s life now (unity, conscience, the priesthood of all, the table) is the future in miniature. (4) And the future is the test: a doctrine is judged by its effects, set beside what the Millennium proposes (MH 1830, p. 7; on screen before &ldquo;Not legalism&rdquo;).'))
A(LIST('What was distinctive', 'Barton Stone&rsquo;s eschatology',
       ['<b>Breaking in now:</b> Cane Ridge and the <i>Last Will</i> as its dawn.',
        '<b>Christ comes first,</b> to judge: not a world gradually converted.',
        '<b>The church as an alternative government:</b> no voting, office or war.',
        '<b>Humble about the scheme:</b> &ldquo;Our wisdom is to be always ready.&rdquo;'],
       'Stone moved from revival hope (1801&ndash;04) to an explicit premillennialism (1832&ndash;33): Christ returns in person before the thousand years. In 1835 he mocked the Presbyterian notion that Bible, tract and temperance societies were the chain binding Satan. Yet the end&rsquo;s nearness was a summons: &ldquo;Let the unity of Christians be our polar star&rdquo; (1832). The last line is from 1834 (<i>Christian Messenger</i> 8, p. 148); in 1842 he said which system one holds &ldquo;is not absolutely necessary to our salvation.&rdquo;'))
A(QK('&ldquo;Let Christians shew by their peaceful, holy lives, <b>that his laws are sufficient to govern the whole world in peace and love</b>.&rdquo;',
     'Barton W. Stone, &ldquo;Reflections of Old Age,&rdquo; <i>Christian Messenger</i> 13, August 1843, p. 126', 'Stone, 1843', 'cm13',
     'Just before: Christ &ldquo;will shortly put them all down, and reign with his Saints on earth a thousand years&rdquo; (p. 125); so &ldquo;we must cease to support any other government on earth by our counsels, co-operation, and choice.&rdquo; The church shows a better government by living it.', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;<b>In doing this they were clearing away the rubbish from the foundation of God&rsquo;s government of the world</b>.&rdquo;',
     'Barton W. Stone, &ldquo;Reply to T. P. Ware,&rdquo; <i>Christian Messenger</i> 14, October 1844, p. 170', 'Stone, 1844', 'cm14',
     '&ldquo;Doing this&rdquo;: arguing against human creeds and laws for governing the church. A month before his death (November 9, 1844), Stone carries the <i>Last Will</i>&rsquo;s logic from the church to the state.', size='clamp(36px,7.6vmin,96px)'))
A(CARD('Same hope.<br>' + G('Opposite routes.'),
  'Campbell: the future comes through the gospel in history, and the church reforms the world. Stone: Christ breaks in, and the church stands apart from the world&rsquo;s powers to show a better one. Both: the church should already look like what is coming.'))
A(QK('&ldquo;We expect <b>no new Sun</b>, no new revelation of the Spirit, no other than the same gospel and the same religion, only that it shall be disinterred from the rubbish of the dark ages&hellip;&rdquo;',
     AC + ', &ldquo;Prefatory Remarks,&rdquo; ' + MH + ', January 1830, p. 5', 'Nothing new, only renewed', 'mh1830',
     'The first issue. The millennium is the same gospel, recovered.'))
A(QK('&ldquo;&hellip;our best political institutions we can part with <b>without a tear or a sigh, when Jesus reigns on earth</b>, and has placed a throne in every heart and built a temple in every family.&rdquo;',
     AC + ', Fourth of July oration, ' + MH + ', 1830, p. 306', 'Jesus reigns on earth', 'mh1830',
     'The same oration: &ldquo;Not by might, nor by sword, but by the Spirit of the Lord.&rdquo;'))
A(QK('&ldquo;The Bible begins with the generations of the heavens and the earth; but the christian revelation ends with the regenerations, or new creation of the heavens and the earth&hellip; <b>God recreates, regenerates, but annihilates nothing</b>; and, therefore, the present earth is not to be annihilated.&rdquo;',
     CS + ', p. 311', 'A new creation', 'cs',
     'Between the sentences: &ldquo;The bodies of the saints will be as homogeneous with the new earth and heavens, as their present bodies are with the present heavens and earth.&rdquo;'))
A(QK('&ldquo;&hellip;John saw the New Jerusalem, the holy city, coming down from God out of heaven, prepared as a bride for her husband, to locate in the new earth, <b>the everlasting home of man</b>; for the tabernacle of God is to be there forever.&rdquo;',
     AC + ', &ldquo;The Coming of the Lord&mdash;No. II,&rdquo; ' + MH + ', February 1841, p. 54', 'Coming down, not going up', 'mh1841',
     'His 26-part series against the Millerites: the dead raised, the living changed, judgment, &ldquo;New heavens and a new earth shall be created.&rdquo;'))
A(QK('&ldquo;For man he made this planet, and all the tenantry thereof. And for him he has promised to <b>create a new earth out of this earth</b>, and a new heaven out of this heaven&hellip;&rdquo;',
     AC + ', ' + MH + ', 1855, p. 146', 'This earth, made new', 'mh1855',
     '&rarr; Back to the quiz song. &ldquo;This world is not my home&rdquo;? For Campbell, this world is exactly the home God is making new.'))
A(QK('&ldquo;The notion, so very prevalent, that the Christian&rsquo;s future home lies away in some immeasurably distant region, is <b>only a vulgar error</b>&hellip; God built this earth for man, and he does not intend to be defeated in his purpose.&rdquo;',
     'Moses E. Lard, &ldquo;A Theory of the Millennium,&rdquo; <i>Lard&rsquo;s Quarterly</i> 2, October 1864, p. 21', 'Not just Campbell', 'lq1865',
     'Next line: &ldquo;The earth in its renewed form will be man&rsquo;s everlasting dwelling-place.&rdquo; Lard expected Christ to return before the millennium; on the renewed earth he agrees with Campbell.'))
A(QK('&ldquo;Beat your swords into ploughshares, your spears into pruning-hooks; <b>convert your war-ships into missionary packets</b>, your arsenals and munitions of war into Bibles, school-books, and all the appliances of literature, science and art&hellip;&rdquo;',
     AC + ', &ldquo;Address on War,&rdquo; Wheeling, 1848, <i>Popular Lectures</i>, p. 364', 'Peace', 'pla',
     'Stone, 1842: &ldquo;Nothing appears so repugnant to the kingdom of heaven as war&hellip; Lord! hasten the happy day!&rdquo; The 1830 Fourth of July hymn: &ldquo;To ploughshares men shall beat their swords!&rdquo;'))
A(C('John 17', '&ldquo;That they all may be one&hellip; that the world may believe.&rdquo; The church&rsquo;s unity comes first.', 'The prayer they lived by'))
A(QK('&ldquo;&hellip;that they all may be one; as thou, Father, art in me and I in thee, that they also may be one in us; <b>that the world may believe that thou hast sent me</b>.&rdquo;',
     DA + ', quoting John 17:21', 'Thomas Campbell, 1809', 'dna',
     'And: &ldquo;This gracious unity and unanimity in Jesus would afford the best external evidence of their union with him.&rdquo;'))
A(QK('&ldquo;I pray&mdash;for those who shall believe on me through their teaching, that all may be one&hellip; <b>that the world may believe that thou hast sent me</b>&hellip;&rdquo; Thus Messiah prayed.',
     CS + ', &ldquo;Foundation of Christian Union,&rdquo; p. 110', 'Alexander&rsquo;s motto', 'cs',
     'Campbell sets John 17:20&ndash;23 in his own translation at the head of the essay, then begins: &ldquo;Thus Messiah prayed.&rdquo;'))
A(QK('&ldquo;1st. <b>Nothing is essential to the conversion of the world but the union and co-operation of christians.</b> 2nd. Nothing is essential to the union of christians but the apostles teaching or testimony.&rdquo;',
     CS + ', p. 112', 'The two propositions', 'cs',
     'Next page: &ldquo;to suppose that all christians will form one communion in that happy age of the world, and not before it, is to suppose a moral effect without a cause.&rdquo;'))
A(QK('&ldquo;&hellip;the union of christians, and the destruction of sects, are <b>indispensable prerequisites</b> to the subjection of the world to the government of Jesus&hellip; While the Army of the Faith is enlisted under so many different generals&hellip; they may make havoc upon one another, but it is impossible they can convert the world.&rdquo;',
     AC + ', &ldquo;Millennium&mdash;No. I,&rdquo; ' + MH + ', February 1830, p. 55', 'Unity first', 'mh1830', 'The first of his two essays titled &ldquo;Millennium.&rdquo;'))
A(QK('&ldquo;Let the unity of Christians be our <b>polar star</b>&hellip; that the world may believe, and be saved&hellip; But let that man, who opposes Christian union, remember, that he opposes the prayer of Jesus, and the salvation of the world.&rdquo;',
     CM + ' 6, 1832, p. 266', 'Stone, 1832', 'cm6', 'The year of the union with the Campbell reformers.'))
A(QK('&ldquo;Some of you say it will be effected in the millenium. <b>No, it must be effected before</b>, that the world may be brought to believe and be saved.&rdquo;',
     CM + ' 13, May 1843, p. 8', 'Stone, 1843', 'cm13',
     'By 1843 Stone expected Christ to return first and reign. He still would not postpone unity to the coming age.'))

# ---------- 7. THE COMING CHURCH: UNITY, CONSCIENCE, PRIESTHOOD ----------
A(C('The church to come', 'Unity, freedom of conscience and the priesthood of all believers were the nature of the millennial church, so they were the church&rsquo;s work now.'))
A(QK('&ldquo;&lsquo;And the kingdom and dominion&hellip; shall be given to the people of the saints of the Most High&hellip;&rsquo; <b>But this can not be in their present broken and divided state</b>&hellip;&rdquo;',
     DA, 'Thomas Campbell, 1809', 'dna', 'Daniel 7:27, then the turn.'))
A(QK('&ldquo;Are we not all praying for that happy event, when there shall be but one fold, as there is but one chief Shepherd? <b>What! shall we pray for a thing, and not strive to obtain it!!</b>&rdquo;',
     DA, 'Thomas Campbell, 1809', 'dna', 'The two exclamation points are his.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;When then we see a people making new divisions and keeping up old ones, while praying for the Millennium or the triumph of love and harmony, <b>we as naturally suspect that they are any thing but in earnest</b>.&rdquo;',
     AC + ', ' + CB + ' 5, 1828, p. 263', 'Alexander, 1828', 'cb5', 'He goes on: like &ldquo;a nation preparing for war, and praying for peace.&rdquo;'))
A(QK('&ldquo;We do not ask them to give up their opinions&mdash;<b>We ask them only not to impose them upon others</b>.&rdquo;',
     AC + ', &ldquo;Millennium&mdash;No. II,&rdquo; ' + MH + ', April 1830, p. 145', 'How the sects will cease', 'mh1830',
     'His answer to &ldquo;WILL sects ever cease?&hellip; How then shall it be introduced?&rdquo; Same essay: &ldquo;The faith is public property: opinions are, and always have been, private property.&rdquo; (Micah: here, or in a side path on gradualism.)', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;&hellip;who has made all the citizens of his kingdom, not citizens only, but <b>citizen kings and priests to God</b>.&rdquo;',
     AC + ', Fourth of July oration, ' + MH + ', 1830, p. 309', 'The priesthood', 'mh1830', 'Last week&rsquo;s theme, in the kingdom to come.', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;Being a royal priesthood, all children of a King, they have a right to meet in his name to break the loaf of blessing, to drink the cup of blessing, <b>without the intervention of a mediator, priest, or prophet, consecrated by human hands</b>.&rdquo;',
     AC + ', ' + MH + ', August 1830, p. 368', 'At the table', 'mh1830', 'Just before: &ldquo;they are all made sons and daughters, kings and priests to God.&rdquo; The ideal voiced; not yet extended to women.'))
A(QK('&ldquo;&hellip;the emancipation of all the world from faith in, and obedience to, <b>any set of men, titled and enthroned as they may be</b>, as the representatives or successors of the apostles of Christ.&rdquo;',
     AC + ', &ldquo;The Everlasting Gospel&rdquo; No. 3, ' + MH + ', May 1833, p. 226', 'What the coming judgment brings', 'mh1833', 'The end of clerical power is part of what is coming.'))
A(QK('&ldquo;In detecting the false gospels, nothing will aid us so much as an examination of their tendencies, and <b>a comparison of their effects with what the Millennium proposes</b>. The gospel of no sect can convert the world.&rdquo;',
     AC + ', Prefatory Remarks, ' + MH + ' 1, no. 1, 1830, p. 7', 'The future as the test', 'mh1830',
     'The first issue. Not &ldquo;does it match the pattern?&rdquo; but &ldquo;where does it lead?&rdquo; Does it produce the united, converted world God&rsquo;s future promises? A sectarian gospel fails that test by its nature.'))
A(CARD('Not legalism.<br>' + G('Embodying the future God will build.'),
  'Not only that they believed these things were right: their responsibility was to embrace and embody what God was going to build. The name <i>Millennial Harbinger</i> is their confidence in that future.'))
A(C('The other<br>millennial harbinger', 'The Lord&rsquo;s Supper.'))
A(QK('&ldquo;&hellip;in assembling there on that occasion, they furnished <b>an emblem of the millennial state of the Church</b>, nay, an emblem of the heavenly state, when men of different nations, and known by different names, should sit down together in the kingdom of God.&rdquo;',
     'Robert Richardson, <i>Memoirs of Alexander Campbell</i>, vol. 1, p. 369', 'Brush Run&rsquo;s first Supper, May 5, 1811', 'rich1',
     'Richardson&rsquo;s report of Alexander&rsquo;s sermon, not Campbell&rsquo;s own words.'))
A(QK('&ldquo;To see even a few scores of intelligent christians&hellip; <b>meeting around one and the same Lord&rsquo;s table</b>, and uniting in the praises and adorations of one and the same common Lord and Saviour, imparts to us a joy which we are unable to express.&rdquo;',
     AC + ', &ldquo;Prefatory Remarks,&rdquo; ' + MH + ', January 1830, p. 5', 'The first issue', 'mh1830',
     'Next: &ldquo;What we should feel, or how we should feel, among myriads of such, is not for us now to conjecture.&rdquo;'))
A(QK('&ldquo;The Lord&rsquo;s day not only commemorates the resurrection of Jesus, but <b>anticipates the morning of the resurrection</b> in which we shall enter into the rest which remains for the people of God.&rdquo;',
     AC + ', ' + MH + ', January 1834, p. 37', 'Easter every Sunday', 'mh1834', '&rarr; Back to the quiz: when do we celebrate Easter?'))

# ---------- 8. THE FUTURE ITSELF ----------
A(CARD('Campbell was postmillennial.<br>' + G('Most of us are not.'), 'We might get hung up here. A distraction: he went back and forth in his own paper.'))
A(LIST('In his own paper', 'He went back and forth',
  [D('1831', '&ldquo;a deepening gloom overspreads our ecclesiastical heavens&rdquo;'),
   D('1833', '&ldquo;with what caution we have spoken on the prophecies and millennial matters&rdquo;'),
   D('1840', '&ldquo;We had more pressing and important matter on hand&rdquo;'),
   D('1853', '&ldquo;the millennium&rdquo; among the opinions that &ldquo;terminate in schism&rdquo;'),
   D('1856', '&ldquo;Modesty sits most gracefully on&hellip; interpreters of prophecy&rdquo;')],
  'Five clicks. <i>MH</i> 1831, p. 168; 1833, p. 49; 1840, p. 562 (&ldquo;we have not committed ourselves to any of the theories of the present day on the nature and coming of the Millennium&rdquo;); 1853, p. 175; 1856, p. 698. He also printed the other views: the premillennialist &ldquo;Daniel&rdquo; in his first volume; McCorkle&rsquo;s pessimism in 1833; Stone, who expected Christ to come first and reign.',
  size='clamp(22px,4.1vmin,52px)'))
A(QK('&ldquo;Alexander Campbell was a postmillennialist. James A. Harding was a premillennialist. Walter Scott changed his mind several times. <b>David Lipscomb was uncertain</b>.&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'John Mark Hicks, 2015', 'hicks',
     'Hicks teaches theology at Lipscomb University; with Bobby Valentine he wrote <i>Kingdom Come: Embracing the Spiritual Legacy of David Lipscomb and James A. Harding</i> (2006). Harding co-founded the Nashville Bible School (now Lipscomb University) with Lipscomb.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;However, these all agreed that the most important aspect of the Christ&rsquo;s second coming was <b>the regeneration not only of the soul, but the body and the whole cosmos</b>.&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'What they agreed on', 'hicks',
     'He goes on: God will refine the cosmos by fire and renew it into a &ldquo;new heaven and new earth,&rdquo; as he will raise our bodies. Campbell: &ldquo;God recreates, regenerates, but annihilates nothing&rdquo; (<i>Christian System</i>, p. 257).', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;&hellip;it was <b>the dominant perspective among churches of Christ in the late nineteenth century</b>&hellip;&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'A renewed earth: our own tradition', 'hicks',
     'Just before: &ldquo;Many are surprised to learn this about our forbearers in the faith because they associate a renewed, material earth with fringe groups and strange ideas.&rdquo; He continues: &ldquo;particularly as articulated by David Lipscomb and James A. Harding.&rdquo; Lost in the twentieth century (Hicks, &ldquo;From Lipscomb to Wallace,&rdquo; 2012). Compare the opening quiz: &ldquo;This world is not my home.&rdquo;', size='clamp(40px,8.4vmin,108px)'))
A(CARD('Not any particular eschatology.<br>' + G('The future itself.'),
  'Pre-, post- or a-millennial, God&rsquo;s future had deep meaning. The commitment to God&rsquo;s future is the leading emphasis, the motivating impulse, at a deeper layer than any restorationist impulse.'))
# ---- side path: other voices on the future (off "Not any particular eschatology") ----
A('<section class="slide breath"><div class=eyebrow>Side path &middot; other voices on the future</div><h2 style="max-width:none">Other voices on the future</h2><aside class=notes>Off &ldquo;Not any particular eschatology.&rdquo; Different views of the end, one future.</aside></section>')
A(QK('&ldquo;We confidently thought that the Millennium was just at hand&hellip; <b>In this we were wholly mistaken</b>.&rdquo;', 'Robert Marshall and John Thompson, <i>A Brief Historical Account</i> (1811), in <i>Biography of Elder David Purviance</i> (1940 reprint), p. 255', 'Two signers of the Last Will', 'purv', 'Signers of the <i>Last Will</i> (1804), after Cane Ridge.'))
A(QK('&ldquo;The Jews were very wrong in their ideas of Messiah&rsquo;s first coming; so may we be of his second.&mdash;<b>Our wisdom is to be always ready</b>.&rdquo;', CM + ' 8, 1834, p. 148', 'Stone, 1834', 'cm8', 'Stone held that Christ would come first and reign; he never made it a test.'))
A(QK('&ldquo;We believe he came once, and we are pardoned; <b>we hope he will come again, and we shall be glorified!</b>&rdquo;', 'Walter Scott, <i>The Evangelist</i>, October 6, 1834, p. 218', 'Walter Scott', 'ev1834', 'Scott changed his mind twice about the millennium; the hope stayed.'))
A(QK('&ldquo;&hellip;which even of our great men so urges <b>the hope of the gospel</b> upon the brethren as to purify them by it?&rdquo;', 'Walter Scott, <i>The Evangelist</i>, May 1842, p. 98', 'Scott, 1842', 'ev1834',
     'Just before: &ldquo;We have among our preachers&hellip; persons who might be styled faith, repentance and baptism preachers.&rdquo; The last step of Scott&rsquo;s own gospel was eternal life at Christ&rsquo;s return; hope, he said, is what purifies.', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;&hellip;to mingle and mould them into <b>one universal brotherhood</b>, to break in pieces and destroy all earthly kingdoms and dominions, and fill the whole earth and stand forever.&rdquo;', 'David Lipscomb, <i>Civil Government</i> (1889), p. 12', 'David Lipscomb', 'lipcg',
     'The church, God&rsquo;s kingdom, displaces the human governments by spreading, not by force; so Christians do not fight, vote or hold office. The Civil War turned him (preface). Stone&rsquo;s line in the next generation; more in Chapter 9.'))
A(QK('&ldquo;&hellip;the kingdom of God as the ark of safety will ride the sea of fire, <b>bearing all committed to its keeping into the new heavens and to the new earth</b> wherein dwelleth righteousness.&rdquo;', 'David Lipscomb, <i>Civil Government</i> (1889), p. 85', 'A new earth', 'lipcg',
     'What burns is &ldquo;the institutions that have grown up under rule of the devil,&rdquo; not God&rsquo;s works. Renewal on earth, not escape.'))
A(QK('&ldquo;&hellip;the earth is God&rsquo;s nursery, his training grounds&hellip; Then God will take up his abode himself with his great family <b>upon this new, this renovated and purified earth</b>.&rdquo;',
     'James A. Harding, &ldquo;For What Are We Here?&rdquo; <i>The Way</i> 5, no. 33, December 3, 1903, p. 1041', 'James A. Harding', 'way5',
     'Lipscomb&rsquo;s partner at the Nashville Bible School; premillennial; refused to vote. The earth is for the children&rsquo;s training &ldquo;until the end of the Messianic age has come; then it is to be purified a second time&hellip; in a sea of fire.&rdquo; The faithful are &ldquo;to be members of the ruling family of the universe.&rdquo;'))
A(QK('&ldquo;Personally I believe in the pre-millennial coming of our Lord&hellip; but do I think them any less Christian&hellip;? <b>Certainly not</b>.&rdquo;', 'Peter Ainslie, <i>The Message of the Disciples for the Union of the Church</i> (1913)', 'Peter Ainslie, 1913', 'ainslie', 'Of those who disagree with him.'))
A(QK('&ldquo;In this great gathering I see <b>a prophecy of that which is to be</b> when all of God&rsquo;s people, of every race and clime, shall sit down together.&rdquo;', 'L. G. Batman, Centennial Convention, Pittsburgh, 1909', 'The Centennial, 1909', 'cent', 'Shadow: the 1909 table was served by six hundred men, and the same convention spoke of Black Americans in degrading terms.'))
A(QK('&ldquo;That place that God has intended should be <b>a type of heaven</b>, men, by covetousness, hatred, strife, adultery and backbiting, have made the pit of hell.&rdquo;', 'S. R. Cassius, &ldquo;Negro Evangelization,&rdquo; 1897, p. 203', 'S. R. Cassius, 1897', 'cassius', 'Cassius, a Black evangelist in Oklahoma: &ldquo;There are church-members that would not eat at the table with me&rdquo; (p. 204).'))
A(LIST('Where they differed', 'Two questions',
       ['<b>How does the future come?</b> Through the gospel in history, or by Christ breaking in.',
        '<b>How does the church face the world?</b> Reforming it, or showing it an alternative.'],
       'Campbell (and Scott after 1844): the first answer to both. Stone, Scott in the 1830s, Lipscomb: the second.'))
A(CARD('Different views of the end.<br>' + G('One future.'), 'Neither question touched the shared claim: the church should already look like what is coming. &rarr; Back to the spine.'))
A(QK('&ldquo;&hellip;all the Millennium we could scripturally expect was not merely the restoration of the Jerusalem church in all its moral and religious characters, but <b>the extension of it through all nations and languages for one thousand years</b>.&rdquo;',
     AC + ', &ldquo;Millennial Character of the Harbinger,&rdquo; ' + MH + ', December 1840, p. 561', 'Restoration served the future', 'mh1840',
     'Before it: &ldquo;When we put to sea under this banner we had the port of Primitive Christianity&hellip; in our eye.&rdquo; And 1825: &ldquo;Just in so far as the ancient order of things&hellip; is restored, just so far has the Millennium commenced&rdquo; (<i>CB</i> 2, p. 136).'))

# ---------- 9. N. T. WRIGHT ----------
A(C('N. T. Wright', 'Bishop of Durham (2003&ndash;2010); New Testament scholar at St Andrews and Oxford. Read across the Churches of Christ, and here at Otter Creek.', 'Two centuries later'))
A(QK('&ldquo;Most of the Bible does not consist of rules and regulations&mdash;lists of commands to be obeyed. <b>Nor does it consist of creeds</b>&mdash;lists of things to be believed.&rdquo;',
     NTW + ', &ldquo;How Can the Bible Be Authoritative?&rdquo; (1989), <i>Vox Evangelica</i> 21 (1991), p. 9', 'Scripture as story', 'hcba',
     'Campbell: &ldquo;The Bible is a book of facts, not of opinions, theories, abstract generalities, nor of verbal definitions&rdquo; (<i>CS</i> p. 19), and &ldquo;Fact means something done&rdquo; (p. 115).'))
A(QK('&ldquo;Story authority, as Jesus knew only too well, is the authority that really works. Throw a rule book at people&rsquo;s head, or offer them a list of doctrines, and they can duck or avoid it, or simply disagree and go away. <b>Tell them a story, though, and you invite them to come into a different world</b>&hellip;&rdquo;',
     NTW + ', &ldquo;How Can the Bible Be Authoritative?&rdquo;, p. 22', 'Story authority', 'hcba', 'Checked in the lecture PDF (biblicalstudies.org.uk).'))
A(QK('&ldquo;The Bible, in fact, is not simply an authoritative description of a saving plan, as though it were just an aerial photograph of a particular piece of landscape. <b>It is part of the saving plan itself</b>.&rdquo;',
     NTW + ', <i>Simply Christian</i> (2006), pp. 185&ndash;186', 'Part of the plan', 'none',
     'From Micah&rsquo;s ebook (read 2026-10-27); recheck before class. Also his &ldquo;the authority of the triune God, exercised somehow through scripture&rdquo; (<i>Scripture and the Authority of God</i>; page to confirm) and &ldquo;We need to go back to the first century&rdquo; (<i>The Vision of Ephesians</i>, &sect;1).'))
A(QK('&ldquo;And that is the task of the whole church. <b>Need I say, not merely of the professional caste within it</b>&hellip;&rdquo;',
     NTW + ', &ldquo;How Can the Bible Be Authoritative?&rdquo;, p. 27', 'Who tells the story', 'hcba', 'The priesthood of all believers, in Wright&rsquo;s words.', size='clamp(36px,7.4vmin,94px)'))
A(QK('&ldquo;At no point do the resurrection narratives in the four Gospels say, &lsquo;Jesus has been raised, therefore we are all going to heaven.&rsquo; It says that <b>Christ is coming here</b>, to join together the heavens and the Earth in an act of new creation.&rdquo;',
     NTW + ', interview, <i>TIME</i>, February 2008', 'New creation', 'none',
     'Read in full on TIME&rsquo;s archive page by a research helper (2026-11-10); recheck before class. Beside Campbell: &ldquo;God recreates, regenerates, but annihilates nothing&rdquo;; &ldquo;a new earth out of this earth.&rdquo; And the quiz song.'))
A(QK('&ldquo;&hellip;to think of the vocation of the church as the call to live as <b>the small working model of new creation</b>.&rdquo;',
     NTW + ', <i>The Vision of Ephesians</i> (2025), &sect;1', 'The church as microcosm', 'none',
     'From Micah&rsquo;s ebook (read 2026-10-27). Beside Brush Run&rsquo;s &ldquo;emblem of the millennial state of the Church.&rdquo; Also &ldquo;Ephesians is all about the church, and especially about its unity&rdquo; (<i>God&rsquo;s Homecoming</i>, p. 260).', size='clamp(36px,7.4vmin,94px)'))
A(QK('&ldquo;The bread and the wine can be seen as true gifts coming forward to us from God&rsquo;s future&hellip; We are presented, close up and personally, with <b>new creation that we can eat and drink</b>.&rdquo;',
     NTW + ', <i>God&rsquo;s Homecoming</i> (2025), p. 252', 'At the table', 'none',
     'From Micah&rsquo;s ebook (read 2026-10-27). Brush Run&rsquo;s first Supper; the Lord&rsquo;s day that anticipates the resurrection.'))
A(CARD('Two centuries apart:<br>' + G('the same impulse.'),
  'Scripture as the story of what God has done; a future that renews this world; a church that lives it now, above all in its unity.'))

# ---------- CLOSE ----------
DISCUSS = re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>Backup prompts (off the slide): Where do you glimpse God&rsquo;s future in this church? What would change if we believed our unity was the world&rsquo;s best evidence? Which of our practices are ways of living the future now?</aside>',
                 w3b.pick('&#9670; for discussion', 0), flags=re.S).replace('&#9670; for discussion', '&#9670; for discussion &middot; Chapter 7', 1)
for _k in range(1, len(IDEAS) + 1): A(IDEA(_k))
A(IDEASUM('All six at once, before the discussion: Micah&rsquo;s three and the three added on 2026-11-10.'))
A(DISCUSS)
A(re.sub(r'<aside class=notes>.*?</aside>', '<aside class=notes>The site: stone-campbell.micahredding.com. Today&rsquo;s sources: the <i>Millennial Harbinger</i>, the <i>Christian Baptist</i>, <i>The Christian System</i>, Stone&rsquo;s <i>Christian Messenger</i>.</aside>',
          w3b.pick('stone-campbell.micahredding.com'), flags=re.S).replace('<h2 class=url>stone-campbell.micahredding.com</h2>',
          '<h2 class=url style="letter-spacing:.02em"><span style="color:var(--gold)">stone-campbell</span><span style="color:#ede4d3;opacity:.75">.micahredding.com</span></h2>', 1))
A('<section class="slide"><h2>Next week: the handshake at Lexington.</h2>'
  '<div class="sub frag">1832: Stone&rsquo;s Christians and Campbell&rsquo;s reformers, who disagreed on much, unite on the Bible.</div>'
  '<aside class=notes>Chapter 8, the Stone-Campbell merger.</aside></section>')
A(BLACK)

