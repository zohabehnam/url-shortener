from fastapi.testclient import TestClient
from src.main import app


import unittest


class TestShortenAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.url = "https://reddit.com"

    def test_shorten_valid_url(self):
        response = self.client.post(
            "/api/shorten",
            headers={"Content-Type": "application/json"},
            json={"url": self.url},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("short_link", response.json())
        short_link = response.json()["short_link"]
        self.assertEqual(len(short_link), 5)

    def test_redirect_existing_short_link(self):
        response = self.client.post(
            "/api/shorten",
            headers={"Content-Type": "application/json"},
            json={"url": self.url},
        )
        short_link = response.json()["short_link"]

        response = self.client.get(f"/{short_link}", follow_redirects=False)
        self.assertEqual(response.status_code, 307)
        self.assertEqual(response.headers["Location"], self.url)

    def test_non_existing_path(self):
        response = self.client.get("/non-existing-path",
                                   follow_redirects=False)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
