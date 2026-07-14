import pandas as pd
import os

os.makedirs("output", exist_ok=True)

def save_companies(data):
    df = pd.DataFrame(data)
    df.to_csv("output/companies.csv", index=False)

def save_research(data):
    df = pd.DataFrame(data)
    df.to_csv("output/research.csv", index=False)

def save_emails(data):
    df = pd.DataFrame(data)
    df.to_csv("output/emails.csv", index=False)