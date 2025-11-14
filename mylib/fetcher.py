# mylib/fetcher.py
import requests

def get_status(url: str) -> int:
    """Fetch URL and return HTTP status code."""
    resp = requests.get(url, timeout=5)
    return resp.status_code
