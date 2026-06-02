---
name: deep
description: "Run deep research through the Parallel Task API for complex, multi-step questions that need synthesis, source grounding, market/technical analysis, or a full research report rather than a quick web lookup. Use for /deep, deep research, comprehensive investigation, current market research, and high-stakes decisions."
version: 1.0.0
author: HinkoK / OpenClaw import
license: MIT
platforms: [linux, macos]
tags: [research, deep-research, parallel, synthesis, market-analysis, fact-checking]
required_environment_variables: [PARALLEL_API_KEY]
---

# /deep — Parallel Task Deep Research

Запускает асинхронный глубокий ресёрч через Task API и ждёт завершения.


## Hermes usage rules

- Use for complex research where a quick answer would be unreliable or too shallow.
- Prefer `scripts/deep.sh "question" pro 1800` as the default runtime path.
- For urgent or lightweight fact checks, use normal web/perplex instead of this skill.
- Tell the user when the run may take a long time, especially for `pro` or `ultra` processors.
- Return a concise synthesis first, then evidence, caveats, and follow-up questions.

## Usage

```bash
/deep твой исследовательский вопрос
```

Локально:

```bash
scripts/deep.sh "твой исследовательский вопрос" pro 1800
```

Параметры:
- `processor` (опционально): `pro` (по умолчанию), `ultra`, и т.д.
- `timeout_seconds` (опционально): по умолчанию `1800`

## Когда использовать

- Нужен глубокий отчёт, а не обычный поиск
- Многошаговый ресёрч с синтезом
- Аналитические задачи, где важна полнота

## Требования и API-ключ

Для работы нужен `PARALLEL_API_KEY` от Parallel.

Где взять ключ:
1. Открой https://platform.parallel.ai
2. Войди или создай аккаунт.
3. Перейди в раздел API keys / Developer settings.
4. Создай новый API key.
5. Сохрани его локально как переменную окружения:

```bash
export PARALLEL_API_KEY="PASTE_YOUR_KEY_HERE"
```

Для постоянного хранения можно добавить ключ в shell profile (`~/.zshrc`, `~/.bashrc`) или в env-файл, который читает `scripts/deep.sh`:

```bash
mkdir -p ~/.openclaw/workspace/.secrets
printf 'PARALLEL_API_KEY=%s
' 'PASTE_YOUR_KEY_HERE' > ~/.openclaw/workspace/.secrets/deep-ws.env
chmod 600 ~/.openclaw/workspace/.secrets/deep-ws.env
```

Не коммить API key в GitHub и не вставляй его в промпт агенту.

Дополнительно:
- Для Deep Research лучше использовать `pro`/`ultra` (доступны и fast-версии, если включены у аккаунта).
- Входной запрос держать короче `15000` символов.
- Задача может выполняться долго (до ~45 минут на сложных ресёрчах).
- Docs: https://docs.parallel.ai/getting-started/overview

## Runtime (добавлено)

Вместе со скиллом должен быть скрипт:

```bash
scripts/deep.sh "запрос" [processor] [timeout_seconds]
```

Он:
1) создаёт run через `POST /v1/tasks/runs`
2) ждёт завершения через `GET /v1/tasks/runs/{run_id}`
3) забирает результат через `GET /v1/tasks/runs/{run_id}/result`

Возвращает JSON с полями: `run_id`, `status`, `text_plain`, `basis_count`, `raw`.
