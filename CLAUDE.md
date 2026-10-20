# Deck conventions (Our Wild Democracy)

- Build: `python3 decks/src/weekN/build.py` writes `decks/weekN-*.html`. Slides are Python strings in `decks/src/weekN/slides.py`; helpers `Q()` (quote), `N()` (notes), `C()` (card).
- Chapters 3b and 4 build with the Chapter 3 engine: `python3 decks/src/week3b/build.py`, `python3 decks/src/week4/build.py` (both run `decks/src/week3/build.py` with `PART` set).
- Merge every change to `main`.
- **Map decks** (Chapter 4: `decks/week4-last-will-map.html`, a spine with side paths, zoomable source documents, a map overlay) are a view built from the linear deck's `slides.py`. How they work, how to extend them, and how other tools can read or drive them: `decks/src/week4map/README.md`. Rebuild with `python3 decks/src/week4map/build.py` after changing Chapter 4's slides.
- Check every Declaration and Address quotation against the class site's full text (`~/projects/stone-campbell-site/src/documents/declaration-and-address-fulltext.njk`). The map build does this for every quotation in Chapter 4 and lists any it cannot find.
- Keep presenter notes accurate when slides move; keep them tight.
- Make text as large as the slide allows; match earlier weeks' formats (ideas, discussion, quiz, site slide).
- Opening quizzes come from `quizzes.md`, not from the slide material.
- Chapter 3b's presenter notes for slides 1–62 are generated from `week3b-transcript.md` (one `**Slide N · …**` section per slide). Edit notes there, and keep its slide numbers in step when slides move.
- Prioritize keeping Campbell quotations on screen; when simplifying, cut commentary and non-Campbell slides first, never move a Campbell quote to the notes without asking.

## Build-ins

A click adds more of the same kind of thing:
- a list of parallel items (e.g. Spirit / Scripture / Reason; "Not… Not… Christ itself"), or
- the next part of one sentence or question (e.g. "We speak… / …where the Bible speaks"; a question that keeps extending).

Never build a claim, a quotation, and a punchline onto one slide. Different kinds of statements get separate slides; supporting remarks go in the notes.
