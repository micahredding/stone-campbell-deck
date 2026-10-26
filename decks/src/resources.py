# -*- coding: utf-8 -*-
# Shared resources for the map decks (Chapter 5 on): the source documents, whole, and side paths any
# chapter can hang off its spine. A chapter's week*map/build.py picks the documents (DOC_KEYS) and lists
# the side paths' anchors (SIDE); its slides.py adds the side paths' slides with A(...) where they hang.
#
#   docs(between, clean, keys)  -> the documents, in the order given      SHORT[key] -> label on the map
#   doc_order(vis, keys)        -> which documents a slide's quotes are checked against, from its citation
#   westminster(extra=[])       -> side path: quoting the Westminster Confession against itself
#   governance(extra=[])        -> side path: who governs the church (Matthew 18, Westminster 30, the
#                                  Declaration and Address, the Last Will, Alexander Campbell)
#   universals(extra=[])        -> side path: the whole church remembers (priesthood, governance, baptism,
#                                  the table, from Cyprian to the Lima text)
#   campbell_reread(extra=[])   -> side path: Alexander Campbell, reread (the ancient order as liberation and
#                                  foretaste; Lunenburg 1837; the Address on War, 1848)
#   ekklesia(extra=[])          -> side path: the church as ekklesia, the assembly (the Greek citizens' assembly,
#                                  1 Corinthians 14 in Campbell's Living Oracles, Tyndale, Campbell's
#                                  "fountain of official power")
#   table(extra=[])             -> side path: who keeps the table (who may give thanks and serve at the Supper,
#                                  from the Scotch Baptists and Campbell to Stone, Lipscomb and today)
#   unity(extra=[])             -> resource: union, all his life (Thomas Campbell's Declaration and Address, which
#                                  Alexander endorsed; the 1810 party-man address; the Christian Baptist; The Christian
#                                  System; Lunenburg; the open Campbell). Also its own deck: decks/src/unity/build.py
#   WESTMINSTER, GOVERNANCE, UNIVERSALS,
#   CAMPBELL_REREAD, EKKLESIA, TABLE, UNITY -> (label, first-slide anchor, last-slide anchor) for SIDE
#
# Each resource's quotes are checked against a document: give a slide data-src=<key> to route it (see
# doc_order). Keys: church (the-whole-church.html), acr (campbell-reread.html), ekk (ekklesia.html), tbl (the-table.html), uni (campbell-unity.html).
# The catalogue, with how to hang a resource and where its research lives: decks/src/RESOURCES.md
#
# Add a resource: write a function returning a list of slides, give its first slide a unique eyebrow and
# its last a unique phrase, and add the anchor tuple here. Quotes in it must be in one of the documents.
import importlib.util, os

_H = os.path.dirname(os.path.abspath(__file__))
def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(_H, rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
w3b = _load('w3bslides', 'week3b/slides.py')
w4 = _load('w4slides', 'week4/slides.py')
Q, N = w3b.w3.Q, w3b.w3.N
def BIG(slide, size='clamp(34px,7.6vmin,96px)', width='30ch'):   # a quote set larger than Q's default
    import re as _re
    return _re.sub(r'<p class="bigquote( long| xlong)?">', lambda m: '<p class="bigquote%s" style="font-size:%s;max-width:%s;line-height:1.2">' % (m.group(1) or '', size, width), slide, 1)
CARD, G = w4.CARD, w4.G

WILL, WIT, STONE = w4.WILL, w4.WIT, w4.STONE
WCF = 'Westminster Confession of Faith, American text (1788)'
DA = 'Thomas Campbell, <i>Declaration and Address</i> (1809)'
RICH = 'Robert Richardson, <i>Memoirs of Alexander Campbell</i> (1868)'
AC_R = 'Alexander Campbell &middot; in Richardson, <i>Memoirs</i>'

# ---------- documents ----------
def docs(between, clean, keys):
    src = lambda *p: open(os.path.join(_H, *p)).read()
    D = {
        'rich': lambda: {'title': 'Robert Richardson, <i>Memoirs of Alexander Campbell</i>, vol. 1 (1868)',
            'sub': 'The wreck, the first sermon, the Synod&rsquo;s minutes, Alexander&rsquo;s reply, Brush Run, the ordination &middot; excerpts, machine-read from the Internet Archive scan',
            'html': clean(src('week5map', 'sources', 'richardson-memoirs-v1-excerpts.html'))},
        'dna': lambda: {'title': 'Thomas Campbell, <i>Declaration and Address</i> (1809)',
            'sub': 'The whole of it: Declaration, Address, Propositions, Appendix',
            'html': clean(between('declaration-and-address-fulltext.njk', '<h2 id="declaration">', '<!-- SOURCE CITATION -->'))},
        'will': lambda: {'title': 'The Last Will and Testament of the Springfield Presbytery',
            'sub': 'Cane Ridge, June 28, 1804 &middot; with the Witnesses&rsquo; Address',
            'html': clean(between('last-will-fulltext.njk', '<h2 id="epigraph">', '<!-- SOURCE CITATION -->'))},
        'stone': lambda: {'title': 'Barton W. Stone, <i>Biography</i> (1847), chapter VII',
            'sub': 'His own account of the trial, the garden, the cost, and the will',
            'html': clean(between('biography-barton-stone-fulltext.njk', '<h3 id="bio-ch-7">', '<h3 id="bio-ch-8">'))},
        'apology': lambda: {'title': 'The Springfield Presbytery&rsquo;s <i>Apology</i> (1804), Parts I and III',
            'sub': 'The five&rsquo;s own history and their remarks on creeds and the Confession &middot; as reprinted in Stone&rsquo;s <i>Biography</i>',
            'html': clean(between('biography-barton-stone-fulltext.njk', '<h3 id="apology-i">', '<h2 id="apology-ii">')
                          + between('biography-barton-stone-fulltext.njk', '<h2 id="apology-iii">', '<h2 id="character">'))},
        'wcf': lambda: {'title': 'The Westminster Confession of Faith',
            'sub': 'The Presbyterian standard &middot; American text of 1788 (OPC edition)',
            'html': clean(src('week4map', 'sources', 'westminster-confession-american.html'))},
        'cb': lambda: {'title': 'Alexander Campbell, <i>The Christian Baptist</i>, July 5, 1824',
            'sub': '&ldquo;Essays on Ecclesiastical Characters, Councils, Creeds, and Sects, No. III&rdquo; &middot; the opening, transcribed from the 1835 edition',
            'html': clean(src('sources', 'christian-baptist-1824-ecclesiastical-courts.html'))},
        'church': lambda: {'title': 'The whole church: excerpts on priesthood, governance, baptism, and the table',
            'sub': 'Cyprian, Leo the Great, Luther (1523), the Eastern Patriarchs (1848), Schmemann, Afanasiev, Vatican II, Pope Francis, the 2024 Synod, the Lima text',
            'html': clean(src('sources', 'the-whole-church.html'))},
        'acr': lambda: {'title': 'Alexander Campbell, reread: excerpts',
            'sub': '<i>The Christian Baptist</i> (1825, 1829, 1830), the Lunenburg letter (1837), the Address on War (1848) &middot; transcribed from the scans',
            'html': clean(src('sources', 'campbell-reread.html'))},
        'ekk': lambda: {'title': 'The church as <i>ekklēsia</i>: excerpts',
            'sub': 'Euripides, Demosthenes, Hansen, the Living Oracles, van Kooten, Miller, Esler, Tyndale, Carson, Campbell, Lindsay',
            'html': clean(src('sources', 'ekklesia.html'))},
        'tbl': lambda: {'title': 'Who keeps the table: excerpts',
            'sub': 'Scotch Baptists, Campbell, Stone&rsquo;s <i>Christian Messenger</i>, Lipscomb, the ecumenical record, and today',
            'html': clean(src('sources', 'the-table.html'))},
        'uni': lambda: {'title': 'Alexander Campbell on the union of Christians: excerpts',
            'sub': 'Richardson, <i>The Christian System</i>, the <i>Christian Baptist</i> (1825&ndash;1830), the <i>Millennial Harbinger</i> (1837)',
            'html': clean(src('sources', 'campbell-unity.html'))},
        'kjv': lambda: {'title': 'Scripture, King James Version',
            'sub': 'Passages on the church, its officers, and its table',
            'html': clean(src('sources', 'scripture-kjv.html'))},
    }
    return [dict(D[k](), key=k) for k in keys]

SHORT = {'rich': 'Richardson&rsquo;s <i>Memoirs</i>', 'dna': 'The Declaration and Address', 'will': 'The whole will',
         'stone': 'Stone&rsquo;s own account', 'apology': 'The five&rsquo;s own history', 'wcf': 'The Westminster Confession',
         'kjv': 'Scripture (KJV)', 'cb': 'The <i>Christian Baptist</i>, 1824', 'church': 'The whole church',
         'acr': 'Campbell, reread', 'ekk': 'The assembly', 'tbl': 'Who keeps the table', 'uni': 'Campbell on union'}

def doc_order(vis, K):
    has = lambda *k: [K.index(x) for x in k if x in K]
    if 'data-src=church' in vis: o = has('church') + [i for i in range(len(K)) if K[i] != 'church']
    elif 'data-src=acr' in vis: o = has('acr')
    elif 'data-src=ekk' in vis: o = has('ekk')
    elif 'data-src=tbl' in vis: o = has('tbl')
    elif 'data-src=uni' in vis: o = has('uni')
    elif 'Westminster' in vis or 'same Confession' in vis: o = has('wcf')
    elif '(KJV)' in vis: o = has('kjv')
    elif 'Christian Baptist' in vis: o = has('cb')
    elif 'Declaration and Address' in vis: o = has('dna')
    elif ('<i>Apology</i>' in vis and 'Biography' not in vis) or 'letter to their congregations' in vis: o = has('apology')
    elif 'Biography' in vis: o = has('stone', 'apology')
    elif 'Last Will and Testament' in vis or 'Witnesses' in vis: o = has('will')
    elif 'Richardson' in vis or 'Campbell' in vis or 'Synod of Pittsburg' in vis: o = has('rich')
    else: o = []
    return o or list(range(len(K)))

# ---------- side path: quoting the Westminster Confession against itself ----------
WESTMINSTER = ('Quoting the Confession against itself',
               '<div class=eyebrow>Quoting the Confession against itself</div>', 'honoring its deepest impulses')
def westminster(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>Quoting the Confession against itself</div>'
        '<h2 style="max-width:none">The Westminster Confession</h2>'
        '<div class=sub>The standard they were all tried by.</div>'
        '<aside class=notes>A resource. Every Presbyterian minister, Seceder or not, swore to it: McNemar was tried by it in Kentucky (1803), Thomas Campbell by the Seceders (1807&ndash;08), and the Synod of Pittsburg cited it against him (1810). Each time the accused answered from the Confession itself.</aside></section>',

        Q('&ldquo;The whole counsel of God&hellip; is either expressly set down in Scripture, or by good and necessary consequence may be deduced from Scripture: <b>unto which nothing at any time is to be added</b>, whether by new revelations of the Spirit, or <b>traditions of men</b>.&rdquo;', WCF + ', 1.6') +
        N('Chapter 1, Of the Holy Scripture. Nothing to be added by &ldquo;traditions of men&rdquo;: a creed is a tradition of men.'),

        '<section class="slide"><div class=eyebrow>Westminster Confession &middot; chapter 1</div>'
        '<div class=litany style="text-align:left;gap:3.4vmin;margin-top:1.4vmin;max-width:88vw;font-size:1.3em">'
        '<div class="no frag"><b style="color:var(--gold)">1.9</b> &ldquo;The infallible rule of interpretation of Scripture is <b>the Scripture itself</b>&hellip;&rdquo;</div>'
        '<div class="no frag"><b style="color:var(--gold)">1.10</b> &ldquo;The supreme judge by which all controversies of religion are to be determined, and all decrees of councils&hellip; are to be examined&hellip; can be no other but <b>the Holy Spirit speaking in the Scripture</b>.&rdquo;</div>'
        '</div><div class=cite>' + WCF + '</div>'
        '<aside class=notes>Two clicks. Every council&rsquo;s decree is to be examined by Scripture, and the only supreme judge is the Spirit speaking in Scripture. That includes the synod, and the Confession itself.</aside></section>',

        '<section class="slide"><div class=eyebrow>The same Confession</div>'
        '<div class=litany style="text-align:left;gap:3.4vmin;margin-top:1.4vmin;max-width:88vw;font-size:1.3em">'
        '<div class="no frag"><b style="color:var(--gold)">20.2</b> &ldquo;<b>God alone is Lord of the conscience</b>, and hath left it free from the doctrines and commandments of men&hellip;&rdquo;</div>'
        '<div class="no frag"><b style="color:var(--gold)">31.3</b> &ldquo;All synods or councils, since the Apostles&rsquo; times, whether general or particular, <b>may err; and many have erred</b>. Therefore they are not to be made the rule of faith, or practice&hellip;&rdquo;</div>'
        '</div><div class=cite>' + WCF + '</div>'
        '<aside class=notes>Two clicks. Chapter 20, Of Christian Liberty and Liberty of Conscience; chapter 31, Of Synods and Councils (31.4 in the 1646 original). 31.3 ends: &ldquo;but to be used as a help in both.&rdquo; &rarr; A synod, by its own Confession, may err.</aside></section>',
    ] + list(extra) + [
        CARD('They were not breaking with their tradition.<br>' + G('They were honoring its deepest impulses.'),
             'Scripture the only infallible rule; God alone Lord of the conscience; councils may err. All of it in the Westminster Confession. They took it at its word, further than the synods would.'),
    ]

# ---------- side path: who governs the church ----------
GOVERNANCE = ('Church government', '<div class=eyebrow>Church government &middot; a resource</div>', 'Every other office answers to that')
def governance(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>Church government &middot; a resource</div>'
        '<h2 style="max-width:none">Who governs the church?</h2>'
        '<div class=sub>What Jesus said, what the Confession said,<br>what Cane Ridge willed, and what Brush Run did.</div>'
        '<aside class=notes>A resource, to take when the room asks. The sources run in order: Matthew 18, the priesthood texts, Westminster 30, the <i>Declaration and Address</i>, the Witnesses&rsquo; Address and the Last Will, Alexander Campbell.</aside></section>',

        Q('&ldquo;&hellip;<b>tell it unto the church</b>: but if he neglect to hear the church, let him be unto thee as an heathen man and a publican. Verily I say unto you, <b>Whatsoever ye shall bind on earth shall be bound in heaven</b>&hellip;&rdquo;', 'Matthew 18:17&ndash;18 (KJV)', 'To the gathered church') +
        N('In Matthew 16:19 the keys go to Peter. Here the binding and loosing go to &ldquo;the church&rdquo;: the gathering that hears a brother&rsquo;s trespass. The next verses: two who agree; two or three gathered.'),

        Q('&ldquo;For where <b>two or three are gathered together in my name</b>, there am I in the midst of them.&rdquo;', 'Matthew 18:20 (KJV)') +
        N('The <i>Declaration and Address</i> quotes it to the friends of reform: &ldquo;Let not the paucity of your number&hellip; prove an insuperable discouragement.&rdquo;'),

        Q('&ldquo;&lsquo;What ye bind on earth shall be bound in heaven&rsquo; is <b>the awful sanction of the Church&rsquo;s judgment</b>, in justly rejecting any person. Take away this, and it has no sanction at all.&rdquo;', DA, 'Thomas Campbell on Matthew 18 &middot; Appendix') +
        N('Matthew 18:18 gives the church&rsquo;s verdict heaven&rsquo;s weight. So to cast someone out over an opinion is to pronounce him lost: &ldquo;Does he not henceforth become to us as a heathen man and a publican?&rdquo; The weight is why the church must not spend it on opinions.'),

        Q('&ldquo;An individual church or congregation of Christ&rsquo;s disciples is <b>the only ecclesiastical body recognized in the New Testament</b>. Such a society is &lsquo;the highest court of Christ&rsquo; on earth.&rdquo;', 'Alexander Campbell, <i>Christian Baptist</i>, July 5, 1824') +
        N('From &ldquo;Essays on Ecclesiastical Characters, Councils, Creeds, and Sects, No. III.&rdquo; Every session, presbytery, synod, assembly or conference that legislates or rules &ldquo;essentially becomes &lsquo;the man of sin and the son of perdition.&rsquo;&rdquo; He then reprints Alexander Carson on Matthew 18: &ldquo;Here the last appeal is to the church. He does not say, If he does not hear the church, take him to the presbytery&hellip;&rdquo;'),

        '<section class="slide"><div class=eyebrow>Every believer</div>'
        '<div class=litany style="gap:3vmin;font-size:1.35em;max-width:84vw">'
        '<div class="no frag">&ldquo;But ye are a chosen generation, <b>a royal priesthood</b>, an holy nation, a peculiar people&hellip;&rdquo; <span class=lcite>1 Peter 2:9 (KJV)</span></div>'
        '<div class="no frag">&ldquo;And hath made us <b>kings and priests unto God</b> and his Father&hellip;&rdquo; <span class=lcite>Revelation 1:6 (KJV)</span></div>'
        '</div><aside class=notes>Two clicks. Said of the whole church, not of an order within it. Richardson&rsquo;s note on Alexander&rsquo;s reply cites both.</aside></section>',

        '<section class="slide"><div class=eyebrow>The other answer &middot; Westminster Confession, chapter 30</div>'
        '<div class=litany style="text-align:left;gap:3vmin;max-width:88vw;font-size:1.35em">'
        '<div class="no frag"><b style="color:var(--gold)">30.1</b> &ldquo;The Lord Jesus, as King and Head of his church, hath therein appointed a government, <b>in the hand of church officers</b>&hellip;&rdquo;</div>'
        '<div class="no frag"><b style="color:var(--gold)">30.2</b> &ldquo;To these officers <b>the keys of the kingdom of heaven are committed</b>&hellip;&rdquo;</div>'
        '</div><div class=cite>' + WCF + '</div>'
        '<aside class=notes>Two clicks. Of Church Censures. Matthew 18 gives the binding and loosing to the church; Westminster gives the keys to its officers. Richardson: Thomas Campbell, applying to the Synod of Pittsburg, accepted the Confession &ldquo;with the exception that&hellip; [he] objected to the chapter conferring power upon the clergy.&rdquo;</aside></section>',

        Q('&ldquo;&hellip;the New Testament is <b>as perfect a constitution for the worship, discipline, and government of the New Testament Church</b>&hellip; as the Old Testament was for the worship, discipline, and government of the Old Testament Church&hellip;&rdquo;', DA, 'Proposition 4') +
        N('The constitution is the New Testament. Nothing written since governs the church.'),

        Q('&ldquo;That although the Church of Christ upon earth must necessarily exist in <b>particular and distinct societies, locally separate one from another</b>, yet there ought to be no schisms, no uncharitable divisions among them.&rdquo;', DA, 'Proposition 2') +
        N('Local congregations, many; one church. The locality is natural; the division is the sin.'),

        Q('&ldquo;&hellip;they soon found that there was <b>neither precept nor example in the New Testament</b> for such confederacies as modern Church Sessions, Presbyteries, Synods, General Assemblies, etc.&rdquo;', WIT) +
        N('Researching a book on church government, the Springfield Presbytery found that it was itself one of these confederacies; it dissolved itself.'),

        '<section class="slide"><div class=eyebrow>The will&rsquo;s bequests on government</div>'
        '<div class=litany style="text-align:left;gap:2.4vmin;max-width:90vw;font-size:1.25em">'
        '<div class="no frag">To the church: &ldquo;assume her <b>native right of internal government</b>&hellip; and admit no other proof of their authority, but Christ speaking in them.&rdquo;</div>'
        '<div class="no frag">To each congregation: &ldquo;choose her own preacher&hellip; and <b>never henceforth delegate her right of government</b> to any man or set of men whatever.&rdquo;</div>'
        '<div class="no frag">To the ministers: &ldquo;obtain <b>license from God</b> to preach the simple Gospel&hellip;&rdquo;</div>'
        '</div><div class=cite>' + WILL + '</div>'
        '<aside class=notes>Three clicks. Cane Ridge, 1804. &ldquo;Native&rdquo;: it was always hers.</aside></section>',

        Q('&ldquo;Why do we contend for uninterrupted succession in ordination, seeing it is <b>not the persons called bishops who have the power, but the people?</b>&rdquo;', AC_R + ', sermon on Titus 1:5') +
        N('Brush Run, winter 1811&ndash;12. The same sermon: ordination &ldquo;consists in the choice of the people, which must be hearty.&rdquo;'),

        Q('&ldquo;As to the form or ceremony of ordination, he did not regard it as conferring any authority, but as <b>a public testimony that the persons ordained possessed the necessary authority</b>.&rdquo;', RICH) +
        N('Richardson&rsquo;s summary of Alexander&rsquo;s view, which he says &ldquo;he continued to maintain unchanged through life.&rdquo; Ordination recognizes; it does not confer.'),
    ] + list(extra) + [
        CARD('Christ in the midst of two or three.<br>' + G('Every other office answers to that.'),
             'The end of the resource. &rarr; Back to the spine.'),
    ]

# ---------- side path: the whole church remembers (the universals) ----------
UNIVERSALS = ('The whole church remembers', '<div class=eyebrow>The whole church remembers', 'we try to practice every Lord')
def _u(quote, cite, eyebrow='', note=''):
    """a quote slide whose quotes are checked against the whole-church excerpts"""
    return Q(quote, cite, eyebrow).replace('<section class="slide"', '<section data-src=church class="slide"', 1) + N(note)
def universals(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>The whole church remembers &middot; a resource</div>'
        '<h2 style="max-width:none">What the whole church knows</h2>'
        '<div class=sub>The priesthood of all &middot; the governance of all<br>baptism &middot; the table every Lord&rsquo;s day</div>'
        '<aside class=notes>A resource. The claim: the Church of Christ stands for what is most universal in the church, and is distinctive only where others have let one of these slip. Catholic, Orthodox, Lutheran and ecumenical voices, in their own words. Every quote is in the document &ldquo;The whole church.&rdquo;</aside></section>',

        # the priesthood of all
        _u('&ldquo;The New Testament never uses the term &lsquo;priesthood&rsquo; or &lsquo;priest&rsquo; (<i>hiereus</i>) to designate the ordained ministry&hellip; the term is reserved&hellip; for the unique priesthood of Jesus Christ and&hellip; for <b>the royal and prophetic priesthood of all baptized</b>.&rdquo;',
           'World Council of Churches, <i>Baptism, Eucharist and Ministry</i> (1982), Ministry 17', 'The priesthood of all',
           'The Lima text: the most widely studied ecumenical document of the century, drafted by a commission that included Catholic and Orthodox theologians.'),
        _u('&ldquo;The gift of the Spirit that every member of the faithful receives in the sacrament of initiation is <b>the charism of royal priesthood</b>.&rdquo;',
           'Nicolas Afanasiev, <i>The Church of the Holy Spirit</i>, p. 3', 'Orthodox',
           'A Russian Orthodox theologian in Paris (d. 1966). His second chapter is titled &ldquo;The Ordination of Laics&rdquo;: every baptized Christian is ordained.'),
        _u('&ldquo;The first, the basic definition of man is that <b>he is the priest</b>.&rdquo;',
           'Alexander Schmemann, <i>For the Life of the World</i> (1963)', 'Orthodox',
           'Not of clergy: of every human being, who receives the world from God and offers it back. The same book: &ldquo;Religion is needed where there is a wall of separation between God and man. But Christ&hellip; has broken down the wall&hellip; He has inaugurated a new life, not a new religion.&rdquo; (Page to verify against the book.)'),

        # the governance of all
        _u('&ldquo;&hellip;I made up my mind to do nothing on my own private opinion, without your advice and <b>without the consent of the people</b>.&rdquo;',
           'Cyprian, bishop of Carthage, c. 250', 'The governance of all',
           'A bishop of the third century, to his clergy, on how he had governed from the beginning.'),
        _u('&ldquo;<b>He who is to govern all, should be chosen by all.</b>&rdquo;',
           'Leo the Great, bishop of Rome, Letter 10 (444)', '',
           'The next sentence: &ldquo;The consent of the clergy, the testimony of those held in honour, the approval of the orders and the laity should be required.&rdquo; A pope.'),
        '<section data-src=church class="slide"><div class=eyebrow>Luther, 1523 &middot; for the congregation at Leisnig</div>'
        '<div class=litany style="font-size:1.6em;max-width:86vw;gap:3.4vmin">'
        '<div class="no frag">&ldquo;&hellip;<b>the sheep are to judge</b> whether what they teach is the voice of Christ or the voice of strangers.&rdquo;</div>'
        '<div class="no frag">&ldquo;All teachers should and must, therefore, be <b>subject with their teaching to the judgment of the hearers</b>.&rdquo;</div>'
        '</div><div class=cite>Martin Luther, <i>That a Christian Assembly or Congregation Has the Right and Power to Judge All Teaching and to Call, Appoint, and Dismiss Teachers</i> (1523)</div>'
        '<aside class=notes>Two clicks. Leisnig had dismissed the priest its patron appointed and elected its own. Luther: &ldquo;If the bishop does not confirm him, he is none the less confirmed by virtue of the call of the congregation.&rdquo; Later he settled for princes running the church. Our preachers answer to the congregation: this is why.</aside></section>',
        _u('&ldquo;&hellip;<b>the protector of religion is the very body of the Church, even the people themselves</b>&hellip;&rdquo;',
           'Encyclical of the Eastern Patriarchs (1848)', 'Orthodox',
           'The four Orthodox patriarchs, answering Pius IX: neither patriarchs nor councils could introduce novelties, because the people guard the faith. And at every Orthodox ordination the people still shout <i>Axios!</i>, &ldquo;He is worthy!&rdquo;, the trace of the time when the whole church chose.'),
        _u('&ldquo;&hellip;in this Church, as in an inverted pyramid, <b>the top is located beneath the base</b>. Consequently, those who exercise authority are called &lsquo;ministers&rsquo;, because, in the original meaning of the word, <b>they are the least of all</b>.&rdquo;',
           'Pope Francis, October 17, 2015', 'Catholic',
           'The same address quotes &ldquo;a principle dear to the Church of the first millennium&rdquo;: <i>quod omnes tangit ab omnibus tractari debet</i>, what touches all should be discussed by all.'),
        _u('&ldquo;<b>Juridical power is a substitute for love</b> in actual social life&hellip; In the Church, where perfect love dwells, there is no need for such a substitute.&rdquo;',
           'Nicolas Afanasiev, <i>The Church of the Holy Spirit</i>, p. 274', 'Why it is beautiful',
           'The case for congregational governance is not a legal one. Where love governs, the apparatus of power is unnecessary.'),

        # baptism
        '<section data-src=church class="slide"><div class=eyebrow>Baptism &middot; the Synod on Synodality, 2024</div>'
        '<div class=litany style="font-size:1.6em;max-width:86vw;gap:3.4vmin">'
        '<div class="no frag">&ldquo;There is <b>nothing higher than this baptismal dignity</b>, equally bestowed upon each person&hellip;&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;as well as constituting the basis of synodality, <b>Baptism is also the foundation of ecumenism</b>.&rdquo;</div>'
        '</div><div class=cite>Final Document of the Synod on Synodality, October 26, 2024, &sect;21, &sect;23</div>'
        '<aside class=notes>Two clicks. Received by Pope Francis as part of his ordinary teaching. Baptism, not ordination, as the root of the church&rsquo;s life and of its unity.</aside></section>',
        _u('&ldquo;Our common baptism, which unites us to Christ in faith, is thus <b>a basic bond of unity</b>.&rdquo;',
           'World Council of Churches, <i>Baptism, Eucharist and Ministry</i> (1982), Baptism 6', 'Baptism',
           'Baptism as what unites. Where baptism becomes a fence, a universal has slipped.'),

        # the table
        '<section data-src=church class="slide"><div class=eyebrow>The table every Lord&rsquo;s day</div>'
        '<div class=litany style="font-size:1.6em;max-width:86vw;gap:3.4vmin">'
        '<div class="no frag">&ldquo;&hellip;the Lord&rsquo;s Supper&hellip; <b>was now celebrated weekly</b>.&rdquo; <span class=lcite>Brush Run, 1811 &middot; Richardson, <i>Memoirs</i></span></div>'
        '<div class="no frag">&ldquo;As the eucharist celebrates the resurrection of Christ, it is appropriate that it should take place <b>at least every Sunday</b>.&rdquo; <span class=lcite><i>Baptism, Eucharist and Ministry</i> (1982), Eucharist 31</span></div>'
        '</div>'
        '<aside class=notes>Two clicks. A congregation by a creek in 1811, and the ecumenical movement in 1982, arriving at the same table.</aside></section>',
    ] + list(extra) + [
        Q('&ldquo;To the intent that now unto the principalities and powers in heavenly places <b>might be known by the church the manifold wisdom of God</b>&hellip;&rdquo;', 'Ephesians 3:10 (KJV)') +
        N('The church exists to show something. Our practices (no clergy class, members at the table, the congregation choosing, everyone singing) are testimony as much as order: a small visible demonstration of what the whole church confesses.'),
        CARD('What the whole church confesses,<br>' + G('we try to practice every Lord&rsquo;s day.'),
             'The end of the resource. Distinctive only where others let a universal slip. &rarr; Back to the spine.'),
    ]


# ---------- side path: Alexander Campbell, reread ----------
CAMPBELL_REREAD = ('Alexander Campbell, reread', '<div class=eyebrow>Alexander Campbell, reread', 'A future to rehearse')
AC_CB = 'Alexander Campbell, <i>The Christian Baptist</i>'
AC_MH = 'Alexander Campbell, <i>Millennial Harbinger</i>, September 1837'
AC_W = 'Alexander Campbell, &ldquo;Address on War,&rdquo; Wheeling, 1848'
def _a(quote, cite, eyebrow='', note=''):
    """a quote slide whose quotes are checked against the Campbell excerpts"""
    return Q(quote, cite, eyebrow).replace('<section class="slide"', '<section data-src=acr class="slide"', 1) + N(note)
def campbell_reread(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>Alexander Campbell, reread &middot; a resource</div>'
        '<h2 style="max-width:none">The ancient order was a hope,<br>not a fence</h2>'
        '<aside class=notes>A resource. Campbell is remembered as the father of the pattern: get the forms right. In his own words the ancient order was the means; freedom of conscience, the union of all Christians and a foretaste of the age to come were the end. Every quote is in the document &ldquo;Campbell, reread.&rdquo;</aside></section>',

        # the ancient order, reread
        _a('&ldquo;A restoration of the ancient order of things is all that is necessary to <b>the happiness and usefulness of christians</b>.&rdquo;',
           AC_CB + ', 1825', 'The ancient order, reread',
           'The first essay of the series, &ldquo;A Restoration of the Ancient Order of Things. No. I.&rdquo; Its measure: happiness and usefulness, not correctness. The same essay: &ldquo;we have had reformations enough.&rdquo;'),
        _a('&ldquo;Just in so far as the ancient order of things&hellip; is restored, <b>just so far has the Millennium commenced</b>, and so far have its blessings been enjoyed.&rdquo;',
           AC_CB + ', 1825', 'Not a rulebook: a foretaste',
           'Restoration looks forward. Recovering the church&rsquo;s first practices is how the age to come begins early, the same thought as Brush Run&rsquo;s table, &ldquo;an emblem of the millennial state of the Church.&rdquo;'),
        _a('&ldquo;If, then, the phrases &lsquo;Ancient Gospel,&rsquo; or &lsquo;Ancient Order of Things,&rsquo; should become <b>a dividing discrimination among Christians</b>, we must enter our protest against them&hellip;&rdquo;',
           AC_CB + ', 1829', 'Against his own slogan',
           'The next line: &ldquo;We now use them not for the discrimination of persons, but for the discrimination of truth from error.&rdquo; He foresaw the phrase becoming a badge, and protested in advance.'),
        _a('&ldquo;&hellip;the time will come when the terms <b>glad tidings, christian, and congregation</b>, without any epithet or adjunct, will be universally received&hellip;&rdquo;',
           AC_CB + ', 1829', '',
           'No party name, not even his own. The plain words, held in common by all.'),
        '<section data-src=acr class="slide"><div class=eyebrow>What the <i>Christian Baptist</i> was for &middot; 1830</div>'
        '<div class=litany style="font-size:1.75em;max-width:88vw;gap:2.8vmin">'
        '<div class="no frag">&ldquo;&hellip;to restore <b>a pure speech</b> to the people of God&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;to restore <b>the ancient order of things</b> in the christian kingdom&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;to <b>emancipate the conscience</b> from the dominion of human authority in matters of religion&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;for <b>the union of all christians</b>&rdquo;</div>'
        '</div><div class=cite>' + AC_CB + ', &ldquo;Concluding Remarks&rdquo; (1830)</div>'
        '<aside class=notes>Four clicks. His own summary of seven years. The ancient order is one item of four, and the list ends in conscience and union.</aside></section>',
        CARD('The ancient order was the means.<br>' + G('Freedom and union were the end.'),
             'The pattern served the promise. Read him the other way round and you get the legalism he is blamed for.'),

        # the open Campbell
        Q('&ldquo;<b>God loves his children more than our creeds</b>, and man was not made for the Bible, but the Bible for man.&rdquo;',
          AC_R + ', 1810', 'The open Campbell') +
        N('Twenty-one years old, explaining why he would not join a party: &ldquo;Because no party will receive into communion all whom God would receive into heaven.&rdquo;'),
        _a('&ldquo;But who is a Christian? I answer, Every one that believes in his heart that Jesus of Nazareth is the Messiah, the Son of God; repents of his sins, and obeys him in all things <b>according to his measure of knowledge of his will</b>.&rdquo;',
           AC_MH, 'Lunenburg, 1837',
           'He had written that &ldquo;we find in all Protestant parties Christians as exemplary as ourselves.&rdquo; A sister in Lunenburg, Virginia, wrote to object: how could the unimmersed be Christians? This is his answer.'),
        _a('&ldquo;I cannot, therefore, make <b>any one duty</b> the standard of Christian state or character, <b>not even immersion</b>&hellip;&rdquo;',
           AC_MH, 'Lunenburg, 1837',
           'The father of believer&rsquo;s immersion in our movement, refusing to make it the test of who is a Christian. He went on teaching immersion; he would not use it to unchurch anyone.'),
        _a('&ldquo;&hellip;I could not hesitate a moment in giving the preference of my heart <b>to him that loveth most</b>. Did I act otherwise, I would be a pure sectarian, <b>a Pharisee among Christians</b>.&rdquo;',
           AC_MH, 'Lunenburg, 1837',
           'The sentence before: &ldquo;Should I find a Pedobaptist more intelligent in the Christian Scriptures, more spiritually-minded and more devoted to the Lord than a Baptist&hellip;&rdquo; The letters that came in were angry; he answered them for months and did not retreat.'),
        _a('&ldquo;&hellip;we have no Christian nation or kingdom in the world, but that <b>Christ has one grand kingdom, composed of all the Christian communities in the world</b>&hellip;&rdquo;',
           AC_W, 'The Address on War',
           'Delivered in 1848, during the Mexican War, as a lecture on whether one Christian nation may make war on another. The church is one kingdom across every border, so the question becomes: can Christ&rsquo;s kingdom fight itself?'),
        _a('&ldquo;Their sovereign Lord, the King of nations, is called &lsquo;the Prince of Peace.&rsquo; How, then, could a Christian soldier&hellip; enlist to fight the battles of <b>a Caesar, a Hannibal, a Tamerlane, a Napoleon, or even a Victoria</b>?&rdquo;',
           AC_W, 'The Address on War',
           'He goes further than refusal: &ldquo;Why not&hellip; have a congress of nations and a high court of nations&rdquo; to settle disputes, decades before anyone built one. And: &ldquo;the moral desolations of war surpass even its horrors.&rdquo;'),
    ] + list(extra) + [
        CARD('Not a pattern to police.<br>' + G('A future to rehearse.'),
             'The end of the resource. Honest shadows: the same man was slow and divided on slavery, and later writers drew the narrower Campbell from him too. Both are in him; we choose which to inherit. &rarr; Back to the spine.'),
    ]

# ---------- side path: the church as ekklesia, the assembly ----------
EKKLESIA = ('The assembly', '<div class=eyebrow>The church as <i>ekklēsia</i>', 'The people, assembled')
LO = 'The Living Oracles, Alexander Campbell&rsquo;s New Testament (1826)'
def _e(slide):
    return slide.replace('<section class="slide', '<section data-src=ekk class="slide', 1)
def ekklesia(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>The church as <i>ekklēsia</i> &middot; a resource</div>'
        '<h2 style="max-width:none">The word Paul chose<br>was the name of the citizens&rsquo; assembly</h2>'
        '<aside class=notes>A resource. In every Greek city Paul visited, <i>ekklēsia</i> was the regular meeting of the citizens: the body that heard, debated and voted. Paul named the churches with that word. Scholars now argue the democratic overtones were deliberate; others trace the word to the Greek Old Testament&rsquo;s word for Israel&rsquo;s assembly (<i>qahal</i>). Both are assemblies of the whole people. Every quote is in the document &ldquo;The assembly.&rdquo;</aside></section>',

        _e(Q('&ldquo;Freedom&rsquo;s mark is also seen in this: <b>Who hath wholesome counsel to declare unto the state?</b>&hellip; What greater equality can there be in a city?&rdquo;',
             'Euripides, <i>Suppliants</i> (c. 423 BC), trans. Coleridge', 'Athens: the open floor') +
           N('Theseus, defending democracy to a king&rsquo;s herald. The line echoes what the herald cried at every Athenian assembly: <i>Tis agoreuein bouletai?</i>, &ldquo;Who wishes to speak?&rdquo; Any citizen could stand. Demosthenes remembers the morning Philip of Macedon took Elatea: &ldquo;the marshal put the question, Who wishes to speak? No one came forward.&rdquo; He calls that cry &ldquo;the civic voice of our country.&rdquo;',
             'All citizens over twenty could attend; votes were by show of hands. &ldquo;Citizens&rdquo; meant adult men only: women, slaves and foreigners were shut out.')),

        _e(Q('&ldquo;&hellip;it shall be determined in <b>a legal congregation</b>&hellip; And when he had said these things, <b>he dismissed the congregation</b>.&rdquo;',
             'Acts 19:39&ndash;41 &middot; ' + LO, 'The same word, in the New Testament') +
           N('The riot at Ephesus. The town clerk sends the mob home and points them to the city&rsquo;s regular assembly. Luke calls both the mob and the lawful assembly <i>ekklēsia</i>. Campbell&rsquo;s New Testament gives the civic assembly and the church one English word: congregation.')),

        _e(Q('&ldquo;&hellip;Paul wished to portray his communities as <b>alternative organizations existing alongside the civic assemblies</b>&hellip; in many respects, the functioning of the Christian <i>ekklēsia</i> mirrors the operations of the civic assemblies.&rdquo;',
             'George H. van Kooten, <i>New Testament Studies</i> (2012)', 'The scholars') +
           N('Van Kooten (Groningen, now Cambridge). Anna C. Miller, <i>Corinthian Democracy</i> (2015): the Corinthians understood themselves as &ldquo;a powerful, democratic assembly.&rdquo; Philip Esler, who thinks the word came from the Greek Old Testament, still says Paul&rsquo;s churches took on the connotations of &ldquo;civic voting assemblies.&rdquo;')),

        _e(Q('&ldquo;When you are come together, <b>each of you has a psalm, has a discourse</b>, has a foreign language, has a revelation, has an interpretation!&rdquo;',
             '1 Corinthians 14:26 &middot; ' + LO, 'The Christian assembly') +
           N('Not a herald asking who wishes to speak: the Spirit has given every member something to bring. &ldquo;To each is given the manifestation of the Spirit&rdquo; (12:7).')),

        '<section data-src=ekk class="slide"><div class=eyebrow>The floor passes &middot; 1 Corinthians 14:29&ndash;31</div>'
        '<div class=litany style="font-size:2.7em;max-width:88vw;gap:3vmin">'
        '<div class="no frag">&ldquo;&hellip;<b>and let the others judge</b>.&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;you can all prophesy, <b>one by one</b>,&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;<b>that all may learn, and all may be comforted</b>.&rdquo;</div>'
        '</div><div class=cite>' + LO + '</div>'
        '<aside class=notes>Three clicks. Speakers take turns; the gathered body weighs what is said. And the verse before: &ldquo;if to another, sitting by, any thing be revealed, let the first be silent.&rdquo; The floor passes. Caution: 14:34&ndash;35 silences women, against 11:5 where they pray and prophesy; many scholars think those verses were added later.</aside></section>',

        '<section data-src=ekk class="slide"><div class=eyebrow>The assembly decides</div>'
        '<div class=litany style="font-size:2.7em;max-width:88vw;gap:3vmin">'
        '<div class="no frag">&ldquo;&hellip;this punishment, which was inflicted <b>by the majority</b>.&rdquo; <span class=lcite>2 Corinthians 2:6</span></div>'
        '<div class="no frag">&ldquo;&hellip;who was also <b>chosen by the congregations</b> our fellow-traveller.&rdquo; <span class=lcite>2 Corinthians 8:19</span></div>'
        '</div><div class=cite>' + LO + '</div>'
        '<aside class=notes>Two clicks. A vote, and an election. The Greek for &ldquo;chosen&rdquo; in 8:19 is <i>cheirotonētheis</i>, literally &ldquo;by stretching out the hand&rdquo;: the word for electing by show of hands. Esler: 2:6 &ldquo;takes us straight into the dynamics of the political <i>ekklēsia</i> as a voting assembly.&rdquo;</aside></section>',

        _e(Q('&ldquo;&hellip;where I found this word <i>ecclesia</i>, <b>I interpreted it by this word congregation</b>.&rdquo;',
             'William Tyndale, answering Thomas More (1531)', 'The translators&rsquo; fight') +
           N('Tyndale&rsquo;s reason: the clergy had taken for themselves &ldquo;the term that of right is common unto all the whole congregation of them that believe in Christ.&rdquo; More attacked him for it. King James&rsquo;s rules for the 1611 translators, rule 3: &ldquo;the Word Churche not to be translated Congregation.&rdquo;')),

        _e(Q('&ldquo;<b>Wherever the word church is found</b> in the common version, <b>congregation will be found in this</b>.&rdquo;',
             'Alexander Campbell, appendix to the Living Oracles', 'Campbell takes Tyndale&rsquo;s side') +
           N('His reason: &ldquo;The term church, or kirk, is an abbreviation of the word <i>kyriou oikos</i>, the house of the Lord, and does not translate the term <i>ekklēsia</i>.&rdquo; In 1824 he had printed Alexander Carson&rsquo;s gloss: the Greeks, &ldquo;particularly the Athenians,&rdquo; used it &ldquo;for their popular assemblies&hellip; in which none but citizens had a right to sit.&rdquo;')),

        _e(BIG(Q('&ldquo;<b>The community, the church, the multitude of the faithful, are the fountain of official power.</b> This power descends from the body itself &mdash; not from its servants.&rdquo;',
                 'Alexander Campbell, <i>The Christian System</i> (1839)', 'Where authority comes from'))) +
        N('From his chapter on the ministry. It continues: &ldquo;How much surer and purer is ecclesiastic authority thus derived from Christ the head, immediately through his body, than when derived through a long, doubtful, corrupt dynasty of bishops or pontiffs!&rdquo;'),

        _e(BIG(Q('&ldquo;<b>Servants made by servants are servants of servants.</b>&rdquo;', 'Alexander Campbell, <i>The Christian System</i> (1839)'), 'clamp(44px,10vmin,130px)', '20ch')) +
        N('The next sentence after &ldquo;the fountain of official power.&rdquo; Against ordination handed down through a line of clergy: office comes from the body, through Christ, not from the officers.'),

        _e(Q('&ldquo;&hellip;<b>modern democracy began with the experience of the Puritan congregations</b>.&rdquo;',
             'A. D. Lindsay, <i>The Modern Democratic State</i> (1943)', 'And back again') +
           N('A political philosopher (Master of Balliol, Oxford), seeing it from the other direction: the self-governing congregation as the seedbed of modern democracy. The <i>ekklēsia</i> took the city&rsquo;s word; the city later learned from the congregation.')),
    ] + list(extra) + [
        CARD('Not a building. Not a clergy.<br>' + G('The people, assembled.'),
             'The end of the resource. <i>Ekklēsia</i> names the gathering, every member with a voice, under Christ. &rarr; Back to the spine.'),
    ]

# ---------- side path: who keeps the table ----------
TABLE = ('Who keeps the table', '<div class=eyebrow>Who keeps the table', 'Everyone waits on everyone')
CS_LOAF = 'Alexander Campbell, <i>The Christian System</i> (1839), &ldquo;Breaking the Loaf&rdquo;'
CM = 'Stone&rsquo;s <i>Christian Messenger</i>'
def _t(slide):
    return slide.replace('<section class="slide', '<section data-src=tbl class="slide', 1)
def table(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>Who keeps the table &middot; a resource</div>'
        '<h2 style="max-width:none">Who may give thanks<br>for the bread?</h2>'
        '<aside class=notes>A resource. Ask the room first: in your congregation, who gives thanks for the bread, and why that person? The answer in our churches (any disciple, not a priest) has two roots: the royal priesthood, and Matthew 18:20, where the smallest gathering is a church that may keep the Supper. It was contested from the start: in Scotland, between Campbell and Stone, and among us still. Every quote is in the document &ldquo;Who keeps the table.&rdquo;</aside></section>',

        _t(Q('&ldquo;&hellip;<b>where three are, a church is</b>, albeit they be laics.&rdquo;',
             'Tertullian, <i>On Exhortation to Chastity</i> 7 (c. 210)', 'Before us') +
           N('The sentence before: where there is no clergy, &ldquo;you offer, and baptize, and are priest, alone for yourself.&rdquo; Tertullian is echoing Matthew 18:20. The old church knew the thought; it did not keep it.')),

        _t(Q('&ldquo;The apparent question at issue was: <b>may a group of believers not set in order with a presbytery eat the Lord&rsquo;s Supper</b> or not?&rdquo;',
             'D. B. Murray, on the Scotch Baptists, <i>Baptist Quarterly</i> (1989)', 'Scotland') +
           N('The Scottish independents the Campbells knew in Glasgow were split on exactly this. Glasites and strict Scotch Baptists: no Supper without an elder. The Glasgow Scotch Baptists divided over &ldquo;eating without elders&rdquo; in 1810, the year after Alexander left. The British Churches of Christ grew from the side that ate without elders.')),

        _t(Q('&ldquo;&hellip;were only two christians in any place, <b>such as on shipboard</b>&hellip; they ought to commemorate the death of Christ on the first day of the week&hellip;&rdquo;',
             'Ballantine&rsquo;s <i>Essays on the Elder&rsquo;s Office</i>, reprinted in ' + CM + ' (1835)', 'Two or three') +
           N('The ground: &ldquo;our Lord gives directions, Mat. xviii. 15&mdash;20. to the smallest number that might thus meet in his name.&rdquo; Two or three gathered are a church, and a church keeps the Supper. (Recall Alexander on the Hibernia.)')),

        _t(BIG(Q('&ldquo;Is there any thing to be done at the table of the Lord, which <b>any brother, who can give thanks for a crucified Savior</b>, and repeat the words of the institution, cannot do?&rdquo;',
                 'The same essay, in ' + CM + ' (1835)'))) +
        N('It goes on: to suppose &ldquo;that none but an Elder can administer the Supper&rdquo; attributes &ldquo;some sanctity and power to an Elder which the scriptures do not warrant.&rdquo; Printed in Barton Stone&rsquo;s own paper.'),

        _t(BIG(Q('&ldquo;&lsquo;The administration of ordinances&rsquo; is <b>a popish phrase</b>, and ought to be cashiered from the christian vocabulary.&rdquo;',
                 'Alexander Campbell, <i>The Christian Baptist</i> (1827)', 'Campbell'))) +
        N('Answering a reader. He goes on: persons the church appoints, &ldquo;when attending their respective duties,&rdquo; are &ldquo;administering all the ordinances.&rdquo; The church&rsquo;s appointment is what gives &ldquo;an official right&rdquo;; no sacred power passes through it.'),

        _t(Q('&ldquo;He would not tolerate a disciple in his church to baptize a candidate, nor to &lsquo;administer the Lord&rsquo;s supper,&rsquo; <b>nor to pray over the loaf or the cup</b>.&rdquo;',
             'Alexander Campbell, <i>Millennial Harbinger</i> (1830)', 'The test of a clergy') +
           N('His proof that a preacher belongs to &ldquo;the aspiring priesthood&rdquo;: he will not let an ordinary disciple give thanks at the table. If he does permit it, Campbell says, &ldquo;I will except him from the priesthood.&rdquo;')),

        '<section data-src=tbl class="slide"><div class=eyebrow>A church with no bishop &middot; from Campbell&rsquo;s memorandum book</div>'
        '<div class=litany style="font-size:1.85em;max-width:88vw;gap:2.8vmin;text-align:left">'
        '<div class="no frag">&ldquo;&hellip;they had appointed <b>two senior members</b>, of a very grave deportment, <b>to preside in their meetings</b>.&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;he took a small loaf from the table, and in one or two periods <b>gave thanks for it</b>.&rdquo;</div>'
        '<div class="no frag">&ldquo;&hellip;<b>each one waiting upon his brother, until all were served</b>.&rdquo;</div>'
        '</div><div class=cite>' + CS_LOAF + '</div>'
        '<aside class=notes>Three clicks. About fifty members, no one fit to be a bishop; the two presiders &ldquo;were not competent to labor in the word and teaching.&rdquo; The loaf passed &ldquo;from one to another&rdquo;: &ldquo;no stiffness, no formality, no pageantry; all was easy, familiar, solemn, cheerful.&rdquo; Campbell&rsquo;s picture of the ancient order at the table.</aside></section>',

        _t(Q('&ldquo;He may of right <b>preach, baptize, and dispense the supper</b>, as well as pray for all men, when circumstances demand it.&rdquo;',
             'Alexander Campbell, <i>The Christian System</i> (1839)', 'His qualifier') +
           N('Of every Christian. But: &ldquo;This concession does not&hellip; authorize any individual to assume to do what has been given in charge to them&rdquo; (the appointed officers). &ldquo;Liberty without licentiousness, and government without tyranny.&rdquo; In 1840: &ldquo;Official grace and official virtue are the very essence of popery.&rdquo;')),

        _t(Q('&ldquo;For you cannot find in the New Testament one instance of the church having authority to ordain elders or bishops or deacons, or to administer baptism or the supper. <b>You will find that the ministry existed before the church</b>&hellip;&rdquo;',
             CM + ' (1830)', 'Stone&rsquo;s Christians') +
           N('Attributed to Stone by the <i>Messenger</i>&rsquo;s index. The Christians ordained their elders, kept the Supper seldom, and held that the ordained should administer it. The exact opposite of &ldquo;the fountain of official power.&rdquo;')),

        _t(Q('&ldquo;&hellip;they believe that <b>no person but a preacher has a right to administer the ordinances</b> &mdash; such as the breaking of the loaf&hellip;&rdquo;',
             'A letter from Lexington, Kentucky, February 1832 &middot; <i>Millennial Harbinger</i>', 'The union, 1832') +
           N('The month after Stone and &ldquo;Raccoon&rdquo; John Smith shook hands in Lexington. A local union of Christians and Reformers broke up over this: whether a church without an ordained preacher could break the loaf. They &ldquo;become very much alarmed at the idea of uncommon folks receiving the name of kings and priests to the Lord.&rdquo;')),

        _t(BIG(Q('&ldquo;When he is absent the church can do nothing. <b>Like a widow forlorn and desolate, she is solitary and silent.</b>&rdquo;',
                 'Alexander Campbell, &ldquo;The Union,&rdquo; <i>Millennial Harbinger</i> (1832)'))) +
        N('Campbell&rsquo;s reply, about the preacher &ldquo;called and sent&hellip; to administer ordinances&rdquo;: make him indispensable and the congregation cannot even meet at its own table.'),

        _t(Q('&ldquo;One, of course, leads in giving thanks. <b>This is not officiating, for any disciple can do this.</b> It does not pertain to any office.&rdquo;',
             'David Lipscomb, <i>Queries and Answers</i> (1910)', 'The Churches of Christ settle it') +
           N('Lipscomb (Gospel Advocate, Nashville): &ldquo;The elders, or those who preside, can call on any disciple to do this. He only expresses aloud and leads in what every disciple does.&rdquo; Our practice: members give thanks at the table; the elders arrange it.')),

        '<section data-src=tbl class="slide"><div class=eyebrow>Three paths from one table</div>'
        '<div class=litany style="font-size:1.7em;max-width:88vw;gap:2.8vmin;text-align:left">'
        '<div class="no frag">&ldquo;An ordained minister, as representative of Christ presiding at the Lord&rsquo;s Table, <b>serves in Christ&rsquo;s place as host</b> at the Table.&rdquo; <span class=lcite>Disciples&ndash;Catholic dialogue, 2009</span></div>'
        '<div class="no frag">&ldquo;&hellip;within Australian Churches of Christ <b>&lsquo;lay presidency&rsquo; is almost the norm</b>&hellip;&rdquo; <span class=lcite>Churches of Christ in Australia to the World Council, 1986</span></div>'
        '<div class="no frag">&ldquo;&hellip;we have denied women the opportunity to pass Communion trays because <b>we have described it as a &lsquo;leadership role.&rsquo;</b>&rdquo; <span class=lcite>David Kneip, Siburt Institute, ACU, 2025</span></div>'
        '</div>'
        '<aside class=notes>Three clicks. The Disciples, in dialogue with Rome, came back to the minister as Christ&rsquo;s representative; Campbell had said the one who breaks the loaf does so &ldquo;not as the representative of the Lord, but after his example.&rdquo; Australia kept mutual ministry. Our churches kept &ldquo;any disciple&rdquo; but read it as &ldquo;any man,&rdquo; and now argue whether passing a tray is leadership or service. In 2020 every household became its own table.</aside></section>',
    ] + list(extra) + [
        CARD('No one stands in Christ&rsquo;s place.<br>' + G('Everyone waits on everyone.'),
             'The end of the resource. &ldquo;Each one waiting upon his brother, until all were served.&rdquo; Open to all; hosted by any. &rarr; Back to the spine.'),
    ]

# ---------- resource: union, all his life (also built as its own deck: decks/src/unity/build.py) ----------
UNITY = ('Union, all his life', '<div class=eyebrow>Union, all his life', 'He never stopped saying it')
DA_TC = 'Thomas Campbell, <i>Declaration and Address</i> (1809)'
AC_R10 = 'Alexander Campbell, c. 1810 &middot; in Richardson, <i>Memoirs</i>'
MH37 = 'Alexander Campbell, <i>Millennial Harbinger</i>'
WAR = 'Alexander Campbell, &ldquo;Address on War,&rdquo; Wheeling, 1848'
def _n(slide):
    return slide.replace('<section class="slide', '<section data-src=uni class="slide', 1)
def _sec(title, sub):   # a section heading inside the resource
    return ('<section class="slide breath"><div class=eyebrow>Union, all his life</div><h2 style="max-width:none">%s</h2>'
            '<div class=sub>%s</div></section>' % (title, sub))
def unity(extra=()):
    return [
        '<section class="slide breath"><div class=eyebrow>Union, all his life &middot; a resource</div>'
        '<h2 style="max-width:none">The union of all Christians,<br>from his father&rsquo;s page to Lunenburg</h2>'
        '<aside class=notes>A resource, and its own deck. Alexander Campbell is remembered for the Ancient Order. He began with his father&rsquo;s plea for union, called it the first statement of the whole cause, and kept saying it through the Ancient Order years and after; and outside the Ancient Order he was a man of free inquiry and wide sympathy. Every Campbell quote is in the document &ldquo;Campbell on union.&rdquo;</aside></section>',

        # ---- his father's plea ----
        _sec('His father&rsquo;s plea', 'Washington, Pennsylvania, 1809'),
        BIG(Q('&ldquo;That the Church of Christ upon earth is <b>essentially, intentionally, and constitutionally one</b>&hellip;&rdquo;',
              DA_TC + ', Proposition 1', 'Thomas Campbell, 1809')) +
        N('It goes on: &ldquo;consisting of all those in every place that profess their faith in Christ and obedience to him in all things according to the Scriptures.&rdquo; Not one denomination: everyone, everywhere, who confesses Christ.'),
        Q('&ldquo;That division among the Christians is <b>a horrid evil, fraught with many evils</b>. It is antichristian, as it destroys the visible unity of the body of Christ; as if he were divided against himself&hellip;&rdquo;',
          DA_TC + ', Proposition 10') +
        N('Then: &ldquo;antiscriptural&hellip; antinatural.&rdquo; Division is not a difference of style. It is Christ divided against himself.'),
        _n(Q('&ldquo;While examining the proof-sheets of the &lsquo;Declaration and Address&rsquo;&hellip; <b>he was greatly impressed with the importance of the principles laid down</b>&hellip;&rdquo;',
             'Robert Richardson, <i>Memoirs of Alexander Campbell</i> (1868)', 'The son reads the proofs') +
           N('Autumn 1809: Alexander, just over from Scotland, read his father&rsquo;s pages as they came from the printer. He took them as his own program for life.')),
        _n(Q('&ldquo;&hellip;a project many years ago for <b>uniting the sects, or rather the Christians in all the sects</b>, upon a clear and scriptural bond of union&hellip; This was offered in the year 1809, in the &lsquo;Declaration and Address.&rsquo;&rdquo;',
             'Alexander Campbell, <i>The Christian System</i> (1839), Preface', 'Thirty years later, he says so') +
           N('&ldquo;The first piece that was written on the subject of the great position appeared from the pen of Thomas Campbell, Senior, in the year 1809.&rdquo; It made &ldquo;faith in Christ and obedience to him the only test of Christian character, and the only bond of church union.&rdquo; Wryly: &ldquo;It was indeed approved by all; but adopted and practised by none.&rdquo;')),

        # ---- the young Campbell ----
        _sec('No party man', 'The young Alexander, 1810&ndash;1811'),
        _n(BIG(Q('&ldquo;I dare not be a party man for these reasons&hellip; <b>Because no party will receive into communion all whom God would receive into heaven.</b>&rdquo;',
                 AC_R10), 'clamp(34px,7.6vmin,96px)', '32ch')) +
        N('An address after a sermon at Mr. Buchanan&rsquo;s; Richardson dates it only &ldquo;about this period&rdquo; (1810). Reason 1: &ldquo;Christ has forbidden me.&rdquo; Reason 3: &ldquo;The man that promotes the interests of a party stands next in guilt to the man that made it.&rdquo;'),
        _n(BIG(Q('&ldquo;<b>God loves his children more than our creeds</b>, and man was not made for the Bible, but the Bible for man.&rdquo;',
                 AC_R10), 'clamp(38px,8.4vmin,108px)', '26ch')) +
        N('The very next sentence of the same address. Twenty-one years old.'),
        '<section class="slide"><div class=eyebrow>Who is James Foster?</div>'
        '<div class=litany style="text-align:left;gap:2.6vmin;font-size:1.9em;max-width:88vw">'
        '<div class="no frag">Born in Ireland, 1785; knew Alexander as a boy at Rich-Hill.</div>'
        '<div class="no frag">&ldquo;An Independent in Ireland&rdquo;: already doubted infant baptism.</div>'
        '<div class="no frag">Came over in 1807; a member of the Christian Association from the start.</div>'
        '</div><div class=cite>' + RICH + '</div>'
        '<aside class=notes>Three clicks. Thomas Hodgens&rsquo;s son-in-law; they sailed together and settled near Hickory. It was Foster who asked Thomas Campbell, riding together, &ldquo;Father Campbell, how could you, in the absence of any authority in the Word of God, baptize a child&hellip;?&rdquo; Later elder of Brush Run (1813). Alexander rode out to visit him in 1864; Foster outlived him, dying in 1869.</aside></section>',
        BIG(Q('&ldquo;&hellip;each should be required to give a satisfactory answer to the question: <b>What is the meritorious cause of a sinner&rsquo;s acceptance with God?</b>&rdquo;', RICH, 'Thomas Campbell&rsquo;s test, spring 1811')) +
        N('Before forming the church at Brush Run, Thomas had each member give &ldquo;some personal and public evidence of a fitting knowledge of the way of salvation.&rdquo; Two answers were judged unsatisfactory; their admission was postponed.',
          'A doctrinal test at the door, from the author of the <i>Declaration and Address</i>.'),
        BIG(Q('&ldquo;<b>Is James Foster a member</b>, not having been present at the time the test question was propounded?&rdquo;', RICH, 'May 4, 1811 &middot; the day of organizing')) +
        N('Foster had missed the meeting where the question was asked. &ldquo;Some seemed to think not.&rdquo;'),
        _n(BIG(Q('&ldquo;Certainly, James Foster is a member, <b>having been with us from the beginning</b>, and his religious sentiments being perfectly well known to all.&rdquo;',
                 'Alexander Campbell, Brush Run, May 4, 1811 &middot; in Richardson, <i>Memoirs</i>', 'Alexander stands up'))) +
        N('Alexander was &ldquo;not entirely convinced that there was any authority for such a test.&rdquo;',
          'Richardson: &ldquo;The test question, accordingly, was not propounded to him, nor to any one else afterward.&rdquo; No creed at the door, from the first day.'),

        # ---- free inquiry ----
        _n(Q('&ldquo;<b>I call no man master upon the earth</b>&hellip; I have endeavored to read the scriptures <b>as though no one had read them before me</b>&hellip;&rdquo;',
             'Alexander Campbell, <i>The Christian Baptist</i>, 1826', 'Free inquiry') +
           N('Even his father: &ldquo;there is no man with whom I have debated more, and reasoned more&hellip; than he.&rdquo; And against himself: &ldquo;I am as much on my guard against reading them to-day, through the medium of my own views yesterday, or a week ago, as I am against being influenced by any foreign name, authority, or system, whatever.&rdquo; No fixed pattern, not even his own.')),

        # ---- in the middle of the Ancient Order ----
        _sec('In the middle of the Ancient Order', 'The <i>Christian Baptist</i>, 1823&ndash;1830, and <i>The Christian System</i>'),
        _n(Q('&ldquo;I have no idea of seeing, nor one wish to see, the sects unite in one grand army&hellip; It is only <b>the disciples of Christ dispersed among them</b>, that reason and benevolence would call out of them. <b>Let them unite who love the Lord</b>&hellip;&rdquo;',
             'Alexander Campbell, <i>The Christian Baptist</i>, April 1825', 'The same months as &ldquo;the Ancient Order&rdquo;') +
           N('The first &ldquo;Restoration of the Ancient Order&rdquo; essays began that February. Not a merger of denominations (&ldquo;dangerous to our liberties and laws&rdquo;): the Christians scattered through every denomination, uniting. In 1837 he quoted this passage to prove he had always believed there were Christians among the sects.')),
        _n(BIG(Q('&ldquo;&hellip;if I thought there was <b>any man on this continent who would go farther than I to heal all divisions</b> and to unite all christians&hellip; I would travel on foot a hundred miles <b>to see him and to confess my faults to him</b>.&rdquo;',
                 'Alexander Campbell, <i>The Christian Baptist</i>, 1827', 'If anyone loved union more'))) +
        N('To a Baptist critic, Spencer Clack. He goes on: the union of all who acknowledge Jesus is &ldquo;the <i>summum bonum</i>, the grand ultimatum of all my &lsquo;writings, orations, lectures,&rsquo; and social prayers.&rdquo;'),
        _n(Q('&ldquo;&hellip;those human institutions supplanted the Bible, made the word of God of non-effect, <b>were fatal to the intelligence, union, purity, holiness, and happiness of the disciples of Christ</b>&hellip;&rdquo;',
             'Alexander Campbell, <i>The Christian System</i> (1839), Preface', 'Why he fought the creeds') +
           N('Not to put his own opinions in their place: the enterprise &ldquo;warred against them, not because of their hostility to any private or favorite opinions which were desired to be substituted for them.&rdquo; The creeds were against union.')),
        _n(Q('&ldquo;But the Bible will do no better if men approach it with a set of opinions or a human symbol in their minds. <b>For then it is not the Bible, but the opinions in the mind, that form the bond of union.</b>&rdquo;',
             'Alexander Campbell, <i>The Christian System</i> (1839)', 'And against <i>no creed but the Bible</i>') +
           N('A creed can hide inside the slogan that rejects creeds. He saw it.')),
        _n(Q('&ldquo;If, then, the phrases &lsquo;Ancient Gospel,&rsquo; or &lsquo;Ancient Order of Things,&rsquo; should become <b>a dividing discrimination among Christians</b>, we must enter our protest against them&hellip;&rdquo;',
             'Alexander Campbell, <i>The Christian Baptist</i>, 1829', 'Against his own slogan') +
           N('He saw the danger in his own phrase: the Ancient Order turning into one more party badge. He protested in advance.')),
        _n(Q('&ldquo;&hellip;to lay a foundation, <b>an imperishable foundation, for the union of all christians</b>, and for their co-operation in spreading the glorious gospel throughout the world.&rdquo;',
             'Alexander Campbell, <i>The Christian Baptist</i>, &ldquo;Concluding Remarks,&rdquo; 1830', 'What the Ancient Order was for') +
           N('His summary of seven years: restore the ancient order, emancipate the conscience, and lay a foundation for the union of all Christians. The order was the means; union was the end.')),
        '<section data-src=uni class="slide"><div class=eyebrow>Two propositions &middot; <i>The Christian System</i>, 1839</div>'
        '<div class=litany style="font-size:2.4em;max-width:90vw;gap:3vmin">'
        '<div class="no frag">&ldquo;1st. <b>Nothing is essential to the conversion of the world but the union and co-operation of Christians.</b>&rdquo;</div>'
        '<div class="no frag">&ldquo;2d. <b>Nothing is essential to the union of Christians but the Apostles&rsquo; teaching or testimony.</b>&rdquo;</div>'
        '</div><div class=cite>Alexander Campbell, <i>The Christian System</i>, &ldquo;Foundation of Christian Union&rdquo;</div>'
        '<aside class=notes>Two clicks. John 17: &ldquo;that they all may be one&hellip; that the world may believe.&rdquo; He goes on: &ldquo;Neither truth alone nor union alone is sufficient to subdue the unbelieving nations; but truth and union combined are omnipotent.&rdquo;</aside></section>',

        # ---- Lunenburg ----
        _sec('Lunenburg, 1837', 'Are there Christians among the sects?'),
        _n(BIG(Q('&ldquo;&hellip;if there be no Christians in the Protestant sects&hellip; for many centuries there has been no church of Christ, no Christians in the world; and the promises&hellip; have failed, and the gates of hell have prevailed against his church! <b>This cannot be; and therefore there are Christians among the sects.</b>&rdquo;',
             MH37 + ', September 1837', 'His answer to a sister in Lunenburg'), 'clamp(28px,6vmin,76px)', '44ch') +
           N('He had written that &ldquo;we find in all Protestant parties Christians as exemplary as ourselves.&rdquo; A woman in Lunenburg, Virginia, wrote to object: how could the unimmersed be Christians?')),
        '<section data-src=uni class="slide"><div class=eyebrow>Lunenburg, 1837</div>'
        '<div class=litany style="font-size:2.3em;max-width:90vw;gap:2.6vmin">'
        '<div class="no frag">&ldquo;But <b>who is a Christian?</b>&rdquo;</div>'
        '<div class="no frag">&ldquo;I answer, Every one that believes in his heart that Jesus of Nazareth is the Messiah, the Son of God; repents of his sins, and obeys him in all things</div>'
        '<div class="no frag"><b>according to his measure of knowledge of his will</b>.&rdquo;</div>'
        '</div><div class=cite>' + MH37 + ', September 1837</div>'
        '<aside class=notes>Three clicks: the question, the answer, and the phrase that carries it, &ldquo;according to his measure of knowledge.&rdquo;</aside></section>',
        _n(BIG(Q('&ldquo;I cannot, therefore, make <b>any one duty</b> the standard of Christian state or character, <b>not even immersion</b>&hellip;&rdquo;',
                 MH37 + ', September 1837'), 'clamp(38px,8.4vmin,108px)', '26ch')) +
        N('The rest of the sentence: nor &ldquo;in my heart regard all that have been sprinkled in infancy without their own knowledge and consent, as aliens from Christ and the well-grounded hope of heaven.&rdquo; He went on teaching immersion. He would not use it to unchurch anyone.'),
        _n(BIG(Q('&ldquo;It is the image of Christ the Christian looks for and loves; and this does not consist in <b>being exact in a few items</b>, but in general devotion to the whole truth as far as known.&rdquo;',
                 MH37 + ', September 1837'))) +
        N('The best single answer in his own words to the charge of legalism.'),
        _n(BIG(Q('&ldquo;&hellip;I could not hesitate a moment in giving the preference of my heart <b>to him that loveth most</b>. Did I act otherwise, I would be a pure sectarian, <b>a Pharisee among Christians</b>.&rdquo;',
                 MH37 + ', September 1837'))) +
        N('The sentence before: &ldquo;Should I find a Pedobaptist more intelligent in the Christian Scriptures, more spiritually-minded and more devoted to the Lord than a Baptist, or one immersed on a profession of the ancient faith&hellip;&rdquo;'),
        _n(Q('&ldquo;&hellip;the term Christian was given first to immersed believers&hellip; but we do not think that it was given to them because they were immersed, <b>but because they had put on Christ</b>&hellip;&rdquo;',
             MH37 + ', November 1837', 'The letters came') +
           N('Answering the objections that poured in.')),
        _n(Q('&ldquo;It would indeed fully open the eyes of the community to the fact that <b>there are but few &lsquo;Campbellites&rsquo; in the country</b>. Too many of my correspondents, however, seem to me to have written rather to show that they are not &lsquo;Campbellites&rsquo;&hellip;&rdquo;',
             MH37 + ', December 1837') +
           N('His readers were more exclusive than he was. Ask: where did the exclusivity come from?')),
        _n(Q('&ldquo;&hellip;what could mean all that we have written upon the union of Christians on apostolic grounds, <b>had we taught that all Christians in the world were already united in our own community</b>?&rdquo;',
             MH37 + ', December 1837', 'He did not retreat') +
           N('&ldquo;I have neither conceded nor surrendered any thing for which I ever contended; but that, on the contrary, the opinion now expressed&hellip; is one that I have always avowed.&rdquo; A plea for union only makes sense if there are Christians outside your own church.')),

        # ---- the open Campbell, beyond ----
        _sec('The open Campbell', 'Discussion, schools, and peace'),
        _n(BIG(Q('&ldquo;We must, then, all submit to the new order of things, and <b>do homage to his Majesty Free Discussion</b>.&rdquo;',
                 MH37 + ', February 1845'), 'clamp(38px,8.4vmin,108px)', '26ch')) +
        N('Honest context: this sentence opens his 1845 series &ldquo;Our Position to American Slavery,&rdquo; which held that the relation of master and slave was not in itself sinful and refused to make slavery a test of fellowship. His open principle, and his shadow, on the same page.'),
        _n(Q('&ldquo;&hellip;Government is wanting in the essential ends of its being&hellip; which makes not <b>the education of every child born upon its territory</b> its primary concern&hellip; <b>intelligence and freedom are but two names for the same thing</b>.&rdquo;',
             'Alexander Campbell, &ldquo;On Common Schools,&rdquo; Clarksburg, Virginia, 1841', 'Schools for every child') +
           N('He campaigned for tax-supported common schools in western Virginia and founded Bethany College (1840). Shadow: in 1841 Virginia, &ldquo;every child&rdquo; did not include enslaved children; in 1845 he called the ban on teaching slaves to read an &ldquo;unchristian ordinance.&rdquo;')),
        _n(Q('&ldquo;&hellip;we have no Christian nation or kingdom in the world, but that <b>Christ has one grand kingdom, composed of all the Christian communities in the world</b>&hellip;&rdquo;',
             WAR, 'The Address on War') +
           N('Delivered in 1848, after the Mexican War, on whether one Christian nation may make war on another. The church is one kingdom across every border; so can Christ&rsquo;s kingdom fight itself?')),
        _n(Q('&ldquo;Their sovereign Lord, the King of nations, is called &lsquo;the Prince of Peace.&rsquo; How, then, could a Christian soldier&hellip; enlist to fight the battles of <b>a Caesar, a Hannibal, a Tamerlane, a Napoleon, or even a Victoria</b>?&rdquo;',
             WAR) +
           N('And a proposal decades early: &ldquo;Why not&hellip; have a congress of nations and a high court of nations for adjudicating and terminating all international misunderstandings and complaints?&rdquo;')),
    ] + list(extra) + [
        CARD('From 1809 to 1848,<br>' + G('He never stopped saying it.'),
             'The end. The Church of Christ upon earth is one. The Ancient Order was meant to serve that, never to replace it. &rarr; Back to the spine.'),
    ]
