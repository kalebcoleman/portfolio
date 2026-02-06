# Resume Reference — Kaleb Coleman

> This file is a comprehensive reference of skills, projects, and accomplishments extracted
> directly from the codebase. Use it to populate and improve the portfolio website content.

---

## Profile

**Name:** Kaleb Coleman
**Headline:** Data Science Undergraduate | Machine Learning, Sports Analytics & AI Systems
**Degree:** B.S. in Data Science, Cybersecurity minor — Northern Arizona University (Expected May 2026)
**Contact:** 480-359-8122 | kaleb.a.coleman@gmail.com
**Links:** [GitHub](https://github.com/kalebcoleman) | [LinkedIn](https://linkedin.com/in/kaleb-coleman-a1807a284)

**Summary:**
Data science undergraduate who builds end-to-end systems — from raw API ingestion and schema-validated pipelines to predictive models and interactive dashboards. Core strengths in statistical modeling, feature engineering, and reproducible workflows across Python, R, and SQL. Experience shipping full-stack AI applications (Django + React), spatial sports analytics packages, and leakage-aware predictive models. Exploring deep learning, computer vision, and autonomous systems.

---

## Experience

**Data Analyst — Recording Academy (GRAMMYs)**
Website audience analysis, exploratory data analysis and visualization, user segmentation, and A/B testing to inform content strategy.

**Operations Manager — Moody Concepts**
Managed operations workflows, tracked performance metrics, and coordinated execution across day-to-day business activities.

---

## Technical Skills

### Languages
Python, R, JavaScript, SQL, C, HTML/CSS

### Data & ML
pandas, NumPy, scikit-learn, PyTorch, PyGAM, XGBoost, joblib, pyarrow, Weights & Biases

### Statistical Methods
Logistic regression, GAMs (generalized additive models), ridge/elastic net/LASSO, random forests, GBM, BART, LDA/QDA, KNN, B-splines, natural splines, smoothing splines, loess, bootstrap (up to 100K resamples), k-fold cross-validation, LOOCV, best subset selection, stepwise AIC/BIC, VIF diagnostics, Elo ratings

### Unsupervised Learning
Gaussian mixture models (EM algorithm with BIC selection), K-means (k-means++, mini-batch), spectral clustering, PCA, color quantization

### Deep Learning
Feedforward neural networks (ANN), convolutional neural networks (CNN), recurrent neural networks (RNN), hyperparameter optimization (grid/random search), filter visualization, custom tokenizers

### AI & Agents
Google Gemini (via LlamaIndex), ReAct agent framework, retrieval-augmented generation (RAG), HuggingFace embeddings (BAAI/bge-small-en-v1.5), PDF vector indexing, multi-tool orchestration, minimax with alpha-beta pruning

### Data Engineering
API ingestion (ESPN, NBA Stats, Alpha Vantage, OpenWeatherMap, NewsAPI), JSON parsing, schema validation, SQLite, PostgreSQL, SQLAlchemy (upsert/chunked batch writes), ETL pipelines, parquet, RDS/CSV export, database migrations, schema versioning

### Web Development
Flask, Django REST Framework, React 18, Vite 5, JWT authentication (access/refresh token rotation), Axios interceptors, Jinja2 templating, REST API design

### DevOps & Tools
Docker, docker-compose, Makefile, Git/GitHub, GitHub Actions CI/CD, Azure Web App deployment, Gunicorn, launchd scheduling, Conda, renv, pip, npm

### R Ecosystem
tidyverse (dplyr, tidyr, ggplot2, purrr, readr), devtools, testthat, roxygen2, renv, glmnet, pROC, slider, janitor, httr/httr2, DBI, RSQLite, rmarkdown, knitr, broom, ISLR/ISLR2, hoopR, future/future.apply

### Visualization
matplotlib, plotly, Streamlit, ggplot2, seaborn, partial dependence plots, court heatmaps, shot charts

---

## Projects

### 1. NBA Shot Data Engineering Package (spatialSportsR)
**R package + Python ML pipeline for NBA shot data engineering, modeling, and player profiling**

- Trained expected field goal (xFG) logistic regression model on 1.1M+ shots across 5 NBA seasons (2020-21 through 2024-25) with true out-of-sample evaluation on 2025-26 (~136K shots)
- xFG shot-make prediction achieved 62.7% holdout accuracy
- Engineered 15+ features: spatial coordinates (LOC_X, LOC_Y), shot distance, shot angle, shot type indicators (layup/dunk/jump/hook/floater), period, game clock, clutch flag, zone categories
- Built preprocessing pipeline with StandardScaler + OneHotEncoder (handle_unknown='ignore') via sklearn Pipeline
- Trained Generalized Additive Model (PyGAM LogisticGAM) with tensor product spatial surface (te(LOC_X, LOC_Y)), univariate smooths for distance/angle/clock/period, and linear shot-type terms
- Generated partial dependence plots showing marginal log-odds contribution per feature
- Developed Shot Difficulty Index (SDI): weighted composite of distance (30%), shot clock pressure (20%), shot type difficulty (20%), zone difficulty (15%), angle difficulty (15%)
- Built role-aware player archetype clustering using Gaussian Mixture Models with BIC model selection (2-6 components), 10 clustering features (zone percentages, distance entropy/std, SDI, xFG, pull-up rate, usage%, attempts/game), PCA projection for visualization
- Computed Points Over Expected (POE) and POE/$M salary-adjusted value efficiency using scraped salary data for 467 players from Basketball-Reference
- Created interactive Streamlit dashboard with shot map explorer, SDI scatter plots, and player filters
- Automated daily data refresh at 4:00 AM via macOS launchd job
- R package with roxygen2 documentation, testthat test suite (13 test files), and code coverage via covr

**Tech:** R (devtools, dplyr, rvest, DBI, RSQLite, future.apply), Python (scikit-learn, PyGAM, pandas, NumPy, matplotlib, plotly, Streamlit, joblib, pyarrow, beautifulsoup4)

### 2. AI Multitool Assistant
**Full-stack AI web application with chat, PDF Q&A, and real-time data tools**

- Built two-service architecture: React 18/Vite 5 SPA frontend + Django 5/DRF backend
- Implemented JWT authentication with 30-minute access tokens, 1-day refresh token rotation, and Axios interceptors for automatic token refresh on 401 responses
- Integrated Google Gemini 2.5-Flash via LlamaIndex ReAct agent framework supporting up to 10 reasoning iterations
- Built PDF document Q&A pipeline: upload handler parses multipart forms, creates per-user vector indexes using HuggingFace BAAI/bge-small-en-v1.5 embeddings, supports multi-document querying with persistent index storage
- Developed 5 real-time tool modules: stock prices (Alpha Vantage intraday), cryptocurrency (daily with USD normalization), weather (OpenWeatherMap with regex city extraction from natural language), news aggregation (NewsAPI), market gainers/losers analysis
- Designed 7 REST API endpoints: user registration, JWT token pair/refresh, notes CRUD, AI query with chat history context, chat history retrieval/clear, PDF upload and indexing
- User-scoped data models for notes (with author FK) and chat messages (with timestamps)
- Lazy LLM initialization with @lru_cache for fast startup; context-gated system prompts

**Tech:** Django 5, Django REST Framework, React 18, Vite 5, JWT, Google Gemini, LlamaIndex, HuggingFace Transformers, Axios, React Router v6

### 3. NAU Course Catalog Scraper
**Automated web scraping and AI curriculum analysis pipeline built with IAAAI collaboration**

- Scraped 12,944 course records across 150+ prefixes and 2 academic terms (Fall 2025, Spring 2026) using Selenium with headless Chrome
- Extracted course prefixes from NAU Course-Numbering-and-Prefixes PDF using pdfplumber
- Built resumable scraper architecture: deduplicates by URL set, logs empty/error prefixes, supports --overwrite and incremental modes with 0.25s politeness delays
- Developed 3-tier AI classification system:
  - High-precision script (95% fuzzy threshold): 16 primary AI patterns + context-gated secondary patterns
  - High-recall script (85% threshold): broader candidate detection for manual review
  - Ethics analysis: independent ethics keyword classification
- Fuzzy string matching via thefuzz library for typo-tolerant keyword detection
- Output artifacts: full term-level CSV (12,945 rows), deduplicated courses with AI/ethics flags, AI subset, prefix totals, summary metrics, empty prefix audit log
- R Markdown report (report.Rmd/report.pdf) with precision-versus-recall framing
- Unit tests covering normalization, context gating, and dedup/flag behavior

**Tech:** Python, Selenium, pdfplumber, pandas, thefuzz, R Markdown

### 4. ESPN NBA Data Pipeline (nba-data)
**R package for end-to-end ESPN NBA data collection, parsing, validation, and storage**

- Built complete pipeline: ESPN API JSON collection → parsing → schema validation → multi-format storage (RDS, CSV, SQLite)
- Parallel game collection via future::multisession with configurable worker count
- Exponential backoff retry logic (5 attempts, pause_base=1, pause_cap=60) with 403/429 detection and fallback to serial processing
- Parses 4 core tables: games (1 row/game), team_box (2 rows/game), player_box (N rows/game), betting lines (0-N rows/game)
- Schema enforcement: janitor::clean_names standardization, explicit type casting (integers, numerics, dates, logicals), central schema map with required/optional columns and NA defaults
- Database layer: SQLite with DBI abstraction, composite primary keys, indexes on (game_id, team_id, athlete_id, game_date), schema versioning via nbadata_meta table, migration system
- Upsert strategy: on_conflict_do_update for incremental season updates; ingest log table tracks run metadata
- Manifest system: compares expected vs. scraped games, detects missing/postponed/canceled, validates completeness against configurable threshold
- 13 testthat test files using saved JSON fixtures (no live API dependency); optional integration tests with NBDATA_LIVE=true
- Handles 1,000+ games per season across multi-season backfill

**Tech:** R (dplyr, tidyr, purrr, janitor, httr/httr2, jsonlite, DBI, RSQLite, lubridate, glue, future, future.apply, testthat, covr)

### 5. NBA Win Probability Models (nba-modeling)
**Leakage-aware predictive modeling for NBA home-team win probability**

- Engineered rolling window features (3/5/10-game lookbacks with lag-1 to prevent temporal leakage): eFG%, TS%, ORtg, DRtg, net rating, turnover%, rebounding rates, pace
- Computed possession-based advanced stats: possessions = FGA + 0.4*FTA - ORB + TOV
- Built matchup differentials (home minus away) and ratio features for all rolling metrics
- Integrated Elo rating system (season-reset and all-time variants) as predictive feature
- Inferential model: logistic regression with exponentiated odds ratios and 95% confidence intervals on 5 core predictors
- Predictive models compared: logistic regression, ridge (L2), elastic net (alpha grid: 0.25/0.5/0.75 via glmnet), random forest
- Holdout evaluation on final season (2025): ridge logistic achieved 67% accuracy, 0.684 AUC vs. 59.2% majority baseline
- Cross-validation (5-fold) for model selection; bootstrap resampling for threshold optimization and confidence intervals
- Chronological train/test split preserving temporal ordering across 2002-2025 seasons (~2,500 games with rolling features)
- Reproducible pipeline: set.seed(42), modular R scripts (AdvancedStats.R → InferentialModel.R → PredictiveModels.R)

**Tech:** R (dplyr, tidyr, readr, lubridate, slider, glmnet, pROC, ggplot2, scales, magrittr, hoopR)

### 6. NBA Data Ingestion Service (scrape)
**Containerized data ingestion pipeline with Docker and PostgreSQL**

- Designed PostgreSQL schema: nba_team_box (61 columns, composite PK), nba_player_box (45 columns, composite PK), nba_ingest_failures audit table
- Parallel ESPN API fetching with exponential backoff on 429/503 errors
- SQLAlchemy upsert logic: insert().on_conflict_do_update() with chunked batch processing (500 records/batch), NaN→None sanitization, schema type enforcement
- Partial ingest detection: requires both team_box AND player_box before marking a game as complete
- Makefile automation: `make up` (start PostgreSQL), `make ingest SEASONS=2024`, `make reset`, `make down`
- Docker Compose: PostgreSQL 16 with persistent volume, health checks (pg_isready), configurable environment

**Tech:** Python, PostgreSQL, SQLAlchemy, Docker, docker-compose, Makefile, requests, pandas

### 7. Deep Learning Projects
**Four progressive deep learning projects (Spring 2026 coursework)**

- **Project 1 — ANN:** Feedforward neural networks with training loops, loss computation, and data loading pipelines
- **Project 2 — Hyperparameter Optimization:** Grid and random search with model factory pattern; Weights & Biases experiment tracking; runnable via bash scripts
- **Project 3 — CNN:** Convolutional neural networks with filter visualization utilities for understanding learned feature representations
- **Project 4 — RNN:** Recurrent networks with custom tokenizer for sequence preprocessing, sequence batching, and sequence-level analysis
- Shared utilities module for reproducible seed management across all projects

**Tech:** Python, PyTorch, TorchVision, scikit-learn, Weights & Biases, Conda, Jupyter

### 8. Flask Portfolio Website
**Personal portfolio deployed to Azure with CI/CD**

- Flask 3 application serving 5 pages: professional overview, project showcase, analytics gallery, case studies, cross-project build notes
- NBA visualization gallery with shot difficulty and player archetype plots
- AI curriculum findings table (20 AI-related NAU courses)
- Case study pages using challenge/role/process/outcomes narrative format
- Automated deployment to Azure Web App via GitHub Actions workflow
- Gunicorn production server (--bind=0.0.0.0 --timeout 600)
- Route smoke tests and API contract verification

**Tech:** Flask 3, Jinja2, Gunicorn, GitHub Actions, Azure Web App, HTML/CSS/JavaScript

### 9. Halma AI
**Game-playing agent with adversarial search**

- Minimax algorithm with alpha-beta pruning and iterative deepening search
- Move ordering optimization for better pruning efficiency
- Heuristic evaluation function tuned to positional pressure
- Tkinter GUI for human-versus-AI play; headless arena for AI-versus-AI benchmarking

**Tech:** Python, Tkinter

---

## Coursework Highlights

### STA 478 — Statistical Learning (Fall 2025)
Classification (LDA, QDA, logistic regression, KNN with multiple kernels), resampling (100,000 bootstrap resamples, 300-iteration repeated holdout), regularization (VIF diagnostics with iterative removal, AIC/BIC stepwise selection, best subset via leaps), splines (B-splines with manual knots, natural splines, smoothing splines with CV-selected df, loess), GAMs (smooth terms with ANOVA model comparison), tree methods (random forests, GBM, BART). Datasets: ISLR Auto (392 obs), Boston (506 obs, 13 predictors), Wage.

### STA 486C — Advanced Statistical Modeling (NBA Capstone)
Leakage-aware NBA win prediction using rolling metrics. Possession-based efficiency metrics (eFG%, TS%, ORtg, DRtg, net rating). Ridge/elastic net/random forest comparison with chronological holdout. AUC/ROC calibration. Full proposal, report, and presentation.

### CS 472 — Unsupervised Machine Learning
K-means variants (k-means++, random init, mini-batch), Gaussian Mixture Models with EM algorithm (E-step/M-step implementation), spectral clustering, silhouette analysis, adjusted Rand index. Applied to color quantization (image compression to k colors by clustering RGB pixel values).

### Deep Learning (Spring 2026)
Progressive curriculum: ANN baselines → hyperparameter optimization → CNN with filter visualization → RNN with custom tokenizers. PyTorch + Weights & Biases tracking.

### Cybersecurity — Malware Analysis
Technical analysis of Stuxnet: 500KB multi-component worm targeting Siemens S7-315 PLCs, 4 zero-day exploits, stolen code-signing certificates, man-in-the-middle attack on industrial control systems. Referenced Zetter (2014), Langner (2011), Symantec W32.Stuxnet Dossier.

---

## Competitions

### DataFest 2026
Team data science competition. Reproducible workflow: data prep → feature engineering → modeling → visualization. Organized with separated concerns (src/data_prep, src/features, src/modeling, src/viz) and presentation materials.

---

## Key Metrics & Scale

| Metric | Value | Source |
|--------|-------|--------|
| xFG holdout accuracy | 62.7% | spatialSportsR |
| xFG training shots | 1.1M+ (5 seasons) | spatialSportsR |
| xFG evaluation shots | ~136K (2025-26) | spatialSportsR |
| Player salaries scraped | 467 | spatialSportsR |
| NAU courses scraped | 12,944 records | nau_course_scraping |
| Course prefixes processed | 150+ | nau_course_scraping |
| Win model holdout accuracy | 67% (ridge) vs 59.2% baseline | nba-modeling |
| Win model AUC | 0.684 | nba-modeling |
| NBA seasons modeled | 2002-2025 | nba-modeling |
| PostgreSQL schema columns | 61 (team_box) + 45 (player_box) | scrape |
| R package test files | 13 (nba-data) | nba-data |
| API tools integrated | 5 (stocks, crypto, weather, news, market) | ai-multitool-assistant |
| REST endpoints built | 7+ | ai-multitool-assistant |
| Bootstrap resamples | 100,000 | sta478 |
