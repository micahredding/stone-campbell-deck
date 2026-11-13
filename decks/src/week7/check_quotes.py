# Check every on-screen quotation in Chapter 7 against its source text, with the quote standard's tool
# (agent-framework/tools/quote_check.py; agent-framework/QUOTES.md). Each quote slide carries data-chk=<key>.
#   python3 decks/src/week7/check_quotes.py [DB] [QUOTE_CHECK]
# DB defaults to ../stone-campbell-database beside this repo; QUOTE_CHECK to ../agent-framework/tools/quote_check.py.
import html, os, re, subprocess, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
DB = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'stone-campbell-database')
QC = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, '..', 'agent-framework', 'tools', 'quote_check.py')
X = os.path.join(DB, '91 Extracted Text'); P = os.path.join(X, 'Primary Periodicals'); ES = os.path.join(X, 'Eschatology Sources (2026-11-09)')
MHF = lambda y: os.path.join(P, 'Millennial Harbinger', 'Millennial Harbinger %s.md' % y)
SRC = {
    'cb1': os.path.join(P, 'Christian Baptist', 'Christian Baptist Volume 1.md'),
    'cb3': os.path.join(P, 'Christian Baptist', 'Christian Baptist Volume 3.md'),
    'cb5': os.path.join(P, 'Christian Baptist', 'Christian Baptist Volume 5.md'),
    'mh1830': MHF(1830), 'mh1833': MHF(1833), 'mh1834': MHF(1834), 'mh1840': MHF(1840), 'mh1841': MHF(1841), 'mh1855': MHF(1855),
    'cs': os.path.join(X, 'The Christian System (Alexander Campbell).md'),
    'dna': os.path.join(X, 'declaration-and-address-1809_fulltext.md'),
    'rich1': os.path.join(X, 'Memoirs of Alexander Campbell Volume 1 (Robert Richardson).md'),
    'pla': os.path.join(X, 'Popular Lectures and Addresses (Alexander Campbell 1863).md'),
    'lq1865': os.path.join(ES, 'lq1865.md'),   # Lard's Quarterly vol. 2 (Oct. 1864 - 1865)
    'cm6': os.path.join(P, 'Christian Messenger', 'Christian Messenger Volume 6 (1832).md'),
    'cm8': os.path.join(P, 'Christian Messenger', 'Christian Messenger Volume 8 (1834).md'),
    'cm13': os.path.join(P, 'Christian Messenger', 'Christian Messenger Volume 13 (1843).md'),
    'cm14': os.path.join(P, 'Christian Messenger', 'Christian Messenger Volume 14 (1844).md'),
    'lipcg': os.path.join(X, 'Civil Government (David Lipscomb).md'),
    'purv': os.path.join(ES, 'biographyofelder00purv.md'),
    'ev1834': os.path.join(P, 'The Evangelist', 'Issues 1832-1842'),
    'ainslie': os.path.join(ES, 'messageofdiscipl0000pete.md'),
    'cent': os.path.join(ES, 'centennialconven0000disc.md'),
    'cassius': os.path.join(ES, 'Black sources'),
    'hcba': os.path.join(DB, '10 Research Projects', 'The Church as Working Model (Wright)', 'sources', 'hcba.txt'),
}
spec = importlib.util.spec_from_file_location('w7', os.path.join(H, 'slides.py')); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
bad = 0
for i, s in enumerate(m.S, 1):
    k = re.search(r'data-chk="([^"]+)"', s)
    if not k: continue
    k = k.group(1)
    q = re.search(r'<span class=q>(.*?)</span></p>', s, re.S).group(1)
    q = html.unescape(re.sub(r'<[^>]+>', '', q)).strip().strip('“”"').replace('…', '...')
    q = re.sub(r'”\s*Thus Messiah prayed\.?$', '', q)
    if k == 'none':
        print('%3d  SKIP  (checked elsewhere; see notes)  %s' % (i, q[:70])); continue
    r = subprocess.run([sys.executable, QC, q, SRC[k], '--context', '8'], capture_output=True, text=True)
    v = (r.stdout.strip().split('\n') or [''])[0].split(':')[0]
    ok = v in ('EXACT', 'ELLIPSIS')
    bad += not ok
    print('%3d  %-9s %-7s %s' % (i, v, k, q[:70]))
    if not ok: print('      ' + '\n      '.join(r.stdout.strip().split('\n')[:6]))
print('\n%d quotation(s) need attention' % bad)
