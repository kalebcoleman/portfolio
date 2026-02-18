import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import CASE_STUDIES, PROJECTS, PROJECT_BUILD_NOTES, app  # noqa: E402


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
        response = self.client.post(
            "/api/toolbox/query", json={"query": "run monte carlo"}
        )
        self.assertEqual(response.status_code, 200)

        payload = response.get_json()
        self.assertIsNotNone(payload)
        assert payload is not None

        for key in ("query", "matched_tool", "suggestion", "example_call"):
            self.assertIn(key, payload)

    def test_project_counts(self) -> None:
        self.assertEqual(len(PROJECTS), 10)
        self.assertEqual(len(CASE_STUDIES), 10)
        self.assertEqual(len(PROJECT_BUILD_NOTES), 10)

    def test_new_projects_render(self) -> None:
        page_two = self.client.get("/2")
        self.assertEqual(page_two.status_code, 200)
        self.assertIn(b"NBA Analytics Platform", page_two.data)
        self.assertIn(b"Stuxnet", page_two.data)

        page_four = self.client.get("/4")
        self.assertEqual(page_four.status_code, 200)
        self.assertIn(b"NAU Capstone", page_four.data)

        page_five = self.client.get("/5")
        self.assertEqual(page_five.status_code, 200)
        self.assertIn(b"Dockerized", page_five.data)

    def test_theme_toggle_and_bootstrap_script_present(self) -> None:
        page_one = self.client.get("/1")
        self.assertEqual(page_one.status_code, 200)
        self.assertIn(b"theme-toggle", page_one.data)
        self.assertIn(b"localStorage", page_one.data)


if __name__ == "__main__":
    unittest.main()
