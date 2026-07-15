from openai import OpenAI
from config import OPENROUTER_API_KEY

print(OPENROUTER_API_KEY)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[
        {"role":"user","content":"Say hello"}
    ]
)

print(response.choices[0].message.content)