from openai import OpenAI
from config import OPENROUTER_API_KEY
import pandas as pd

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def extract_companies(search_results):

    prompt = f"""
You are an Enterprise SDR at FlytBase.

Your task is to identify high-value outbound target accounts.

FlytBase sells autonomous drone software for:

- Mining
- Metals
- Energy
- Heavy Industry
- Large Industrial Sites

Target companies should:

- Operate large mining sites
- Have multiple mines or industrial facilities
- Be enterprise companies
- Have significant operations in Latin America
- Be good candidates for drone inspections, surveying, asset monitoring, stockpile management, safety inspections, perimeter security, or industrial automation.

Exclude:

- SQM
- Small exploration companies
- Junior mining companies
- Consulting firms

Search Results:

{search_results}

Return ONLY this markdown table.

| Company | Country | Primary Minerals | Why FlytBase should target them |

Return 5–8 companies.

Prefer companies such as large copper, lithium, gold, iron ore, or diversified mining operators if supported by the search results.
"""

    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content


def save_companies(markdown_table):

    rows = []

    for line in markdown_table.split("\n"):

        line = line.strip()

        if (
            not line.startswith("|")
            or "Company" in line
            or "---" in line
        ):
            continue

        cols = [c.strip() for c in line.split("|")[1:-1]]

        if len(cols) >= 4:
            rows.append({
                "Company": cols[0],
                "Country": cols[1],
                "Primary Minerals": cols[2],
                "Why FlytBase should target them": cols[3]
            })

    df = pd.DataFrame(rows)

    df.to_csv(
        "output/companies.csv",
        index=False
    )

    return df