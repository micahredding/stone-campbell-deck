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

- **Session one's ideas rewritten (Micah, 1 Nov 2026):** five ideas (the table that excludes; nothing required that God has not required; neither side is the gospel; the gates as wide as heaven; the table a foretaste), with a summary slide. Session two keeps two (the church gathers for the shut out; the priesthood makes its ministers). "The Lord's table turns no Christian away" was retired. Hidden: session one's "Every Lord's day" copy, and the D&A "This Society by no means considers itself a Church" slide.

- **"Who may come?" became title slides** (Micah, 1 Nov 2026): "They were rebuffed" and "Alexander's response" (November 1, 1810), with section slides "On baptism…" and "On creeds…" before each run.

- **"Two ways not to become a sect" is a side path** (Micah, 1 Nov 2026), off "the Society must obtain admission…": the title, the two-column slide (the Last Will beside "obtain admission") and what was *Becoming Baptists* (the 1813 overture, *The Christian Baptist*, "Refused by the Presbyterians, they became Baptists."), five slides in one path.

- **"Brush Run 1810–1811" (the meeting-house picture slide) became a title slide, "The Campbells seek out Presbyterian Communion"** (Micah, 1 Nov 2026). The meeting-house photograph (Bethany College) is no longer shown in Chapter 5; the image file is still in `decks/src/week5/`.

- **Act I reshuffle (Micah, 1 Nov 2026):** the "October 1808: the family sails" day-timeline is now a map (Londonderry, Inishowen, Malin Head, Loch Indaal; one click per stop; the dates are also in its notes; it starts at home, Rich Hill, County Armagh, four days overland from Londonderry). The Islay map now comes before "He had just vowed…"; "With his father an ocean away" before "He went to hear other preachers"; Robert Haldane's "Everything or nothing" right after "Ewing told him the story of the Haldanes". Hidden (`HIDE`): Richardson's "The avowed object in forming this church was…" (the Haldanes' Edinburgh church, 1799) and "…the principles of Congregationalism entertained by Mr. Ewing…" ("What he came to want"); the Haldanes' 1797 notice, "to two or two hundred… a preacher of the gospel" (Richardson, *Memoirs*).
- **The Islay map ("Where the sea left them") now uses slide 6's map** (Micah, 1 Nov 2026): Rich Hill, Londonderry, the route round Malin Head, the wreck in Loch Indaal, Glasgow. Slide 6 no longer says "all night before the gale" (it gave the storm away).
- **Session one's end reordered (Micah, 1 Nov 2026):** after the Synod's refusal, "Brush Run Church Formed" now comes before Thomas's "great reluctance", and "Three instigators, one table" moved after the sermon's close, just before the discussion.
- **Split into two decks (Micah, 1 Nov 2026):** session one (`decks/week5-brush-run-map.html`) ends at the black slide after "Next time: Brush Run and *Where two or three are gathered…*"; session two is `decks/week5b-brush-run-map.html`, numbered from 1. Nothing was dropped.
- **Hidden in session one (Micah, 1 Nov 2026):** the card "Still seeking a larger union, they became a church." and Richardson's "Why a church" ("…on account of the continued hostility of the different parties…"); the card's point is now in the notes of "great reluctance", and the card still opens session two. "On creeds…" now reads "On creeds as terms of communion…". "Brush Run Church Formed" (both copies) is now over the photograph of the rebuilt meeting house.
- **New title card (Micah, 1 Nov 2026):** "Alexander takes up his father's cause" (1809), after "Neither knew." and before "The Campbells seek out Presbyterian Communion".
- **The session-one chapter title is hidden** (`HIDE`, Micah, 1 Nov 2026): the deck goes from the recap documents straight to the shipwreck. Session two keeps its title slide.

- **1 Nov 2026, Micah's edits.** Dropped from the reunion: the *Declaration and Address* "essentially, intentionally, and constitutionally one" slide (it is in the recap). "Three founders" became "Three instigators", now after the Synod's refusal. Brush Run Church Formed through "Every Lord's day" (six slides) are copied into session one after "great reluctance"; session two keeps its own copies (its side paths fork from those).

- **End of session one trimmed (Micah, 1 Nov 2026).** Dropped from the spine: "In Glasgow he gave back the token. / In Washington he said why."; the card "Three founders. One open table."; and the Synod's "important reasons" slide (still in the reserve deck; two of its reasons are now in the notes of "cannot be granted"). The three founders are now three portraits side by side. The card "Still seeking a larger union, they became a church." now comes right after the Synod, before "Why a church" and "great reluctance".

- **McGill condensed (Micah, 1 Nov 2026).** The two McGill quotation slides became one statement, "Meanwhile, a prominent minister of the church published a book denying the divinity and the atonement of Christ…"; the quotations (Richardson 1:153, note) are in its presenter notes and in the Richardson excerpts. New after the vow: a map, Londonderry to the wreck at Loch Indaal to Glasgow ("about 80 miles"). The Synod's "cannot be granted" now elides "ministerial and".

- **Session one lands on the decision to become a church (Micah, 1 Nov 2026).** "In Glasgow he gave back the token", the three founders and their card now come before the Synod; after the Synod's reasons come "Why a church" and "great reluctance" (moved from session two) and a new card, "Still seeking a larger union, they became a church.", which is also session two's recap. Session two opens on "Brush Run Church Formed".

- **Act I reordered to Micah's spoken run-through (1 Nov 2026).**
  - Haldane's "everything or nothing" now follows the General Assembly's vote: the conviction that sold his estate, turned on Scotland.
  - New after the Kintyre arrest: Dr. McGill of Ayr (Richardson 1:153, note, quoting McKerrow): "he was not God, equal with the Father"; the complaint "hushed up"; the card "Laymen preaching Christ: arrested. / A minister denying him: kept his pulpit."
  - The token: what he came to want and his father's church come first, then the examination and token, then "He was welcome… Ewing was not… The Haldanes were not.", "Can you be included…?", and a new slide "Eight hundred communicants… He waited for the last one." (split from the token slide).
  - The reunion: the *Declaration and Address* slide now follows the road ("what his father showed him"), before "the very same conclusions".
  - "Two ways not to become a sect", the two-column slide and *Becoming Baptists* moved back from session two into Act I, after "must obtain admission"; then "Who may come?" (now headed "Alexander, 1810": the ground already implicit in the D&A), and only then the Synod's refusal and its reasons. Session two now opens on "Why a church".

- **"Your questions" is a side path** off the recap documents slide (Micah, 31 Oct 2026): Catholics, and unity or uniformity, 23 slides. It was on the spine for a day.

- **Two sessions, one deck (Micah, 28 Oct 2026).** Chapter 5 now runs as two class sessions in the same deck:
  - Session one: the class title, the preacher-title quiz (swapped back here 31 Oct 2026), the recap, Act I, and its own close (discussion, Idea 1, the site, "Next time: shut out by every church they asked, they become one.").
  - Session two: the class title again, the communion-table quiz ("What was carved on the front of the communion table?"), a session-two title slide, the "Three founders. One open table." card as recap, then Brush Run through "Why the people?" and the close (Ideas 2 and 3, the chapter's three ideas together, the site, next week).
  - Luke 22:19 was added to the shared Scripture source (`decks/src/sources/scripture-kjv.html`) so the quiz answer is checked.

- **Act I ends on the open table (Micah, 28 Oct 2026).** The token now leads, through the reunion and the Society's need of a church, straight to the Synod's refusal and Alexander's November 1810 reply, so his refusal of the token connects to his words on openness, the position that kept his father out of the Synod. In order:
  - "cannot be granted";
  - the Synod's four "important reasons" (copied from the reserve deck, gold on "opposing creeds and confessions"; the reserve deck keeps its own copy);
  - "Who may come?" (now "Alexander answers, November 1810") with *Creeds as tests*;
  - new: "In Glasgow he gave back the token. / In Washington he said why.";
  - new: "Three founders, one table" (Stone 1803 "not from their communion", Thomas 1807, Alexander 1809), and the card "Three founders. One open table." If the class ends at Act I, it ends here.
  - "Two ways not to become a sect", the two-column slide and *Becoming Baptists* moved from before the Synod to after Act I, opening Brush Run's turn to becoming a church.

- **The May 4, 1811 licensing slide** moved after "The Ordination" card, out of timeline order but next to the ordination it belongs with (Micah, 28 Oct 2026).
- **Luther on the spine.** Six verified Luther slides now follow "Why the people?" as the witness for baptismal succession: three from 1520 (*To the Christian Nobility*, *Babylonian Captivity*, taken from `priesthood()`) and three from the 1523 Leisnig treatise (taken from `consent()`). Chapter 5's copy of *The whole church remembers* leaves its Luther slides out so they aren't shown twice. The resource itself is unchanged.

- **"What the hands do"** (Richardson: ordination is not "conferring any authority, but… a public testimony") moved from the spine into the side path *Who may ordain?* (Micah, 28 Oct 2026). Micah's line: the tradition narrates its ordinations in two ways, (1) Christians and congregations have authority (Matthew 18), and (2) no authority is needed. The second resolves into the first, since the authority was already given in baptism ("baptismal succession", as in Luther's "whatever issues from baptism…"). The spine argues (1) only; arguments of form (2) go to side paths.

- **Side paths reorganized around the four arguments (Micah, 28 Oct 2026).** Eleven became nine:
  - *Where two or three are gathered* was dropped; its Matthew 18 and two-or-three slides duplicate *Church government*.
  - *Church government* and *Against succession* merged into **Who may ordain?**, off "the choice of the people". Dropped from it as duplicates of spine slides: "As to the form or ceremony of ordination" and "The will's bequests on government". Dropped from *Against succession*: its "Why do we contend…" slide, which duplicates *Church government*.
  - *Who serves the table?* and *Who keeps the table* merged into **Who may serve?**, off "Every Lord's day" (the table resource's own title and closing card are left out).
  - *Who was not at the table* (Joseph Bryant) was removed at Micah's direction. The passage is still in Richardson's excerpts, and the baptism story is in *One Baptism*.
  - *The assembly* lost its two "fountain of official power" slides, which duplicate the spine slide it forks from. *Confession or constitution* now forks beside it.
  - New: **Creeds as tests** (D&A Propositions 7 and 6), off "the gates of admission".

- **"Who may come?"** (Alexander's November 1810 address and the "party man" address) moved from after the first Supper to directly after the Synod of Pittsburg's refusal, as Alexander's answer to it, before Brush Run became a church (Micah, 28 Oct 2026).

- **The two points became side paths (Micah's story outline, 27 Oct 2026).** Both now fork from the closing card, "A minister, made by the priesthood of all believers":
  - "Who serves the table?" (Campbell's royal-priesthood passages, "a horrid evil," "Open to all. Hosted by any.") is the side path *Who serves the table?*, with *Who keeps the table* beside it.
  - "Where two or three are gathered" (Matthew 18, the D&A on Matthew 18, the Last Will's "choose her own preacher," "Brush Run chose.") is the side path *Where two or three are gathered*.
  - *The assembly* (`ekklesia()`) and *The whole church remembers* now fork from the "fountain of official power" slide in the new section "Why the people?".
- **Brush Run, shortened.** Two slides are now `HIDE(...)` in `slides.py`: kept in the source, left out of the deck. Change `HIDE` back to `A` to show one again.
  - The 1810 meeting house.
  - Job 8:7, "Though thy beginning was small."
- **"Two ways not to become a sect"** (Micah, 27 Oct 2026). Stone's side dissolved its own body; the Campbells tried to join existing ones. This is now a run in Brush Run:
  - "the Society must obtain admission into some regularly organized religious body…" (shown again, no longer hidden);
  - the Synod of Pittsburg's "cannot be granted" (also in the reserve deck);
  - the two-column slide (the Last Will's "sink into union" beside "obtain admission");
  - the Baptist flash-forward, now its own side path *Becoming Baptists* off the two-column slide (28 Oct 2026): the 1813 overture "provided always…" and Richardson on the name *The Christian Baptist* (1823). Alexander's 1848 "I had no idea of uniting with the Baptists…" was on screen briefly and was dropped at Micah's direction (28 Oct 2026) as hindsight that isn't part of this story. The passage is still in `richardson-memoirs-v1-excerpts.html`.
  - the card "Refused by the Presbyterians, they became Baptists."
- **The opening question slide** ("Who has authority? / Who may serve the table?") is hidden (`HIDE`) while Micah works on a reframing (27 Oct 2026).
- **The Last Will's ministry items** ("choose her own preacher", "obtain license from God") and the card "Brush Run chose." moved from the *Where two or three are gathered* side path into "Why the people?". They are now two highlighted Springfield slides, joined by "our power of making laws… forever cease" and "assume her native right of internal government". That side path now holds Matthew 18 and the *D&A* on Matthew 18:20.
- **"I dare not be a party man…"** moved from point one to the new spine section on Alexander's own words about the table (1810).
- **"The clergy are the opposite to the laity…"** is now on the spine, in "Why the people?". It is still in the reserve deck too.

- **Glasgow summary slides.** "He went to hear Greville Ewing" and the "from Chapter 2" Glasgow summary were replaced by the full Chapter 2 Glasgow sequence: hearing other preachers (Article 4), Ewing's house and the Haldanes, and the token.
- **Foster material** moved out to the unity resource (above).

## Superseded drafts, kept in git history only

Recover any of these with `git show <commit>:decks/src/week5/slides.py`.

- `a818a3a`, `a21b441`: the recap as portraits with the captions "So far" / "Unity in Communion." Replaced at Micah's direction by the current recap:
  - Stone, "Let the unity of Christians be our polar star" (*Christian Messenger* 6, 1832).
  - Thomas Campbell, "With you all we desire to unite in the bonds of an entire Christian unity…" (*D&A*); "Resume that precious, that dear-bought liberty…" was on the slide until 1 Nov 2026.
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
