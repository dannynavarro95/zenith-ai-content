import os
import requests

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

RAW_FILE = os.path.expanduser(
    "~/zenith-ai-content/brand/website_raw.txt"
)

OUTPUT_FILE = os.path.expanduser(
    "~/zenith-ai-content/brand/website_knowledge.txt"
)

with open(RAW_FILE, "r", encoding="utf-8") as f:
    raw_content = f.read()

raw_content = raw_content[:30000]

prompt = f"""
You are an expert brand strategist.

Analyze this website source content and create a clean knowledge base for an AI marketing system.

Extract:
- company identity
- services
- tone
- target audience
- style
- positioning
- branding
- communication style
- differentiators
- visual direction

Do NOT summarize code.

Focus on:
- texts
- marketing
- branding
- content
- structure
- messaging

Return a professional clean knowledge document.

WEBSITE CONTENT:

{raw_content}
"""

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-3.3-70b-versatile",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.4,
    "max_tokens": 2500
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

result = response.json()

print("\n")
print(result)
print("\n")

content = result["choices"][0]["message"]["content"]

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(content)

print("\n")
print("Knowledge base generated.")
print("\n")
print(f"Saved to: {OUTPUT_FILE}")
print("\n")
