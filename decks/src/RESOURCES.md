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
| Quoting the Westminster Confession against itself | `westminster(extra)` / `WESTMINSTER` | `wcf` → `week4map/sources/westminster-confession-american.html` | The reserve deck "The Synod and the Reply" (`decks/reserve-synod-and-reply-map.html`) |
| Church government (Matthew 18, the priesthood texts, the D&A on Matthew 18, the Last Will, Campbell) | `governance()` / `GOVERNANCE` | `kjv`, `dna`, `will`, `cb` | Ch. 5 |
| Confession or constitution (Westminster 30; D&A Propositions 4 and 2) | `constitution()` / `CONSTITUTION` | `wcf`, `dna` | Ch. 5 (beside Church government) |
| The whole church remembers (the priesthood of all; consent and the governance of all, with Luther 1523 as a witness; baptism that unites; Cyprian to the 2024 Synod) | `universals()` / `UNIVERSALS` | `church` → `sources/the-whole-church.html` | Ch. 5 |
| Every Lord's day (weekly communion: Acts 20:7, the *Didache*, Justin, Abitina, Calvin, the Lutheran Apology, Wesley, Vatican II, the 2024 Synod, Lima and the churches' answers, the Disciples–Catholic dialogue, Brush Run) | `weekly()` (short, 9 slides) / `weekly(full=True)`; `WEEKLY` | `lord` → `sources/every-lords-day.html` | Ch. 5 (short). **Its own deck:** `decks/every-lords-day-map.html`, `python3 decks/src/weekly/build.py` |
| The priesthood of all believers, in every tradition (1 Peter 2, Revelation 1 and 5, Tertullian, Luther 1520 and 1523, Vatican II, the 2024 Synod, Afanasiev, Schmemann, the Lima text, the Campbells) | `priesthood(table=...)` / `PRIESTHOOD` | `priest` → `sources/priesthood-of-all.html`, with `church`, `kjv`, `rich`, `acr` | **Its own deck:** `decks/priesthood-of-all-map.html`, `python3 decks/src/priesthood/build.py` (side path: Who keeps the table) |
| The consent of all (Cyprian, Leo, Luther 1523, the 1848 Patriarchs, Francis, Afanasiev): part of *The whole church remembers*, reusable alone | `consent()` | `church` | Inside `universals()`; in *The Assembly Governs* |
| Against succession ("not the persons called bishops… but the people"; "Who gave the Presbytery authority…?") | `succession()` / `SUCCESSION` | `rich` | Ch. 5; *The Assembly Governs* |
| **The Assembly Governs** (deck): `ekklesia()` + `consent()` + `governance()`, side paths `constitution()` and `succession()` | `decks/src/governance/` | `ekk`, `church`, `kjv`, `wcf`, `dna`, `will`, `cb`, `rich` | **Its own deck:** `decks/the-assembly-governs-map.html`, `python3 decks/src/governance/build.py` |
| **The Whole Church Sings** (deck): congregational singing as the priesthood of all (Colossians 3:16, Hebrews 13:15, 1 Peter 2:9, Pliny, Ignatius, Tertullian, Chrysostom, Augustine, Luther, Calvin, Wesley, Vatican II, Stone, the 1818 New York church, Campbell 1849); side path *The instrument question* (Campbell 1851, the 1906 census) | `singing()` / `SINGING`, `INSTRUMENT` | `sing` → `sources/the-whole-church-sings.html` | **Its own deck:** `decks/the-whole-church-sings-map.html`, `python3 decks/src/singing/build.py` |
| **Whose Conscience?** (deck): freedom of conscience claimed and extended (Romans 14, Tertullian, Augustine's turn, Luther at Worms, Calvin on Servetus, Schaff, Hubmaier, Castellio, Westminster 20.2, Williams, Madison, Thomas Campbell's Declaration, Protest to the Synod and Proposition 6, Alexander 1830, Vatican II, the ELCA); side path *The honest limits* (Campbell on the Fugitive Slave Law, 1851; the Berrien Disciples' reply) | `conscience()` / `CONSCIENCE`, `CONSCIENCE_LIMITS` | `consc` → `sources/freedom-of-conscience.html` (D&A quotes check against `dna`) | **Its own deck:** `decks/whose-conscience-map.html`, `python3 decks/src/conscience/build.py` |
| **The Bible in Every Hand** (deck): access to Scripture as the priesthood of all (Acts 17:11, Jeremiah 31, 1 John 2, 1 Peter 2, Chrysostom, Erasmus, Tyndale, Luther 1520, the Index of 1564 against *Dei Verbum* 1965, the Last Will, the Declaration, Campbell 1823 and 1826, the Living Oracles, the Six Nations chief's question, Campbell's own limit); side path *Who interprets?* (Trent, Dositheus, Purcell 1837) | `bible()` / `BIBLE`, `WHO_INTERPRETS` | `bible` → `sources/bible-in-every-hand.html` (D&A quotes check against `dna`) | **Its own deck:** `decks/the-bible-in-every-hand-map.html`, `python3 decks/src/scripture/build.py` |
| Alexander Campbell, reread (the Ancient Order as liberation and foretaste; Lunenburg; the Address on War) | `campbell_reread()` / `CAMPBELL_REREAD` | `acr` → `sources/campbell-reread.html` | Side path in the "Union, All His Life" deck (off the Ancient Order section); no longer in Ch. 5 |
| The assembly: the church as *ekklēsia* (the Greek citizens' assembly, 1 Cor 14, Tyndale, Campbell's "fountain of official power") | `ekklesia()` / `EKKLESIA` | `ekk` → `sources/ekklesia.html` | Ch. 5 |
| Who keeps the table (who may serve and preside at the Lord's Supper, from the Scotch Baptists to today) | `table()` / `TABLE` | `tbl` → `sources/the-table.html` | Ch. 5 |
| Union, all his life (Thomas Campbell's *Declaration and Address*, which Alexander endorsed; the 1810 "party man" address; the *Christian Baptist*; *The Christian System*; the Lunenburg letter; the open Campbell: free inquiry, schools, the Address on War) | `unity()` / `UNITY` | `uni` → `sources/campbell-unity.html` (D&A quotes check against `dna`) | Not in a chapter. **Its own deck:** `decks/union-all-his-life-map.html`, built by `python3 decks/src/unity/build.py` |

Whole source documents available to any deck (`docs(between, clean, keys)`): `rich` Richardson's *Memoirs* (excerpts), `dna` the Declaration and Address, `will` the Last Will, `stone` Stone's *Biography* ch. VII, `apology` the Springfield Presbytery's *Apology*, `wcf` the Westminster Confession, `kjv` Scripture, `cb` the *Christian Baptist* (July 1824), plus the four excerpt documents above.

## Planned resource decks (Micah, 2026-10-27)

1. The priesthood of all believers, in every tradition: **built** (`decks/src/priesthood`).
2. Church governance, *ekklēsia*, and the consent of all: **built** (`decks/src/governance`).
3. Weekly communion: **built** (`decks/src/weekly`).
5. Congregational singing as priesthood: **built** (`decks/src/singing`).
6. Access to Scripture as priesthood: **built** (`decks/src/scripture`).
7. Freedom of conscience: **built** (`decks/src/conscience`).
4. Baptism. Research for it goes into the research database (`10 Research Projects/`) first; then the decks are built the same way.

## Where the research behind them lives

- **The research database**, `micahredding/stone-campbell-database` on GitHub (the GitHub copy of Micah's iCloud folder `Documents/3/research/stone-campbell-research`, synced from it by "Sync iCloud vault" commits; work added on GitHub reaches iCloud only when copied or pulled back). Folder `10 Research Projects/`:
  - `Ekklesia and Greek Democracy/`
  - `The Ecumenical Consensus/` (the Lima text, weekly communion, the Disciples–Catholic dialogue)
  - `Alexander Campbell Reread/` (including honest shadows: slavery and more)
  - `Who Keeps the Table/`
  - `The Whole Church Sings/`
  - `Freedom of Conscience/`
  - `The Bible in Every Hand/`
  - `Arguments/`: arguments in progress ("The Ancient Order as the Great Stream"; "The Priesthood of All, Anticipated")
- **In this repo:** `research/universals.md` (the "whole church" quotes with links).
- **Verification rule:** every quotation in these dossiers was read in its source; anything seen only second-hand is marked **to verify** and must not go on a slide until checked.

## Primary texts used (archive.org identifiers)

*The Christian Baptist*, Burnet ed. 1835 (`christianbaptis00burngoog`); *The Christian System*, 1871 printing (`christiansystem00camp`); *Millennial Harbinger* 1830, 1832, 1837 (`millennialharbinger1837`), 1845, 1851; *Popular Lectures and Addresses* (`popularlecturesa00camp`); Richardson's *Memoirs* vols. 1–2 (`memoirsofalexand00rich`, `memoirsofalexand12rich`); *Memoirs of Thomas Campbell* (`memoirsofelderth00camp`); the Living Oracles, 6th ed. 1839 (`sacredwritingsof00incamp`). Download `<identifier>_djvu.txt` from archive.org to search them; join hyphenated line breaks before matching.
