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
#   WESTMINSTER, GOVERNANCE     -> (label, first-slide anchor, last-slide anchor) for SIDE
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
        'kjv': lambda: {'title': 'Scripture, King James Version',
            'sub': 'Passages on the church, its officers, and its table',
            'html': clean(src('sources', 'scripture-kjv.html'))},
    }
    return [dict(D[k](), key=k) for k in keys]

SHORT = {'rich': 'Richardson&rsquo;s <i>Memoirs</i>', 'dna': 'The Declaration and Address', 'will': 'The whole will',
         'stone': 'Stone&rsquo;s own account', 'apology': 'The five&rsquo;s own history', 'wcf': 'The Westminster Confession',
         'kjv': 'Scripture (KJV)'}

def doc_order(vis, K):
    has = lambda *k: [K.index(x) for x in k if x in K]
    if 'Westminster' in vis or 'same Confession' in vis: o = has('wcf')
    elif '(KJV)' in vis: o = has('kjv')
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
