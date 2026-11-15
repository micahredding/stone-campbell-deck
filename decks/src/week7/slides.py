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

import base64 as _b64
def MAST(img, eyebrow, cite, note):   # a scanned masthead, full width, with its source under it
    _src = 'data:image/jpeg;base64,' + _b64.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', img), 'rb').read()).decode()
    return ('<section class="slide"><div class=eyebrow>%s</div>'
            '<img src="%s" alt="" style="width:min(92vw,150vh);height:auto;background:#fff;border:1px solid rgba(201,162,74,.55);box-shadow:0 6px 24px rgba(0,0,0,.6)">'
            '<div class=cite style="margin-top:2vmin">%s</div><aside class=notes>%s</aside></section>' % (eyebrow, _src, cite, note))

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
  '<aside class=notes>The answer (not on the slide): &ldquo;&hellip;somewhere beyond the blue.&rdquo; Extra points if anyone sings the next line (&ldquo;The angels beckon me from heaven&rsquo;s open door&rdquo;). Let them sing. Don&rsquo;t comment yet: we come back to this song when we get to &ldquo;a new earth out of this earth.&rdquo;</aside></section>')
A('<section class="slide"><div class=eyebrow>Our Wild Democracy &middot; Chapter 7</div>'
  '<h1>Living into<br>God&rsquo;s Future</h1><div class=table-line></div>'
  '<div class=sub>The <i>Millennial Harbinger</i> &middot; 1830&ndash;1870</div>'
  '<aside class=notes>Chapter 7. Last week: Brush Run ordains Alexander by the choice of the people. This morning: what they were reaching for.</aside></section>')

# ---------- 1. RECAP (Micah's plan, 2026-11-14: recap; Alexander becomes a Baptist; Baptist communion;
# the Christian Baptist's purpose; Baptist excommunication; a tangent, backward and forward; the pivot) ----------
A(LIST('Where we are', 'From Ireland to Brush Run',
  [D('1808', 'Ireland: the family sets sail to join Thomas in America'), D('1809', 'Scotland: shipwrecked off Islay; a winter in Glasgow'),
   D('1809', 'The family reunited in Pennsylvania; the <i>Declaration and Address</i>'),
   D('1810', 'The Synod of Pittsburg refuses them'), D('May 1811', 'Brush Run constituted; the first Supper'), D('Jan. 1812', 'Alexander ordained by the choice of the people')],
  'Six clicks. One breath each. The ordination was last week.'))

# ---------- 2. ALEXANDER BECOMES A BAPTIST ----------
A(LIST('Among the Baptists', 'Alexander becomes a Baptist',
  [D('March 1812', 'A first child, Jane: the question of infant baptism'),
   D('June 1812', 'Alexander, his wife, his parents and others immersed'),
   D('1812&ndash;13', 'Baptist preachers press Brush Run to join them'),
   D('Fall 1813', 'Brush Run joins the Redstone Baptist Association on their own terms'),
   D('July 1823', 'A Baptist paper: the <i>Christian Baptist</i> begins'),
   D('1824', 'The Wellsburg Church joins the Mahoning Baptist Association'),
   D('1827', 'The Mahoning Baptist Association sends out Walter Scott as its evangelist')],
  'Seven clicks. Jane was born March 13, 1812; &ldquo;soon after this event, a considerable change took place in his views in regard to baptism&rdquo; (Richardson, <i>Memoirs</i> I). Their terms were written: no creed. Campbell calls it &ldquo;a conditional union with the Redstone Association during the fall of 1813&rdquo; (<i>MH</i> 1848, p. 344, in Richardson, <i>Memoirs</i> I). The first issue is dated Buffaloe, July 4, 1823: he edited it as a Baptist, for Baptists. Scott: sent out by Mahoning in 1827, he gained more than 2,000 additions on the Western Reserve in two years (<i>Encyclopedia</i>, &ldquo;Scott, Walter&rdquo;).',
  size='clamp(24px,4.4vmin,56px)', gap='1.6vmin'))

# ---------- 3. BAPTIST COMMUNION ----------
A(QK('&ldquo;I and the church with which I am connected are in <b>full communion with the Mahoning Baptist Association, and through them with the whole Baptist society</b>.&rdquo;',
     CB + ', 1826, &ldquo;To an Independent Baptist,&rdquo; p. 200', 'Baptist communion', 'cb3',
     'Campbell quoting his own earlier declaration, which &ldquo;An Independent Baptist&rdquo; had attacked as inconsistent.',
     'His defense (pp. 201&ndash;202): the only bond of union the paper ever advocated is the confession &ldquo;that Jesus is the Christ.&rdquo; He would be the inconsistent one, he says, &ldquo;If I had refused communion with the whole Baptist society.&rdquo;'))

# ---------- 4. THE CHRISTIAN BAPTIST: PURPOSE AND AIM ----------
A(C('The <i>Christian Baptist</i>', '1823&ndash;1830. Seven years of attack journalism against the clergy, creeds and &ldquo;the kingdom of the clergy.&rdquo;', '1823&ndash;1830'))
A(MAST('christian_baptist_masthead_1825.jpg', 'Its masthead', 'The <i>Christian Baptist</i>, vol. 3, no. 1, August 1, 1825 (Internet Archive scan)',
  'Matthew 23:8&ndash;10, in Campbell&rsquo;s rendering: &ldquo;Style no man on earth your Father: for he alone is your Father who is in heaven; and all ye are brethren. Assume not the title of Rabbi; for ye have only One Teacher; neither assume the title of Leader; for ye have only One Leader&mdash;the Messiah.&rdquo; ' + 'Also on the title page: &ldquo;Prove all things: hold fast that which is good,&rdquo; and Benson: &ldquo;May all Christians use this liberty of judging for themselves in matters of religion, and allow it to one another.&rdquo; (Read in the 1827 edition, reprinted 1955.)'))

# ---------- 5. BAPTIST EXCOMMUNICATION ----------
A(LIST('Out of the Baptists', 'Baptist excommunication',
  [D('1823', 'Redstone moves to put him out; he leaves first, to a new church at Wellsburg'),
   D('1824', 'Wellsburg is received into the Mahoning Association'),
   D('1824&ndash;26', 'Redstone disfellowships Brush Run and four more churches'),
   D('1829', 'The Beaver Anathema'),
   D('1829&ndash;30', 'Baptist associations follow, expelling the &ldquo;Reformers&rdquo;'),
   D('Aug. 1830', 'Mahoning dissolves itself')],
  'Six clicks. Redstone had turned against him after his &ldquo;Sermon on the Law&rdquo; (1816). Wellsburg (Richardson, <i>Memoirs</i> II, pp. 68&ndash;69, 100): in August 1823 Campbell learned that his opponents in Redstone had packed the next meeting to expel him. With his debate with McCalla coming, he &ldquo;thought it best to evade the denominational discredit.&rdquo; Brush Run dismissed him and some thirty members to form a church at Wellsburg, &ldquo;the second church of the Reformation&rdquo;; he attended Redstone &ldquo;as a spectator,&rdquo; no longer a member. His own memory of the moment: &ldquo;Never did hunters, on seeing the game unexpectedly escape from their toils at the moment when its capture was sure, glare upon each other a more mortifying disappointment&rdquo; (&ldquo;Anecdotes, Incidents, and Facts,&rdquo; <i>MH</i> 1848, p. 556). In September 1824 Mahoning received Wellsburg on his written statement of belief, not a creed. They did not leave the Baptists; the Baptists put them out, association by association (Dover, Virginia, 1830, among others). Mahoning, the friendly one, dissolved at Austintown, Ohio, judging it had no scriptural standing.',
  size='clamp(24px,4.4vmin,56px)', gap='1.6vmin'))

A(QK('&ldquo;<b>Who gave to the Beaver Association the right to anathematize the Mahoning Association?</b> Has she a divine authority to mount the tribunal of judgment and to condemn the faith of another Association?&rdquo;',
     AC + ', &ldquo;The Beaver Anathema,&rdquo; ' + CB + ' 7 (1829&ndash;30), p. 198', 'The Beaver Anathema, 1829', 'cb7',
     'The Beaver Association, a small Pennsylvania body joined by fragments of Western Reserve churches that refused the Reformation, circulated an anathema against Mahoning and Campbell as &ldquo;disbelieving and denying many of the doctrines of the Holy Scripture&rdquo; (as quoted by Richardson, <i>Memoirs</i> II, pp. 322&ndash;323). Baptist papers reprinted it; the Franklin Association (Kentucky) and the Appomattox Association (Virginia) took it up; Richardson: it &ldquo;induced the Baptists almost everywhere to separate the Reformers from their communion.&rdquo;',
     'Campbell&rsquo;s piece opens: &ldquo;There is nothing falling into less repute than bulls of excommunication and clerical denunciations.&rdquo;'))

# ---------- 6. A TANGENT: BACKWARD AND FORWARD ----------
A(R.ASSOC_SUMMARY.replace('<div class=eyebrow>From the Evangelical Society on</div>', '<div class=eyebrow>A tangent &middot; backward and forward</div>', 1)
   .replace('<h2 style="max-width:none">Joined, refused, dissolved</h2>', '<h2 style="max-width:none">They kept trying to join</h2>', 1))
for _x in R.associations(): A(_x)   # side path: the whole timeline, off the tangent
# the eternal pattern (Micah, 2026-11-14: right after the tangent's timeline)
A('<section class="slide breath"><div class=eyebrow>The eternal pattern</div>'
  '<div class=litany style="gap:3vmin;max-width:86vw">'
  '<div class=no style="font-size:clamp(36px,7.2vmin,92px)">They want the fellowship.</div>'
  '<div class="no frag" style="font-size:clamp(36px,7.2vmin,92px);color:var(--gold)">They won&rsquo;t accept the fence.</div></div>'
  '<aside class=notes>One click. The Seceders, the Synod of Pittsburg, Redstone, and by 1827&ndash;30 the Baptists at large, whose associations expelled the &ldquo;Reformers.&rdquo; Every time: they reach for the widest fellowship there is, and refuse any body that makes a creed the test.</aside></section>')

A(QK('&ldquo;I confess I was alarmed at the impassioned and hasty manner in which the association was, in a few minutes, dissolved&hellip; <b>the Regular Baptist Mahoning Association died of a moral apoplexy, in less than a quarter of an hour</b>.&rdquo;',
     AC + ', &ldquo;Church Organization&mdash;No. IV,&rdquo; ' + MH + ', May 1849, p. 272', 'Mahoning, remembered', 'mh1849',
     'He remembers it as 1828; it was August 1830, at Austintown. Between the two lines: &ldquo;Counsel and caution, argument and remonstrance were wholly in vain&hellip; that remonstrance was quashed by the previous question.&rdquo; Then: &ldquo;Reformation and annihilation are not with me now, as formerly, convertible or identical terms&rdquo; (read in the page scan; the OCR garbles &ldquo;as formerly&rdquo;). He admits he once treated them as the same. Richardson: at Austintown he &ldquo;was in favor of continuing the Association, or something like it&rdquo; (<i>Memoirs</i> II, p. 328). Even after the Baptists put them out, he wanted the larger connection.'))
A(QK('&ldquo;<b>Reformation and annihilation are not with me now, as formerly, convertible or identical terms.</b>&rdquo;',
     AC + ', &ldquo;Church Organization&mdash;No. IV,&rdquo; ' + MH + ', May 1849, p. 272', 'A confession', 'mh1849',
     'Read in the page scan (the OCR garbles &ldquo;as formerly&rdquo;). &ldquo;Formerly&rdquo; is most likely the <i>Christian Baptist</i> years (1823&ndash;30): in the previous essay he speaks of the &ldquo;appendages, against which we remonstrated twenty-five years ago&rdquo; (No. III, <i>MH</i> 1849, p. 271), and Mahoning&rsquo;s dissolution in 1830 is where that zeal ended. He does not name the years himself. Next sentence: &ldquo;We want occasional, if not stated, deliberative meetings on questions of expediency in adaptation to the ever changing fortune and character of society.&rdquo;',
     size='clamp(40px,8.4vmin,108px)'))

# ---------- 5. THE PIVOT ----------
A(C('The pivot', 'January 1830. Campbell starts a new paper; by July he closes the old one.', '1830'))
A(QK('&ldquo;It shall have for its object the developement, and introduction of that political and religious order of society called <b>THE MILLENNIUM</b>, which will be the consummation of that ultimate amelioration of society proposed in the Christian Scriptures.&rdquo;',
     'Prospectus, ' + MH + ', vol. 1, no. 1 (dated 1829), p. 1', 'The <i>Millennial Harbinger</i>', 'mh1830',
     '&ldquo;developement&rdquo; is the original spelling.',
     'The rest of the Prospectus lists real work in the real world: the end of sectarianism, education, injustice in government, &ldquo;the treatment of African slaves, as preparatory to their emancipation.&rdquo;'))
A(C('The <i>Millennial Harbinger</i>', 'January 1830. The new paper, alongside the old one until July.', '1830&ndash;1870'))
A(LIST('The <i>Millennial Harbinger</i>', 'The flagship',
  ['Published for four decades, 1830&ndash;1870', 'Campbell editing to 1864; then W. K. Pendleton', 'The movement&rsquo;s most influential editorial voice', 'Read for generations after'],
  'Four clicks.'))
A(CARD('What do you notice<br>' + G('about the name?'),
  '&rarr; Besides the fact that <i>Millennial Harbinger</i> is the most badass name for a religious journal ever. Let them talk.', 'For discussion'))
A('<section class="slide breath"><div class=litany style="gap:2.4vmin;max-width:86vw">'
  '<div class="no" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Restoration Quarterly</i>.</div>'
  '<div class="no frag" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Primitivist Paper</i>.</div>'
  '<div class="no frag" style="font-size:clamp(34px,6.6vmin,84px)">Not the <i>Old Ways Digest</i>.</div></div>'
  '<aside class=notes>Two clicks. It&rsquo;s not about the past at all.</aside></section>')
A(CARD('It&rsquo;s about<br>' + G('the future.'), 'From Cane Ridge to Brush Run&rsquo;s first Supper: they saw what was happening as a sign that the Spirit was on the move, that God&rsquo;s future could be glimpsed now, and that their job was to get on board.', style=';font-size:clamp(60px,12.6vmin,150px);line-height:1.08'))

# ---------- 6. HOW THEY SPOKE ABOUT THE FUTURE ----------
A(C('How they spoke<br>about the future', 'Not escape from the world: a world made new. And the church&rsquo;s unity first, so that the world may believe.'))
A(LIST('What was distinctive', 'Campbell&rsquo;s eschatology',
       ['<b>New creation,</b> not just heaven: this earth made new.',
        '<b>Brought by the gospel,</b> not the sword: the church&rsquo;s unity comes first, &ldquo;that the world may believe.&rdquo;',
        '<b>The church as its foretaste:</b> living God&rsquo;s future now.',
        '<b>The future as the test:</b> judge a doctrine by its effects, measured against what God&rsquo;s future promises.'],
       'Four marks, one per click. The new earth comes right after this slide; the church as foretaste, unity (John 17) and the future as the test follow in their own sections. (1) Not escape to heaven but a world made new (MH 1830, 1855). (2) How it comes: by the gospel, peacefully and gradually, with the church&rsquo;s unity as the prerequisite for the world&rsquo;s conversion (John 17, the D&amp;A, the <i>Christian System</i>). This is what made him postmillennial, and it is what put unity at the center. (3) So the church&rsquo;s life now (unity, conscience, the priesthood of all, the table) is the future in miniature. (4) And the future is the test: a doctrine is judged by its effects, set beside what the Millennium proposes (MH 1830, p. 7; on screen before &ldquo;Not legalism&rdquo;).'))
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
  'Separation: Stone, Lipscomb, Harding: no voting, office or war; the church as the alternative government. A social agenda: Campbell, and Scott after 1844: societies, schools, missions (the American Christian Missionary Society, 1849, Campbell its president); and P. J. Martin&rsquo;s postmillennial new earth (1913), with &ldquo;no exploitation&hellip; no foreclosing of mortgages&rdquo; (as quoted by John Mark Hicks; book not yet seen). Both: the church should already look like what is coming.'))
A(QK('&ldquo;We expect <b>no new Sun</b>, no new revelation of the Spirit, no other than the same gospel and the same religion, only that it shall be disinterred from the rubbish of the dark ages&hellip;&rdquo;',
     AC + ', &ldquo;Prefatory Remarks,&rdquo; ' + MH + ', January 1830, p. 5', 'Nothing new, only renewed', 'mh1830',
     'The first issue. The Sun is a metaphor: just before, the first step toward &ldquo;this glorious age&rdquo; is &ldquo;to dissipate the darkness which covers the people and hides from their eyes the Sun, the quickening, renewing, animating Sun of Mercy.&rdquo; No new gospel: the same one, recovered from &ldquo;the rubbish of the dark ages.&rdquo;'))
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
A(LIST('The future, practiced now', 'What the church will be, it does now',
       ['<b>Unity:</b> one body, gathered around Christ alone.',
        '<b>Freedom:</b> faith binds; opinions do not.',
        '<b>Priesthood:</b> no titled class between God and his people.'],
       'Three marks of the coming church, one per click. Each was the nature of the millennial church, so each was the church&rsquo;s work now. First the general idea in their words, then each mark.'))
A(QK('&ldquo;And are we not all looking for a Millennium of universal peace and prosperity&hellip;? These things being so, <b>our grand concern and present duty is, to adopt the proper means</b> for accomplishing this truly blissful and desirable object.&rdquo;',
     'Thomas Campbell, &ldquo;Christian Union,&rdquo; ' + MH + ', April 1839, p. 155', 'Therefore, now', 'mh1839',
     'Thirty years after the <i>Declaration and Address</i>, written while he edited the <i>Harbinger</i> in Alexander&rsquo;s absence. The grounds: &ldquo;the prayer of Christ for it, John xvii. 20&mdash;23; and the promise of God, Isai. xi. 9.&rdquo;'))
A(QK('&ldquo;The kingdom of heaven is divided into <b>small societies, called churches</b>, or congregations of the Lord.&rdquo;',
     CS + ', p. 166', 'The kingdom now', 'cs',
     'Just before: &ldquo;The supreme law of this kingdom is love&mdash;love of the King and love of each other.&rdquo; Wright&rsquo;s small working models, in Campbell&rsquo;s idiom.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;Would not the same effect be now produced, if the same means were used? <b>Certainly; for this is the very order of heaven</b>.&rdquo;',
     'Barton W. Stone, &ldquo;The Responsibility of the Church to God,&rdquo; <i>Christian Messenger</i> 11, 1840, p. 33', 'Stone, 1840', 'cm11',
     'Of the Corinthian assembly, where an unbeliever comes in and falls down to worship (1 Cor. 14:24&ndash;25). Earlier: the church is &ldquo;as visible as a city set on a hill&hellip; for the good of the world in darkness and death&rdquo; (p. 31). A congregation in right order shows heaven&rsquo;s order.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;&lsquo;And the kingdom and dominion&hellip; shall be given to the people of the saints of the Most High&hellip;&rsquo; <b>But this can not be in their present broken and divided state</b>&hellip;&rdquo;',
     DA, 'Thomas Campbell, 1809', 'dna', 'Daniel 7:27, then the turn.'))
A(QK('&ldquo;Are we not all praying for that happy event, when there shall be but one fold, as there is but one chief Shepherd? <b>What! shall we pray for a thing, and not strive to obtain it!!</b>&rdquo;',
     DA, 'Thomas Campbell, 1809', 'dna', 'The two exclamation points are his.', size='clamp(34px,7vmin,88px)'))
HIDE(QK('&ldquo;We are so sanguine (perhaps many will say, so visionary) as to imagine that <b>a nucleus has been formed, or may be formed, around which may one day congregate all the children of God</b>.&rdquo;',
     CS + ', p. 111', 'Unity', 'cs',
     'Same page: no one can say it is &ldquo;either impious or immoral&hellip; to meditate upon the possibility or practicability of any scheme of gathering together the children of God under the ensign of the cross alone.&rdquo; The church now is the nucleus of the church to come.'))
A(QK('&ldquo;Who that thinks of heaven, of eternal peace and love, <b>can refrain from pleading the union</b>, concert, and co-operation of all the sincere followers of the Lamb of God?&rdquo;',
     AC + ', &ldquo;Union,&rdquo; ' + MH + ', November 1840, p. 481', 'Unity', 'mh1840',
     'Just before: &ldquo;Union, love, and social bliss, are only three ways of expressing the same idea.&rdquo; Heaven, therefore union now.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;When then we see a people making new divisions and keeping up old ones, while praying for the Millennium or the triumph of love and harmony, <b>we as naturally suspect that they are any thing but in earnest</b>.&rdquo;',
     AC + ', ' + CB + ' 5, 1828, p. 263', 'Alexander, 1828', 'cb5', 'He goes on: like &ldquo;a nation preparing for war, and praying for peace.&rdquo;'))
A(QK('&ldquo;&hellip;our differences, at most, are about <b>the things in which the kingdom of God does not consist</b>, that is, about matters of private opinion or human invention. What a pity that the kingdom of God should be divided about such things!&rdquo;',
     DA, 'Freedom', 'dna',
     'Opinions are not what the kingdom is made of, so they cannot be what divides it.'))
A(QK('&ldquo;Resume that precious, that dear-bought liberty, wherewith Christ has made his people free; <b>a liberty from subjection to any authority but his own, in matters of religion</b>.&rdquo;',
     DA, 'Freedom', 'dna',
     'The <i>Declaration&rsquo;s</i> &ldquo;therefore&rdquo; after the signs of the times: &ldquo;Is it time for us to sit still in our corruptions and divisions&hellip;?&rdquo; It goes on: &ldquo;Call no man father, no man master on earth.&rdquo;'))
A(QK('&ldquo;We do not ask them to give up their opinions&mdash;<b>We ask them only not to impose them upon others</b>.&rdquo;',
     AC + ', &ldquo;Millennium&mdash;No. II,&rdquo; ' + MH + ', April 1830, p. 145', 'How the sects will cease', 'mh1830',
     'His answer to &ldquo;WILL sects ever cease?&hellip; How then shall it be introduced?&rdquo; Same essay: &ldquo;The faith is public property: opinions are, and always have been, private property.&rdquo; (Micah: here, or in a side path on gradualism.)', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;&hellip;who has made all the citizens of his kingdom, not citizens only, but <b>citizen kings and priests to God</b>.&rdquo;',
     AC + ', Fourth of July oration, ' + MH + ', 1830, p. 309', 'The priesthood', 'mh1830', 'Last week&rsquo;s theme, in the kingdom to come.', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;Being a royal priesthood, all children of a King, they have a right to meet in his name to break the loaf of blessing, to drink the cup of blessing, <b>without the intervention of a mediator, priest, or prophet, consecrated by human hands</b>.&rdquo;',
     AC + ', ' + MH + ', August 1830, p. 368', 'At the table', 'mh1830', 'Just before: &ldquo;they are all made sons and daughters, kings and priests to God.&rdquo; The ideal voiced; not yet extended to women.'))
A(QK('&ldquo;&rsquo;Tis here, and here alone, that <b>the king and the beggar meet on one platform and stand on equal ground</b> before God, angels and demons.&rdquo;',
     AC + ', letter to the church in Paisley, ' + MH + ' 1853, pp. 174&ndash;175', 'Paisley, 1853 &middot; one platform', 'mh1853',
     'Of the church, &ldquo;God&rsquo;s school, his primary school, in which he is to be trained and disciplined for the celestial university.&rdquo; He goes on: &ldquo;Faith, then, and not opinion; fact, and not fable; truth, and not hypothesis; reality, and not fiction, are the bond of union and the terms of communion.&rdquo;'))
A(QK('&ldquo;&hellip;the emancipation of all the world from faith in, and obedience to, <b>any set of men, titled and enthroned as they may be</b>, as the representatives or successors of the apostles of Christ.&rdquo;',
     AC + ', &ldquo;The Everlasting Gospel&rdquo; No. 3, ' + MH + ', May 1833, p. 226', 'What the coming judgment brings', 'mh1833', 'The end of clerical power is part of what is coming.'))
A(QK('&ldquo;&hellip;our religion was destined&hellip; to <b>cancel all orders of nobility in the state and in the church</b>&hellip; and finally to restore the long-lost liberties of mankind.&rdquo;',
     'Walter Scott, <i>The Messiahship</i> (1859), p. 240', 'Walter Scott, 1859', 'scott59',
     'His full list: &ldquo;to put down princes from their thrones; subvert ancient dynasties&hellip; dissolve armies; break down navies.&rdquo; Shadow: by 1859 Scott fused this hope with America&rsquo;s destiny.'))
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
A(QK('&ldquo;&hellip;immersion, I mean Christian immersion, is the gospel in water, and that <b>the Lord&rsquo;s supper is the gospel in bread and wine</b>.&rdquo;',
     AC + ', &ldquo;Ancient Gospel No. II,&rdquo; ' + CB + ' 5, February 1828', 'The table', 'cb5',
     'He goes on: &ldquo;These two ordinances&hellip; fully exhibit the gospel in the most appropriate symbols.&rdquo; John Mark Hicks opens his essay on the eschatological table with this line.', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;&hellip;the original impulse of the Stone-Campbell Movement stressed <b>the metaphor of table rather than altar</b>. As a consequence, early traditions emphasized the role of Jesus as host at the table and the joy of table fellowship.&rdquo;',
     'John Mark Hicks, &ldquo;The Lord&rsquo;s Supper as Eschatological Table&rdquo; (2026)', 'Table, not altar', 'hicks2',
     'The background: Scottish communion festivals at long tables; Cane Ridge (1801) &ldquo;was designed as a communal festival.&rdquo; Campbell: &ldquo;In the house of God there is always the table of the Lord&rdquo;; all Christians, &ldquo;a holy and royal priesthood,&rdquo; may &ldquo;approach it without fear, and partake of it with joy&rdquo; (<i>Christian System</i>, pp. 265, 269).'))
A(QK('&ldquo;In the afternoon, <b>we had heaven upon earth</b>; that is, we had the Lord&rsquo;s Supper.&rdquo;',
     'Walter Scott, diary, 1848, in William Baxter, <i>Life of Elder Walter Scott</i> (1874), p. 411', 'Walter Scott', 'baxter',
     'From his diary (the next entry is dated December 17, 1848). John Mark Hicks points to it as an exception: the movement kept the table, weekly and joyful, but mostly as a memorial; Campbell called the Supper &ldquo;not an ordinance for receiving new blessings, but for commemorating those already received&rdquo; (<i>MH</i> 1846, p. 396).', size='clamp(40px,8.4vmin,108px)'))
A(QK('&ldquo;<b>We already eat at the eschatological table of the Lord</b>; we already sit at the table with Jesus in his kingdom.&rdquo;',
     'John Mark Hicks, &ldquo;The Lord&rsquo;s Supper as Eschatological Table&rdquo; (2026)', 'The table now', 'hicks2',
     'His verdict on the tradition: it &ldquo;stressed memorialism&hellip; and reduced eschatological perspectives to the promised fact of a future reality.&rdquo; His exceptions: Scott, and William Robinson (the &ldquo;kingdom is both present and future,&rdquo; so &ldquo;we are with Him at the Lamb&rsquo;s great Bridal Feast&rdquo;; as quoted by Hicks). His call: &ldquo;The church needs to revision the Supper as an experience of resurrection joy at the kingdom table rather than as an altar of sacrifice.&rdquo;', size='clamp(36px,7.6vmin,96px)'))
A(QK('&ldquo;The Lord&rsquo;s day not only commemorates the resurrection of Jesus, but <b>anticipates the morning of the resurrection</b> in which we shall enter into the rest which remains for the people of God.&rdquo;',
     AC + ', ' + MH + ', January 1834, p. 37', 'Easter every Sunday', 'mh1834', 'Easter every Sunday.'))

# ---------- 8. THE FUTURE ITSELF ----------
A(CARD('Not a particular<br>' + G('timeline.'),
  'Campbell was postmillennial. Most of us are not. We might get hung up here; it is a distraction. In his own paper, he went back and forth: 1831, &ldquo;a deepening gloom overspreads our ecclesiastical heavens&rdquo; (<i>MH</i> 1831, p. 168); 1833, &ldquo;with what caution we have spoken on the prophecies and millennial matters&rdquo; (p. 49); 1840, &ldquo;We had more pressing and important matter on hand&rdquo; (p. 562; also &ldquo;we have not committed ourselves to any of the theories of the present day on the nature and coming of the Millennium&rdquo;); 1853, &ldquo;the millennium&rdquo; among the opinions that &ldquo;terminate in schism&rdquo; (p. 175); 1856, &ldquo;Modesty sits most gracefully on&hellip; interpreters of prophecy&rdquo; (p. 698). He also printed the other views: the premillennialist &ldquo;Daniel&rdquo; in his first volume; McCorkle&rsquo;s pessimism in 1833; Stone, who expected Christ to come first and reign.',
  style=';font-size:clamp(60px,12.6vmin,150px);line-height:1.08'))
A(QK('&ldquo;Alexander Campbell was a postmillennialist. James A. Harding was a premillennialist. Walter Scott changed his mind several times. <b>David Lipscomb was uncertain</b>.&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'John Mark Hicks, 2015', 'hicks',
     'Hicks teaches theology at Lipscomb University; with Bobby Valentine he wrote <i>Kingdom Come: Embracing the Spiritual Legacy of David Lipscomb and James A. Harding</i> (2006). Harding co-founded the Nashville Bible School (now Lipscomb University) with Lipscomb.', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;However, these all agreed that the most important aspect of the Christ&rsquo;s second coming was <b>the regeneration not only of the soul, but the body and the whole cosmos</b>.&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'What they agreed on', 'hicks',
     'He goes on: God will refine the cosmos by fire and renew it into a &ldquo;new heaven and new earth,&rdquo; as he will raise our bodies. Campbell: &ldquo;God recreates, regenerates, but annihilates nothing&rdquo; (<i>Christian System</i>, p. 257). Lipscomb: &ldquo;earth itself shall become heaven&rdquo; (<i>Gospel Advocate</i>, 1903, p. 328, as quoted by Hicks; not yet checked in the original).', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;&hellip;it was <b>the dominant perspective among churches of Christ in the late nineteenth century</b>&hellip;&rdquo;',
     'John Mark Hicks, &ldquo;What Will Become of the Earth: A Nashville Bible School Perspective&rdquo; (2015)', 'A renewed earth: our own tradition', 'hicks',
     'Just before: &ldquo;Many are surprised to learn this about our forbearers in the faith because they associate a renewed, material earth with fringe groups and strange ideas.&rdquo; He continues: &ldquo;particularly as articulated by David Lipscomb and James A. Harding.&rdquo; Lost in the twentieth century (Hicks, &ldquo;From Lipscomb to Wallace,&rdquo; 2012). Compare the opening quiz: &ldquo;This world is not my home.&rdquo;', size='clamp(40px,8.4vmin,108px)'))
A(QK('&ldquo;Biblical faith, according to Lipscomb and Harding, <b>is lived as if the future is already present</b>, as if the heavenly city has already been planted on the earth.&rdquo;',
     'John Mark Hicks, &ldquo;Extending the Kingdom Theology of Lipscomb and Harding&rdquo; (2019)', 'Living the future now', 'hicks',
     'Just before: &ldquo;This apocalyptic vision is a form of inaugurated eschatology, which calls us to live in the present as if the kingdom of God has fully arrived in anticipation of that fullness.&rdquo; Next: &ldquo;And the present church on the earth is that heavenly city.&rdquo; The Wright link, in our own tradition&rsquo;s terms.', size='clamp(36px,7.6vmin,96px)'))
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
     AC + ', Millennial Character of the Harbinger, ' + MH + ', December 1840, p. 561', 'Restoration served the future', 'mh1840',
     'Before it: &ldquo;When we put to sea under this banner we had the port of Primitive Christianity&hellip; in our eye.&rdquo; And 1825: &ldquo;Just in so far as the ancient order of things&hellip; is restored, just so far has the Millennium commenced&rdquo; (<i>CB</i> 2, p. 136).').replace('<section ', '<section data-src="mh40" ', 1))

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
  'A future that renews this world; a church that lives it now, above all in its unity and at its table. (Wright on reading Scripture as story, and how far we follow him: next week.)'))

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

# ---------- RESHAPE (Micah, 2026-11-14) ----------
# The shape: institutions; the Christian Baptist; the Harbinger, about the future; their eschatology across
# the movement; everything so far read forward (unity, freedom, priesthood, communion, the church as
# foretaste); two ways into the world (separation, or a social agenda); some Wright (his reading of
# Scripture moves to Chapter 8: the slides are kept in NEXT_WEEK). New slides are made here, then S is reordered.
_old = list(S); del S[:]
A(C('Everything so far,<br>read forward', 'Unity, freedom, the priesthood of all, communion, and the church as a foretaste: every chapter so far, seen from the future they were living toward.'))
A(LIST('Chapters 1&ndash;6, read forward', 'Everything so far',
  ['<b>Cane Ridge</b> (1801): a communion festival, read as the dawn of the millennial day.',
   '<b>The <i>Declaration and Address</i></b> (1809): unity and liberty, because the kingdom is coming.',
   '<b>The <i>Last Will</i></b> (1804): a presbytery dies into union, expecting redemption.',
   '<b>Alexander&rsquo;s defense</b> (1810): the church&rsquo;s gates as wide as heaven&rsquo;s.',
   '<b>Brush Run</b> (1811): the first Supper an emblem of the millennial church.'],
  'Five clicks, in the order we taught them. Each was already about the future: the table (Cane Ridge, Brush Run), unity (the <i>Declaration</i>, the <i>Last Will</i>), liberty (the <i>Declaration</i>), the gates of admission (Alexander&rsquo;s defense, November 1810). Quotations for four follow; the Brush Run Supper comes back at the table.',
  size='clamp(24px,4.3vmin,54px)', gap='1.3vmin'))
A(QK('&ldquo;Many were fully persuaded that <b>the glorious millennial day had commenced</b>, and that the world would soon become the Kingdom of our Lord Jesus Christ.&rdquo;',
     'An eyewitness of Cane Ridge, in Levi Purviance, <i>Biography of Elder David Purviance</i> (1848), p. 301', 'Chapter 1 &middot; Cane Ridge', 'purv48',
     'An anonymous eyewitness, about ten years old in 1801. He goes on: &ldquo;But alas! That enemy of God and man, sectarianism, raised its hydra head&hellip; and the fair prospects of Zion were in some degree blasted.&rdquo; Stone himself: from that revival &ldquo;a fountain of light has sprung&hellip; and it promises fair to enlighten the world&rdquo; (<i>Biography</i>, p. 46).'))
A(QK('&ldquo;It is our consolation, in the mean time, that <b>the desired event, as certain as it will be happy and glorious, admits of no dispute</b>, however we may hesitate or differ about the proper means of promoting it.&rdquo;',
     DA, 'Chapter 3 &middot; The <i>Declaration and Address</i>', 'dna',
     'The close of the Address. The future is certain; the means are disputed. The &ldquo;desired event&rdquo;: the church&rsquo;s unity, and through it the conversion of the world.'))
A(QK('&ldquo;&hellip;pray more and dispute less; and while they behold the signs of the times, look up, and <b>confidently expect that redemption draweth nigh</b>.&rdquo;',
     'Springfield Presbytery, <i>Last Will and Testament</i> (1804), in Stone, <i>Biography</i>, p. 52', 'Chapter 4 &middot; The <i>Last Will</i>', 'bio',
     'Its epigraph is Hebrews 12:27, &ldquo;that those things which cannot be shaken may remain.&rdquo; The Witnesses&rsquo; Address hopes the work &ldquo;will terminate in the universal spread of the gospel, and the unity of the church&rdquo; (pp. 54&ndash;55).', size='clamp(34px,7vmin,88px)'))
A(QK('&ldquo;We have decided, therefore,&hellip; <b>to open the gates of admission into the Church as wide as the gates of heaven</b>.&rdquo;',
     AC + ', November 1810 &middot; in Richardson, <i>Memoirs</i>, vol. 1, p. 341', 'Chapter 5 &middot; Alexander&rsquo;s defense', 'rich1',
     'From Chapter 5. The church&rsquo;s door measured by heaven&rsquo;s: the future sets the terms of fellowship now.', size='clamp(38px,8.4vmin,106px)'))
A(LIST('The future, practiced now', 'What the church will be, it does now',
  ['<b>Unity:</b> one body, gathered around Christ alone.',
   '<b>Priesthood:</b> no titled class between God and his people.',
   '<b>Freedom:</b> faith binds; opinions do not.'],
  'Three marks, one per click. Each was the nature of the coming church, so each was the church&rsquo;s work now. Their words follow for priesthood and freedom; unity&rsquo;s came just before. John 17 (unity so that the world may believe) is a side path off this slide.'))
A(C('Eschatology and government:<br>two paths', 'The same hope pointed two ways in public life: a strong separation of church and state, or an institutional social agenda.'))
A(QK('&ldquo;It took but little thought to see that Christians cannot fight&hellip; <b>But if he cannot fight himself, can he vote to make another fight?</b>&rdquo;',
     'David Lipscomb, <i>Civil Government</i> (1889), preface, p. 4', 'Separation', 'lipcg',
     'The Civil War turned him. The church, God&rsquo;s kingdom, displaces the human governments by spreading, not by force; so Christians do not fight, vote or hold office. Stone&rsquo;s line in the next generation; more in Chapter 9.'))
A(QK('&ldquo;Society is not yet fully civilized. It is only beginning to be. Things are in process, <b>in progress to another age&mdash;a golden&mdash;a millennial&mdash;a blissful period</b> in human history.&rdquo;',
     AC + ', &ldquo;Address on the Amelioration of the Social State,&rdquo; <i>Popular Lectures and Addresses</i> (1863), p. 69', 'A social agenda', 'pla',
     'He goes on: &ldquo;Woman, I believe, is destined to be the great agent in this grandest of all human enterprises&mdash;an effort to advance society to the acme of its most glorious destiny on earth,&rdquo; and calls for &ldquo;universal female education.&rdquo; Shadows: in the same address her sphere is &ldquo;the domestic circle&rdquo;; elsewhere he expects an &ldquo;Anglo-Saxon triumph in the great work of human civilization and redemption.&rdquo;'))
A(QK('&ldquo;&hellip;it is not an age to drop down from heaven, but <b>a period of light, religion and enjoyment to arise out of the natural and gradual progress of society</b>.&rdquo;',
     'Walter Scott, <i>The Messiahship</i> (1859), p. 335', 'A social agenda', 'scott59',
     'Scott after 1844, reversing his own premillennial reading of the 1830s. Shadow: he proves it from &ldquo;the elements of the Revolution of 1776&rdquo;; hope fused with the nation.'))
_new = list(S); del S[:]
def _ix(sub):
    hits = [i for i, x in enumerate(_old) if sub in x]
    assert len(hits) == 1, (sub, hits)
    return hits[0]
def _run(a, b): return [_old[i] for i in range(_ix(a), _ix(b) + 1)]
def _one(*subs): return [_old[_ix(x)] for x in subs]
NEXT_WEEK = _run('Most of the Bible does not consist', 'Who tells the story')   # Wright on reading Scripture: Chapter 8
S.extend(_old[:_ix('It&rsquo;s about<br>') + 1]                       # opening, recap, institutions, Christian Baptist, the Harbinger
  + _one('Restoration served the future')
  # their eschatology across the movement
  + _one('How they spoke<br>about the future', 'Campbell&rsquo;s eschatology')
  + _run('Nothing new, only renewed', 'Beat your swords into ploughshares')
  + _run('The prayer they lived by', 'Some of you say it will be effected')
  + _one('Barton Stone&rsquo;s eschatology', 'In his own paper, he went back and forth',
         'James A. Harding was a premillennialist', 'these all agreed that the most important aspect',
         'the dominant perspective among churches of Christ', 'The commitment to God&rsquo;s future is the leading emphasis')
  + _run('Side path &middot; other voices on the future', 'which even of our great men')
  + _run('ride the sea of fire', 'a type of heaven</b>')
  + _one('Different views of the end.')
  # everything so far, read forward
  + _new[:6] + _new[6:7]
  + _one('shall be given to the people of the saints', 'pray for a thing, and not strive',
         'Who that thinks of heaven', 'making new divisions and keeping up old ones')                       # unity
  + _one('the things in which the kingdom of God does not consist', 'Resume that precious', 'We do not ask them to give up their opinions&mdash;<b>')  # freedom
  + _one('citizen kings and priests to God</b>', 'without the intervention of a mediator', 'the king and the beggar meet',
         'titled and enthroned as they may be', 'cancel all orders of nobility')                              # priesthood
  + _run('The other<br>millennial harbinger', 'not only commemorates the resurrection of Jesus')                 # communion
  + _one('is lived as if the future is already present', 'our grand concern and present duty',
         'small societies, called churches', 'very order of heaven')                                         # foretaste
  + _one('In detecting the false gospels', 'Not legalism.')
  # two ways into the world
  + _new[7:8] + _one('Where they differed', 'Let Christians shew', 'clearing away the rubbish', 'one universal brotherhood')
  + _new[8:] + _one('Same hope.<br>')
  # some Wright
  + _one('Bishop of Durham', 'Christ is coming here', 'small working model of new creation</b>', 'new creation that we can eat', 'Two centuries apart')
  + _old[_ix('Two centuries apart') + 1:])                               # close
_dropped = [x for x in _old if x not in S]   # the two old "church to come" openers and the four Wright-on-Scripture slides
assert len(_dropped) == 6 and len(S) == len(_old) - 6 + len(_new), (len(S), len(_old), [re.sub('<[^>]+>', ' ', x)[:80] for x in _dropped])
# Micah, 2026-11-14: the Prospectus comes after "It's about the future."
_pro = [i for i, x in enumerate(S) if 'It shall have for its object' in x]
_fut = [i for i, x in enumerate(S) if 'It&rsquo;s about<br>' in x]
assert len(_pro) == len(_fut) == 1 and _pro[0] < _fut[0]
S.insert(_fut[0], S.pop(_pro[0]))
# Micah, 2026-11-15: the Harbinger's first masthead, right after its title card.
_mhc = [i for i, x in enumerate(S) if 'sect' in x and '<h2>The <i>Millennial Harbinger</i></h2>' in x]
assert len(_mhc) == 1, _mhc
S.insert(_mhc[0] + 1, MAST('millennial_harbinger_masthead_1830.jpg', 'Its masthead', 'The <i>Millennial Harbinger</i>, vol. 1, no. 1, January 4, 1830 (Internet Archive scan)',
  'Revelation 14:6&ndash;7 (credited to &ldquo;John&rdquo;; &ldquo;messenger&rdquo; and &ldquo;good news&rdquo; rather than the King James &ldquo;angel&rdquo; and &ldquo;gospel&rdquo;): &ldquo;I saw another messenger flying through the midst of heaven, having everlasting good news to proclaim to the inhabitants of the earth&hellip; for the hour of his judgments is come.&rdquo; Then: &ldquo;Great is the truth and mighty above all things, and will prevail&rdquo; (compare 1 Esdras 4:41). Compare the <i>Christian Baptist</i>&rsquo;s masthead: titles forbidden. Here, a messenger from heaven with news for every nation: the paper&rsquo;s name in a verse.'))
# Micah, 2026-11-14: a side path off "It's about the future.": the Prospectus and "Restoration served the future".
_pro = [i for i, x in enumerate(S) if 'It shall have for its object' in x]
assert len(_pro) == 1 and 'Restoration served the future' in S[_pro[0] + 1]
S.insert(_pro[0], '<section class="slide breath"><div class=eyebrow>Side path &middot; the Harbinger&rsquo;s aim</div>'
                  '<h2 style="max-width:none">The <i>Harbinger</i>&rsquo;s aim, in its own words</h2>'
                  '<aside class=notes>Off &ldquo;It&rsquo;s about the future.&rdquo; The Prospectus (1829) and its subjects. Campbell&rsquo;s look back (1840), &ldquo;Restoration served the future,&rdquo; is on the main line under &ldquo;Restoration, reframed.&rdquo;</aside></section>')
# Micah, 2026-11-14: the new-creation run (a new creation; coming down; this earth made new; not just Campbell)
# right after "Campbell's eschatology", before "Nothing new, only renewed".
_mv = [i for i, x in enumerate(S) if any(k in x for k in ('<div class=eyebrow>A new creation</div>', '<div class=eyebrow>Coming down, not going up</div>',
                                                         '<div class=eyebrow>This earth, made new</div>', '<div class=eyebrow>Not just Campbell</div>'))]
assert len(_mv) == 4 and _mv == list(range(_mv[0], _mv[0] + 4)), _mv
_blk = S[_mv[0]:_mv[0] + 4]; del S[_mv[0]:_mv[0] + 4]
_ce = [i for i, x in enumerate(S) if 'Campbell&rsquo;s eschatology' in x and 'What was distinctive' in x]
assert len(_ce) == 1
S[_ce[0] + 1:_ce[0] + 1] = _blk
# Micah, 2026-11-14: Hicks's first two (they disagreed; what they agreed on) right after "How they spoke about the future".
_h = [i for i, x in enumerate(S) if 'James A. Harding was a premillennialist' in x or 'these all agreed that the most important aspect' in x]
assert len(_h) == 2 and _h[1] == _h[0] + 1, _h
_blk = S[_h[0]:_h[0] + 2]; del S[_h[0]:_h[0] + 2]
_hs = [i for i, x in enumerate(S) if 'How they spoke<br>about the future' in x]
assert len(_hs) == 1
S[_hs[0] + 1:_hs[0] + 1] = _blk
# Micah, 2026-11-14: the Prospectus's list of subjects (with the treatment of slaves), on the side path after the Prospectus.
_pro = [i for i, x in enumerate(S) if 'It shall have for its object' in x]
assert len(_pro) == 1
S.insert(_pro[0] + 1, LIST('The Prospectus, 1829', 'Subjects &ldquo;subservient to this comprehensive object&rdquo;',
  ['1. &ldquo;The incompatibility of any sectarian establishment, now known on earth, with the genius of the glorious age to come.&rdquo;',
   '2. &ldquo;The inadequacy of all the present systems of education, literary and moral&hellip;&rdquo;',
   '4. &ldquo;The <i>injustice</i> which yet remains in many of the political regulations under the best political governments, when contrasted with the <i>justice</i> which Christianity proposes, and which the millennial order of society promises.&rdquo;',
   '5. &ldquo;Disquisitions upon the treatment of African slaves, as preparatory to their emancipation, and exaltation from their present degraded condition.&rdquo;'],
  'Four clicks: subjects 1, 2, 4 and 5 of nine; read in the page scan (vol. 1, no. 1, p. 1). The others: freeing the Scriptures from the commentators; religious news; reviews; queries, including &ldquo;a restoration of the <i>Ancient Order of Things</i>&rdquo;; miscellanea. The program of the millennial order: against sects, for education, the Scriptures freed, political injustice measured by the millennium, and (5) slavery, toward &ldquo;their emancipation, and exaltation.&rdquo; Shadow: Campbell inherited enslaved people, freed them, and advocated gradual emancipation, while trying to hold the brotherhood together across the question.',
  size='clamp(22px,3.8vmin,46px)', gap='1.6vmin'))
# Acts 2 (Micah, 2026-11-15): the Jerusalem church as model, and Campbell against a liturgy drawn from Acts 2:42.
A(QK('&ldquo;Now this congregation was intended to be a model, and <b>did actually become such to Judea, Samaria, and to the uttermost parts of the earth</b>.&rdquo;',
     AC + ', A Restoration of the Ancient Order of Things, No. VII, ' + CB + ' 3, September 1825, p. 30', 'Acts 2: a model for the world', 'cb3',
     'Of the Jerusalem church after Pentecost: the apostles &ldquo;proceeded to organize a congregation of disciples, and to set them in the order which the Lord had commanded.&rdquo; Then he quotes Acts 2:41&ndash;42: &ldquo;they continued stedfastly in the apostles&rsquo; doctrine, and in the fellowship, and in breaking of bread, and in prayers.&rdquo; The first church as a model sent outward, to the ends of the earth (Acts 1:8). Be candid about the essay (whole text: press Z): its argument is that &ldquo;Apostolic example is justly esteemed of equal authority with an apostolic precept,&rdquo; and from Acts 2 and Acts 20:7 it concludes the Supper was weekly, on the first day, &ldquo;the most prominent object of their meeting.&rdquo; This is a root of the later command-and-example reading; here its aim is weekly communion.').replace('<section ', '<section data-src="cb25" ', 1))
# Micah, 2026-11-15: one slide on what was distinctive, then a title card before each mark's quotations.
for _gone in ('How they spoke<br>about the future', 'Campbell&rsquo;s eschatology</h2>', 'Everything so far,<br>read forward'):   # replaced by the slide and cards below
    _g = [i for i, x in enumerate(S) if _gone in x]; assert len(_g) == 1, _gone; del S[_g[0]]
A(LIST('What was distinctive', 'Their eschatology, in three marks',
  ['<b>A new creation:</b> this earth made new, not an escape to heaven.',
   '<b>The church as a microcosm:</b> a small working model of what is coming.',
   '<b>Practicing the future today:</b> unity, priesthood, freedom, the table.'],
  'Three clicks; each has its own section next, behind a title card. Across the movement, whatever their timeline (Campbell post-, Stone pre-, Scott changing, Lipscomb uncertain), these three held.',
  size='clamp(26px,4.8vmin,60px)', gap='2vmin'))
A(C('A new creation', 'Not an escape to heaven: this earth made new.'))
A(C('The church as a microcosm', 'The church now as a small working model of God&rsquo;s future.'))
A(C('Practicing the future today', 'The church does now what it will be: unity, priesthood, freedom, and the table.'))
# ---------- Micah's structure from "It's about the future" (2026-11-14) ----------
# not a timeline, the future in general; the whole movement is about eschatology; a new earth; the church as
# microcosm; unity, priesthood, freedom; practices; restoration reframed, not legalism. Then two ways, Wright, close.
def _f(sub):
    h = [i for i, x in enumerate(S) if sub in x]
    assert len(h) == 1, (sub, h)
    return h[0]
def _r(a, b): return list(range(_f(a), _f(b) + 1))
_seq = (
    list(range(0, _f('It&rsquo;s about<br>') + 1))
    + _r('Side path &middot; the Harbinger&rsquo;s aim', 'subservient to this comprehensive object')
    # 1. not postmillennialism: the future in general
    + [_f('In his own paper, he went back and forth'), _f('James A. Harding was a premillennialist'),
       _f('The commitment to God&rsquo;s future is the leading emphasis')]
    + _r('Side path &middot; other voices on the future', 'Different views of the end.')
    # 2. the whole movement is about eschatology
    + _r('Chapters 1&ndash;6, read forward', 'gates of admission into the Church as wide as the gates of heaven</b>')
    # what was distinctive, in one slide; then each mark behind its own title card
    + [_f('Their eschatology, in three marks')]
    + [_f('<h2>A new creation</h2>'), _f('these all agreed that the most important aspect'), _f('the dominant perspective among churches of Christ')]
    + [i for i in _r('<div class=eyebrow>A new creation</div>', '<div class=eyebrow>Peace</div>') if i != _f('We expect <b>no new Sun</b>')]
    + [_f('<h2>The church as a microcosm</h2>')]
    + _r('is lived as if the future is already present', 'Certainly; for this is the very order of heaven')
    + [_f('<h2>Practicing the future today</h2>'), _f('What the church will be, it does now')]
    + _r('<h2>John 17</h2>', 'Some of you say it will be effected')
    + _r('shall be given to the people of the saints', 'making new divisions and keeping up old ones')
    + _r('citizen kings and priests to God</b>', 'cancel all orders of nobility')
    + _r('the things in which the kingdom of God does not consist', 'We do not ask them to give up their opinions&mdash;<b>')
    + _r('The other<br>millennial harbinger', 'not only commemorates the resurrection of Jesus')
    # 7. restoration reframed, not legalism
    + [_f('Millennial Character of the Harbinger'), _f('We expect <b>no new Sun</b>'), _f('Now this congregation was intended to be a model'),
       _f('In detecting the false gospels'), _f('Not legalism.')]
    # two ways into the world (Stone's eschatology opens it), Wright, close
    + [_f('Eschatology and government:<br>two paths'), _f('Barton Stone&rsquo;s eschatology</h2>')]
    + list(range(_f('Eschatology and government:<br>two paths') + 1, len(S)))
)
_seq2 = []
for i in _seq:
    if i not in _seq2: _seq2.append(i)
assert sorted(_seq2) == list(range(len(S))), sorted(set(range(len(S))) - set(_seq2))
S[:] = [S[i] for i in _seq2]
# Micah, 2026-11-15: "Peace" (the Address on War) belongs with eschatology and government, after Lipscomb on fighting and voting.
_pe = [i for i, x in enumerate(S) if '<div class=eyebrow>Peace</div>' in x]
assert len(_pe) == 1
_peace = S.pop(_pe[0])
_lf = [i for i, x in enumerate(S) if 'It took but little thought to see that Christians cannot fight' in x]
assert len(_lf) == 1
S.insert(_lf[0] + 1, _peace)
# Micah, 2026-11-15: "The table now", "Easter every Sunday" and "Restoration served the future" belong with the church as microcosm.
_mv = [[i for i, x in enumerate(S) if k in x] for k in ('We already eat at the eschatological table of the Lord',
                                                         'not only commemorates the resurrection of Jesus',
                                                         'Millennial Character of the Harbinger')]
assert all(len(h) == 1 for h in _mv), _mv
_blk = [S[h[0]] for h in _mv]
for x in _blk: S.remove(x)
_oh = [i for i, x in enumerate(S) if 'Certainly; for this is the very order of heaven' in x]
assert len(_oh) == 1
S[_oh[0] + 1:_oh[0] + 1] = _blk
# Micah, 2026-11-15: Brush Run's emblem and Scott's "heaven upon earth" into the microcosm section (before "The table now");
# "the gospel in bread and wine" and Hicks's "table, not altar" dropped.
def _one_ix(k):
    h = [i for i, x in enumerate(S) if k in x]; assert len(h) == 1, (k, h); return h[0]
for _k in ('is the gospel in water, and that', 'stressed <b>the metaphor of table rather than altar</b>'):
    del S[_one_ix(_k)]
_blk = [S[_one_ix('they furnished <b>an emblem of the millennial state of the Church</b>')], S[_one_ix('we had heaven upon earth</b>')]]
for x in _blk: S.remove(x)
_tn = _one_ix('We already eat at the eschatological table of the Lord')
S[_tn:_tn] = _blk
# Micah, 2026-11-15: the 1830 "one Lord's table" into the microcosm section, after Brush Run; its title card dropped.
del S[_one_ix('<h2>The other<br>millennial harbinger</h2>')]
_fi = S.pop(_one_ix('meeting around one and the same Lord&rsquo;s table</b>'))
S.insert(_one_ix('they furnished <b>an emblem of the millennial state of the Church</b>') + 1, _fi)
# Micah, 2026-11-15: the Paisley letter (1853) in fuller context, around "the king and the beggar"; whole letter behind Z.
_PAIS = AC + ', letter to the church in Paisley, ' + MH + ' 1853, p. %s'
def _P(q, page, eyebrow, key_note, size=None):
    return QK(q, _PAIS % page, eyebrow, 'mh1853', key_note, size=size).replace('<section ', '<section data-src="mh53" ', 1)
_pa_before = [
  _P('&ldquo;Man&hellip; was predestined and created <b>for a citizenship in the whole universe</b>, and not for any locality in the solar or material realms. God and his whole creation is the patrimonial inheritance of man.&rdquo;', '174', 'Paisley, 1853 &middot; a citizenship',
     'To the church in Paisley, Scotland, after Dr. John Thomas (later founder of the Christadelphians) had split it over his speculations. Campbell begins with destiny: &ldquo;Man, the most sublime and awful object that man himself or angel ever saw&hellip;&rdquo; It goes on: &ldquo;God himself is his portion. Therefore, all things are man&rsquo;s, because man is Christ&rsquo;s.&rdquo; Press Z for the whole letter.'),
  _P('&ldquo;To educate man in harmony with his origin and his destiny, <b>the church is God&rsquo;s school, his primary school, in which he is to be trained and disciplined for the celestial university</b>&hellip;&rdquo;', '174', 'Paisley, 1853 &middot; God&rsquo;s school',
     'It ends: &ldquo;that he may ultimately be a peer of the realm of creation, in its broadest, fullest, and highest import.&rdquo; The church now as training for what is coming: the microcosm in Campbell&rsquo;s idiom.'),
  _P('&ldquo;In it the ruined and undone wretch is taken from the mire of his own pollutions, renovated and sanctified, <b>adopted and enrolled amongst princes&mdash;peers of the celestial realm</b>&hellip;&rdquo;', '174', 'Paisley, 1853 &middot; princes',
     'It ends: &ldquo;over which Jehovah reigns the supreme and eternal Autocrat. This is his school, and the Bible is his text-book, from its Alpha to its Omega.&rdquo; Kings and priests to God, in the language of royalty.'),
  _P('&ldquo;Hence in the church there is neither Jew nor Greek, there is neither bond nor free, <b>there is neither male nor female</b>. We are all one&mdash;in one Lord, one faith, one baptism, and in one hope of one and the same inheritance.&rdquo;', '174', 'Paisley, 1853 &middot; all one',
     'Just before: &ldquo;Located here, we see all things right, and in their true colors and proportions, and no where else.&rdquo; Galatians 3:28 and Ephesians 4: the ideal voiced, including women; not yet extended to them in practice.'),
]
_pa_after = [
  _P('&ldquo;Doctors of theology, as such&hellip; doctors of opinions&hellip; have <b>no moral chairs, or moral authority, no ecclesiastic power, no prescriptive rights, over the understanding, the conscience, or the hearts of the citizens of Messiah&rsquo;s spiritual empire</b>.&rdquo;', '175', 'Paisley, 1853 &middot; no chairs',
     'Between the king and the beggar and this: &ldquo;Faith, then, and not opinion; fact, and not fable; truth, and not hypothesis; reality, and not fiction, are the bond of union and the terms of communion.&rdquo; &ldquo;Doctors of opinions&rdquo; names Thomas. Next: opinions on &ldquo;the millennium&rdquo; among them &ldquo;centre in self-esteem and terminate in schism.&rdquo; Priesthood and freedom together: no title gives anyone authority over a believer&rsquo;s conscience.'),
]
_kb = _one_ix('the king and the beggar meet on one platform')
S[_kb] = S[_kb].replace('<section ', '<section data-src="mh53" ', 1)
S[_kb + 1:_kb + 1] = _pa_after
S[_kb:_kb] = _pa_before
# Micah, 2026-11-15: Daniel 7, "pray for a thing", and "Who that thinks of heaven" right after the "Practicing the future today" card.
_blk = [S[_one_ix(k)] for k in ('shall be given to the people of the saints', 'pray for a thing, and not strive', 'Who that thinks of heaven')]
for x in _blk: S.remove(x)
_pf = _one_ix('<h2>Practicing the future today</h2>')
S[_pf + 1:_pf + 1] = _blk
# Micah, 2026-11-15: Alexander's 1828 "praying for the Millennium" right after "Who that thinks of heaven".
_x = S.pop(_one_ix('making new divisions and keeping up old ones'))
S.insert(_one_ix('Who that thinks of heaven') + 1, _x)
# Micah, 2026-11-15: "pray for a thing" before Daniel 7.
_d7 = _one_ix('shall be given to the people of the saints'); _pr = _one_ix('pray for a thing, and not strive')
assert _pr == _d7 + 1
S[_d7], S[_pr] = S[_pr], S[_d7]
# Micah, 2026-11-15: Hicks's "lived as if the future is already present", Thomas Campbell's "present duty" and
# Stone's "very order of heaven" open "Practicing the future today".
_blk = [S[_one_ix(k)] for k in ('is lived as if the future is already present', 'our grand concern and present duty', 'Certainly; for this is the very order of heaven')]
for x in _blk: S.remove(x)
_pf = _one_ix('<h2>Practicing the future today</h2>')
S[_pf + 1:_pf + 1] = _blk
# Micah, 2026-11-15: hide "Jesus reigns on earth" (kept in the source).
del S[_one_ix('without a tear or a sigh, when Jesus reigns on earth')]
