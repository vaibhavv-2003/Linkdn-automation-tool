import requests
import json
from utils import load_config

config = load_config()  # Load the configuration to access the Wit.ai token

def get_witai_message(query):  # Updated function name
    """
    Generate a cold message using Wit.ai.
    """
    witai_token = config.get("witai_server_access_token")
    url = f"https://api.wit.ai/message?v=20241221&q={query}"

    headers = {
        "Authorization": f"Bearer {witai_token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print(f"Wit.ai Response: {data}")
        return data.get("text", "Unable to generate a message.")
    except Exception as e:
        print(f"Error interacting with Wit.ai: {e}")
        return "Could not generate a personalized message."
