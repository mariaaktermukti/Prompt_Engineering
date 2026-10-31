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

# Display generated prompt
print("\n--- Generated Prompt ---")
print(prompt)