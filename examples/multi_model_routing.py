#!/usr/bin/env python3
"""
Hybrid multi-model routing: DeepSeek V4 + Kimi K2 via one taotok.io key.

Best-practice pattern from https://taotok.io/deepseek-v4-vs-kimi-k2:
- images / PDFs / screenshots  -> Kimi K2   (native vision)
- simple text                  -> V4-Flash  (cheap, high throughput)
- complex reasoning            -> V4-Pro    (thinking mode)

Both are OpenAI-compatible, so routing is just choosing the model string.
"""
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("TAOTOK_API_KEY", "sk-your-totok-key"),
    base_url="https://api.taotok.io/v1",
)


def route(user_message: str, has_image: bool = False) -> str:
    """Pick the cheapest model that can handle the task."""
    if has_image:
        return "kimi-k2"          # vision required
    if len(user_message) < 200:
        return "deepseek-v4-flash"  # simple text -> cheap
    return "deepseek-v4-pro"        # complex reasoning


def ask(user_message: str, image_url: str | None = None) -> str:
    model = route(user_message, has_image=bool(image_url))
    content = {"type": "text", "text": user_message}
    messages = [{
        "role": "user",
        "content": [content] + ([{"type": "image_url", "image_url": {"url": image_url}}] if image_url else []),
    }]
    resp = client.chat.completions.create(model=model, messages=messages)
    return f"[{model}] {resp.choices[0].message.content}"


if __name__ == "__main__":
    print(ask("Summarize this in one line: we built an AI gateway that routes to many models."))
    print(ask("Prove that sqrt(2) is irrational. Show the full proof step by step."))
    # print(ask("Read this chart.", image_url="https://example.com/chart.png"))
