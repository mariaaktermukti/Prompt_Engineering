
from google import genai
import os

# Check API key
if not os.getenv("GEMINI_API_KEY"):
    print("API Key Missing!")
    exit()

print("API Key Found!")

# Create Gemini client
client = genai.Client()

# Reusable Prompt Template
template = """
You are an experienced {role}.

Explain {topic} to a {audience}.

Requirements:
1. Use {language}.
2. Provide real-world examples.
3. Keep the answer within {word_limit} words.
"""

# Get input from user
role = input("Enter AI Role: ")
topic = input("Enter Topic: ")
audience = input("Enter Audience: ")
language = input("Enter Language: ")
word_limit = input("Enter Word Limit: ")

# Generate prompt
prompt = template.format(
    role=role,
    topic=topic,
    audience=audience,
    language=language,
    word_limit=word_limit
)

print("\n--- Generated Prompt ---")
print(prompt)

# Send prompt to Gemini API
print("\n--- Gemini Response ---")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    print(response.text)

except Exception as e:
    print("API Error:", e)
