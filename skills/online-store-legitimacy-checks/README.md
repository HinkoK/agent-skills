# online-store-legitimacy-checks

A research workflow for checking whether an unfamiliar online shop or checkout page looks legitimate before buying.

## What it checks

- URL/domain sanity;
- HTTPS/certificate basics;
- company identity and legal entity;
- delivery/returns/terms;
- payment risk;
- reputation patterns;
- price plausibility;
- scam red flags and safe-buying advice.

## Install

```bash
hermes skills install https://raw.githubusercontent.com/HinkoK/agent-skills/main/skills/online-store-legitimacy-checks/SKILL.md
```

## Example

```text
Check if this webshop is safe to buy from: https://example.com/product
```

The skill should return a clear verdict first: likely OK / mixed / avoid.
