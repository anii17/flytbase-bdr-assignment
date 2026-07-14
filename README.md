# FlytBase AI-Powered BDR Assignment

## Overview

This project is an AI-powered outbound prospecting workflow built for FlytBase.

The system automates the initial stages of enterprise outbound sales by:

- Identifying target mining companies similar to SQM
- Finding relevant operations decision-makers
- Researching each company
- Generating personalized outbound emails
- Exporting all outputs into CSV files

The solution demonstrates how AI can significantly reduce manual SDR research effort while producing personalized outbound campaigns.

---

## Workflow

```
Google Search (Serper API)
            │
            ▼
Identify Target Companies
            │
            ▼
Find Decision Makers
            │
            ▼
Research Company
            │
            ▼
Generate Personalized Email
            │
            ▼
Export CSV Files
```

---

## Features

- AI-powered company discovery
- AI-powered contact identification
- Company research generation
- Personalized outbound email generation
- CSV export for all outputs

---

## Project Structure

```
flytbase_bdr_assignment/

├── company.py
├── contacts.py
├── csv_export.py
├── email_agent.py
├── main.py
├── research.py
├── search.py
├── config.py
├── requirements.txt
├── README.md

└── output/
    ├── companies.csv
    ├── contacts.csv
    ├── research.csv
    └── emails.csv
```

---

## Tech Stack

- Python
- OpenRouter API
- Serper API
- Pandas
- Requests

---

## Installation

Clone the repository.

Install dependencies.

```bash
pip install -r requirements.txt
```

Add your API keys inside `config.py`.

Example:

```python
SERPER_API_KEY = "YOUR_SERPER_API_KEY"
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
```

---

## Running the Project

```bash
python main.py
```

---

## Output Files

The script generates four CSV files inside the `output/` folder.

### companies.csv

Target mining companies identified by the AI.

### contacts.csv

Relevant operational decision-makers for each company.

### research.csv

Company research including:

- Company overview
- Mining operations
- Recent developments
- Automation opportunities
- Why FlytBase is relevant

### emails.csv

Personalized outbound emails generated using the research.

---

## Future Improvements

- CRM integration (HubSpot / Salesforce)
- Apollo or Clay contact enrichment
- Email verification
- Multi-touch outbound sequences
- Better contact ranking using AI
- Automated meeting scheduling

---

## Author

Anisha Singh
