# Lessons journal

One line per accepted improvement: date, lesson, evidence. Newest first. The
rules themselves live in the skill files; this journal says where each came
from.

- 2026-10-30: Compare the installed copy with the repository before a run: the installed copy dated from 2026-10-14 and the Keychain bug fixed on 2026-10-22 failed three times again ("Missing key").
- 2026-10-30: Stop on a sign-in page before every shot: an expired session filmed the Clerk sign-in page as the first capture, with no error.
- 2026-10-30: Roogo's own numbers stay visible: hiding every phone number blurred the whole Studio script, which ends with Roogo's WhatsApp.
- 2026-10-30: Re-read example records right before filming: a listing was published by staff between the script and the shoot, and the publish window had to be filmed on a test listing.
- 2026-10-30: Per-video respellings go on the command line (`--respell`): "CNIB" had to be read "C N I B", which took two copies of the script.
- 2026-10-30: Give the virtual environment command for noisereduce: the system Python lacked it (ModuleNotFoundError).
- 2026-10-22: Keychain lookup puts the service right after `-s`; the account is optional. Evidence: every run failed with "Missing key" and needed a manual export of the key.
- 2026-10-22: Slow clones to speed 0.9 with 0.9 s pauses between paragraphs: Salif's clone read 185 words a minute; the same 138 words took 52.8 s instead of 44.7 s. The previous video had been rejected as too fast.
- 2026-10-22: Leave digital silence out of the noise profile: with pauses, 12% of frames were pure silence and cleaning crashed (zero-size array). A clone's background varied from 14.5 to 31.7 dB between takes, so every take is measured.
- 2026-10-22: Size, centred captions in a dark box and the badge come from the plan: a 150-line wrapper was needed for a vertical video, and cream captions were unreadable on cream screens.
- 2026-10-22: An opening « belongs to the next word: captions ended on a lone « and lost the sentence break after "note.".
- 2026-10-22: Public pages are filmed signed out at phone size, zoom 1.15 at most, and every test upload is listed: zooms above 1.15 cut text, and three form runs left 5 orphan uploads in production storage.
- 2026-10-14: Every run must end with improvement candidates tied to a gap and evidence. Source: Salif, when the skill was created.
- 2026-10-12: Cloned narration needs noise reduction: Salif's clone measured a 15 dB speech-to-background gap against 31 dB for the house voice; reducing noise from the quietest 12% of 20 ms frames raised it to 18.7 dB, and the user chose the cleaned version by ear.
- 2026-10-12: Bring the capture tab to the front before every session: screenshots of a background tab timed out because hidden tabs do not paint.
- 2026-10-12: Re-record when the product changes: the first Studio video was made on an older version and the user rejected it for that reason ("the studio evolved a lot since").
- 2026-10-12: Title and closing cards need a slow push-in: a still card longer than 3 seconds failed the motion check.
- 2026-10-11: Music runs to the last frame and rises when nobody speaks; credit it on the closing card.
