# taotok.io API Examples

Ready-to-run examples for the [taotok.io](https://taotok.io) unified LLM API gateway
(GPT-4o / Claude / Gemini / DeepSeek V4 / Kimi K2, one OpenAI-compatible endpoint, pay with USDT).

## Setup

```bash
pip install openai
export TAOTOK_API_KEY="sk-your-key"   # get it at https://taotok.io
```

## Examples

| File | Shows |
|------|-------|
| [`deepseek_v4.py`](deepseek_v4.py) | DeepSeek V4 basic + streaming + thinking mode + dynamic model switch |
| [`kimi_k2.py`](kimi_k2.py) | Kimi K2 text + native multimodal image input + function calling |
| [`multi_model_routing.py`](multi_model_routing.py) | Hybrid routing: vision→K2, simple text→V4-Flash, reasoning→V4-Pro |

## Full guides

- [DeepSeek V4 API guide](https://taotok.io/deepseek-v4-api-guide)
- [Kimi K2 API guide](https://taotok.io/kimi-k2-api-integration)
- [DeepSeek V4 vs Kimi K2](https://taotok.io/deepseek-v4-vs-kimi-k2)
