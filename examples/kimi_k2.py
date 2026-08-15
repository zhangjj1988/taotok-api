#!/usr/bin/env python3
"""
Kimi K2 API integration example (Moonshot AI), via taotok.io.

Kimi K2's superpower is native multimodal vision: pass image_url parts
straight into chat.completions. Long-document QA and agent swarms welcome.

Docs: https://taotok.io/kimi-k2-api-integration
Install: pip install openai
"""
import os
from openai import OpenAI

# --- Setup ---
client = OpenAI(
    api_key=os.getenv("TAOTOK_API_KEY", "sk-your-totok-key"),
    base_url="https://api.taotok.io/v1",  # OpenAI-compatible gateway
)

# --- 1. Basic text completion ---
print("=== Kimi K2: basic completion ===")
resp = client.chat.completions.create(
    model="kimi-k2",
    messages=[{"role": "user", "content": "Summarize AI agent development trends in 2 sentences."}],
    max_tokens=256,
)
print(resp.choices[0].message.content)

# --- 2. Multimodal vision input (K2 differentiator) ---
print("\n=== Kimi K2: image input ===")
resp = client.chat.completions.create(
    model="kimi-k2",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What is wrong with this dashboard? Be specific."},
            {"type": "image_url", "image_url": {"url": "https://example.com/dashboard.png"}},
        ],
    }],
)
print(resp.choices[0].message.content)

# --- 3. Streaming ---
print("\n=== Kimi K2: streaming ===")
stream = client.chat.completions.create(
    model="kimi-k2",
    messages=[{"role": "user", "content": "Give me 3 prompt engineering tips."}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
print()

# --- 4. Function calling (agent workflow) ---
print("\n=== Kimi K2: function calling ===")
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
resp = client.chat.completions.create(
    model="kimi-k2",
    messages=[{"role": "user", "content": "What's the weather in Tokyo?"}],
    tools=tools,
)
print(resp.choices[0].message.tool_calls)
