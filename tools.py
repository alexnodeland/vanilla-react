import httpx

def calculate(what):
    """
    Dynamically evaluate mathematical expressions provided as strings.
    """
    return eval(what)

def wikipedia(q):
    """
    Fetch a summary from Wikipedia based on a query string.
    """
    return httpx.get(
        "https://en.wikipedia.org/w/api.php",
        params={"action": "query", "list": "search", "srsearch": q, "format": "json"},
    ).json()["query"]["search"][0]["snippet"]

# Add more predefined actions here as needed