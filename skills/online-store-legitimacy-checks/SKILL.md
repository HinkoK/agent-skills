---
name: online-store-legitimacy-checks
description: "Assess whether an unfamiliar webshop, checkout page, ecommerce domain, or product listing is likely legitimate before a user buys. Use for scam checks, suspicious stores, fake-shop concerns, checkout URL sanity, EU cross-border ecommerce, payment-risk review, and safe-buying advice."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
tags: [research, ecommerce, scam-check, due-diligence, shopping, consumer-safety]
---

# Online store legitimacy checks

Use this skill when the user asks whether an unfamiliar webshop, checkout page, product listing, or ecommerce domain is trustworthy enough to buy from.


## Hermes usage rules

- Start with a clear verdict: **likely OK**, **mixed / caution**, or **avoid**.
- Use web evidence when available; do not infer legitimacy from HTTPS alone.
- Never ask the user to enter card details, credentials, or checkout information for verification.
- Prefer official registries, company identity, terms, payment protections, reputation patterns, and price plausibility.
- When evidence is incomplete, say what was not verifiable and give a safe buying path.

## Default answer shape

1. Give a **clear verdict first**: likely OK / mixed / avoid.
2. Then list **specific evidence checked**.
3. End with **practical safe-buying advice**: payment method, URL hygiene, return/delivery caveats.
4. Avoid overclaiming: say “looks legitimate” rather than “guaranteed safe”.

## Evidence workflow

Check as many of these as are available without logging in or entering sensitive data:

1. **URL and domain sanity**
   - Confirm the domain is the expected store domain, not a lookalike or tracking redirect.
   - Prefer the store homepage and navigate from there when the user sends a deep checkout URL.
   - Old CGI/cart paths can be legitimate if they remain under the correct domain.

2. **Transport/security basics**
   - Check HTTPS and whether the certificate matches the domain or parent brand.
   - Treat valid HTTPS as necessary but not sufficient.

3. **Company identity**
   - Find legal entity name, VAT/CVR/org number, physical address, email, and phone in terms/contact pages.
   - Cross-check the legal name/VAT/domain through search snippets or official/company registries when possible.

4. **Commerce terms**
   - Look for purchase terms, delivery page, returns/cancellation policy, warranty/complaints process, and privacy/cookie pages.
   - For EU/cross-border shops, note if the company ships from another country and whether returns may be inconvenient.

5. **Payment risk**
   - Prefer card or well-known payment providers with buyer protections.
   - Be cautious with bank transfer, crypto, PayPal Friends & Family, or off-site payment requests.
   - Recognize reputable payment providers, but do not let that alone decide the verdict.

6. **Reputation and age**
   - Search for Trustpilot/review pages, scam reports, company registry pages, and domain age/WHOIS where available.
   - Do not rely only on star ratings; scan for patterns: non-delivery, fake tracking, refund refusal, chargebacks.

7. **Product/price plausibility**
   - Compare the deal with market norms when the item is expensive or high-risk.
   - Very low prices, pressure timers, or impossible availability are red flags.

## Red flags

- Domain mismatch between product page and checkout/payment page without a well-known payment processor.
- No legal entity, VAT/org number, address, or workable contact path.
- New domain plus large discounts on high-demand products.
- Payment only by bank transfer/crypto or requests to pay outside the website.
- Copied terms, broken checkout, inconsistent languages/currencies, or fake social proof.
- Reviews dominated by recent non-delivery/refund complaints.

## Green flags

- Long-lived domain and consistent brand across local country domains.
- Legal entity and VAT/org number visible in terms/contact pages.
- Address and phone match the claimed company.
- Normal card/payment-provider checkout.
- Clear delivery, return, complaint, and refund terms.
- Independent review/registry presence with no obvious scam pattern.

## Reporting template

Use concise bullets:

```md
Вердикт: [можно / осторожно / лучше не рисковать]

Что проверил:
- домен/HTTPS: ...
- компания: ...
- оплата: ...
- доставка/возврат: ...
- репутация: ...

Как безопаснее купить:
- заходить вручную через основной домен;
- платить картой/защищённым провайдером;
- не использовать банковский перевод;
- проверить итоговую цену, доставку и возврат перед оплатой.
```

## References

- `references/spelexperten-example.md` — example of checking a legitimate-looking EU webshop with an old CGI checkout and Swedish legal entity serving Denmark.
