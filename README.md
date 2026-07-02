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
curl https://api.taotok.io/v1/models \
  -H "Authorization: Bearer $TAOTOK_API_KEY"
