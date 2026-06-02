# Agent Skills by HinkoK

Custom Hermes Agent skills used in my personal AI-agent workflow.

## Skills

### 1. `troitsa`
Multi-model decision workflow: Conductor plans/synthesizes, Worker does volume, Critic red-teams.

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/troitsa/SKILL.md
```

Standalone repo: https://github.com/HinkoK/hermes-troitsa

### 2. `webd`
Web-design workflow for landing pages, SaaS frontends, non-generic UI, shadcn/ui component libraries, and conversion-oriented pages.

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/webd/SKILL.md
```

### 3. `online-store-legitimacy-checks`
Due-diligence workflow for checking suspicious webshops, checkout URLs, ecommerce domains, payment risk, and scam signals before buying.

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/online-store-legitimacy-checks/SKILL.md
```

### 4. `aftercall`
Post-call workflow for recordings/transcripts: summaries, decisions, action items, follow-ups, study notes, and speaker-aware transcripts.

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/aftercall/SKILL.md
```

Standalone repo: https://github.com/HinkoK/aftercall-skill

### 5. `deep`
Deep research through the Parallel Task API for complex, multi-step questions that need synthesis and source-grounded reports.

Requires a Parallel API key: https://platform.parallel.ai

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/deep/SKILL.md
```

Then set your key:

```bash
export PARALLEL_API_KEY="PASTE_YOUR_KEY_HERE"
```

## Install all

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/troitsa/SKILL.md
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/webd/SKILL.md
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/online-store-legitimacy-checks/SKILL.md
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/aftercall/SKILL.md
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/deep/SKILL.md
```

## Notes

- These are custom/local skills, not official Hermes built-ins.
- `webd`, `aftercall`, and `deep` include references/scripts; clone the repo if you want the full reference pack.
- `deep` requires `PARALLEL_API_KEY`.
- Never commit API keys or secrets.

## Hermes Agent

Hermes Agent: https://github.com/NousResearch/hermes-agent
