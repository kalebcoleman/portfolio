import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import app


class PortfolioRouteTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_root_redirects_to_page_one(self) -> None:
        response = self.client.get("/", follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].endswith("/1"))

    def test_pages_render(self) -> None:
        route_markers = {
            "/1": b"Professional Overview",
            "/2": b"Project Showcase",
            "/3": b"Data Analytics",
            "/4": b"Featured Project Case Studies",
            "/5": b"Build Notes Across Portfolio Projects",
        }

        for route, marker in route_markers.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertIn(marker, response.data)

    def test_toolbox_api_contract(self) -> None:
        response = self.client.post("/api/toolbox/query", json={"query": "run monte carlo"})
        self.assertEqual(response.status_code, 200)

        payload = response.get_json()
        self.assertIsNotNone(payload)
        assert payload is not None

        for key in ("query", "matched_tool", "suggestion", "example_call"):
            self.assertIn(key, payload)


if __name__ == "__main__":
    unittest.main()
