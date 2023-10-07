import openai

# Set up the API key
openai.api_key = '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' # Replace with your API Key

# Use the API (e.g., using the "davinci" engine for completions)
response = openai.Completion.create(
    engine="davinci",
    prompt="What is finance IQ?",
    max_tokens=50
)

print(response.choices[0].text.strip())