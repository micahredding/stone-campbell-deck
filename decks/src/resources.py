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
#   WESTMINSTER, GOVERNANCE,
#   UNIVERSALS, CAMPBELL_REREAD -> (label, first-slide anchor, last-slide anchor) for SIDE
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
        'kjv': lambda: {'title': 'Scripture, King James Version',
            'sub': 'Passages on the church, its officers, and its table',
            'html': clean(src('sources', 'scripture-kjv.html'))},
    }
    return [dict(D[k](), key=k) for k in keys]

SHORT = {'rich': 'Richardson&rsquo;s <i>Memoirs</i>', 'dna': 'The Declaration and Address', 'will': 'The whole will',
         'stone': 'Stone&rsquo;s own account', 'apology': 'The five&rsquo;s own history', 'wcf': 'The Westminster Confession',
         'kjv': 'Scripture (KJV)', 'cb': 'The <i>Christian Baptist</i>, 1824', 'church': 'The whole church',
         'acr': 'Campbell, reread'}

def doc_order(vis, K):
    has = lambda *k: [K.index(x) for x in k if x in K]
    if 'data-src=church' in vis: o = has('church') + [i for i in range(len(K)) if K[i] != 'church']
    elif 'data-src=acr' in vis: o = has('acr')
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
