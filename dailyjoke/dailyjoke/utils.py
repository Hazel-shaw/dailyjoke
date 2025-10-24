import requests

def fetch_joke():
    """Fetch a random joke from an online API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    except requests.RequestException as e:
        return f"Error fetching joke: {e}" 