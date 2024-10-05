from openai import OpenAI
import os


api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(organization=os.getenv("OPENAPI_ORG"), api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with text, and your task is to translate it into emojis. Do not use any regular text. Do your best with emojis only."
    },
    {
      "role": "user",
      "content": "Artificial intelligence is a technology with great promise."
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1
)

print(response.choices[0].message)