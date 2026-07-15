from search import google_search
from company import extract_companies, save_companies
from contacts import find_contacts, save_contacts
from research import research_company
from email_agent import generate_email
from csv_export import save_research, save_emails


def run_pipeline():

    print("STEP 1: Finding companies...")

    search_results = google_search(
        "Top enterprise mining companies Latin America copper lithium gold mining Chile Peru Brazil autonomous operations"
    )

    company_table = extract_companies(search_results["organic"])

    companies_df = save_companies(company_table)

    contacts_data = []
    research_data = []
    email_data = []

    for company in companies_df["Company"][:5]:

        print(f"\nProcessing {company}...\n")

        contacts = find_contacts(company)

        contacts_data.append({
            "Company": company,
            "Contacts": contacts
        })

        results = google_search(
            f"{company} mining automation latest news"
        )

        research = research_company(
            company,
            results["organic"]
        )

        research_data.append({
            "Company": company,
            "Research": research
        })

        email = generate_email(
            company,
            research
        )

        email_data.append({
            "Company": company,
            "Email": email
        })

    save_contacts(contacts_data)
    save_research(research_data)
    save_emails(email_data)

    print("\nAll outputs generated successfully!")

    return True


if __name__ == "__main__":
    run_pipeline()