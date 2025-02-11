import requests

def generate_cold_message_gemini(api_key, query):
    """
    Generate a cold message using Google Gemini API.

    :param api_key: Your Google Gemini API key.
    :param query: Query string for the cold message.
    :return: Generated cold message or an error message.
    """
    url = "https://gemini.googleapis.com/v1beta/generateMessage"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemini-1",
        "input": {
            "text": query
        },
        "parameters": {
            "maxOutputTokens": 200
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        if response.status_code == 200:
            return response_data.get("output", {}).get("text", "No output received.")
        else:
            return f"Error: {response_data.get('error', 'Unknown error occurred.')}"
    except Exception as e:
        return f"Error connecting to Google Gemini API: {e}"
