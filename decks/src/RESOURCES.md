# Shared resources: side paths any map deck can hang

Start here if you are a new session picking up the class decks. The code is `decks/src/resources.py`; the decks are built by `decks/src/mapdeck.py` (how the map works: `decks/src/week4map/README.md`).

## What a resource is

A resource is a function in `resources.py` that returns a list of slides, plus an anchor tuple `(label, first-slide anchor, last-slide anchor)`. To hang one in a chapter:

1. In `decks/src/weekN/slides.py`: `for _x in R.<name>(): A(_x)` right after the spine slide it should fork from.
2. In `decks/src/weekNmap/build.py`: add `R.<ANCHOR>` to `SIDE`, and its document key to `DOC_KEYS`.
3. Build: `SITE=<class site checkout> python3 decks/src/weekNmap/build.py`. The build checks every `&ldquo;…&rdquo;` quotation against the documents and prints `NOT FOUND` for any it cannot match. Fix every one before committing; quotations must be verified.

A slide is routed to its document by a `data-src=<key>` attribute on its `<section>` (see `doc_order` in `resources.py`), or otherwise by words in its citation (Westminster, Declaration and Address, Richardson…).

## The resources

| Resource | Function / anchor | Document key → file | Hung in |
|---|---|---|---|
| Quoting the Westminster Confession against itself | `westminster(extra)` / `WESTMINSTER` | `wcf` → `week4map/sources/westminster-confession-american.html` | Ch. 5 |
| Church government (Matthew 18, Westminster 30, the D&A, the Last Will, Campbell) | `governance()` / `GOVERNANCE` | `kjv`, `wcf`, `dna`, `will`, `cb` | Ch. 5 |
| The whole church remembers (priesthood, governance, baptism, the table, from Cyprian to the Lima text) | `universals()` / `UNIVERSALS` | `church` → `sources/the-whole-church.html` | Ch. 5 |
| Alexander Campbell, reread (the Ancient Order as liberation and foretaste; Lunenburg; the Address on War) | `campbell_reread()` / `CAMPBELL_REREAD` | `acr` → `sources/campbell-reread.html` | Ch. 5 |
| The assembly: the church as *ekklēsia* (the Greek citizens' assembly, 1 Cor 14, Tyndale, Campbell's "fountain of official power") | `ekklesia()` / `EKKLESIA` | `ekk` → `sources/ekklesia.html` | Ch. 5 |
| Who keeps the table (who may serve and preside at the Lord's Supper, from the Scotch Baptists to today) | `table()` / `TABLE` | `tbl` → `sources/the-table.html` | Ch. 5 |
| Union, all his life (Thomas Campbell's *Declaration and Address*, which Alexander endorsed; the 1810 "party man" address; the *Christian Baptist*; *The Christian System*; the Lunenburg letter; the open Campbell: free inquiry, schools, the Address on War) | `unity()` / `UNITY` | `uni` → `sources/campbell-unity.html` (D&A quotes check against `dna`) | Not in a chapter. **Its own deck:** `decks/union-all-his-life-map.html`, built by `python3 decks/src/unity/build.py` |

Whole source documents available to any deck (`docs(between, clean, keys)`): `rich` Richardson's *Memoirs* (excerpts), `dna` the Declaration and Address, `will` the Last Will, `stone` Stone's *Biography* ch. VII, `apology` the Springfield Presbytery's *Apology*, `wcf` the Westminster Confession, `kjv` Scripture, `cb` the *Christian Baptist* (July 1824), plus the four excerpt documents above.

## Where the research behind them lives

- **The research database**, `micahredding/stone-campbell-database` on GitHub (the GitHub copy of Micah's iCloud folder `Documents/3/research/stone-campbell-research`, synced from it by "Sync iCloud vault" commits; work added on GitHub reaches iCloud only when copied or pulled back). Folder `10 Research Projects/`:
  - `Ekklesia and Greek Democracy/`
  - `The Ecumenical Consensus/` (the Lima text, weekly communion, the Disciples–Catholic dialogue)
  - `Alexander Campbell Reread/` (including honest shadows: slavery and more)
  - `Who Keeps the Table/`
  - `Arguments/`: arguments in progress ("The Ancient Order as the Great Stream"; "The Priesthood of All, Anticipated")
- **In this repo:** `research/universals.md` (the "whole church" quotes with links).
- **Verification rule:** every quotation in these dossiers was read in its source; anything seen only second-hand is marked **to verify** and must not go on a slide until checked.

## Primary texts used (archive.org identifiers)

*The Christian Baptist*, Burnet ed. 1835 (`christianbaptis00burngoog`); *The Christian System*, 1871 printing (`christiansystem00camp`); *Millennial Harbinger* 1830, 1832, 1837 (`millennialharbinger1837`), 1845, 1851; *Popular Lectures and Addresses* (`popularlecturesa00camp`); Richardson's *Memoirs* vols. 1–2 (`memoirsofalexand00rich`, `memoirsofalexand12rich`); *Memoirs of Thomas Campbell* (`memoirsofelderth00camp`); the Living Oracles, 6th ed. 1839 (`sacredwritingsof00incamp`). Download `<identifier>_djvu.txt` from archive.org to search them; join hyphenated line breaks before matching.
