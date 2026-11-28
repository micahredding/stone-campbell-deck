# Check every on-screen quotation in Chapter 9 against its source text, with the quote standard's tool
# (agent-framework/tools/quote_check.py; agent-framework/QUOTES.md). Each quote slide carries data-chk=<key>.
#   python3 decks/src/week9/check_quotes.py [DB] [QUOTE_CHECK]
import html, os, re, subprocess, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
DB = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, '..', 'stone-campbell-database')
QC = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, '..', 'agent-framework', 'tools', 'quote_check.py')
X = os.path.join(DB, '91 Extracted Text'); P = os.path.join(X, 'Primary Periodicals'); U = os.path.join(X, 'Universalism Sources (2026-11-24)')
SRC = {
    'hay': os.path.join(X, 'Early History of the Disciples in the Western Reserve (A. S. Hayden 1875).txt'),
    'rich2': os.path.join(X, 'Memoirs of Alexander Campbell Volumes 1-2 (Richardson, archive.org memoirsofalexand12rich).txt'),
    'mh1830': os.path.join(P, 'Millennial Harbinger', 'Millennial Harbinger 1830.md'),
    'mh1846': os.path.join(P, 'Millennial Harbinger', 'Millennial Harbinger 1846.md'),
    'cs': os.path.join(X, 'The Christian System (Alexander Campbell).md'),
    'eddy2': os.path.join(U, 'universalisminam02eddy.txt'),
    'winc31': os.path.join(U, 'universalrestora1831winc.txt'),
    'whit': os.path.join(U, 'modernhistoryun01whitgoog.txt'),
    'bax': os.path.join(X, 'Life of Elder Walter Scott (William Baxter 1874).txt'),
    'cb2': os.path.join(P, 'Christian Baptist', 'Christian Baptist Volume 2.md'),
    'cb6': os.path.join(P, 'Christian Baptist', 'Christian Baptist Volume 6.md'),
    'w18': os.path.join(DB, '10 Research Projects', 'Facts and Story (Campbell and Wright)', 'sources', 'wright-2018-meanings-of-history-JAT.txt'),
    'rog': os.path.join(DB, '10 Research Projects', 'Facts and Story (Campbell and Wright)', 'sources', 'rogers-1889-recollections-rains-chapter (web transcription).txt'),
    'hcba': os.path.join(DB, '10 Research Projects', 'The Church as Working Model (Wright)', 'sources', 'hcba.txt'),
}
spec = importlib.util.spec_from_file_location('w9', os.path.join(H, 'slides.py')); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
bad = 0
def items(s):
    # a quote slide (data-chk on the section), or a paired slide (data-chk on each quotation)
    pairs = re.findall(r'<span class=q data-chk="([^"]+)">(.*?)</span></p>', s, re.S)
    if pairs: return pairs
    k = re.search(r'data-chk="([^"]+)"', s)
    if not k: return []
    return [(k.group(1), re.search(r'<span class=q>(.*?)</span></p>', s, re.S).group(1))]
for i, s in enumerate(m.S, 1):
  for k, q in items(s):
      q = html.unescape(re.sub(r'<[^>]+>', '', q)).strip().strip('“”"').replace('…', '...')
      if k == 'none':
          print('%3d  SKIP  (checked by eye; see notes)  %s' % (i, q[:70])); continue
      r = subprocess.run([sys.executable, QC, q, SRC[k], '--context', '8'], capture_output=True, text=True)
      v = (r.stdout.strip().split('\n') or [''])[0].split(':')[0]
      ok = v in ('EXACT', 'ELLIPSIS')
      bad += not ok
      print('%3d  %-9s %-7s %s' % (i, v, k, q[:70]))
print('\n%d not exact' % bad)
