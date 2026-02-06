# Portfolio Agent Notes

This file captures implementation decisions for the Flask portfolio app in this repository.

## Current Product Decisions

- Keep a single visual theme across all endpoint pages using the existing light blue/clean style from page 1.
- Keep all five endpoints active: `/1`, `/2`, `/3`, `/4`, `/5`.
- On `/2`, do not render the NAU sample table under the scraper card.
- `/3` should show only:
  - the NBA image gallery
  - the AI course findings table
- Do not re-add the two top dashboard charts on `/3` unless explicitly requested.
- `/4` is a case-studies page and should use challenge/role/process/outcomes format for featured projects.
- `/5` is a cross-project build-notes page (not NAU-only) and should cover all showcased projects.

## `/3` NBA Gallery Rules

- Use exactly two images in the gallery:
  - `static/images/nba_plots/shot_difficulty_vs_actual_efficiency.png`
  - `static/images/nba_plots/player_archetypes_scatter.png`
- Gallery layout must be responsive and fit cleanly on desktop/mobile:
  - keep the framed image container (`.plot-media`)
  - keep `img` width fluid with `height: auto`
  - avoid overflow/cropping

## Content Accuracy Rules

- Keep project descriptions factual and consistent with real work.
- NAU Course Catalog Scraper:
  - Selenium + PDF prefix extraction + cleaning + CSV/export analysis flow
  - AI/ethics analysis in R Markdown
  - supports high-precision and broad recall analysis scripts plus ethics analysis
  - not presented as a SQLite storage project
- NBA Shot Data Engineering Package:
  - multi-source ingestion + cleaning + schema validation
  - rerunnable load/upsert behavior in SQLite
  - GAM modeling, clustering, and shot-archetype analysis
- Any NAU pipeline wording must remain CSV/report based (not NAU SQLite load claims).

## Naming Preferences

- Keep project name: `NBA Shot Data Engineering Package`
- Keep project name: `NAU Course Catalog Scraper`

## Run/Test Commands

- Install deps: `pip install -r requirements.txt`
- Run app: `export FLASK_APP=app.py && flask run --port 5001`
- Run tests: `python3 tests/test_routes.py`

## Deployment Notes

- Deployment target is Azure **Web App** (not Azure Static Web Apps).
- GitHub workflow: `.github/workflows/azure-webapp-deploy.yml`
- Required GitHub config:
  - Secret: `AZURE_WEBAPP_PUBLISH_PROFILE`
  - Variable: `AZURE_WEBAPP_NAME`
- Azure Web App startup command should be:
  - `gunicorn --bind=0.0.0.0 --timeout 600 app:app`
