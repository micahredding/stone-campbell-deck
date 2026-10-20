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


# ---------- the whole documents, with every quoted passage marked ----------
# Texts come from the class site (stone-campbell-site/src/documents), the same full texts the
# deck's quotes were checked against. Each quoted run on a slide is found in its source and
# wrapped in <mark data-s="slide slide…">; anything that cannot be found is reported below.
import html as H
SITE = os.environ.get('SITE', os.path.expanduser('~/projects/stone-campbell-site')) + '/src/documents/'
def between(path, a, b):
    t = open(SITE + path).read(); i = t.index(a); return t[i:t.index(b, i)]
def clean(h):
    h = re.sub(r'<aside\b.*?</aside>', '', h, flags=re.S)
    h = re.sub(r'<div class="reading-pull">.*?</div>', '', h, flags=re.S)
    h = re.sub(r'<span[^>]*page-anchor[^>]*></span>', '', h)
    h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
    h = re.sub(r'\s(id|style)="[^"]*"', '', h)
    return h
DOCS = [
    {'key': 'will', 'title': 'The Last Will and Testament of the Springfield Presbytery',
     'sub': 'Cane Ridge, June 28, 1804 &middot; with the Witnesses&rsquo; Address',
     'html': clean(between('last-will-fulltext.njk', '<h2 id="epigraph">', '<!-- SOURCE CITATION -->'))},
    {'key': 'stone', 'title': 'Barton W. Stone, <i>Biography</i> (1847), chapter VII',
     'sub': 'His own account of the trial, the garden, the cost, and the will',
     'html': clean(between('biography-barton-stone-fulltext.njk', '<h3 id="bio-ch-7">', '<h3 id="bio-ch-8">'))},
]
DOC_DOORS = [('Stone&rsquo;s own account, whole', 'fiery ordeal', 1),
             ('The whole will', 'The reading of the will.', 0)]

def norm_map(pieces):
    """normalized letters/digits of all text pieces, with each char's (piece, offset)"""
    n, m = [], []
    for pi, (kind, t) in enumerate(pieces):
        if kind != 'text': continue
        for ci, c in enumerate(t):
            c = c.lower()
            if c.isalnum(): n.append(c); m.append((pi, ci))
    return ''.join(n), m
def nz(t): return ''.join(c.lower() for c in t if c.isalnum())

for d in DOCS:
    d['pieces'] = [('tag', x) if x.startswith('<') else ('text', H.unescape(x)) for x in re.split(r'(<[^>]+>)', d['html']) if x]
    d['norm'], d['map'] = norm_map(d['pieces'])
    d['labels'] = {}          # (piece, offset) -> set of slides

def segments(s):
    vis = re.sub(r'<aside class=notes>.*?</aside>', '', s, flags=re.S)
    out = []
    for q in re.findall(r'&ldquo;(.*?)&rdquo;', vis, flags=re.S):
        q = H.unescape(re.sub(r'<[^>]+>', '', q))
        out += [x for x in re.split(r'…|\.\.\.|\[[^\]]*\]', q) if len(nz(x)) >= 16]
    return out
def locate(d, seg):
    t = nz(seg); i = d['norm'].find(t)
    if i >= 0: return i, i + len(t)
    for oa in (0, 14, 28):                       # fuzzy: two windows found in order, at about the right distance;
        for ob in (0, 14, 28):                   # shifted inward to step over an OCR slip near either end
            a, b = t[oa:oa + 24], t[len(t) - ob - 24:len(t) - ob]
            if len(a) < 24 or len(b) < 24: continue
            i = d['norm'].find(a)
            while i >= 0:
                j = d['norm'].find(b, i)
                if j >= 0 and abs((j + len(b) + ob) - (i - oa) - len(t)) < len(t) * .15: return max(0, i - oa), j + len(b) + ob
                i = d['norm'].find(a, i + 1)
    return None
slide_doc, missed = {}, []
for si, s in enumerate(S):
    vis = re.sub(r'<aside class=notes>.*?</aside>', '', s, flags=re.S)
    if 'Biography' in vis: order = [1]
    elif 'Last Will and Testament' in vis or 'Witnesses' in vis: order = [0]
    else: order = [0, 1]
    for seg in segments(s):
        for di in order:
            r = locate(DOCS[di], seg)
            if r:
                for k in range(*r): DOCS[di]['labels'].setdefault(DOCS[di]['map'][k], set()).add(si)
                slide_doc.setdefault(si, di); break
        else:
            missed.append((si, seg))

def render_doc(d):
    """emit the document with marks; a space or punctuation mark between two runs quoted by the
    same slides joins them, even across a tag (We <em>will</em>, that…), so a quote reads as one"""
    import bisect
    pos = d['map']
    def lab_at(k): return frozenset(d['labels'].get(pos[k], ())) if 0 <= k < len(pos) else frozenset()
    out = []
    for pi, (kind, t) in enumerate(d['pieces']):
        if kind == 'tag': out.append(t); continue
        run, lab = [], None
        def flush():
            if not run: return
            txt = H.escape(''.join(run), quote=False)
            out.append('<mark data-s="%s">%s</mark>' % (' '.join(map(str, sorted(lab))), txt) if lab else txt)
        for ci, c in enumerate(t):
            if c.isalnum(): l = frozenset(d['labels'].get((pi, ci), ()))
            else:
                k = bisect.bisect_left(pos, (pi, ci))          # next letter after this char
                a, b = lab_at(k - 1), lab_at(k)
                l = a if (a and a == b) else frozenset()
            if l != lab: flush(); run, lab = [], l
            run.append(c)
        flush()
    return ''.join(out)
docs_out = [{'title': d['title'], 'sub': d['sub'], 'html': render_doc(d)} for d in DOCS]
doc_doors = []
for label, a, di in DOC_DOORS:
    f = find(a); assert side_of[f] is None, label
    doc_doors.append({'label': label, 'fork': f, 'doc': di})

MAP = {'spine': spine, 'branches': branches, 'sections': sections,
       'titles': [title(i) for i in range(len(S))],
       'docs': docs_out, 'slideDoc': slide_doc, 'docDoors': doc_doors}

mjs = open('decks/src/week4map/engine-map.js').read().replace('/*MAP*/null', json.dumps(MAP))
assert js in html
html = html.replace(js, mjs)
html = html.replace('Chapter 4 &middot; The Last Will and Testament</title>', 'Chapter 4 &middot; The Last Will and Testament &middot; map</title>')
html = html.replace('</style>', open('decks/src/week4map/map.css').read() + '</style>')
html = re.sub(r'<div id=hint>.*?</div>',
              '<div id=hint>&rarr; / space next &middot; &darr; or 1&ndash;3 take a side path &middot; &uarr; back to the spine &middot; z the quote in its document &middot; m map &middot; f fullscreen &middot; p presenter</div>'
              '<div id=doors></div><div id=crumb></div><div id=ctx></div><div id=map></div><div id=docv></div>', html, flags=re.S)

out = 'decks/week4-last-will-map.html'
open(out, 'w').write(html)
print('wrote', out)
print('spine', len(spine), 'slides;', len(branches), 'side paths:',
      ', '.join('%s (%d, off slide %d)' % (b['label'], len(b['slides']), b['fork'] + 1) for b in branches))
print('quote slides linked to a document:', len(slide_doc), '·', ', '.join('%d→%s' % (k + 1, DOCS[v]['key']) for k, v in sorted(slide_doc.items())))
for si, seg in missed: print('  NOT FOUND in source, slide %d: %s' % (si + 1, seg.strip()[:100]))
