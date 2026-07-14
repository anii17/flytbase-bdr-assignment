from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def generate_email(company, research):

    prompt = f"""
Write a cold outbound email.

Company:

{company}

Research:

{research}

Requirements:

- Mention one recent company insight.
- Explain why FlytBase is relevant.
- Keep it under 150 words.
- End with a clear CTA.

Return:

Subject

Email
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        max_tokens=600
    )

    return response.choices[0].message.content