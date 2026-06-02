# troitsa

Троица is a multi-model decision workflow for Hermes Agent.

## What it does

Splits important tasks into three roles:

- **Conductor** — strong model plans and synthesizes.
- **Worker** — cheap/high-throughput model does the heavy volume.
- **Critic** — independent model red-teams the result.

Default mental model:

```text
GPT      = Conductor
DeepSeek = Worker
Gemini   = Critic
```

## Install

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/troitsa/SKILL.md
```

## Example

```text
Используй Троицу: оцени 3 идеи для AI YouTube-видео и выбери лучшую.
```

Original standalone repo: https://github.com/HinkoK/hermes-troitsa
