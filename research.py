from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def research_company(company, search_results):

    prompt = f"""
You are an Enterprise Sales Researcher.

Research this company.

Company:

{company}

Google Search Results:

{search_results}

Return:

Company Overview

Mining Operations

Recent News

Automation Opportunities

Why FlytBase is relevant

Keep everything factual.
"""

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        max_tokens=800
    )

    return response.choices[0].message.content