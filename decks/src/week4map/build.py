# Chapter 4 as a map: the same slides as decks/week4-last-will.html, arranged as a spine
# with side paths. Content stays in decks/src/week4/slides.py; this file only says which
# runs of slides are side paths. Edit the slides there and both decks pick it up.
#   python3 decks/src/week4map/build.py   ->  decks/week4-last-will-map.html
#
# A side path is a contiguous run of slides, named by an anchor phrase on its first and last
# slide. Everything not inside a side path is the spine. A side path hangs from the spine
# slide just before it, so a new slide added inside a run joins that side path.
import os, re, json

SIDE = [
    # (label,                                first-slide anchor,                         last-slide anchor)
    ('Five years later: Thomas Campbell',     'Five years later, the same move',           'Five years later, the same move'),
    ('Quoting the Confession against itself', 'Quoting the Confession against itself',     'honoring its deepest impulses'),
    ('The Synod strikes back',                'sends a committee to win them back',        'pope of Rome had to suspend Luther'),
    ('What their research found',             'make the Presbytery of Springfield their king', 'a job only Christ can do'),
    ('The rest of the bequests',              'our name of distinction',                   'native right of internal government'),
    ('Why, in their own words',               'dying sinners who are kept from the Lord',  'dying sinners who are kept from the Lord'),
    ('Addendum',                              "Reference material; not part of the telling", 'What this week touched'),
]
# Sections of the spine, for the map's labels: (label, anchor on the section's first slide)
SECTIONS = [
    ('Opening', 'Otter Creek'), ('The hook', 'in more than ordinary bodily health'),
    ('The trial', 'fiery ordeal'), ('The cost', 'not only were churches divided'),
    ('It worked', 'It worked.'), ('The reading of the will', 'The reading of the will.'),
    ('Why', 'voluntary and happy death'), ('Our table', 'Our table'), ('Close', 'for discussion'),
]

os.environ['PART'] = '4'
src = open('decks/src/week3/build.py').read()
for line in ("open(out,'w').write(html)", 'print("wrote", out)'):
    assert line in src, line
    src = src.replace(line, 'pass')
ns = {'__name__': '__main__'}
exec(compile(src, 'decks/src/week3/build.py', 'exec'), ns)
html, S, js = ns['html'], ns['S'], ns['js']

assert all(s.count('class="slide') == 1 for s in S), 'one section per slide expected'
assert html.count('<section') == len(S)

def find(anchor, after=-1):
    hits = [i for i, s in enumerate(S) if anchor in s and i > after]
    assert hits, 'anchor not found: %r' % anchor
    return hits[0]

def title(i):
    t = re.sub(r'<aside.*?</aside>', '', S[i], flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&(rsquo|lsquo);', "'", t); t = re.sub(r'&(ldquo|rdquo);', '"', t)
    t = re.sub(r'&hellip;', '...', t); t = re.sub(r'&mdash;|&ndash;', '-', t); t = re.sub(r'&\w+;|&#\d+;', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()[:90] or '(black)'

side_of = [None] * len(S)
branches = []
for k, (label, a, b) in enumerate(SIDE):
    i = find(a); j = find(b, i - 1)
    assert j >= i, label
    for x in range(i, j + 1):
        assert side_of[x] is None, 'side paths overlap at slide %d' % x
        side_of[x] = k
    fork = i - 1
    while side_of[fork] is not None: fork -= 1     # the spine slide this hangs from
    branches.append({'label': label, 'fork': fork, 'slides': list(range(i, j + 1))})
spine = [i for i in range(len(S)) if side_of[i] is None]
sections = []
for label, a in SECTIONS:
    i = find(a)
    assert side_of[i] is None, label
    sections.append({'label': label, 'at': spine.index(i)})

MAP = {'spine': spine, 'branches': branches, 'sections': sections,
       'titles': [title(i) for i in range(len(S))]}

mjs = open('decks/src/week4map/engine-map.js').read().replace('/*MAP*/null', json.dumps(MAP))
assert js in html
html = html.replace(js, mjs)
html = html.replace('Chapter 4 &middot; The Last Will and Testament</title>', 'Chapter 4 &middot; The Last Will and Testament &middot; map</title>')
html = html.replace('</style>', open('decks/src/week4map/map.css').read() + '</style>')
html = re.sub(r'<div id=hint>.*?</div>',
              '<div id=hint>&rarr; / space next &middot; &darr; or 1&ndash;3 take a side path &middot; &uarr; back to the spine &middot; m map &middot; f fullscreen &middot; p presenter</div>'
              '<div id=doors></div><div id=crumb></div><div id=map></div>', html, flags=re.S)

out = 'decks/week4-last-will-map.html'
open(out, 'w').write(html)
print('wrote', out)
print('spine', len(spine), 'slides;', len(branches), 'side paths:',
      ', '.join('%s (%d, off slide %d)' % (b['label'], len(b['slides']), b['fork'] + 1) for b in branches))
