# taotok API

> One credit pool. Multiple models. Pay with PayPal or USDT. No credit card required.

**Live:** https://taotok.io | **Quickstart:** https://api.taotok.io/go/gh01

---

## What Makes This Different

| Pain Point | Traditional Providers | taotok |
|------------|----------------------|--------|
| Tracking multiple API keys | One key per provider | **One key, all models** |
| Complex billing | Per-token math | **Simple credits** |
| Stripe required | Credit card only | **PayPal + USDT (OKX)** |
| Missing models | Limited selection | **GPT-4o, Claude Sonnet 4, Gemini 2.0 Flash, Kimi K2 & more** |

---

## Supported Models

Every model below is reachable with the same API key and the same
OpenAI-compatible endpoint. These are the exact strings to pass in the `model`
field:

| Vendor | Model ID |
|--------|----------|
| OpenAI | `gpt-4o` |
| Anthropic | `claude-sonnet-4-20250514` |
| Google | `gemini-2.0-flash` |
| DeepSeek | `deepseek-chat`, `deepseek-v4-flash`, `deepseek-v4-pro` |
| Moonshot | `kimi-k2` |

For the full list of what is currently routed, call:

```bash
curl https://api.taotok.io/v1/models -H "Authorization: Bearer $TAOTOK_API_KEY"
```

---

## Quick Start

1. Sign up at [taotok.io](https://api.taotok.io/register) — your API key is created automatically.
2. Make your first call: copy-paste snippets for curl, Python or Node at the **[Quickstart](https://api.taotok.io/go/gh01)** (~5 minutes, includes a 401/429 checklist).
3. Point any OpenAI-compatible SDK at `https://api.taotok.io/v1` and swap the model name.

**Availability:** Taotok does not serve mainland China. Availability varies by region — please make sure your use complies with local law and our terms.

---

## Pricing

| Plan | Credits | Price | Best For |
|------|---------|-------|----------|
| Trial Pack | 200 | $5 | First test |
| Starter | 1,000 | $19 | Side projects |
| Pro | 3,000 | $49 | Production apps |
| Business | 9,600 | $149 | Teams |
| Scale | 19,960 | $499 | High volume |

All plans share one credit pool across every model.

---

## How It Works

1. Sign up at taotok.io → get one API key
2. Top up credits via PayPal or USDT (OKX)
3. Call any model with standard OpenAI-compatible endpoints

---

## Why crypto-native?

taotok-api is built so that **access comes before paperwork**. Instead of
attaching a credit card and passing a KYC step, the account balance is topped up
and settled in **USDT** — a stablecoin used here purely as a *payment method*,
the same role a card would play.

What that means in practice:

- **No credit card required.** Useful if international cards are hard to get,
  get declined for cross-border SaaS, or you simply don't want one attached.
- **No KYC document upload.** Your API key is your account — there's no separate
  identity-verification gate before your first request.
- **One key, many models.** The same key hits the unified
  `/v1/chat/completions` endpoint and routes to GPT-4o, Claude, Gemini, and
  DeepSeek.

USDT is a payment rail here, not an asset to hold — there is no staking, no
return, and no "earn" mechanic. You pay for tokens; you get tokens.

---

## Links

- Website: https://taotok.io
- Quickstart: https://api.taotok.io/go/gh01

---

## Community

- **Site & signup:** https://taotok.io
- **Discord:** https://discord.gg/eEsTYXpZJn — small, low-signal group for API builders and crypto-native devs. No spam, no recruiting.

---

## License

MIT
