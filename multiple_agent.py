import time
import os
from dotenv import load_dotenv
from openai import OpenAI
from google import genai

# Load API keys
load_dotenv()

# OpenAI client (NEW API)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Gemini client (NEW API)
gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_openai(prompt):
    start = time.time()

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    latency = time.time() - start
    text = response.choices[0].message.content
    tokens = response.usage.total_tokens

    return text, round(latency, 2), tokens


def call_gemini(prompt):
    start = time.time()

    response = gemini_client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    latency = time.time() - start
    text = response.text
    tokens = len(text.split())  # Gemini token count workaround

    return text, round(latency, 2), tokens


prompt = input("Enter your prompt: ")

results = []

# OpenAI
text, latency, tokens = call_openai(prompt)
results.append(("OpenAI GPT", text, latency, tokens))

# Gemini
text, latency, tokens = call_gemini(prompt)
results.append(("Google Gemini", text, latency, tokens))

print("\n--- REAL AI AGENT BENCHMARKING OUTPUT ---\n")

for r in results:
    print("Provider:", r[0])
    print("Latency:", r[2], "seconds")
    print("Token Count:", r[3])
    print("Response:")
    print(r[1])
    print("-" * 60)
