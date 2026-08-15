#!/usr/bin/env python3
"""
DeepSeek V4 API integration example via taotok.io.

One OpenAI-compatible endpoint for DeepSeek V4-Pro / V4-Flash.
Switch models by changing a single string. Pay with USDT - no credit card needed.

Docs: https://taotok.io/deepseek-v4-api-guide
Install: pip install openai
"""
import os
from openai import OpenAI

# --- Setup ---
# Get your key at https://taotok.io (top up with USDT, no card required)
client = OpenAI(
    api_key=os.getenv("TAOTOK_API_KEY", "sk-your-totok-key"),
    base_url="https://api.taotok.io/v1",  # OpenAI-compatible gateway
)

# --- 1. Basic completion (V4-Flash: low cost, high throughput) ---
print("=== DeepSeek V4-Flash: basic completion ===")
resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Explain Mixture-of-Experts in one paragraph."}],
    max_tokens=512,
)
print(resp.choices[0].message.content)

# --- 2. Streaming (real-time output) ---
print("\n=== DeepSeek V4-Pro: streaming ===")
stream = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "Write a short haiku about APIs."}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
print()

# --- 3. Thinking / reasoning mode (V4-Pro) ---
print("\n=== DeepSeek V4-Pro: thinking mode ===")
resp = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[{"role": "user", "content": "A train leaves at 9:00 at 80 km/h; another at 9:30 at 100 km/h. When do they meet?"}],
    extra_body={"thinking": {"type": "enabled"}},
)
print("reasoning:", resp.choices[0].message.reasoning_content)
print("answer:", resp.choices[0].message.content)

# --- 4. Switch model dynamically (just change the model string) ---
print("\n=== Dynamic model routing ===")
for model in ["deepseek-v4-flash", "deepseek-v4-pro"]:
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Say 'hello' in one word."}],
        max_tokens=10,
    )
    print(f"{model}: {r.choices[0].message.content}")
