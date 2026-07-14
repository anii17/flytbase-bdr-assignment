import requests
from config import SERPER_API_KEY


def google_search(query):

    url = "https://google.serper.dev/search"

    payload = {
        "q": query
    }

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        if "organic" not in data:
            data["organic"] = []

        return data

    except requests.exceptions.RequestException as e:
        print(f"Serper API Error: {e}")
        return {"organic": []}

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return {"organic": []}