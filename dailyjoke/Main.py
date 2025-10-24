from .utils import fetch_joke

def run():
    """Get a daily joke."""
    print("Welcome to today's joke...")
    joke = fetch_joke()
    print(joke)

if __name__ == "__main__":
    run()