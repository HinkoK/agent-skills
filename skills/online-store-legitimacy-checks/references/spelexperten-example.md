# Example: Spelexperten.dk legitimacy check

Session context: user asked whether `https://www.spelexperten.dk/cgi-bin/ibutik/AIR_ibutik.fcgi?funk=bestall_steg1` was a normal shop.

## Useful findings

- Deep link opened an old-looking CGI checkout/cart step, but it was under the real domain `www.spelexperten.dk`.
- Empty cart message appeared; navigating via “continue shopping” reached the normal storefront.
- Site had normal ecommerce pages: purchase terms (`KØBSVILKÅR`), delivery (`FRAGT`), FAQ, cookies.
- Terms listed a consistent legal entity, business address, VAT number, phone, and email.
  - Exact contact details are intentionally omitted from this public skill example; re-check the live site during an actual investigation.
- Payment terms said Danish card payments are handled through **Svea**, a normal Nordic payment provider.
- WHOIS showed `spelexperten.dk` registered in 2018 and active.
- TLS certificate was valid and tied to the Spelexperten brand/domain family.
- Search found Trustpilot/company-registry style results for the store/company, though some pages may be bot-protected.

## Verdict pattern used

Verdict: likely legitimate / OK to buy, with normal caution.

Safe-buying advice given:
- Navigate manually through `spelexperten.dk`, not only from an ad/email deep link.
- Pay by card or protected payment provider; avoid bank transfer.
- Check delivery/return terms because the company is Swedish and appears to ship from Sweden.
- Be more cautious if the item price is far below market.

## Generalizable lesson

An old CGI checkout URL is not by itself a scam signal if it stays on the correct domain and the surrounding evidence (company identity, terms, payment provider, domain age, reputation) is consistent. Treat it as a UI/legacy-system clue to verify, not as a standalone reason to reject the shop.