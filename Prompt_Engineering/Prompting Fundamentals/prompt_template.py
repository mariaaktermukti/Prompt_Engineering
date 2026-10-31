# Prompt Template
template = """
You are an experienced {role}.

Explain {topic} to a {audience}.

Requirements:
1. Use {language}.
2. Provide real-world examples.
3. Keep the answer within {word_limit} words.
"""

# Dynamic Variables
# role = "AI Engineer"
# topic = "Prompt Injection"
# audience = "Beginner CSE Student"
# language = "Bangla"
# word_limit = 200

role = "Data Scientist"
topic = "Neural Networks"
audience = "Intermediate CSE Student"
language = "Simple English"
word_limit = 300

# Generate Prompt
prompt = template.format(
    role=role,
    topic=topic,
    audience=audience,
    language=language,
    word_limit=word_limit
)

# Display Generated Prompt
print("Generated Prompt:")
print(prompt)