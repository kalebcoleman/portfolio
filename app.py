from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

PROFILE: dict[str, Any] = {
    "name": "Kaleb Coleman",
    "headline": "Data Science Undergraduate | Machine Learning, Sports Analytics & AI Systems",
    "summary": (
        "Data science undergraduate who builds end-to-end systems \u2014 from raw API "
        "ingestion and schema-validated pipelines to predictive models and interactive "
        "dashboards. Core strengths in statistical modeling, feature engineering, and "
        "reproducible workflows across Python, R, and SQL. Experience shipping full-stack "
        "AI applications (Django + React), spatial sports analytics packages, and "
        "leakage-aware predictive models. Exploring deep learning, computer vision, "
        "and autonomous systems."
    ),
    "degree": "B.S. in Data Science",
    "minor": "Cybersecurity minor",
    "graduation": "May 2026",
    "phone": "480-359-8122",
    "email": "kaleb.a.coleman@gmail.com",
    "linkedin_url": "https://linkedin.com/in/kaleb-coleman-a1807a284",
    "github_url": "https://github.com/kalebcoleman",
    "resume_url": "https://docs.google.com/document/d/1Vox1f_4pb3lWcYDWgTEYG1koPp9b1vb4VD6p2ZpMkpQ/edit?usp=sharing",
}

EDUCATION: list[dict[str, str]] = [
    {
        "institution": "Northern Arizona University",
        "program": "B.S. in Data Science",
        "details": "Cybersecurity minor",
        "timeline": "Expected graduation: May 2026",
    }
]

SKILLS: dict[str, list[str]] = {
    "Languages": ["Python", "R", "JavaScript", "SQL", "C", "HTML/CSS"],
    "Data & ML": [
        "pandas", "NumPy", "scikit-learn", "PyTorch", "PyGAM",
        "XGBoost", "Weights & Biases",
    ],
    "Statistical Methods": [
        "Logistic regression", "GAMs", "Ridge/Elastic Net/LASSO",
        "Random forests", "GBM", "Bootstrap", "k-fold CV",
    ],
    "Deep Learning": [
        "Feedforward networks (ANN)", "CNN", "RNN",
        "Hyperparameter optimization", "Filter visualization",
    ],
    "AI & Agents": [
        "Google Gemini", "LlamaIndex ReAct", "RAG",
        "HuggingFace embeddings", "PDF vector indexing",
        "Minimax / alpha-beta pruning",
    ],
    "Data Engineering": [
        "API ingestion", "JSON parsing", "Schema validation",
        "SQLite", "PostgreSQL", "SQLAlchemy", "ETL pipelines",
    ],
    "Web Development": [
        "Flask", "Django REST Framework", "React 18", "Vite",
        "JWT auth", "REST API design", "Jinja2",
    ],
    "DevOps & Tools": [
        "Docker", "docker-compose", "Makefile", "Git/GitHub",
        "GitHub Actions CI/CD", "Azure Web App", "Gunicorn",
    ],
    "R Ecosystem": [
        "tidyverse", "devtools", "testthat", "roxygen2",
        "glmnet", "pROC", "DBI/RSQLite", "rmarkdown",
    ],
    "Visualization": [
        "matplotlib", "plotly", "Streamlit", "ggplot2",
        "seaborn", "court heatmaps",
    ],
}

EXPERIENCE: list[dict[str, str]] = [
    {
        "title": "Data Analyst",
        "company": "Recording Academy (GRAMMYs)",
        "summary": (
            "Website audience analysis, exploratory data analysis and visualization, "
            "user segmentation, and A/B testing to inform content strategy."
        ),
    },
    {
        "title": "Operations Manager",
        "company": "Moody Concepts",
        "summary": (
            "Managed operations workflows, tracked performance metrics, and coordinated "
            "execution across day-to-day business activities."
        ),
    },
]

PROJECTS: list[dict[str, Any]] = [
    {
        "name": "NBA Shot Data Engineering Package",
        "tag": "spatialSportsR",
        "description": (
            "Multi-source NBA shot data engineering package with cleaning, schema validation, "
            "and rerunnable SQLite upserts that power GAM modeling and shot archetype analysis "
            "across five NBA seasons."
        ),
        "key_features": [
            "Multi-source ingestion + normalization across 5 NBA seasons",
            "Schema validation and rerunnable SQLite load/upsert behavior",
            "xFG logistic regression + GAM with tensor product spatial surface",
            "Shot Difficulty Index (SDI) feature layer for difficulty modeling",
            "GMM player archetype clustering with BIC selection and PCA projection",
        ],
        "tech_stack": [
            "R", "Python", "scikit-learn", "PyGAM", "SQLite",
            "Streamlit", "matplotlib", "pandas",
        ],
        "metrics": {
            "xFG Accuracy": "62.7%",
            "Training shots": "1.1M+",
            "Eval shots": "~136K",
            "Players": "467",
            "Seasons": "5",
        },
    },
    {
        "name": "AI Multitool Assistant",
        "tag": "ai-multitool",
        "description": (
            "Full-stack AI web application with chat, PDF Q&A, and real-time data tools. "
            "Two-service architecture with JWT authentication and Gemini 2.5-Flash via a "
            "LlamaIndex ReAct agent."
        ),
        "key_features": [
            "ReAct-style chat agent powered by Gemini 2.5-Flash via LlamaIndex",
            "PDF upload + BAAI/bge-small-en-v1.5 embeddings for vector search",
            "5 real-time tool modules: stocks, crypto, weather, news, market",
            "JWT auth with 30-min access tokens and automatic refresh rotation",
            "7 REST API endpoints with user-scoped data models",
        ],
        "tech_stack": [
            "Django REST", "React 18", "Vite", "JWT",
            "Gemini", "LlamaIndex", "HuggingFace",
        ],
        "metrics": {
            "API tools": "5",
            "Endpoints": "7+",
            "Architecture": "2-service",
        },
    },
    {
        "name": "ESPN NBA Data Pipeline",
        "tag": "nba-data",
        "description": (
            "R package for end-to-end ESPN NBA data collection, parsing, validation, "
            "and storage. Handles 1,000+ games per season with parallel collection and "
            "exponential backoff retry logic."
        ),
        "key_features": [
            "Complete pipeline: ESPN API JSON \u2192 parsing \u2192 schema validation \u2192 storage",
            "Parallel game collection via future::multisession with retry logic",
            "4 core tables: games, team_box, player_box, betting lines",
            "SQLite with composite primary keys, schema versioning, upsert strategy",
            "13 testthat test files using saved JSON fixtures",
        ],
        "tech_stack": [
            "R", "dplyr", "httr2", "DBI", "RSQLite",
            "testthat", "future", "jsonlite",
        ],
        "metrics": {
            "Games/season": "1,000+",
            "Test files": "13",
            "Core tables": "4",
        },
    },
    {
        "name": "NAU Course Catalog Scraper",
        "tag": "nau-scraper",
        "description": (
            "Automated web scraping and AI curriculum analysis pipeline built with IAAAI "
            "collaboration. Scraped 12,944 course records across Fall 2025 and Spring 2026 "
            "with a 3-tier classification system."
        ),
        "key_features": [
            "Selenium scraper across 150+ prefixes and 2 academic terms",
            "Prefix extraction from NAU PDF via pdfplumber",
            "3-tier AI classification: high-precision, high-recall, and ethics analysis",
            "Fuzzy string matching via thefuzz for typo-tolerant detection",
            "R Markdown report with precision-versus-recall framing",
        ],
        "tech_stack": [
            "Python", "Selenium", "pdfplumber", "pandas",
            "thefuzz", "R Markdown",
        ],
        "metrics": {
            "Courses": "12,944",
            "Prefixes": "150+",
            "Terms": "2",
        },
    },
    {
        "name": "NBA Win Probability Models",
        "tag": "nba-modeling",
        "description": (
            "Leakage-aware predictive modeling for NBA home-team win probability using "
            "rolling window features across 2002\u20132025 seasons."
        ),
        "key_features": [
            "Rolling window features (3/5/10-game lookbacks) with lag-1 leakage prevention",
            "Possession-based advanced stats: eFG%, TS%, ORtg, DRtg, net rating",
            "Model comparison: logistic, ridge, elastic net, random forest",
            "Elo rating system (season-reset and all-time variants)",
            "Chronological train/test split preserving temporal ordering",
        ],
        "tech_stack": [
            "R", "glmnet", "pROC", "ggplot2",
            "slider", "hoopR",
        ],
        "metrics": {
            "Accuracy": "67%",
            "AUC": "0.684",
            "Baseline": "59.2%",
            "Seasons": "2002\u20132025",
        },
    },
    {
        "name": "Deep Learning Projects",
        "tag": "deep-learning",
        "description": (
            "Four progressive deep learning projects (Spring 2026 coursework): feedforward "
            "networks, hyperparameter optimization, CNNs with filter visualization, and "
            "RNNs with custom tokenizers."
        ),
        "key_features": [
            "ANN: Training loops, loss computation, data loading pipelines",
            "HPO: Grid/random search with Weights & Biases experiment tracking",
            "CNN: Filter visualization for understanding learned features",
            "RNN: Custom tokenizer for sequence preprocessing and analysis",
            "Shared seed management utilities for reproducibility",
        ],
        "tech_stack": [
            "PyTorch", "TorchVision", "scikit-learn",
            "Weights & Biases", "Conda",
        ],
        "metrics": {
            "Projects": "4",
            "Framework": "PyTorch",
            "Tracking": "W&B",
        },
    },
]

NBA_PLOTS: list[dict[str, str]] = [
    {
        "file": "nba_plots/shot_difficulty_vs_actual_efficiency.png",
        "title": "Shot Difficulty vs Actual Efficiency",
        "caption": "Volume-weighted SDI versus field goal efficiency with residual color context.",
    },
    {
        "file": "nba_plots/player_archetypes_scatter.png",
        "title": "PCA Clustering of Player Shot Archetypes",
        "caption": "Role-aware clustering projection showing grouped player shot-profile archetypes.",
    },
]

AI_COURSES: list[dict[str, str]] = [
    {"prefix": "BAN", "number": "518", "title": "E-commerce Analytics And Strategy"},
    {"prefix": "CIT", "number": "460", "title": "Emerging Technologies In Information Technology"},
    {"prefix": "CS", "number": "102", "title": "Artificial Intelligence Literacy"},
    {"prefix": "CS", "number": "413", "title": "Virtual Worlds"},
    {"prefix": "CS", "number": "413H", "title": "Virtual Worlds - Honors"},
    {"prefix": "CS", "number": "470", "title": "Artificial Intelligence"},
    {"prefix": "CS", "number": "470H", "title": "Artificial Intelligence - Honors"},
    {"prefix": "CS", "number": "472", "title": "Unsupervised Machine Learning"},
    {"prefix": "CS", "number": "570", "title": "Advanced Intelligent Systems"},
    {"prefix": "CS", "number": "572", "title": "Unsupervised Machine Learning"},
    {"prefix": "CS", "number": "573", "title": "Interpretable Machine Learning"},
    {"prefix": "EE", "number": "443", "title": "Foundations Of Intelligent Systems"},
    {"prefix": "EE", "number": "543", "title": "Pattern Recognition"},
    {"prefix": "ETC", "number": "767", "title": "Research In Learning Analytics And Artificial Intelligence"},
    {"prefix": "INF", "number": "504", "title": "Data Mining And Machine Learning"},
    {"prefix": "INF", "number": "586", "title": "Data Analytics Capstone"},
    {"prefix": "MRE", "number": "372", "title": "Introduction To Probability And Machine Learning"},
    {"prefix": "PRM", "number": "165", "title": "AI And The Future Of Fun"},
    {"prefix": "PSY", "number": "305", "title": "Data Science And AI In Psychology"},
    {"prefix": "PSY", "number": "305H", "title": "Data Science And AI In Psychology - Honors"},
    {"prefix": "PSY", "number": "628", "title": "Research Dissemination Skills In The Psychological Sciences"},
]

KEY_METRICS: list[dict[str, str]] = [
    {"label": "xFG Holdout Accuracy", "value": "62.7%", "source": "spatialSportsR"},
    {"label": "xFG Training Shots", "value": "1.1M+", "source": "spatialSportsR"},
    {"label": "Courses Scraped", "value": "12,944", "source": "nau_course_scraping"},
    {"label": "Win Model Accuracy", "value": "67%", "source": "nba-modeling"},
    {"label": "Win Model AUC", "value": "0.684", "source": "nba-modeling"},
    {"label": "NBA Seasons Modeled", "value": "2002\u20132025", "source": "nba-modeling"},
    {"label": "R Package Test Files", "value": "13", "source": "nba-data"},
    {"label": "API Tools Integrated", "value": "5", "source": "ai-multitool"},
    {"label": "REST Endpoints", "value": "7+", "source": "ai-multitool"},
    {"label": "Bootstrap Resamples", "value": "100,000", "source": "sta478"},
    {"label": "Players Profiled", "value": "467", "source": "spatialSportsR"},
]

CASE_STUDIES: list[dict[str, Any]] = [
    {
        "project": "NBA Shot Data Engineering Package",
        "role": "Data engineer and modeling workflow builder",
        "challenge": (
            "Create a repeatable multi-source shot-data pipeline that supports downstream modeling, "
            "player archetype discovery, and visual analysis without schema drift issues."
        ),
        "process": [
            "Ingested and merged 1.1M+ shots across 5 NBA seasons from multiple sources",
            "Standardized schema and validation checks before model features were generated",
            "Built rerunnable load behavior in SQLite to keep analytics tables stable",
            "Engineered xFG/residual/difficulty features for GAM and clustering workflows",
            "Developed Streamlit dashboard with daily automated refresh via launchd",
        ],
        "outcomes": [
            "xFG shot-make classifier reached 62.7% holdout accuracy",
            "Consistent feature layer for shot-quality and player-value analysis",
            "PCA/archetype outputs and residual plots suitable for portfolio storytelling",
            "Salary-adjusted POE/$M value efficiency metrics for 467 players",
        ],
    },
    {
        "project": "AI Multitool Assistant",
        "role": "Full-stack developer and AI integration lead",
        "challenge": (
            "Build one assistant experience that combines authenticated chat, PDF Q&A, "
            "and real-time market/weather/news tools without turning the UI into separate silos."
        ),
        "process": [
            "Split the app into a React/Vite frontend and Django REST backend",
            "Implemented JWT auth with 30-min access tokens and refresh rotation",
            "Integrated Gemini via LlamaIndex ReAct agent with up to 10 reasoning iterations",
            "Added PDF upload and indexing flow for document-grounded querying",
        ],
        "outcomes": [
            "Single app flow for chat, documents, and tools with consistent auth",
            "Composable backend endpoint surface for iterative feature additions",
            "Clear separation between frontend UX and backend orchestration logic",
        ],
    },
    {
        "project": "ESPN NBA Data Pipeline",
        "role": "R package developer and data pipeline architect",
        "challenge": (
            "Build a robust, testable R package that ingests 1,000+ NBA games per season "
            "from ESPN APIs with graceful error handling and schema enforcement."
        ),
        "process": [
            "Designed parallel collection via future::multisession with configurable workers",
            "Implemented exponential backoff retry logic with 403/429 detection",
            "Built schema enforcement with janitor::clean_names and explicit type casting",
            "Created manifest system to detect missing/postponed/canceled games",
        ],
        "outcomes": [
            "4 core parsed tables with composite primary keys and schema versioning",
            "13 testthat test files using saved JSON fixtures (no live API dependency)",
            "Upsert strategy enabling incremental season updates without duplicates",
        ],
    },
    {
        "project": "NAU Course Catalog Scraper",
        "role": "Scraper and analysis pipeline developer",
        "challenge": (
            "Audit AI and ethics coverage across NAU courses where catalog content is spread "
            "across term pages and prefix sources with inconsistent coverage."
        ),
        "process": [
            "Extracted and maintained course prefixes from PDF plus manual missing-prefix review",
            "Built Selenium scrape flow with headless/non-headless and overwrite/incremental modes",
            "Logged empty/error prefixes and preserved term-level metadata for traceability",
            "Separated high-precision AI analysis, broad candidate search, and ethics analysis scripts",
        ],
        "outcomes": [
            "12,944 course records scraped across 150+ prefixes and 2 academic terms",
            "Report-ready findings in report.Rmd/report.pdf with precision-versus-recall framing",
            "Transparent pipeline where each transformation stage is independently inspectable",
        ],
    },
    {
        "project": "NBA Win Probability Models",
        "role": "Statistical modeler and feature engineer",
        "challenge": (
            "Build win probability models across 23 NBA seasons while preventing temporal "
            "data leakage that would inflate performance metrics."
        ),
        "process": [
            "Engineered rolling window features (3/5/10-game) with lag-1 to prevent leakage",
            "Computed possession-based advanced stats and matchup differentials",
            "Integrated Elo rating system as predictive feature (season-reset and all-time)",
            "Compared logistic, ridge, elastic net, and random forest via 5-fold CV",
        ],
        "outcomes": [
            "Ridge logistic achieved 67% accuracy and 0.684 AUC on holdout (vs 59.2% baseline)",
            "Chronological train/test split preserving temporal ordering across 2002\u20132025",
            "Bootstrap-optimized classification thresholds with confidence intervals",
        ],
    },
    {
        "project": "Deep Learning Projects",
        "role": "Deep learning practitioner and experiment tracker",
        "challenge": (
            "Complete four progressive DL projects building from basic ANNs to RNNs "
            "while maintaining reproducibility and tracking experiment results."
        ),
        "process": [
            "Built feedforward networks with custom training loops and data pipelines",
            "Implemented grid/random HPO with model factory pattern and W&B tracking",
            "Developed CNN with filter visualization utilities for feature interpretation",
            "Created RNN with custom tokenizer for sequence preprocessing",
        ],
        "outcomes": [
            "Comprehensive DL portfolio covering ANN, CNN, RNN, and hyperparameter optimization",
            "Reproducible experiments with shared seed management across all projects",
            "W&B experiment tracking for systematic hyperparameter comparison",
        ],
    },
]

PROJECT_BUILD_NOTES: list[dict[str, Any]] = [
    {
        "project": "NBA Shot Data Engineering Package",
        "focus": "SQLite-backed multi-source shot modeling and clustering pipeline.",
        "notes": [
            "Ingests shot and context data from multiple sources and seasons into SQLite",
            "Normalizes schema and validates integrity before downstream modeling",
            "Uses rerunnable load/upsert behavior to keep SQLite tables stable",
            "Builds xFG, residual, and shot-difficulty feature layers",
            "Runs GAM modeling and clustering workflows for player archetype analysis",
            "Automates daily refresh via macOS launchd job at 4:00 AM",
        ],
        "tech_focus": ["R", "Python", "SQLite", "PyGAM", "scikit-learn", "Streamlit"],
    },
    {
        "project": "AI Multitool Assistant",
        "focus": "Two-service full-stack AI product with secure API workflows.",
        "notes": [
            "React/Vite frontend with Django REST backend and JWT auth lifecycle",
            "Gemini + LlamaIndex orchestration for tool-augmented chat responses",
            "Document upload/index/query flow for PDF question answering",
            "Tool modules for stocks, crypto, weather, market data, and news",
            "User-scoped notes and chat-history endpoints for persistent workspace state",
        ],
        "tech_focus": ["React", "Vite", "Django REST", "JWT", "Gemini", "LlamaIndex"],
    },
    {
        "project": "ESPN NBA Data Pipeline",
        "focus": "R package with parallel collection, schema enforcement, and fixture-based tests.",
        "notes": [
            "Parallel game collection via future::multisession with configurable workers",
            "Exponential backoff retry logic (5 attempts) with 403/429 detection",
            "4 core tables with composite primary keys and schema versioning via nbadata_meta",
            "Manifest system compares expected vs scraped games for completeness validation",
            "13 testthat test files using saved JSON fixtures; optional live integration tests",
        ],
        "tech_focus": ["R", "devtools", "testthat", "DBI", "RSQLite", "future"],
    },
    {
        "project": "NAU Course Catalog Scraper",
        "focus": "Scraping and analysis workflow for curriculum coverage auditing.",
        "notes": [
            "Extracts prefixes from the NAU PDF and maintains a reusable prefix list",
            "Supports headless/non-headless runs plus overwrite/incremental controls",
            "Writes term-level course rows and empty-prefix audit logs to CSV outputs",
            "Splits analysis into ai_analysis.py, ai_analysis_broad.py, and ethics_analysis.py",
            "Summarizes findings in report.Rmd/report.pdf with precision-versus-recall tradeoffs",
        ],
        "tech_focus": ["Python", "Selenium", "pdfplumber", "pandas", "thefuzz", "R Markdown"],
    },
    {
        "project": "NBA Win Probability Models",
        "focus": "Leakage-aware predictive modeling with rolling features and model comparison.",
        "notes": [
            "Rolling window features (3/5/10-game) with lag-1 to prevent temporal leakage",
            "Possession-based advanced stats: eFG%, TS%, ORtg, DRtg, net rating, pace",
            "Matchup differentials (home minus away) and ratio features for all rolling metrics",
            "Elo rating system integrated as predictive feature (season-reset and all-time)",
            "Reproducible pipeline: set.seed(42), modular R scripts in execution order",
        ],
        "tech_focus": ["R", "glmnet", "pROC", "ggplot2", "slider", "hoopR"],
    },
    {
        "project": "Deep Learning Projects",
        "focus": "Progressive DL curriculum from ANNs to RNNs with experiment tracking.",
        "notes": [
            "ANN: Feedforward networks with training loops and data loading pipelines",
            "HPO: Grid/random search with model factory pattern and W&B experiment tracking",
            "CNN: Convolutional networks with filter visualization utilities",
            "RNN: Recurrent networks with custom tokenizer for sequence preprocessing",
            "Shared utilities module for reproducible seed management across all projects",
        ],
        "tech_focus": ["PyTorch", "TorchVision", "scikit-learn", "W&B", "Conda"],
    },
]

TOOLBOX_MATCHERS: list[dict[str, Any]] = [
    {
        "keywords": ["resample", "bootstrap", "permutation"],
        "matched_tool": "resampling_utils",
        "suggestion": "Use bootstrap and permutation helpers to estimate uncertainty.",
        "example_call": "bootstrap_ci(data = scores, stat = mean, reps = 5000)",
    },
    {
        "keywords": ["vif", "collinearity", "diagnostic"],
        "matched_tool": "model_diagnostics",
        "suggestion": "Run VIF diagnostics and compare best subset alternatives.",
        "example_call": "vif_metrics(lm(target ~ ., data = train_df))",
    },
    {
        "keywords": ["classification", "f1", "precision", "recall"],
        "matched_tool": "classification_metrics",
        "suggestion": "Summarize confusion outcomes and metric tradeoffs.",
        "example_call": "classification_report(y_true, y_pred, positive = 'yes')",
    },
    {
        "keywords": ["monte", "simulation", "sample"],
        "matched_tool": "monte_carlo",
        "suggestion": "Set up repeated simulation draws with fixed random seeds.",
        "example_call": "mc_simulate(iter = 10000, model_fn = run_trial)",
    },
]

DEFAULT_TOOL_MATCH: dict[str, str] = {
    "matched_tool": "general_helper",
    "suggestion": "Describe your task in more detail to map it to a STA478 helper.",
    "example_call": "help('sta478pkg')",
}

NAV_ITEMS: list[dict[str, str]] = [
    {"label": "Overview", "endpoint": "page_one", "page_id": "1"},
    {"label": "Projects", "endpoint": "page_two", "page_id": "2"},
    {"label": "Analytics", "endpoint": "page_three", "page_id": "3"},
    {"label": "Case Studies", "endpoint": "page_four", "page_id": "4"},
    {"label": "Build Notes", "endpoint": "page_five", "page_id": "5"},
]


def build_context(
    *,
    page_title: str,
    active_page: str,
    page_styles: list[str],
    page_scripts: list[str] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    context: dict[str, Any] = {
        "profile": PROFILE,
        "nav_items": NAV_ITEMS,
        "page_title": page_title,
        "page_class": "dark-theme",
        "active_page": active_page,
        "page_styles": page_styles,
        "page_scripts": page_scripts or [],
    }
    context.update(extra)
    return context


def resolve_toolbox_match(query: str) -> dict[str, str]:
    normalized = query.lower()
    for matcher in TOOLBOX_MATCHERS:
        if any(keyword in normalized for keyword in matcher["keywords"]):
            return {
                "matched_tool": matcher["matched_tool"],
                "suggestion": matcher["suggestion"],
                "example_call": matcher["example_call"],
            }
    return DEFAULT_TOOL_MATCH


@app.get("/")
def index() -> Any:
    return redirect(url_for("page_one"))


@app.get("/1")
def page_one() -> str:
    return render_template(
        "page1.html",
        **build_context(
            page_title="Professional Overview",
            active_page="1",
            page_styles=["page1.css"],
            education=EDUCATION,
            skills=SKILLS,
            experience=EXPERIENCE,
        ),
    )


@app.get("/2")
def page_two() -> str:
    return render_template(
        "page2.html",
        **build_context(
            page_title="Project Showcase",
            active_page="2",
            page_styles=["page1.css"],
            projects=PROJECTS,
        ),
    )


@app.get("/3")
def page_three() -> str:
    return render_template(
        "page3.html",
        **build_context(
            page_title="Data Analytics",
            active_page="3",
            page_styles=["page1.css"],
            ai_courses=AI_COURSES,
            nba_plots=NBA_PLOTS,
        ),
    )


@app.get("/4")
def page_four() -> str:
    return render_template(
        "page4.html",
        **build_context(
            page_title="Case Studies",
            active_page="4",
            page_styles=["page1.css"],
            page_scripts=[],
            case_studies=CASE_STUDIES,
        ),
    )


@app.get("/5")
def page_five() -> str:
    return render_template(
        "page5.html",
        **build_context(
            page_title="Build Notes",
            active_page="5",
            page_styles=["page1.css"],
            page_scripts=[],
            project_build_notes=PROJECT_BUILD_NOTES,
        ),
    )


@app.post("/api/toolbox/query")
def toolbox_query() -> Any:
    payload = request.get_json(silent=True) or {}
    query = str(payload.get("query", "")).strip()
    match = resolve_toolbox_match(query)

    return jsonify(
        {
            "query": query,
            "matched_tool": match["matched_tool"],
            "suggestion": match["suggestion"],
            "example_call": match["example_call"],
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
