import streamlit as st
import pandas as pd
from main import run_pipeline
from config import OPENROUTER_API_KEY

st.set_page_config(
    page_title="FlytBase AI Outbound Agent",
    page_icon="🚁",
    layout="wide"
)

st.title("🚁 FlytBase AI Outbound Agent")

st.write("""
This application automates outbound prospecting for FlytBase by:

- Identifying enterprise mining companies
- Finding relevant operations decision-makers
- Researching each company
- Generating personalized outbound emails
""")

if st.button("Run Agent"):

    with st.spinner("Running AI workflow... This may take a few minutes."):

        run_pipeline()

    st.success("Workflow completed successfully!")

    st.header("Companies")
    st.dataframe(pd.read_csv("output/companies.csv"))

    st.header("Contacts")
    st.dataframe(pd.read_csv("output/contacts.csv"))

    st.header("Research")
    st.dataframe(pd.read_csv("output/research.csv"))

    st.header("Emails")
    st.dataframe(pd.read_csv("output/emails.csv"))