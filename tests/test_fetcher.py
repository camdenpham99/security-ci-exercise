# tests/test_fetcher.py
from mylib.fetcher import get_status

class DummyResp:
    def __init__(self, status_code):
        self.status_code = status_code

def test_get_status(monkeypatch):
    def fake_get(url, timeout=5):
        return DummyResp(200)
    monkeypatch.setattr("requests.get", fake_get)
    assert get_status("https://example.com") == 200
