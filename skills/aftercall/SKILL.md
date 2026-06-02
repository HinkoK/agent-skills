---
name: aftercall
description: "Analyze post-call materials such as recordings, transcripts, meeting notes, therapy/coaching sessions, study calls, and voice notes. Use for aftercall/post-call workflows: transcribe recordings, label speakers, summarize decisions, extract action items/owners, draft follow-ups, export notes, and reflect on themes after a conversation."
version: 1.0.0
author: HinkoK / OpenClaw import
license: MIT
platforms: [linux, macos, windows]
tags: [meetings, transcription, summaries, follow-up, action-items, notes, coaching]
---

# aftercall

## Hermes usage rules

- Use after a conversation has happened; do not use for live note-taking.
- If the user provides audio/video, transcribe first, then analyze.
- If the user provides transcript/notes, analyze directly.
- Pick the narrowest mode that fits: work call, client follow-up, study call, therapy/coaching reflection, voice note, or speaker-labeling.
- For therapy/coaching content, do not diagnose; separate observations from interpretations and use careful language.
- End with practical next steps, owners, deadlines, or a ready-to-send follow-up when relevant.

## Overview

Use this skill when the user wants to turn a finished conversation into a clear outcome: transcript, structured recap, decisions, owners, next steps, follow-up draft, task list, study notes, or deeper reflection.

This skill is for **after** a conversation happened. It is not for live note-taking during a call.

## Trigger examples

Typical requests:
- "Разбери этот созвон и собери итоги"
- "Вот запись звонка, сделай выжимку и action items"
- "Проанализируй мою сессию с психологом и скажи, над чем поработать"
- "Из этого transcript сделай follow-up письмо"
- "Что мы решили на этом колле и кто за что отвечает?"
- "Сделай учебную выжимку из этого study call"
- "Подготовь заметку в Obsidian по итогам звонка"
- "Сделай транскрипт с Speaker 1 / Speaker 2"
- "Попробуй отличить, кто говорит в записи"

## Workflow

### 1) Identify the input type

Start by determining what the user provided:
- **Audio/video recording** → transcribe first, then analyze
- **Transcript** → analyze directly
- **Raw notes/messages** → normalize into a clean after-call recap
- **Several materials** → merge them, deduplicate overlaps, then analyze

If the input is missing, ask for exactly one thing: the recording, transcript, or notes.

### 2) Pick the right mode

Choose the narrowest mode that fits the conversation. If the user does not specify one, infer it from context.

#### Mode: `work-call`
Use for team syncs, client calls, planning calls, sales calls, and internal work meetings.

Prioritize:
- decisions
- owners
- deadlines
- follow-up message
- unresolved blockers

#### Mode: `therapy-session`
Use for therapy, coaching, self-reflection, personal support, and emotionally important conversations.

Prioritize:
- key themes
- recurring patterns
- tensions / avoided topics
- useful reflection prompts
- practical next step between sessions

Guardrails:
- do **not** diagnose
- separate observations from interpretation
- use careful wording like "похоже", "можно обратить внимание", "стоит исследовать"

#### Mode: `client-follow-up`
Use when the user mainly needs a message or email after the call.

Prioritize:
- concise recap
- agreed scope / commitments
- next step
- ready-to-send follow-up draft

The final output can be just the sendable draft plus a tiny internal summary if that solves the task fastest.

#### Mode: `study-call`
Use for lessons, tutoring, study groups, mentoring sessions, lecture debriefs, and educational calls.

Prioritize:
- main concepts
- what the learner understood / missed
- terms to review
- questions that remain open
- next study steps

Prefer a more educational structure than a business one.

### 3) Transcribe only when needed

If the user gave audio/video but no transcript:
- Use the `openai-whisper` skill for local speech-to-text when available
- Preserve speaker changes when practical
- Clean obvious filler/noise only if it improves clarity
- Do not over-edit meaning

If the user already gave a transcript, do **not** spend time retranscribing.

### 3.5) After transcription, offer speaker-aware mode before analysis

If the transcript was just created from audio/video, pause **before** the deeper analysis and offer the user a short choice — unless they already explicitly requested or declined speaker labeling.

Default interaction:
- tell the user that the transcription is ready
- explain in 1-2 lines what **speaker-aware transcription** means
- offer a simple choice: continue with a normal analysis, or first separate speakers as `Speaker 1 / Speaker 2 / Speaker 3`
- mention that this is **best effort** and depends on audio quality
- if useful, invite the user to provide a rename map such as `Speaker 1 = я`, `Speaker 2 = психолог`

Recommended wording:
```md
Транскрибация готова.

Перед разбором могу дополнительно включить **speaker-aware transcription** — это когда я пытаюсь отделить говорящих в тексте (`Speaker 1`, `Speaker 2`, и т.д.), чтобы было визуально понятно, кто что говорил.

Если хочешь, могу:
1. сразу продолжить обычный разбор,
2. или сначала сделать transcript с разделением по спикерам.

Если знаешь участников, можешь сразу написать:
`Speaker 1 = ...`, `Speaker 2 = ...`
```

Do **not** ask this if:
- the user already asked for speaker-aware mode
- the user already said they do not need speaker separation
- the transcript already has clear speaker labels / roles and no extra separation is needed
- the transcript is obviously single-speaker
- the task is explicitly ultra-fast and a normal transcript is enough

If the source is already a transcript **but it is raw, unlabeled, or visually hard to follow**, it is still valid to offer speaker-aware separation before the deeper analysis.

### 4) Optional function: speaker-aware transcription

Use this only when the user asks to distinguish speakers, or when speaker separation will materially improve the result.

Goal:
- label the transcript as `Speaker 1`, `Speaker 2`, `Speaker 3`, etc.
- optionally rename them to roles or people if the mapping is known
- use those labels in the summary when it improves clarity

Default behavior:
- If no speaker information is requested, a normal transcript is enough
- If speaker labeling is requested, return the best-effort labeled transcript plus a short confidence note when needed

Preferred output:
```md
[Speaker 1]
...

[Speaker 2]
...
```

If the user knows the participants, allow remapping:
- `Speaker 1 = я`
- `Speaker 2 = психолог`

Speaker-aware summary can include:
- **Что говорил Speaker 1 / я**
- **Что отвечал Speaker 2 / психолог**
- commitments by speaker
- open questions by speaker
- concerns or resistance by speaker

Guardrails:
- treat speaker labeling as **best effort**, not certainty
- if attribution is weak, say so clearly
- do not assign real names unless the user provided them or the source makes them explicit
- heavy overlap, noisy audio, or many similar voices reduce reliability

See: [references/speaker-labeling.md](references/speaker-labeling.md)

### 5) Build the analysis with a stable formatter

Before writing the final answer, normalize the request into this internal formatter:
- **mode**: work-call / therapy-session / client-follow-up / study-call
- **source type**: audio / video / transcript / notes / mixed
- **output depth**: short / standard / deep
- **needs transcription**: yes / no
- **speaker aware**: yes / no
- **speaker rename map**: optional
- **needs follow-up draft**: yes / no
- **needs task extraction**: yes / no
- **export format**: chat / telegram / obsidian / task-list
- **language**: ru / en / other
- **special focus**: decisions / themes / tasks / learning / emotions / blockers

Use the formatter template from [references/prompt-formatter.md](references/prompt-formatter.md).

If the task is messy, rewrite the task to yourself once using that formatter before generating the answer.

### 6) Produce the core after-call output

Default output should be practical, not literary.

Return these blocks when available:
1. **О чем был разговор** — 3-7 bullets
2. **К чему пришли** — decisions / conclusions
3. **Кто за что отвечает** — owners if present
4. **Что делать дальше** — next steps with priority/order
5. **Открытые вопросы** — unresolved items

Prefer explicit wording:
- "Решили"
- "Нужно сделать"
- "Осталось уточнить"
- "Ответственный: ..."

If some fields are absent in the source, say so briefly instead of inventing.

### 7) Add optional layers only when useful

#### A. Follow-up draft
Use when the user wants to send something after the call.

Possible outputs:
- short Telegram/Slack message
- email follow-up
- client recap
- internal handoff note

Keep it ready to paste.

#### B. Deeper reflection
Use when the user asks for analysis beyond summary.

Good examples:
- recurring themes
- hidden tension or ambiguity in the discussion
- where the conversation drifted
- what was avoided or left vague
- what the user should think through before the next session

#### C. Task extraction
If the conversation clearly implies tasks, convert them into a checklist.

Good format:
- [ ] Task
- Owner: Name / me / unclear
- Deadline: explicit date or "не указан"

### 8) Export in the format the user will actually use

Default export is chat-friendly markdown.

If the user wants a specific destination, use the matching export template:
- **Telegram summary** → [references/export-templates.md](references/export-templates.md)
- **Obsidian note** → [references/export-templates.md](references/export-templates.md)
- **Task list** → [references/export-templates.md](references/export-templates.md)
- **Speaker-labeled transcript** → [references/output-templates.md](references/output-templates.md)

Rules:
- Telegram → short, scannable, no heavy formatting
- Obsidian → title, sections, tags, and wikilink-ready style
- Task list → action-first, owner/deadline explicit
- Speaker transcript → readable blocks, stable labels, optional rename mapping at the top

### 9) Match depth to the context

Use the smallest output that solves the need:
- quick work call → concise recap + tasks
- strategy call → recap + decisions + open questions
- therapy/coaching session → recap + themes + suggested reflection
- educational call → recap + concepts + next study steps
- client follow-up request → concise recap + ready draft
- speaker-label request → labeled transcript + short recap unless more was asked

Do not drown short calls in unnecessary structure.

## Output defaults

Default response order:
1. Short 1-2 sentence summary
2. Structured blocks
3. Follow-up draft or checklist if requested
4. Exported version if explicitly asked

Use Russian by default unless the user explicitly asks for another language.

## Quality bar

A good after-call result should:
- reduce memory load
- make the next action obvious
- distinguish facts from interpretation
- avoid hallucinating decisions, owners, or deadlines
- stay readable enough to use immediately
- match the chosen mode instead of forcing one universal structure
- be explicit about uncertainty in speaker attribution

## Safety and privacy

- Treat call materials as private by default
- Do not share or quote sensitive details outside the current task
- For highly personal calls, keep the analysis supportive and non-diagnostic
- If the recording quality is poor or attribution is uncertain, say that clearly

## Quick resources

- Modes and routing: [references/modes.md](references/modes.md)
- Prompt formatter: [references/prompt-formatter.md](references/prompt-formatter.md)
- Speaker labeling notes: [references/speaker-labeling.md](references/speaker-labeling.md)
- Output patterns: [references/output-templates.md](references/output-templates.md)
- Export formats: [references/export-templates.md](references/export-templates.md)
- Formatter helper script: [scripts/build_after_call_prompt.py](scripts/build_after_call_prompt.py)
- Evaluation cases: [references/evaluation-cases.json](references/evaluation-cases.json)
