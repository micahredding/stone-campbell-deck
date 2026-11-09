# Carry forward (from Chapter 6 to Chapter 7)

Written 2026-11-08, after Chapter 6 was taught and published. Read this before starting Chapter 7.

## Chapter 7: where it starts

- Teacher page: `week7.md` (Story, Idea, Connections and three draft Ideas; the Narrative is still empty).
- Class site entry: `micahredding/stone-campbell`, `src/_data/classWeeks.json`, number 7, "Living into God's Future: The Millennial Harbinger" (still `anticipated`).
- Primary theme: **the future (eschatology)** (CLAUDE.md, theme 4), with the priesthood of all believers and unity as its fruit.
- The class email (sent text, 2026-11-08) teased it: in 1830 Campbell starts the *Millennial Harbinger*; "what did he think was coming, and what did it mean to live as if it had already begun?"
- Threads already planted in Chapters 5–6 to pick up:
  - Brush Run's first Supper (May 5, 1811): "an emblem of the millennial state of the Church". These are **Richardson's** words summarizing the sermon (*Memoirs* 1:369), not Campbell's verbatim. Credit them that way.
  - The *Millennial Harbinger* began in January 1830. Its title refers to the millennium in general; don't claim it was named for the Brush Run sermon.
  - Chapter 6's notes: Campbell's "highest court of Christ on earth" (*Christian Baptist*, July 5, 1824) and the *Christian System* "fountain of official power". Source links for every Chapter 6 quotation are in `week6.md` under "Sources for the quotations".
- Make a new quiz from `quizzes.md`. Don't build it from the slide material.

## Chapter 6 items left open (all optional)

- The class audio link for 2026-11-08, once Otter Creek posts it. Add it to `classWeeks.json` week 6 (`audio`) on the class site.
- Charles Wesley irony (slide "Anglicans reject the Methodists"). Either retitle the card "Even a Wesley rejects the Methodists" or relabel the quotation "Charles Wesley, on his brother's ordinations".
- Cuts suggested and not taken:
  - Vatican II 1964 (keep 2007).
  - Luther 1520–23 (keep "priest, bishop and pope" and the congregation's call).
  - Afanasiev.
  - Campbell's "clergy/laity" and "the brethren". Campbell quotes: ask first.
- "[Protestants]" in *Unitatis Redintegratio* 22 could read "[the separated Western communities]".
- Hagia Sophia background is a 960px copy. Swap in the full-size file (Wikimedia rate-limited us).

## How things work now (learned this round)

**Slide helpers** (`decks/src/week5/slides.py`):
- `BGC(card, img, pos, credit)` puts a title card over a photograph.
- `LIGHT(BGC(...), size)` is the lighter version: the picture is smaller, its sides fade, and the top is bright.
- `BGQS(quote, img, pos, credit)` puts a quotation over the same picture, darkened.
- `HIDE(...)` keeps a slide out of the deck. Log every cut in `decks/src/week5/WHERE_IT_WENT.md`.

**Images:**
- Chapter 6 images live in `decks/src/chapter6/images/`. Credits are in `credits_conflict.md` there.
- They are *linked*, not embedded: `IMG_O_*` keys in `decks/src/week3/build.py`. This keeps GitHub Pages deploys under the size that times out.
- Use the same pattern for Chapter 7 (e.g. `decks/src/chapter7/images/`).

**Publishing a taught chapter:**
- `mapdeck.build(..., drop_side=True)` builds the spine only.
- `build.py` embeds the images at ≤960px (see the Chapter 6 block in `decks/src/week5map/build.py`).
- Then run `node scripts/strip-deck-notes.mjs <deck> site/decks/week-N.html` in `micahredding/stone-campbell`.
- Add the deck to `src/_data/decks.json`. Mark the week `taught` with its `ideas` in `classWeeks.json`.
- Run `npm run build` to check, then push `main`.
- Don't commit the embedded copy here.

**Remote (Satechi):**
- It sends the arrow keys and Enter.
- The engine (`decks/src/week4map/engine-map.js`) maps:
  - Enter once: the document (or the map where there is none)
  - Enter twice: the map
  - ↑: back out
  - F5: fullscreen
  - `b` or `.`: black screen
- Test page: `decks/remote-test.html`.

**Deploys:**
- A failed GitHub Pages deploy ("updating pages" timeout) is fixed by a fresh commit to `main`, not a re-run.
- Browsers cache for about 10 minutes: Cmd-Shift-R.

**Class emails:**
- Give the text in chat for pasting. The Gmail connector rewrites links in drafts.
- Format: "Hey folks," then a recap, Slides / Class page / Class Audio links, "This Sunday:" teaser, then the sign-off (Micah, micahtredding@gmail.com).

**Wikimedia:**
- The API and upload servers rate-limit this environment.
- Find images through ordinary pages (WebSearch/WebFetch or a helper agent).
- Thumbnail widths must be 330/960/1280/1920/3840.

**Quotation checks:**
- Check every on-screen quotation for wording *and* context: label, date, who it was aimed at.
- In Chapter 6 the check caught misdated labels (e.g. "weeks before his ordination"), quotations shown as a person's own words that were really someone else's summary (Richardson's "emblem"), and an ellipsis that joined two separate documents (Brenz).
- Do the same for Chapter 7 before class.

## Repositories touched

- `micahredding/stone-campbell-deck`: this repo.
- `micahredding/stone-campbell`: the public class site.
- `micahredding/stone-campbell-database`: research notes. `Who May Ordain/` was updated this round.

## Research documented for later (2026-11-09)

- **Authority by consent** (`micahredding/stone-campbell-database`, `10 Research Projects/Arguments/Authority by Consent.md`): Campbell's 1840s case for organization by consent at every scale (the Guernsey "Project," 1843, Proposition 8: arrangements not enjoined are "conventional," "enacted by the authority of a whole community"), and Walter Scott's "Who made brother Campbell an organizer over us?" (1844). Also lists the critiques of pattern theology before 1870, including Richardson's "Faith versus Philosophy" (1857). Could serve Chapter 7 (forms judged by their purpose) or Chapter 13 (governance).
- Full texts, cleaned and summarized, in the database: `91 Extracted Text/Primary Periodicals/Millennial Harbinger/Church Organization and Expediency (1841-1849).md` (92 pieces) and `Faith versus Philosophy Exchange (1857-1858).md` (19 pieces). Readers: https://claude.ai/artifact/7y8xh7REirHJQqYU2YmLnP and https://claude.ai/artifact/GTwkh6JcrLbHHw1kE3GLGi (private).
