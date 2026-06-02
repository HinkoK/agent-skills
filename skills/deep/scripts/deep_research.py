#!/usr/bin/env python3
import json
import os
import sys
import time
import urllib.error
import urllib.request

API_BASE = os.getenv("PARALLEL_API_BASE", "https://api.parallel.ai")


def die(msg, code=1):
    print(json.dumps({"error": msg}, ensure_ascii=False))
    sys.exit(code)


def request_json(method, path, api_key, payload=None, timeout=60):
    url = f"{API_BASE}{path}"
    data = None
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "User-Agent": "openclaw-deep-ws/1.0",
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        die(f"HTTP {e.code}: {body[:800]}")
    except Exception as e:
        die(str(e))


def get_nested(obj, *keys):
    cur = obj
    for k in keys:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(k)
    return cur


def main():
    if len(sys.argv) < 2:
        die("usage: deep_research.py \"question\" [processor] [timeout_seconds]")

    question = sys.argv[1].strip()
    processor = (sys.argv[2].strip() if len(sys.argv) > 2 else "pro") or "pro"
    timeout_seconds = int(sys.argv[3]) if len(sys.argv) > 3 else 1800

    api_key = os.getenv("PARALLEL_API_KEY", "").strip()
    if not api_key:
        die("PARALLEL_API_KEY is not set")

    if len(question) > 15000:
        die("input too long (>15000 chars). shorten prompt for Deep Research")

    create_payload = {
        "input": question,
        "processor": processor,
        "task_spec": {
            "output_schema": {
                "type": "text",
                "description": "Return a structured markdown report with inline citations and a brief executive summary."
            }
        }
    }

    created = request_json("POST", "/v1/tasks/runs", api_key, create_payload, timeout=60)
    run_id = created.get("run_id")
    if not run_id:
        die(f"unexpected create response: {json.dumps(created)[:800]}")

    started = time.time()
    status = created.get("status", "queued")

    # Poll status endpoint until terminal state, then fetch result
    while True:
        if time.time() - started > timeout_seconds:
            die(f"timeout after {timeout_seconds}s (run_id={run_id}, status={status})")

        run = request_json("GET", f"/v1/tasks/runs/{run_id}", api_key, timeout=60)
        status = (run.get("status") or status or "").lower()

        if status in {"completed", "failed", "cancelled", "canceled"}:
            break
        time.sleep(6)

    result = request_json("GET", f"/v1/tasks/runs/{run_id}/result", api_key, timeout=120)

    output = result.get("output") if isinstance(result, dict) else None
    if isinstance(output, dict):
        content = output.get("content")
        basis = output.get("basis")
        out_status = output.get("status") or status
    else:
        content = get_nested(result, "result", "output", "content") or output
        basis = get_nested(result, "result", "output", "basis")
        out_status = status

    report_text = content if isinstance(content, str) else json.dumps(content, ensure_ascii=False)

    payload = {
        "run_id": run_id,
        "processor": processor,
        "status": out_status,
        "text_plain": report_text,
        "basis_count": len(basis) if isinstance(basis, list) else None,
        "raw": result,
    }
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()
