# Chapter 5: what left the deck, and where it lives now

Chapter 5 (`decks/week5-brush-run-map.html`) was reshaped several times between 25 and 27 October 2026. Nothing was discarded. Everything that left the spine is in one of the places below. The last check (27 Oct 2026) compared every quotation and slide in all 28 committed versions of `decks/src/week5/slides.py` with the current sources and built decks. Every quotation is still on a slide somewhere, except the superseded drafts listed at the end.

## The reserve deck: "The Synod and the Reply"

`decks/reserve-synod-and-reply-map.html`. Its slides are `RES` in `decks/src/week5/slides.py` (the `RS(...)` calls). Build with `python3 decks/src/reserve5/build.py`.

- Alexander's first sermon (the grove, 1810; "one hundred and six sermons").
- The Synod of Pittsburg's refusal of Thomas Campbell (October 1810), its resolutions, and its "important reasons."
- Quoting the Westminster Confession against itself (`R.westminster`, as a side path).
- Alexander's reply (November 1810):
  - "lay preaching";
  - "The clergy are the opposite to the laity… we find no difference" (this one is also in *The Priesthood of All Believers*);
  - "exquisite keenness of distinction."
- Psalm 118 at Brush Run.
- "Two Wills, One Bequest."

## Shared resources (`decks/src/resources.py`; catalogue in `decks/src/RESOURCES.md`)

| Left the Ch5 spine | Now | Still hung in Ch5? |
|---|---|---|
| Arguments against bishop succession | `succession()` | Yes, as a side path. Also in *The Assembly Governs*. |
| Church government; Westminster 30 with D&A Propositions 2 and 4 | `governance()`, `constitution()` | Yes, as side paths. Also in *The Assembly Governs*. |
| Luther as a witness (1523), consent of the faithful | `consent()` inside `universals()` ("The whole church remembers") | Yes. Also in *The Assembly Governs*. |
| Weekly communion | `weekly()` | Yes (short form). The full form is the deck *Every Lord's Day*. |
| The church as *ekklēsia* | `ekklesia()` | Yes. |
| Who keeps the table | `table()` | Yes. Also in *The Priesthood of All Believers*. |
| Alexander's lifelong insistence on unity, including James Foster and the "party man" address | `unity()` | No. It is the deck *Union, All His Life* (`decks/src/unity`). |
| "Alexander Campbell, reread" | `campbell_reread()` | No. It is a side path in *Union, All His Life*. |
| Campbell's "democracy of the whole" | Dropped at Micah's direction (26 Oct). | No. The passage is still in the research database. |

## Moved within Chapter 5

- **Glasgow summary slides.** "He went to hear Greville Ewing" and the "from Chapter 2" Glasgow summary were replaced by the full Chapter 2 Glasgow sequence: hearing other preachers (Article 4), Ewing's house and the Haldanes, and the token.
- **Foster material** moved out to the unity resource (above).

## Superseded drafts, kept in git history only

Recover any of these with `git show <commit>:decks/src/week5/slides.py`.

- `a818a3a`, `a21b441`: the recap as portraits with the captions "So far" / "Unity in Communion." Replaced at Micah's direction by the current recap:
  - Stone, "Let the unity of Christians be our polar star" (*Christian Messenger* 6, 1832).
  - Thomas Campbell, "Resume that precious, that dear-bought liberty…" (*D&A*).
  - "Unused alternatives" below has the other quotes considered.
- `1d03049`: the short Glasgow slides described above.
- `95f1d1f`: an earlier wording of idea three ("Stone's side willed it in 1804. Tonight, the Campbells' side does it."). The line is still in the presenter notes of the recap documents slide.
- `0d6f485` and earlier: "Who gave him authority? That is tonight's question." This was an earlier opening question. It is now "Who has authority? / Who may serve the table?"

## Unused alternatives for the recap (all verified)

These quotes were considered for the recap and are not on the current slide.

- **Stone, 1835:** "For 32 years of my ministry I have kept in view the unity of Christians as my polar star." (*Christian Messenger* 9, p. 285.) Kept in `decks/src/sources/founders-on-unity.html`.
- **Thomas Campbell, from the *Declaration and Address*** (all checked against the class site's full text):
  - "With you all we desire to unite in the bonds of an entire Christian unity…"
  - "'Union in Truth' is our motto."
  - "That division among the Christians is a horrid evil…" (Proposition 10)
  - "…how to love and receive our brother… and yet refuse to hold communion with him, is, we confess, a mystery too deep for us."
  - "Unite with us in the common cause of simple evangelical Christianity…"
  - "It is not the voice of the multitude, but the voice of truth, that has power with the conscience."
- **Thomas Campbell, to the Synod (c. 1808):** "ready to forbear with you." It is in *Whose Conscience?*.

## Research behind all of it

Everything is in `micahredding/stone-campbell-database`, folder `10 Research Projects/`:

- Ekklesia and Greek Democracy
- The Ecumenical Consensus
- Alexander Campbell Reread
- Who Keeps the Table
- Arguments
- The Whole Church Sings
- Freedom of Conscience
- The Bible in Every Hand
- One Baptism
