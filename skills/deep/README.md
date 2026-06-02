# deep

Deep research skill powered by the Parallel Task API.

## What it does

Runs longer, source-grounded research jobs for questions where a normal quick web search is too shallow.

Use for:
- market research;
- technical research;
- complex comparisons;
- product/niche analysis;
- high-stakes decisions that need more evidence.

## API key required

This skill requires `PARALLEL_API_KEY`.

Get it here:

1. Open https://platform.parallel.ai
2. Create or log into your account.
3. Go to API keys / Developer settings.
4. Create a new API key.
5. Store it locally:

```bash
export PARALLEL_API_KEY="PASTE_YOUR_KEY_HERE"
```

For persistent local storage used by the included script:

```bash
mkdir -p ~/.openclaw/workspace/.secrets
printf 'PARALLEL_API_KEY=%s
' 'PASTE_YOUR_KEY_HERE' > ~/.openclaw/workspace/.secrets/deep-ws.env
chmod 600 ~/.openclaw/workspace/.secrets/deep-ws.env
```

Docs: https://docs.parallel.ai/getting-started/overview

## Install

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/deep/SKILL.md
```

## Run locally

```bash
scripts/deep.sh "your research question" pro 1800
```

Do not commit your API key.
