# Map decks

A map deck is a slide deck laid out as a **map** instead of a single line. It has a **spine** (the talk if nothing else happens), **side paths** that hang off it, and **whole source documents** you can zoom into from any slide that quotes them. Chapter 4 is the first one: `decks/week4-last-will-map.html`.

The map deck is a **view**. It adds no content of its own. The slides come from the linear deck's source (`decks/src/week4/slides.py`), and the documents come from the class site's full texts. So an edit to a slide shows up in both the linear deck and the map deck on the next build. The linear deck (`decks/week4-last-will.html`) is unaffected and still builds as before.

## Files

| Path | What it is |
|---|---|
| `decks/src/week4map/build.py` | The build. Runs the Chapter 3 engine build for `PART=4`, then defines the side paths, loads and marks the documents, swaps in the map engine, and writes the outputs. **Edit the structure here.** |
| `decks/src/week4map/engine-map.js` | The runtime: navigation, doors, map overlay, document view, presenter window. Replaces `decks/src/week3/engine.js` in the map build only. |
| `decks/src/week4map/map.css` | Styles for the doors, breadcrumb, map, document view. Appended to the engine CSS. |
| `decks/src/week4map/sources/` | Documents not on the class site, each with a provenance comment at the top. Currently the Westminster Confession. |
| `decks/week4-last-will-map.html` | Output: the deck, one self-contained file. |
| `decks/week4-last-will-map.json` | Output: the deck's structure, for other tools (see **The sidecar**). |

## Build

```sh
python3 decks/src/week4map/build.py      # from the repo root
```

The build needs a checkout of the class site at `~/projects/stone-campbell-site`, or wherever `SITE=` points. It reads the full texts in that site's `src/documents/`.

The build prints the spine and side paths, which slides link to which document, and **every quotation it could not find in its source**. Treat an unmatched quote as a defect: either the slide misquotes, or the source is missing or damaged. As of 2026-10-20 there are none.

The build fails loudly (an `assert`) if an anchor phrase is missing or ambiguous, if side paths overlap, or if a slide holds more than one `<section>`.

## Structure: spine, side paths, sections

All three are defined by **anchor phrases**, which are text that appears in a slide's HTML. Anchors aren't slide numbers, so reordering slides in `slides.py` doesn't break the map.

```python
SIDE = [  # (label, first-slide anchor, last-slide anchor)
    ('Quoting the Confession against itself', 'Quoting the Confession against itself', 'honoring its deepest impulses'),
    ...
]
SECTIONS = [('The trial', 'fiery ordeal'), ...]   # labels on the map; anchor = the section's first slide
```

The rules:
- A side path is the **contiguous run** of slides from its first anchor to its last. A slide added inside that run joins the side path.
- Every slide not in a side path is on the spine.
- A side path **hangs from the spine slide just before it** (its *fork*). Several side paths in a row share one fork. That's how Idea 1 has three doors.
- An anchor resolves to the **first** slide containing it. Pick a phrase unique to the slide.
- Section anchors must land on spine slides.

## Documents

```python
DOCS = [{'key': 'will', 'title': ..., 'sub': ..., 'html': ...}, ...]   # order matters (see below)
SHORT = {'will': 'The whole will', ...}                                # labels on the map's sources row
DOC_DOORS = [('The whole will', 'The reading of the will.', 0), ...]  # (label, spine-slide anchor, doc index)
```

| key | Document | Source |
|---|---|---|
| `will` | Last Will and Testament, with the Witnesses' Address | site `last-will-fulltext.njk` |
| `stone` | Stone, *Biography* (1847), ch. VII | site `biography-barton-stone-fulltext.njk` |
| `apology` | *Apology* (1804), Part I (with the five's letter to their congregations) and Part III (remarks on creeds and the Confession) | same file, `#apology-i` and `#apology-iii` |
| `dna` | Thomas Campbell, *Declaration and Address* (1809) | site `declaration-and-address-fulltext.njk` |
| `wcf` | Westminster Confession, American text | `sources/westminster-confession-american.html` |

`clean()` strips each document's site sidenotes, pull quotes, page anchors, comments, and all `id`/`style` attributes. The `id`s have to go so they can't collide with the deck's.

**How quotes get marked.** For every slide:
1. Take the visible HTML (presenter notes removed) and collect every `&ldquo;…&rdquo;` run.
2. Split each run at ellipses and `[bracketed insertions]`. Keep pieces with at least 16 letters.
3. Choose which documents to search from the slide's citation text:
   - `<i>Apology</i>` (and no `Biography`) → apology. Checked first, since an *Apology* slide may name Westminster in a bracket.
   - `Westminster` / `same Confession` → wcf
   - `Declaration and Address` → dna
   - `letter to their congregations` → apology
   - `Biography` → stone, then apology
   - `Last Will and Testament` / `Witnesses` → will
   - anything else → all documents, in `DOCS` order.
4. Match on **letters and digits only**, so case, punctuation and spacing don't matter ("Caneridge" matches "Cane Ridge"). If there's no exact match, a fuzzy pass looks for two 24-letter windows in order at about the right distance. The windows are shifted inward to step over an OCR slip near either end.
5. Wrap each matched run in `<mark data-s="13 49">`. The numbers are **0-based slide indices** of every slide quoting that passage. Spaces and punctuation between two runs quoted by the same slides join them, even across a tag, so "We *will*, that…" reads as one highlight.

A slide's linked document (`slideDoc`) is the first document any of its quotes matched.

**To add a document:** put its HTML in `sources/` with a provenance comment (where it came from, when, and what it was checked against), or point at a site file. Add an entry to `DOCS` and `SHORT`. If slides cite it by name, add a rule in step 3. If it should be a door, add it to `DOC_DOORS` (forks must be spine slides). Rebuild and confirm the unmatched list is still empty.

## The sidecar: `decks/week4-last-will-map.json`

This is the deck's structure without the slide or document HTML. Read this instead of parsing the deck.

```jsonc
{
  "deck": "decks/week4-last-will-map.html",
  "source": "decks/src/week4/slides.py",
  "slides": [{"index": 14, "n": 15, "title": "Quoting the Confession…", "path": "Quoting the Confession against itself", "doc": "apology"}],
  "spine": [0, 1, 2, …],                       // slide indices, in order
  "branches": [{"label": "…", "fork": 12, "slides": [13]}],
  "sections": [{"label": "The trial", "at": 6}],   // "at" = position on the spine, not a slide index
  "docs": [{"index": 0, "key": "will", "title": "…", "short": "The whole will"}],
  "doc_doors": [{"label": "…", "fork": 30, "doc": 0}],
  "quotes": [{"slide": 4, "doc": "will", "text": "The Presbytery of Springfield, sitting at Cane Ridge"}],
  "unmatched": []
}
```

There are three ways of counting slides, so be careful which one you're using:
- `index` is 0-based and is what the engine and the `data-s` marks use.
- `n` is 1-based and is what the URL hash and the presenter window show.
- The counter on screen shows the position **along the current path** ("13 / 43", "side 2 / 5"), not the slide number.

## Runtime

### Controls (main window)

| Key | Action |
|---|---|
| → / space / PageDown, click right 4/5 | next build step, then next slide on the current path. At the end of a side path it returns to the fork. |
| ← / Backspace / PageUp, click left 1/5 | back |
| ↓, or 1–4 | take an exit from this slide. ↓ = first one not yet taken. Exits are side paths, then document doors. They appear as buttons once the slide is fully built. |
| ↑ | back to the fork, from anywhere on a side path |
| z, or the "⤢ in the document" button | zoom out to this slide's document with its quote lit (only on slides with a linked document; elsewhere z does nothing and the button is hidden). z or Esc again closes it. Inside the document, arrows scroll, and clicking a highlight zooms into that slide. |
| m | map overlay. Click a dot to go to that slide, or a page to open that document. r clears the visited trail. Esc closes. |
| p | presenter window |
| n | read / present mode · **s** notes strip · **f** fullscreen · **Home / End** spine ends |
| touch | swipe left/right = next/back, swipe up = take an exit, swipe down = back to the fork |

### URL

- `#N`: open at slide N (1-based).
- `?presenter=1`: presenter window (notes, NOW, NEXT along the path, the exits here, and a notice when the room is looking at a document).
- `?preview=1&off=0|1`: the presenter's thumbnail frames (current slide, or next on the path).
- `?mode=read|present`: initial mode.

### State (localStorage, keys prefixed `w4m`)

| Key | Value | Written by |
|---|---|---|
| `w4mseen` | JSON object. Slide indices that have been shown → `1`; also `"d0"`…`"d4"` for documents opened. **This is the visited trail.** Cleared with r on the map. | main window |
| `w4mcur` | current slide index | main |
| `w4mnext` | next slide index along the path (`-1` at the end) | main |
| `w4mdoors` | JSON `[[label, taken 0/1], …]` for the current slide's exits | main |
| `w4mdoc` | open document index, or `-1` | main |
| `w4mmode` / `w4mstrip` | `present`/`read`; notes strip `1`/`0` | main |
| `w4mcmd` | `"<ms>:<seq>:<command>"`: a command for the main window | presenter, or any other tool |

The presenter and preview windows never write state; only the main window does. The main window polls `w4mcmd` every 200 ms and runs a command whenever the value changes. The commands are `next`, `prev`, `door`, `door1`…`door4`, `up`, `map`, `mapoff`, `zoom`. The presenter also pushes `{w4m:1, cur, next, mode}` to its thumbnail frames with `postMessage`, because Chrome partitions storage for embedded frames.

localStorage is per browser and per origin. The trail lives only in the browser that showed the deck, so treat it as a convenience, not a record.

## Working with it from other tools

- **Drive the deck** from another window on the same origin: `localStorage.setItem('w4mcmd', Date.now()+':1:next')`. Change the value each time, since the deck only acts on a new value.
- **Read where the room has been:** parse `w4mseen` in the presenting browser.
- **Find every slide that quotes a passage:** in the sidecar, filter `quotes` by `doc`. In the deck, read the `<mark data-s>` attributes.
- **Link to a slide:** `week4-last-will-map.html#N`.
- **Check the deck's quotations** after editing slides or sources: rebuild and read the `NOT FOUND` lines, or the sidecar's `unmatched`.

## Making another chapter a map

The pieces are built for Chapter 4 and haven't been generalized yet:
- the source module (`decks/src/week4`, through `PART=4`)
- the output name
- the `w4m` storage prefix
- the "Chapter 4" heading on the map

To do Chapter 5, copy `week4map/` to `week5map/` and change those four. Then write that chapter's `SIDE`, `SECTIONS`, `DOCS` and `DOC_DOORS`. The better route, once a second chapter wants it, is to move the engine and CSS to a shared folder and pass the chapter's settings in.

## Verifying a change

1. Build. There should be no assertion errors and no `NOT FOUND` lines, unless you expected some.
2. Serve the folder (`cd decks && python3 -m http.server`) and open the deck in a browser. Playwright blocks `file://`.
3. Walk these paths:
   - a fork with several exits
   - a full side path, back to its fork, then onward
   - z from a quote slide, then click a different highlight to land on that slide
   - m, then click a dot and a page
   - p, with the presenter keys driving the main window
4. Add a cache-busting query (`?v=2`) when reloading, because browsers hold on to the old file.

## Known limits

- **A clicker can't take side paths or zoom.** It only sends next/back, so taking a path needs the keyboard, the number keys, or a tap on a door button.
- **The trail survives reloads.** Press m, then r, before teaching.
- **Not all documents have doors.** Only `will` and `stone` do. The others are reached by z from a quoting slide, or from the map.
- **The Westminster text is a modern American edition.** It's the OPC text, which follows the 1788 revision but has small variants and later amendments elsewhere. The quoted sections were checked against Schaff's 1647 text and agree (see the provenance comment in `sources/`).
- **Not tested in a room.** As of 2026-10-20 it has only been checked in a headless browser.

## Design rules

- **The map deck is a disposable view.** The canonical things are `slides.py`, the site's full texts and `sources/`. Never put content into `build.py` or the engine.
- **The spine must stand alone.** If no one takes a side path, the talk still works.
- **Side paths are made of material that already exists:** slides cut from the spine, glossed lines, sources. Not new material written for the map.
- **New features should read state, not add more of it.** Prefer derived views (from the sidecar, the marks, the trail) over new stored state.
