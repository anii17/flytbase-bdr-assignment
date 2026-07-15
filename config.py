from dotenv import load_dotenv
import os

load_dotenv()

try:
    import streamlit as st

    OPENROUTER_API_KEY = st.secrets.get(
        "OPENROUTER_API_KEY",
        os.getenv("OPENROUTER_API_KEY")
    )

    SERPER_API_KEY = st.secrets.get(
        "SERPER_API_KEY",
        os.getenv("SERPER_API_KEY")
    )

except Exception:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")