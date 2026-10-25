# Chapter 4's deck, as a map: the slides in decks/src/week4/slides.py, arranged as a spine
# with side paths. Content stays in slides.py; this file only says which runs of slides are
# side paths. (Chapter 4 has no separate linear deck; the spine is the straight run.)
#   python3 decks/src/week4map/build.py   ->  decks/week4-last-will-map.html
#
# A side path is a contiguous run of slides, named by an anchor phrase on its first and last
# slide. Everything not inside a side path is the spine. A side path hangs from the spine
# slide just before it, so a new slide added inside a run joins that side path.
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import mapdeck

SIDE = [
    # (label,                                first-slide anchor,                         last-slide anchor)
    ('Quoting the Confession against itself', 'Quoting the Confession against itself',     'honoring its deepest impulses'),
    ('David Rice',                            '<div class=eyebrow>David Rice</div>',       '<div class=eyebrow>David Rice</div>'),
    ('Church government',                     'Writing a book on church government',       'each particular church, as a body'),
    ('Our table',                             '<div class=eyebrow>Our table</div>',        '<div class=eyebrow>Our table</div>'),
    ('Addendum',                              "Reference material; not part of the telling", 'What this week touched'),
]
# Sections of the spine, for the map's labels: (label, anchor on the section's first slide)
SECTIONS = [
    ('Opening', 'Otter Creek'), ('The hook', 'The cold open.'),
    ('The five', 'A few years after Cane Ridge'), ('The trial and the break', '<h2>The Trial</h2>'),
    ('The rise', '<h2>The Rise of the Springfield Presbytery</h2>'),
    ('Why they dissolved', 'endeavored to cultivate a spirit of love'), ('The Last Will', '<h2>The Last Will &amp; Testament</h2>'),
    ('Close', 'for discussion'),
]

# The whole source documents, from the class site (stone-campbell-site/src/documents): the same full
# texts the quotes were checked against. Set SITE to the site checkout if it is not ~/projects/stone-campbell-site.
def docs(between, clean):
    return [
        {'key': 'will', 'title': 'The Last Will and Testament of the Springfield Presbytery',
         'sub': 'Cane Ridge, June 28, 1804 &middot; with the Witnesses&rsquo; Address',
         'html': clean(between('last-will-fulltext.njk', '<h2 id="epigraph">', '<!-- SOURCE CITATION -->'))},
        {'key': 'stone', 'title': 'Barton W. Stone, <i>Biography</i> (1847), chapter VII',
         'sub': 'His own account of the trial, the garden, the cost, and the will',
         'html': clean(between('biography-barton-stone-fulltext.njk', '<h3 id="bio-ch-7">', '<h3 id="bio-ch-8">'))},
        {'key': 'apology', 'title': 'The Springfield Presbytery&rsquo;s <i>Apology</i> (1804), Parts I and III',
         'sub': 'The five&rsquo;s own history (the trial, the protest, the letter to their congregations, the suspension) and their remarks on creeds and the Confession &middot; as reprinted in Stone&rsquo;s <i>Biography</i>',
         'html': clean(between('biography-barton-stone-fulltext.njk', '<h3 id="apology-i">', '<h2 id="apology-ii">')
                       + between('biography-barton-stone-fulltext.njk', '<h2 id="apology-iii">', '<h2 id="character">'))},
        {'key': 'dna', 'title': 'Thomas Campbell, <i>Declaration and Address</i> (1809)',
         'sub': 'The whole of it: Declaration, Address, Propositions, Appendix',
         'html': clean(between('declaration-and-address-fulltext.njk', '<h2 id="declaration">', '<!-- SOURCE CITATION -->'))},
        {'key': 'wcf', 'title': 'The Westminster Confession of Faith',
         'sub': 'The Synod&rsquo;s standard &middot; American text of 1788 (OPC edition; a few later amendments and small variants elsewhere)',
         'html': clean(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources', 'westminster-confession-american.html')).read())},
    ]

SHORT = {'will': 'The whole will', 'stone': 'Stone&rsquo;s own account', 'apology': 'The five&rsquo;s own history',
         'dna': 'The Declaration and Address', 'wcf': 'The Westminster Confession'}
DOC_DOORS = [('Stone&rsquo;s own account, whole', 'fiery ordeal', 1),
             ('The whole will', '<h2>The Last Will &amp; Testament</h2>', 0)]

# Which documents a slide's quotes are looked for in, read from its citation text.
def doc_order(vis, K):
    if '<i>Apology</i>' in vis and 'Biography' not in vis: return [K.index('apology')]
    elif 'Westminster' in vis or 'same Confession' in vis: return [K.index('wcf')]
    elif 'Declaration and Address' in vis: return [K.index('dna')]
    elif 'letter to their congregations' in vis: return [K.index('apology')]
    elif 'Biography' in vis: return [K.index('stone'), K.index('apology')]
    elif 'Last Will and Testament' in vis or 'Witnesses' in vis: return [K.index('will')]
    else: return list(range(len(K)))

mapdeck.build({
    'part': '4', 'key': 'w4', 'chapter': 'Chapter 4', 'title': 'Chapter 4 &middot; The Last Will and Testament',
    'out': 'decks/week4-last-will-map.html', 'source': 'decks/src/week4/slides.py', 'built_by': 'decks/src/week4map/build.py',
    'side': SIDE, 'sections': SECTIONS, 'docs': docs, 'short': SHORT, 'doc_doors': DOC_DOORS, 'doc_order': doc_order,
})
