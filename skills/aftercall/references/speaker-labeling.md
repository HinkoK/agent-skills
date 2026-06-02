# Speaker labeling

## What it is

Speaker labeling (or diarization) is the step that tries to answer **who is speaking when**.

It is different from speech-to-text:
- speech-to-text answers: **what was said**
- speaker labeling answers: **who said it**

## Recommended behavior in this skill

Use speaker labeling as an **optional** layer, not a universal default.

Turn it on when:
- the user explicitly asks to distinguish speakers
- there are multiple participants and attribution matters
- the summary becomes much clearer if statements are tied to speakers

After a fresh transcription from audio/video, the preferred UX is:
- first tell the user the transcription is ready
- briefly explain what speaker-aware transcription means
- offer a choice between normal analysis and speaker-separated transcript
- invite an optional rename map if they know the participants

Leave it off when:
- a plain transcript is enough
- the audio is too messy to label responsibly
- the user only wants a quick summary
- the user already declined speaker separation
- the transcript is already clearly labeled by speaker

If the transcript exists but is raw and unlabeled, speaker-aware separation can still be useful as a cleanup step before analysis.

## Output style

Default labels:
- `Speaker 1`
- `Speaker 2`
- `Speaker 3`

If the user provides the identities, remap them after transcription:
- `Speaker 1 = я`
- `Speaker 2 = психолог`

Do not invent identities.

## Confidence rules

Say explicitly when speaker attribution is uncertain.

Good phrases:
- "Speaker labeling is best-effort here"
- "Possible attribution; overlapping speech reduces confidence"
- "I kept generic labels because names are not certain"

## Good fit

Works best when:
- 1-3 speakers
- decent microphone quality
- limited overlap
- one language dominates

## Weak fit

Be cautious when:
- many interruptions
- strong background noise
- 4+ speakers
- similar voice timbre
- poor recording quality

## Summary guidance

If speaker labels are available, summaries can include:
- who introduced the main issue
- who agreed / disagreed
- who took ownership
- which open questions belong to which speaker

That is often more useful than a flat transcript.
