import os
import json
import requests
import replicate

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

PROMPT_PATH = "../prompts/master_prompt.txt"

KNOWLEDGE_PATH = "../brand/website_knowledge.txt"

with open(PROMPT_PATH, "r") as file:
    MASTER_PROMPT = file.read()

with open(KNOWLEDGE_PATH, "r") as file:
    WEBSITE_KNOWLEDGE = file.read()

topic = "AI automation for modern businesses"

full_prompt = f"""
{MASTER_PROMPT}

WEBSITE KNOWLEDGE:
{WEBSITE_KNOWLEDGE}

TOPIC:
{topic}
"""

print("\n")
print("Generating campaign idea with Groq...")
print("\n")

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
            "content": full_prompt
        }
    ],
    "temperature": 1,
    "max_tokens": 1200
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

result = response.json()

content = result["choices"][0]["message"]["content"]

clean_json = (
    content
    .replace("```json", "")
    .replace("```", "")
    .strip()
)

campaign = json.loads(clean_json)

with open(
    "../output/campaign.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        campaign,
        f,
        indent=2,
        ensure_ascii=False
    )

print("Campaign saved.")
print("\n")

print("\n")
print("TITLE:")
print(campaign["title"])

print("\n")
print("Generating image with Flux...")
print("\n")

output = replicate.run(
    "black-forest-labs/flux-schnell",
    input={
        "prompt": campaign["image_prompt"],
        "aspect_ratio": "4:5",
        "output_format": "png",
        "output_quality": 100
    }
)

image_url = output[0]

print("\n")
print("IMAGE GENERATED:")
print(image_url)
print("\n")

print("Downloading image...")
print("\n")

image_data = requests.get(image_url).content

with open(
    "../output/generated-image.png",
    "wb"
) as f:

    f.write(image_data)

print("Image saved:")
print("../output/generated-image.png")
print("\n")
