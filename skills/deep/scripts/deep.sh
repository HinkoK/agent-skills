#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${DEEP_WS_ENV_FILE:-$HOME/.openclaw/workspace/.secrets/deep-ws.env}"

if [[ -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  set -a; source "$ENV_FILE"; set +a
fi

# Backward compatibility: support DEEP_API_KEY alias
if [[ -n "${DEEP_API_KEY:-}" && -z "${PARALLEL_API_KEY:-}" ]]; then
  export PARALLEL_API_KEY="$DEEP_API_KEY"
fi

QUESTION="${1:-}"
PROCESSOR="${2:-pro}"
TIMEOUT_SECONDS="${3:-1800}"

if [[ -z "$QUESTION" ]]; then
  echo '{"error":"usage: deep.sh \"question\" [processor] [timeout_seconds]"}'
  exit 1
fi

python3 "$BASE_DIR/scripts/deep_research.py" "$QUESTION" "$PROCESSOR" "$TIMEOUT_SECONDS"
