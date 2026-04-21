# Kaleb Coleman Portfolio

Personal portfolio web app built with Flask, Jinja, and a lightweight static frontend.

## Current Site Structure

The portfolio now uses a simplified information architecture:

- `/home`
- `/projects`
- `/skills`
- `/experience`
- `/contact`
- `/resume`

Legacy numbered routes `/1` through `/5` remain in place as redirects so old links do not break.

## Content Direction

This version of the site is intentionally focused on:

- machine learning and deep learning work
- research-facing technical projects
- data engineering and modeling
- internships, labs, and graduate-oriented review

The Projects page is curated around strong public repositories instead of listing every repo.

## Project Structure

- [app.py](/Users/itzjuztmya/Kaleb/portfolio/app.py)
- [templates/](/Users/itzjuztmya/Kaleb/portfolio/templates)
- [static/css/base.css](/Users/itzjuztmya/Kaleb/portfolio/static/css/base.css)
- [static/resume.pdf](/Users/itzjuztmya/Kaleb/portfolio/static/resume.pdf)
- [tests/test_routes.py](/Users/itzjuztmya/Kaleb/portfolio/tests/test_routes.py)

## Run Locally

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
flask run --port 5001
```

Open [http://127.0.0.1:5001/home](http://127.0.0.1:5001/home).

## Test

```bash
python3 tests/test_routes.py
```

## Deployment Notes

- Deployment target is Azure Web App
- Workflow file: `.github/workflows/azure-webapp-deploy.yml`
- Startup command:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 app:app
```
