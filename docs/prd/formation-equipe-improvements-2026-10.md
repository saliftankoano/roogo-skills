# PRDs: formation-equipe improvements (October 2026)

Source: the 22 October 2026 run that produced two recruitment videos ("Comment postuler chez Roogo", vertical, house voice; "Examiner les candidatures", landscape, founder's cloned voice). Every problem below happened in that run; evidence is quoted from its working journal. One PRD per problem, written to the house template (problem first, non-goals, testable requirements with priority, metrics with a guardrail, open questions). PRD 7 is a product problem in roogo-web found while filming, not a skill change.

Owners: Salif approves. The agent implements PRDs 1 to 6 in `skills/formation-equipe/` through one pull request; PRD 7 goes to roogo-web.

---

## PRD 1. Keychain key lookup works

**Summary:** `narration.py` finds the voice key stored in the macOS Keychain without a workaround.

**Problem:** every run fails with « Missing key » even though the Keychain item exists, so the agent has to export the key into the environment by hand, which is exactly the handling of secrets the skill is meant to avoid.

**Why it happens:** `secret()` inserts `-a <account>` at the wrong position, so the service name ends up after the account flag.

**Before**
```
security find-generic-password -s -a default ai.cartesia.api-key -w
-> Missing key: set CARTESIA_API_KEY or add the Keychain item ai.cartesia.api-key.
```
**After**
```
security find-generic-password -s ai.cartesia.api-key -a default -w
-> key read silently, narration starts
```

**Goals:** the key is read from the Keychain with or without an account name. **Non-goals:** a new secret store; reading keys from files.

**Users:** any agent or person running the narration step on a Mac.

| ID | Requirement | Priority |
| --- | --- | --- |
| 1.1 | With only the Keychain item present (no environment variable), narration reads the key and runs. | Must |
| 1.2 | Works with and without an account name. | Must |
| 1.3 | The key is never printed, logged or written to a file. | Must |
| 1.4 | The error message names the environment variable and the Keychain service, never the value. | Should |

**Constraints:** public repository: tests use a fake `security` command, never a real key.

**Success metric:** runs needing a manual `export` of the key: from every run (1 of 1) to none over the next 5 runs. **Guardrail:** zero keys in logs, transcripts or committed files.

**Open questions:** none.

---

## PRD 2. Narration pace and pauses

**Summary:** the voice can be slowed and given short pauses between paragraphs, so staff can follow the screen.

**Problem:** the founder's cloned voice reads too fast for a screen tutorial: about 185 words a minute with no pause longer than 0.5 s. The previous training video (« Inviter quelqu'un dans l'équipe ») was rejected as too fast for that reason.

**Before:** 138 words in 44.7 s, no breath between steps; the screen changes before the viewer has read it.
**After:** the same 138 words in 52.8 s with 7 pauses of about 0.9 s, one at each step change (measured on this run with speed 0.9 and a 0.9 s break).

**Goals:** a pace a first-time viewer can follow; a pause at every step change. **Non-goals:** changing voices, emotion control, per-word timing edits.

**Users:** staff watching a training video on a phone; the agent building it.

| ID | Requirement | Priority |
| --- | --- | --- |
| 2.1 | A speed setting is available for each run. | Must |
| 2.2 | A pause length between paragraphs is available for each run. | Must |
| 2.3 | Defaults for cloned voices give 130 to 160 words a minute with a pause at each paragraph. | Must |
| 2.4 | Word timestamps stay correct after pauses are added (captions still match the voice). | Must |
| 2.5 | `references/voix-et-son.md` explains the settings and the target pace. | Should |

**Success metric:** speaking rate of delivered training videos: from about 185 to 130 to 160 words a minute, measured from the word timestamps of each delivery. **Guardrail:** no training video longer than 3 minutes because of pauses alone.

**Open questions:** should the house voice (Sandrine) keep speed 1.0? This run used 1.0 for her and the result was not judged by ear yet.

---

## PRD 3. Voice cleaning survives silent pauses

**Summary:** `nettoyer_voix.py` works when the narration contains digital silence, and measures each take.

**Problem:** once pauses are added (PRD 2), the cleaning step crashes, so the noisy cloned voice ships uncleaned or the agent patches the script by hand.

**Before**
```
ValueError: zero-size array to reduction operation
(12% of 20 ms frames are pure digital silence, so the "quietest 12%" noise profile is empty)
```
**After:** frames of pure silence are ignored when building the noise profile and measuring; the step reports « gap 31.7 dB -> 35.2 dB » and writes the cleaned file.

**Goals:** cleaning never crashes on silence; every take is measured. **Non-goals:** a new noise-reduction method; music cleaning.

| ID | Requirement | Priority |
| --- | --- | --- |
| 3.1 | Frames below -120 dB are excluded from the noise profile and the gap measurement. | Must |
| 3.2 | A file made only of silence and speech (no hiss) is handled without error and reported as already clean. | Must |
| 3.3 | The reference notes that a clone's background varies from take to take (14.5 dB vs 31.7 dB, same text and settings), so each take is measured, and a take under 18 dB is re-recorded rather than cleaned harder. | Should |

**Success metric:** cleaning crashes: from 1 of 1 runs with pauses to 0 over the next 5. **Guardrail:** cleaned voice never kept when the gap does not improve (the existing rule stays).

**Open questions:** none.

---

## PRD 4. Editing meets the house rules on its own

**Summary:** `montage.py` builds vertical or landscape videos with centred readable captions and the Roogo badge, without a project wrapper.

**Problem:** the editing script hard-codes 1920x1080 and a caption band at the bottom, and has no badge. Roogo's rules require captions toward the centre, never at the bottom edge, and the logo badge top-right on every video. This run needed a 150-line wrapper to comply, and cream captions on the app's cream and white screens were unreadable until replaced by a dark box.

**Before:** `FPS, W, H, SCREEN_H = 30, 1920, 1080, 990`; captions in a band under the screen; no badge; candidate video impossible in 9:16 without the wrapper.
**After:** one plan file sets the size (1080x1920 or 1920x1080), the caption height (for example 70% of the frame), a dark brown box with cream text and line wrapping, and the badge top-right on screen shots (not on title and closing cards that already show the full logo).

**Goals:** a compliant vertical or landscape video from the plan file alone. **Non-goals:** new transitions or effects; animated captions.

| ID | Requirement | Priority |
| --- | --- | --- |
| 4.1 | Size is set in the plan; 1080x1920 and 1920x1080 both work. | Must |
| 4.2 | Captions sit at a set height toward the centre, never at the bottom edge, and wrap to the frame width. | Must |
| 4.3 | Captions stay readable on white and cream screens (dark box, light text, contrast at least 4.5:1). | Must |
| 4.4 | The badge is drawn top-right on every screen shot and skipped on title and closing cards. | Must |
| 4.5 | Card texts accept a manual line break. | Should |
| 4.6 | The landscape output of an existing plan is unchanged unless the new settings are used. | Should |

**Success metric:** project-specific editing wrappers needed per delivery: from 1 to 0 over the next 3 deliveries. **Guardrail:** verifier still passes (no still over 3 s, about -16 LUFS, equal audio and video length).

**Open questions:** should the badge image path live in the plan or in a shared config?

---

## PRD 5. Opening quotation marks stay with their word

**Summary:** the caption aligner attaches « to the following word, so captions read naturally and sentences break correctly.

**Problem:** French opening quotes are glued to the previous word, giving captions that end on a dangling quote and blocking the sentence break.

**Before:** caption 1 « …puis « », caption 2 « Envoyer ma candidature » » ; and « note. « Retenu » » stays in one caption, so the break after « note. » is lost.
**After:** « …puis » / « « Envoyer ma candidature » » ; « …une note. » / « « Retenu » pour la présélection ».

**Goals:** punctuation-only tokens attach to the right word. **Non-goals:** rewriting the alignment method.

| ID | Requirement | Priority |
| --- | --- | --- |
| 5.1 | An opening « (or « followed by a non-breaking space) attaches to the next word. | Must |
| 5.2 | Closing », colon, question and exclamation marks keep attaching to the previous word. | Must |
| 5.3 | A unit test covers both cases with the two sentences above. | Must |

**Success metric:** captions starting or ending on a lone quote mark: from 2 in this run to 0, checked on the contact sheet of each delivery. **Guardrail:** word-to-voice timing unchanged (same timestamps for every non-punctuation word).

**Open questions:** none.

---

## PRD 6. Filming public pages on a phone

**Summary:** the capture guide covers signed-out public pages at phone size and test data hygiene.

**Problem:** the guide only describes filming the signed-in app on desktop. For the candidate video, the agent improvised: zooms above 1.15 on phone captures cut text at the edges, and running the form three times left orphan uploads (3 CVs, 2 videos) in production storage.

**Before:** no rule; text clipped on zoomed phone shots; test files left behind and found only by accident.
**After:** a section in `references/capture.md`: a fresh signed-out browser context at 390x844 and scale 3 in French; zoom at most 1.15 except on a single button; fill the form up to the last step before submitting; every upload and test row created is listed at delivery for deletion.

**Goals:** clean phone shots and a full list of test data created. **Non-goals:** deleting production data automatically (the owner decides).

| ID | Requirement | Priority |
| --- | --- | --- |
| 6.1 | The guide describes the signed-out phone setup. | Must |
| 6.2 | The guide sets the zoom limit for phone captures. | Must |
| 6.3 | The delivery report lists every test row and uploaded file created, with where it lives. | Must |
| 6.4 | Public captures never use the owner's signed-in browser. | Should |

**Success metric:** orphan test uploads not reported at delivery: from 5 in this run to 0 over the next 3 deliveries. **Guardrail:** zero customer personal data on screen.

**Open questions:** should the skill propose a SQL snippet to delete test rows, for the owner to run?

---

## PRD 7. « Carrières » reachable from the phone menu (roogo-web)

**Summary:** candidates on a phone find the careers page from the menu.

**Problem:** the recruitment video says « rubrique Carrières », but on a phone the roogobf.com menu has no « Carrières » entry; it exists only in the footer at the very bottom of the page. Most candidates apply from Android phones, so they may not find the page before the deadline (Wednesday 28 October, 23:59).

**Before:** phone menu: logement, local, publier, etc.; « Carrières » only in the footer.
**After:** « Carrières » in the phone menu (and the desktop public navbar if space allows), linking to /carrieres, which lists the open role.

**Goals:** the careers page is one tap from the menu on a phone. **Non-goals:** a new careers design; changes to the staff navbar.

| ID | Requirement | Priority |
| --- | --- | --- |
| 7.1 | « Carrières » appears in the public phone menu and opens /carrieres. | Must |
| 7.2 | No other public menu entry is removed. | Must |
| 7.3 | Shown on the desktop public navbar too, if it fits without wrapping. | Could |

**Success metric:** visits to /carrieres/commercial-immobilier from the menu: from 0 (no menu entry) to at least a third of page visits before the deadline, measured in PostHog by referrer. **Guardrail:** no drop in clicks on the existing menu entries over the same days.

**Open questions:** should the entry disappear when no role is open?
