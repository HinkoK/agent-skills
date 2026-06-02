# Prompt formatter

Use this formatter before generating the final answer when the user request is broad, messy, or multi-part.

```md
AFTER_CALL_FORMATTER

Mode: [work-call | therapy-session | client-follow-up | study-call]
Source type: [audio | video | transcript | notes | mixed]
Needs transcription: [yes | no]
Speaker aware: [yes | no]
Speaker rename map: [optional; e.g. Speaker 1 = я, Speaker 2 = психолог]
Output depth: [short | standard | deep]
Needs follow-up draft: [yes | no]
Needs task extraction: [yes | no]
Export format: [chat | telegram | obsidian | task-list | speaker-transcript]
Language: [ru | en | other]
Special focus: [decisions | themes | tasks | learning | blockers | emotions | mixed]

Requested outcome:
- ...

Important constraints:
- ...

Return structure:
- ...
```

## Example: work call

```md
AFTER_CALL_FORMATTER

Mode: work-call
Source type: transcript
Needs transcription: no
Speaker aware: no
Speaker rename map: none
Output depth: standard
Needs follow-up draft: yes
Needs task extraction: yes
Export format: telegram
Language: ru
Special focus: decisions, blockers

Requested outcome:
- Summarize the meeting
- Extract decisions and owners
- Draft a short follow-up message

Important constraints:
- Keep it concise
- Do not invent deadlines

Return structure:
- Short summary
- Decisions
- Owners
- Next steps
- Telegram follow-up draft
```

## Example: therapy session with speakers

```md
AFTER_CALL_FORMATTER

Mode: therapy-session
Source type: audio
Needs transcription: yes
Speaker aware: yes
Speaker rename map: Speaker 1 = я, Speaker 2 = психолог
Output depth: deep
Needs follow-up draft: no
Needs task extraction: no
Export format: obsidian
Language: ru
Special focus: themes, emotions

Requested outcome:
- Transcribe the session
- Label speakers
- Summarize key themes
- Suggest what to reflect on between sessions

Important constraints:
- No diagnosis language
- Separate observation from interpretation
- If attribution is uncertain, keep generic labels

Return structure:
- Short recap
- Speaker-labeled transcript
- Key themes
- What surfaced
- Reflection prompts
- Practical next step
```
