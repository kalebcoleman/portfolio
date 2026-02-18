from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

PROFILE: dict[str, Any] = {
    "name": "Kaleb Coleman",
    "headline": "Data Science Undergraduate | ML, Data Engineering, Full-Stack AI, Cybersecurity",
    "summary": (
        "Data science undergraduate who builds end-to-end systems from raw API ingestion and "
        "schema-validated pipelines to predictive models and interactive dashboards. Core strengths "
        "in statistical modeling, feature engineering, and reproducible workflows across Python, R, "
        "and SQL. Experience shipping full-stack AI applications, spatial sports analytics packages, "
        "and leakage-aware predictive models. Exploring deep learning, computer vision, and "
        "autonomous systems."
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
    "Languages": ["Python", "R", "JavaScript", "TypeScript", "SQL", "C", "HTML/CSS"],
    "Data & ML": [
        "pandas", "NumPy", "scikit-learn", "PyTorch", "PyGAM", "Logistic regression",
        "GMM", "PCA", "Ridge/LASSO/Elastic Net", "Random Forest", "Brier score calibration",
    ],
    "Statistical Methods": [
        "GAMs", "Bootstrap", "k-fold CV", "Monte Carlo simulation", "Elo rating system",
        "Leakage-aware rolling windows", "AUC calibration diagnostics",
    ],
    "Deep Learning": [
        "Feedforward networks (ANN)", "CNN", "RNN", "Hyperparameter optimization",
        "Filter visualization", "Experiment tracking (W&B)",
    ],
    "AI & Agents": [
        "Google Gemini", "LlamaIndex ReAct", "RAG", "HuggingFace embeddings",
        "PDF vector indexing", "Intent classification",
    ],
    "Data Engineering": [
        "API ingestion", "JSON parsing", "Schema validation", "SQLite upserts",
        "PostgreSQL", "SQLAlchemy", "ETL pipelines", "concurrent.futures", "Makefile automation",
    ],
    "Web Development": [
        "Flask", "Django REST Framework", "Fastify", "Next.js 14", "React 18", "Vite",
        "JWT auth", "REST API design", "Jinja2", "Prisma", "Zod", "Stripe",
    ],
    "DevOps & Tools": [
        "Docker", "docker-compose", "Git/GitHub", "GitHub Actions CI/CD", "Azure Web App",
        "Gunicorn", "Redis", "pnpm", "Vitest", "pytest", "unittest",
    ],
    "Visualization": [
        "matplotlib", "plotly", "Streamlit", "ggplot2", "Recharts", "Canvas API",
        "Court heatmaps", "PCA scatter plots", "Reliability curves",
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
            "ESPN + NBA Stats ingestion with parallel collection and exponential backoff",
            "Schema validation and rerunnable SQLite upsert behavior",
            "xFG logistic regression + GAM tensor surface modeling",
            "Shot Difficulty Index feature engineering",
            "GMM player archetypes with BIC selection and PCA projection",
        ],
        "tech_stack": ["R", "Python", "scikit-learn", "PyGAM", "SQLite", "Streamlit"],
        "metrics": {
            "xFG Holdout": "62.7%",
            "Training Shots": "1.1M+",
            "Evaluation Shots": "~136K",
            "Players": "467",
            "Seasons": "5",
        },
    },
    {
        "name": "AI Multitool Assistant",
        "tag": "ai-multitool",
        "description": (
            "Full-stack AI web application with chat, PDF Q&A, and real-time tools. "
            "Two-service architecture with JWT authentication and Gemini 2.5-Flash via "
            "a LlamaIndex ReAct agent."
        ),
        "key_features": [
            "Gemini 2.5-Flash + LlamaIndex ReAct orchestration",
            "RAG pipeline for PDF parsing, indexing, and querying",
            "Five real-time tools: stocks, crypto, weather, news, market",
            "JWT access and refresh token lifecycle",
            "User-scoped data isolation for notes, chat, and PDF indexes",
        ],
        "tech_stack": ["Django REST", "React 18", "Vite", "JWT", "Gemini", "LlamaIndex"],
        "metrics": {
            "API Tools": "5",
            "REST Endpoints": "7+",
            "Architecture": "2-service",
        },
    },
    {
        "name": "ESPN NBA Data Pipeline",
        "tag": "nba-data",
        "description": (
            "R package for end-to-end ESPN NBA data collection, parsing, validation, and storage. "
            "Handles 1,000+ games per season with parallel collection and exponential backoff retry logic."
        ),
        "key_features": [
            "Phase-based pipeline: collection, inventory, parsing, quality",
            "Parallel collection via future::multisession",
            "Schema enforcement with explicit type casting",
            "SQLite upserts with schema versioning via nbadata_meta",
            "Fixture-based tests with optional live-gated integration tests",
        ],
        "tech_stack": ["R", "httr2", "DBI", "RSQLite", "future", "testthat"],
        "metrics": {
            "Games/Season": "1,000+",
            "Test Files": "13",
            "Core Tables": "4",
            "Retry Attempts": "5",
        },
    },
    {
        "name": "NAU Course Catalog Scraper",
        "tag": "nau-scraper",
        "description": (
            "Automated web scraping and AI curriculum analysis pipeline. Scraped 12,944 course "
            "records across Fall 2025 and Spring 2026 with a three-tier classification system."
        ),
        "key_features": [
            "PDF prefix extraction with pdfplumber",
            "Selenium browser automation with resumable crawl states",
            "Three analysis scripts: high-precision, broad recall, and ethics",
            "Fuzzy string matching for typo-tolerant detection",
            "CSV exports and R Markdown reporting for precision/recall tradeoffs",
        ],
        "tech_stack": ["Python", "Selenium", "pdfplumber", "pandas", "thefuzz", "R Markdown"],
        "metrics": {
            "Courses": "12,944",
            "Prefixes": "150+",
            "Terms": "2",
            "Analysis Tiers": "3",
        },
    },
    {
        "name": "NBA Win Probability Models",
        "tag": "nba-modeling",
        "description": (
            "Leakage-aware predictive modeling for NBA home-team win probability using rolling "
            "window features across 2002-2025 seasons."
        ),
        "key_features": [
            "Rolling 3/5/10-game windows with lag-1 leakage prevention",
            "Advanced stats and matchup differential feature engineering",
            "Ridge, elastic net, logistic, and random forest model comparison",
            "Elo features with season-reset and all-time variants",
            "Chronological train/test split preserving temporal order",
        ],
        "tech_stack": ["R", "glmnet", "pROC", "randomForest", "slider", "hoopR"],
        "metrics": {
            "Best Accuracy": "67%",
            "Best AUC": "0.684",
            "Baseline": "59.2%",
            "Seasons": "2002-2025",
        },
    },
    {
        "name": "Deep Learning Projects",
        "tag": "deep-learning",
        "description": (
            "Four progressive deep learning projects covering ANN baselines, hyperparameter "
            "optimization, CNN interpretation, and RNN sequence modeling."
        ),
        "key_features": [
            "ANN project with custom training loops",
            "Grid/random hyperparameter optimization with W&B",
            "CNN filter visualization workflow",
            "RNN modeling with a custom tokenizer",
            "Reproducible shared infrastructure across project modules",
        ],
        "tech_stack": ["PyTorch", "TorchVision", "scikit-learn", "Weights & Biases", "pytest"],
        "metrics": {
            "Projects": "4",
            "Framework": "PyTorch",
            "Tracking": "W&B",
        },
    },
    {
        "name": "NBA Analytics Platform",
        "tag": "nba-app",
        "description": (
            "Freemium NBA analytics platform with dashboards, AI-style Q&A over NBA data, "
            "Stripe billing, and production-grade security hardening."
        ),
        "key_features": [
            "Fastify + TypeScript backend with intent-driven Q&A",
            "Next.js 14 App Router frontend with feature gating",
            "Stripe checkout and webhook subscription flow",
            "Security stack: JWT, Zod safeParse, hashing, rate limiting",
            "Redis caching with Lua scripts and performance optimizations",
        ],
        "tech_stack": ["TypeScript", "Fastify", "Next.js", "Prisma", "PostgreSQL", "Redis"],
        "metrics": {
            "Tests Passing": "69",
            "Security Grade": "A+",
            "Test Files": "25",
            "Backend Fixes": "17/17",
        },
    },
    {
        "name": "NAU Capstone: Sports Expected Points Analysis",
        "tag": "nau-capstone",
        "description": (
            "Research capstone analyzing expected points/goals across NBA and NHL with shot-quality "
            "modeling, calibration diagnostics, and player value analysis."
        ),
        "key_features": [
            "xFG logistic regression and POE computation pipeline",
            "GAM tensor surface modeling with partial dependence diagnostics",
            "GMM archetypes with BIC selection and PCA projection",
            "Shot Difficulty Index and residual analysis",
            "POE per million salary value rankings",
        ],
        "tech_stack": ["Python", "scikit-learn", "PyGAM", "Streamlit", "plotly", "matplotlib"],
        "metrics": {
            "Players Profiled": "467",
            "Data Sources": "3",
            "Sports": "NBA + NHL",
        },
    },
    {
        "name": "NBA Dockerized Scrape Pipeline",
        "tag": "scrape-pipeline",
        "description": (
            "Production-grade Python/Docker pipeline for high-volume NBA data ingestion into "
            "PostgreSQL with idempotent upsert behavior."
        ),
        "key_features": [
            "concurrent.futures parallel HTTP fetching",
            "Chunked SQLAlchemy ON CONFLICT DO UPDATE upserts",
            "Complex ESPN JSON normalization to relational tables",
            "Failure-stage tracking through nba_ingest_failures",
            "Makefile automation for ingest/reset/up/down",
        ],
        "tech_stack": ["Python", "Docker", "PostgreSQL", "SQLAlchemy", "pandas", "Makefile"],
        "metrics": {
            "Database": "PostgreSQL 16",
            "Automation": "Makefile",
            "Architecture": "Dockerized",
        },
    },
    {
        "name": "Stuxnet Cyberwarfare Analysis",
        "tag": "stuxnet-analysis",
        "description": (
            "Technical cybersecurity analysis of Stuxnet covering propagation, zero-days, PLC "
            "targeting, sensor spoofing, and critical infrastructure impact."
        ),
        "key_features": [
            "Analysis of four simultaneous zero-day exploits",
            "Code-signing abuse via stolen certificates",
            "Siemens S7-315 PLC hardware targeting and fingerprinting",
            "Man-in-the-middle PLC manipulation and sensor spoofing",
            "Impact comparison against WannaCry and NotPetya",
        ],
        "tech_stack": ["R Markdown", "LaTeX", "ICS/SCADA security", "Exploit analysis"],
        "metrics": {
            "Zero-Days": "4",
            "Attribution": "Operation Olympic Games",
            "Output": "Rmd + PDF",
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
    {"label": "Win Model Accuracy", "value": "67%", "source": "nba-modeling"},
    {"label": "Win Model AUC", "value": "0.684", "source": "nba-modeling"},
    {"label": "NBA Seasons Modeled", "value": "2002-2025", "source": "nba-modeling"},
    {"label": "Courses Scraped", "value": "12,944", "source": "nau_course_scraping"},
    {"label": "Course Prefixes Crawled", "value": "150+", "source": "nau_course_scraping"},
    {"label": "NBA_APP Tests Passing", "value": "69", "source": "nba-app"},
    {"label": "NBA_APP Security Grade", "value": "A+", "source": "nba-app"},
    {"label": "R Package Test Files", "value": "13", "source": "nba-data"},
    {"label": "API Tools Integrated", "value": "5", "source": "ai-multitool"},
    {"label": "REST Endpoints Built", "value": "7+", "source": "ai-multitool"},
    {"label": "Players Profiled", "value": "467", "source": "spatialSportsR"},
    {"label": "Bootstrap Resamples", "value": "100,000", "source": "sta478"},
]

CASE_STUDIES: list[dict[str, Any]] = [
    {
        "project": "NBA Shot Data Engineering Package",
        "role": "Data engineer and modeling workflow builder",
        "challenge": (
            "Create a repeatable multi-source shot-data pipeline that supports stable downstream "
            "modeling and archetype analysis without schema drift."
        ),
        "process": [
            "Ingested and merged 1.1M+ shots across five seasons from multiple sources",
            "Applied schema contracts and validation before feature generation",
            "Implemented rerunnable SQLite load/upsert behavior for repeatable refreshes",
            "Engineered xFG, residual, and SDI features for GAM and clustering workflows",
        ],
        "outcomes": [
            "xFG model reached 62.7% holdout accuracy",
            "Generated stable feature layers for shot-quality and value analysis",
            "Delivered interpretable archetype visuals and residual diagnostics",
        ],
    },
    {
        "project": "AI Multitool Assistant",
        "role": "Full-stack developer and AI integration lead",
        "challenge": (
            "Unify chat, PDF Q&A, and real-time external tools into one secure workflow with "
            "consistent authentication and data isolation."
        ),
        "process": [
            "Split system into React/Vite frontend and Django REST backend",
            "Implemented JWT access and refresh token lifecycle",
            "Integrated Gemini via LlamaIndex ReAct with tool orchestration",
            "Built PDF index persistence and lazy query loading",
        ],
        "outcomes": [
            "Single user workflow for chat, docs, and tools",
            "Composable API surface for fast feature iteration",
            "Reliable user-scoped data separation across notes and history",
        ],
    },
    {
        "project": "ESPN NBA Data Pipeline",
        "role": "R package developer and data pipeline architect",
        "challenge": (
            "Build a robust R package that can ingest and validate 1,000+ games per season with "
            "graceful failure handling."
        ),
        "process": [
            "Implemented parallel collection wrappers with retry logic",
            "Created manifest checks for missing, postponed, and canceled games",
            "Enforced schema maps and type-casting contracts",
            "Built idempotent upsert tables and migration hooks",
        ],
        "outcomes": [
            "Produced four stable parsed core tables",
            "Established 13 fixture-based tests without live API dependency",
            "Enabled repeatable incremental updates without duplicate rows",
        ],
    },
    {
        "project": "NAU Course Catalog Scraper",
        "role": "Scraper and curriculum-analysis pipeline developer",
        "challenge": (
            "Audit AI and ethics course coverage where catalog data is distributed across term pages, "
            "prefix lists, and inconsistent page structures."
        ),
        "process": [
            "Extracted prefixes from PDF and maintained reusable prefix lists",
            "Built Selenium crawl flow with resumability and empty-prefix logging",
            "Separated analysis into precision, broad recall, and ethics scripts",
            "Exported cleaned CSV outputs and report-ready summaries",
        ],
        "outcomes": [
            "Scraped 12,944 records across 150+ prefixes and two terms",
            "Created transparent precision-vs-recall reporting in R Markdown",
            "Delivered inspectable stage-by-stage transformation outputs",
        ],
    },
    {
        "project": "NBA Win Probability Models",
        "role": "Statistical modeler and feature engineer",
        "challenge": (
            "Model home-team win probability across 23 seasons while preventing temporal leakage "
            "that would inflate metrics."
        ),
        "process": [
            "Built lagged rolling features across 3/5/10-game windows",
            "Engineered possession metrics and matchup differential features",
            "Compared ridge, elastic net, logistic, and random forest models",
            "Integrated Elo variants and calibrated holdout thresholds",
        ],
        "outcomes": [
            "Best ridge model achieved 67% accuracy and 0.684 AUC",
            "Maintained chronological train/test integrity",
            "Documented reproducible model comparison workflow",
        ],
    },
    {
        "project": "Deep Learning Projects",
        "role": "Deep learning practitioner and experiment tracker",
        "challenge": (
            "Deliver four progressive deep-learning projects while preserving reproducibility "
            "and making results auditable."
        ),
        "process": [
            "Implemented ANN baseline workflows and regression tests",
            "Built HPO model-factory patterns with W&B experiment tracking",
            "Developed CNN interpretation through filter visualization",
            "Implemented RNN sequence pipelines with custom tokenizer",
        ],
        "outcomes": [
            "Completed ANN, HPO, CNN, and RNN progression",
            "Established reproducible training utilities and shared seeds",
            "Produced tracked experiment outputs for comparison and reporting",
        ],
    },
    {
        "project": "NBA Analytics Platform",
        "role": "Full-stack developer and security hardening engineer",
        "challenge": (
            "Ship a production-ready freemium analytics platform with secure auth, billing, and "
            "AI-style Q&A without exposing raw SQL or sensitive internals."
        ),
        "process": [
            "Built Fastify API modules for auth, routes, billing, and Q&A",
            "Implemented regex-intent Q&A templates to avoid user SQL execution",
            "Added Stripe checkout and webhook subscription management",
            "Hardened with JWT policy, Zod validation, rate limits, and Redis caching",
        ],
        "outcomes": [
            "Reached 69 passing tests across 25 files",
            "Achieved A+ security posture in project audits",
            "Delivered reliable freemium controls and optimized dashboard UX",
        ],
    },
    {
        "project": "NAU Capstone: Sports Expected Points Analysis",
        "role": "Lead analyst and modeling researcher",
        "challenge": (
            "Design a multi-sport expected points framework that explains shot quality and value "
            "while remaining interpretable to both technical and non-technical audiences."
        ),
        "process": [
            "Built xFG and xG workflows with POE and residual diagnostics",
            "Ran GAM tensor-surface models with PDP interpretation",
            "Clustered player shot profiles via GMM and PCA",
            "Combined salary collection with POE per million value rankings",
        ],
        "outcomes": [
            "Produced interpretable cross-sport shot-quality metrics",
            "Built reusable scripts for calibration, clustering, and value analysis",
            "Delivered an interactive Streamlit capstone dashboard",
        ],
    },
    {
        "project": "NBA Dockerized Scrape Pipeline",
        "role": "Data engineer and ingestion pipeline architect",
        "challenge": (
            "Build a Dockerized ingestion system that can rerun safely at scale while preserving "
            "auditability and failure tracing."
        ),
        "process": [
            "Parallelized HTTP fetches with concurrent.futures",
            "Mapped variable ESPN JSON schemas into relational structures",
            "Implemented chunked ON CONFLICT upserts via SQLAlchemy",
            "Automated operations through Makefile commands and Docker compose",
        ],
        "outcomes": [
            "Established idempotent PostgreSQL ingestion behavior",
            "Created failure-stage observability through ingest-failure tracking",
            "Enabled repeatable local and containerized execution workflows",
        ],
    },
    {
        "project": "Stuxnet Cyberwarfare Analysis",
        "role": "Cybersecurity researcher and technical writer",
        "challenge": (
            "Translate highly technical malware behavior into a rigorous, evidence-based analysis "
            "that remains readable and academically structured."
        ),
        "process": [
            "Mapped propagation and exploit chain details across four zero-days",
            "Analyzed certificate abuse and PLC hardware-targeting logic",
            "Documented attack-vector mechanics and sensor spoofing behavior",
            "Structured findings in publication-style R Markdown and LaTeX",
        ],
        "outcomes": [
            "Delivered a comprehensive Stuxnet technical report",
            "Connected exploit mechanics to real-world infrastructure impact",
            "Showcased cybersecurity depth aligned with minor focus",
        ],
    },
]

PROJECT_BUILD_NOTES: list[dict[str, Any]] = [
    {
        "project": "NBA Shot Data Engineering Package",
        "focus": "SQLite-backed multi-source shot modeling and archetype workflow.",
        "notes": [
            "Merges ESPN and NBA Stats shot data across seasons",
            "Applies schema validation before feature generation",
            "Uses rerunnable SQLite upserts for stable refresh behavior",
            "Builds xFG, residual, and SDI feature layers for modeling",
            "Automates daily updates through launchd scheduling",
        ],
        "tech_focus": ["R", "Python", "SQLite", "PyGAM", "scikit-learn", "Streamlit"],
    },
    {
        "project": "AI Multitool Assistant",
        "focus": "Two-service AI web product with secure auth and tool orchestration.",
        "notes": [
            "React/Vite frontend paired with Django REST backend",
            "JWT token lifecycle with refresh and user-scoped storage",
            "Gemini + LlamaIndex ReAct tool orchestration",
            "PDF upload/index/query flow for document-grounded responses",
            "Tool modules for market data, weather, and news",
        ],
        "tech_focus": ["React", "Vite", "Django REST", "JWT", "Gemini", "LlamaIndex"],
    },
    {
        "project": "ESPN NBA Data Pipeline",
        "focus": "R package with parallel collection and schema-safe upsert loading.",
        "notes": [
            "Parallel collection wrappers with retry and rate-limit handling",
            "Schema maps enforce stable typed outputs",
            "Composite-key upsert strategy for idempotent loads",
            "Manifest checks verify schedule completeness",
            "Fixture-based testthat suite covers parse and DB behavior",
        ],
        "tech_focus": ["R", "httr2", "DBI", "RSQLite", "future", "testthat"],
    },
    {
        "project": "NAU Course Catalog Scraper",
        "focus": "Selenium + PDF prefix extraction + CSV/report analysis pipeline.",
        "notes": [
            "Builds prefix inventory from PDF and crawl logs",
            "Supports resumable Selenium crawl with term-aware outputs",
            "Runs precision, broad, and ethics analysis scripts separately",
            "Exports clean CSV artifacts for downstream reporting",
            "Publishes findings in R Markdown report outputs",
        ],
        "tech_focus": ["Python", "Selenium", "pdfplumber", "pandas", "thefuzz", "R Markdown"],
    },
    {
        "project": "NBA Win Probability Models",
        "focus": "Leakage-aware modeling with rolling features and reproducible comparisons.",
        "notes": [
            "Builds lagged rolling metrics and matchup differentials",
            "Compares ridge/elastic/logistic/random forest pipelines",
            "Integrates Elo variants as predictive signals",
            "Uses chronological splits to preserve real-world ordering",
            "Tracks AUC and calibration tradeoffs by model",
        ],
        "tech_focus": ["R", "glmnet", "pROC", "randomForest", "slider", "hoopR"],
    },
    {
        "project": "Deep Learning Projects",
        "focus": "Progressive deep-learning coursework with reproducible experiment tracking.",
        "notes": [
            "ANN baseline modules for data, loss, and training",
            "HPO loops with grid/random strategies and W&B logging",
            "CNN interpretation through filter visualization tooling",
            "RNN sequence modeling with custom tokenizer utilities",
            "Shared seed controls for reproducibility across projects",
        ],
        "tech_focus": ["PyTorch", "TorchVision", "W&B", "pytest", "Conda"],
    },
    {
        "project": "NBA Analytics Platform",
        "focus": "Production monorepo with secure API, billing, and high-performance frontend.",
        "notes": [
            "Fastify API modules split across auth, billing, Q&A, and routes",
            "Regex intent mapping prevents direct user SQL execution",
            "Stripe checkout and webhook flow manages subscriptions",
            "Zod validation, JWT policy, rate limiting, and sanitization hardening",
            "Redis and cache-layer optimizations reduce response latency",
        ],
        "tech_focus": ["TypeScript", "Fastify", "Next.js", "Prisma", "PostgreSQL", "Redis"],
    },
    {
        "project": "NAU Capstone: Sports Expected Points Analysis",
        "focus": "Cross-sport expected-points modeling and interpretability toolkit.",
        "notes": [
            "xFG/xG modeling scripts for NBA and NHL datasets",
            "Calibration diagnostics including Brier and reliability curves",
            "GMM archetype modeling with PCA visualization",
            "Value analysis combining POE with salary data",
            "Interactive Streamlit app for presenting capstone findings",
        ],
        "tech_focus": ["Python", "scikit-learn", "PyGAM", "Streamlit", "plotly", "matplotlib"],
    },
    {
        "project": "NBA Dockerized Scrape Pipeline",
        "focus": "Dockerized PostgreSQL ingestion workflow with idempotent upserts.",
        "notes": [
            "Parallel fetching stage built with concurrent.futures",
            "Normalization maps ESPN JSON into relational model tables",
            "Chunked SQLAlchemy upserts enforce idempotent writes",
            "nba_ingest_failures table captures pipeline breakpoints",
            "Makefile commands orchestrate ingest and infrastructure lifecycle",
        ],
        "tech_focus": ["Python", "Docker", "PostgreSQL", "SQLAlchemy", "Makefile"],
    },
    {
        "project": "Stuxnet Cyberwarfare Analysis",
        "focus": "Technical malware research and publication-quality security reporting.",
        "notes": [
            "Breaks down propagation via USB/LNK exploit chain",
            "Analyzes four zero-day exploits and privilege escalation paths",
            "Documents PLC targeting logic and operational manipulation",
            "Compares impact context with major cyber incidents",
            "Publishes full report using R Markdown + LaTeX formatting",
        ],
        "tech_focus": ["R Markdown", "LaTeX", "ICS/SCADA", "Exploit analysis", "Technical writing"],
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
