from search import google_search
from openai import OpenAI
from config import OPENROUTER_API_KEY
import pandas as pd
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)


def find_contacts(company):

    # Search 1 - Official leadership page
    leadership_results = google_search(
        f'"{company}" leadership executive team'
    )

    # Search 2 - LinkedIn
    linkedin_results = google_search(
        f'site:linkedin.com/in "{company}" ("Head of Operations" OR "VP Operations" OR "Operations Director" OR "Mine Manager" OR "Plant Manager" OR "Site Director" OR COO)'
    )

    # Search 3 - Operations / News
    operations_results = google_search(
        f'"{company}" COO OR "VP Operations" OR "Head of Operations" mining'
    )

    # ONLY KEEP TOP 2 RESULTS FROM EACH SEARCH
    combined_results = f"""
==========================
LEADERSHIP RESULTS
==========================
{leadership_results.get("organic", [])[:2]}

==========================
LINKEDIN RESULTS
==========================
{linkedin_results.get("organic", [])[:2]}

==========================
OPERATIONS RESULTS
==========================
{operations_results.get("organic", [])[:2]}
"""

    prompt = f"""
You are FlytBase's outbound research assistant.

Your job is to identify the BEST operations decision-makers.

Company:
{company}

Search Results:

{combined_results}

Priority Roles:

- Chief Operating Officer
- EVP Operations
- VP Operations
- Vice President Operations
- Head of Operations
- Operations Director
- Mine Manager
- General Manager (Mine)
- Site Director
- VP HSE
- Head of HSE
- Plant Manager

Instructions:

- Use ONLY the provided search results.
- Never invent names.
- Never invent titles.
- Never invent LinkedIn URLs.
- Never include unnamed contacts.
- Never include placeholder contacts.
- Ignore CEOs if an operational leader exists.
- Ignore HR, Finance, Marketing, Sales, Consultants and Recruiters.
- Prefer official leadership pages first.
- Then LinkedIn.
- Then Reuters/company news.
- Return a maximum of 5 contacts.
- Return ONLY contacts with real names.
- If LinkedIn exists, return ONLY the profile URL.
- If unavailable write "Not publicly available".

Return ONLY this markdown table.

| Company | Name | Role | LinkedIn | Source |
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


def save_contacts(data):

    rows = []

    for item in data:

        contacts = item["Contacts"]

        for line in contacts.split("\n"):

            line = line.strip()

            if (
                not line.startswith("|")
                or "Company" in line
                or "---" in line
            ):
                continue

            cols = [c.strip() for c in line.split("|")[1:-1]]

            if len(cols) < 5:
                continue

            company = cols[0]
            name = cols[1]
            role = cols[2]
            linkedin = cols[3]
            source = cols[4]

            if not name.strip():
                continue

            if name.lower().startswith("unnamed"):
                continue

            if (
                role.strip().upper() == "CEO"
                or "chief executive officer" in role.lower()
            ):
                continue

            if linkedin.startswith("[") and "](" in linkedin:
                linkedin = linkedin.split("](")[1].rstrip(")")

            if linkedin in [
                "",
                "-",
                "N/A",
                "Not found",
                "[LinkedIn unavailable]"
            ]:
                linkedin = "Not publicly available"

            rows.append({
                "Company": company,
                "Name": name,
                "Role": role,
                "LinkedIn": linkedin,
                "Source": source
            })

    os.makedirs("output", exist_ok=True)

    df = pd.DataFrame(rows)

    if not df.empty:
        df = (
            df.drop_duplicates(subset=["Company", "Name"])
              .sort_values(["Company", "Role"])
        )

    df.to_csv(
        "output/contacts.csv",
        index=False
    )

    print("contacts.csv saved successfully.")