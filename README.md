# taotok API

> One credit pool. 15+ models. Pay with PayPal or USDT. No credit card required.

**Live:** https://taotok.io | **Docs:** https://taotok.io/api

---

## What Makes This Different

| Pain Point | Traditional Providers | taotok |
|------------|----------------------|--------|
| Tracking multiple API keys | One key per provider | **One key, all models** |
| Complex billing | Per-token math | **Simple credits** |
| Stripe required | Credit card only | **PayPal + USDT (OKX)** |
| Missing models | Limited selection | **GPT-4o, Claude 3.5, Gemini 1.5, DeepSeek V3 & more** |

---

## Supported Models

**Text**

- GPT-4o, GPT-4o-mini, GPT-4-turbo
- Claude 3.5 Sonnet, Claude 3 Opus, Claude 3 Haiku
- Gemini 1.5 Pro, Gemini 1.5 Flash
- DeepSeek-V3, DeepSeek-R1, DeepSeek-V4

**Image & Video**

- DALL-E 3, Midjourney, Imagen 3
- Sora 2

---

## Quick Start

```bash
curl https://api.taotok.io/v1/models -H "Authorization: Bearer $TAOTOK_API_KEY"
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.taotok.io/v1",
    api_key="your-taotok-key"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

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
- API Docs: https://taotok.io/api

---

## Community

- **Site & signup:** https://taotok.io
- **Discord:** https://discord.gg/eEsTYXpZJn — small, low-signal group for API builders and crypto-native devs. No spam, no recruiting.

---

## License

MIT
