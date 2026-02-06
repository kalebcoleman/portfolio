from typing import Any

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

PROFILE: dict[str, Any] = {
    "name": "Kaleb Coleman",
    "headline": "Data Science Undergraduate at Northern Arizona University",
    "summary": (
        "Data science undergraduate with experience building machine-learning systems, "
        "data pipelines and AI agents; strong in statistical modeling, feature engineering "
        "and reproducible workflows; exploring computer vision, unsupervised learning and "
        "deep learning for autonomous systems."
    ),
    "degree": "B.S. in Data Science",
    "minor": "Cybersecurity minor",
    "graduation": "May 2026",
    "phone": "480-359-8122",
    "email": "kaleb.a.coleman@gmail.com",
    "linkedin_url": "https://linkedin.com/in/kaleb-coleman-a1807a284",
    "github_url": "https://github.com/kalebcoleman",
    "resume_url": "https://drive.google.com/file/d/1aAZT_85vPYvmxLt9waOl3y6rrM4nyoGp/view?usp=drive_link",
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
    "Data/ML": ["Pandas", "NumPy", "scikit-learn", "PyTorch", "XGBoost"],
    "Programming": ["Python", "R", "C", "SQL", "JavaScript"],
    "AI": [
        "Minimax and alpha-beta pruning",
        "Heuristic evaluation",
        "LangChain",
    ],
    "Data Engineering": [
        "API ingestion",
        "JSON parsing",
        "Schema validation",
        "Relational modeling",
        "SQLite",
        "Upserts",
    ],
    "Tools/OS": [
        "Git/GitHub",
        "PostgreSQL",
        "Node.js",
        "Linux/Unix",
        "macOS",
        "Windows",
    ],
}

EXPERIENCE: list[dict[str, str]] = [
    {
        "title": "Data Analyst",
        "company": "Recording Academy (GRAMMYs)",
        "summary": (
            "Performed website audience analysis, exploratory data analysis and "
            "visualization, segmentation, and A/B testing to inform content strategy."
        ),
    },
    {
        "title": "Operations Manager",
        "company": "Moody Concepts",
        "summary": (
            "Managed operations workflows, tracked performance, and coordinated "
            "execution across day-to-day business activities."
        ),
    },
    {
        "title": "Service Roles",
        "company": "Prior customer-facing roles",
        "summary": (
            "Built communication, reliability, and team coordination skills across "
            "multi-role service environments."
        ),
    },
]

PROJECTS: list[dict[str, Any]] = [
    {
        "name": "AI Multitool Assistant",
        "description": (
            "Full-stack AI web assistant with chat, PDF Q&A, real-time tools, notes, "
            "and JWT authentication."
        ),
        "key_features": [
            "ReAct-style chat agent powered by Gemini via LlamaIndex",
            "PDF upload, embedding, and question answering workflow",
            "Integrated tools for stocks, crypto, weather, market data, and news",
            "Protected notes and chat-history APIs with JWT auth",
            "Two-service architecture: React/Vite frontend + Django REST backend",
        ],
        "tech_stack": [
            "React",
            "Vite",
            "Django REST Framework",
            "JWT",
            "Gemini",
            "LlamaIndex",
            "HuggingFace embeddings",
        ],
    },
    {
        "name": "NAU Course Catalog Scraper",
        "description": (
            "Python + Selenium catalog pipeline built with IAAAI collaboration to scrape "
            "courses and audit AI and ethics curriculum coverage."
        ),
        "key_features": [
            "Prefix extraction from NAU PDF plus term-aware Selenium scraping",
            "Headless and non-headless modes with overwrite/incremental controls",
            "Logs empty or failed prefixes and exports reproducible CSV deliverables",
            "Cleans and normalizes course fields before analysis exports",
            "Maintains term metadata and URL lineage for manual verification",
            "Narrow and broad AI analysis using regex context gating and fuzzy matching",
            "Ethics subset analysis and overlap reporting in report.Rmd",
        ],
        "tech_stack": [
            "Python",
            "Selenium",
            "pdfplumber",
            "Pandas",
            "thefuzz",
            "R Markdown",
        ],
    },
    {
        "name": "NBA Shot Data Engineering Package",
        "description": (
            "Multi-source NBA shot data pipeline that scrapes, cleans, models, and stores "
            "standardized records in SQLite for analytics and clustering."
        ),
        "key_features": [
            "Collects shot and context data across multiple sources/seasons",
            "Normalizes schema, cleans edge cases, and validates field integrity",
            "Uses rerunnable merge/upsert behavior to keep SQLite tables stable",
            "Builds feature layers for expected FG, residuals, and shot difficulty analysis",
            "Feeds clustering workflows for role-aware player archetype modeling",
        ],
        "tech_stack": ["Python", "SQLite", "Pandas", "ETL", "Schema validation", "Clustering"],
    },
    {
        "name": "STA478 Package",
        "description": (
            "Statistical computing helper package from STA 478 centered on resampling, diagnostics, "
            "and Monte Carlo utilities."
        ),
        "key_features": [
            "Bootstrap and permutation resampling helpers",
            "Variance inflation factor diagnostics and best subset tools",
            "Classification metrics and Monte Carlo sampling functions",
        ],
        "tech_stack": ["R", "Statistical modeling", "Resampling", "Diagnostics"],
    },
    {
        "name": "Halma AI",
        "description": (
            "Python Halma agent with minimax, alpha-beta pruning, and benchmarking tooling "
            "for human-versus-AI and AI-versus-AI play."
        ),
        "key_features": [
            "Iterative deepening search with move ordering",
            "Heuristic evaluation tuned to positional pressure",
            "Tkinter GUI for human matches plus headless arena",
        ],
        "tech_stack": ["Python", "Tkinter", "Game AI", "Search"],
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

CASE_STUDIES: list[dict[str, Any]] = [
    {
        "project": "AI Multitool Assistant",
        "role": "Full-stack developer and AI integration lead",
        "challenge": (
            "Build one assistant experience that combines authenticated chat, PDF Q&A, "
            "and real-time market/weather/news tools without turning the UI into separate silos."
        ),
        "process": [
            "Split the app into a React/Vite frontend and Django REST backend",
            "Implemented JWT auth and protected user-scoped notes/history APIs",
            "Integrated Gemini via LlamaIndex for tool-augmented responses",
            "Added PDF upload and indexing flow for document-grounded querying",
        ],
        "outcomes": [
            "Single app flow for chat, documents, and tools with consistent auth",
            "Composable backend endpoint surface for iterative feature additions",
            "Clear separation between frontend UX and backend orchestration logic",
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
            "Reproducible CSV outputs for course rows, audit logs, and AI/ethics flags",
            "Report-ready findings in report.Rmd/report.pdf with precision-versus-recall framing",
            "Transparent pipeline where each transformation stage is independently inspectable",
        ],
    },
    {
        "project": "NBA Shot Data Engineering Package",
        "role": "Data engineer and modeling workflow builder",
        "challenge": (
            "Create a repeatable multi-source shot-data pipeline that supports downstream modeling, "
            "player archetype discovery, and visual analysis without schema drift issues."
        ),
        "process": [
            "Ingested and merged multi-season shot/context data from multiple sources",
            "Standardized schema and validation checks before model features were generated",
            "Built rerunnable load behavior in SQLite to keep analytics tables stable",
            "Engineered xFG/residual/difficulty features for GAM and clustering workflows",
        ],
        "outcomes": [
            "Consistent feature layer for shot-quality and player-value analysis",
            "PCA/archetype outputs and residual plots suitable for portfolio storytelling",
            "Reusable foundation for extending to new seasons and modeling variants",
        ],
    },
]

PROJECT_BUILD_NOTES: list[dict[str, Any]] = [
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
        "tech_focus": ["Python", "Selenium", "pdfplumber", "Pandas", "thefuzz", "R Markdown"],
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
        "project": "NBA Shot Data Engineering Package",
        "focus": "SQLite-backed multi-source shot modeling and clustering pipeline.",
        "notes": [
            "Ingests shot and context data from multiple sources and seasons",
            "Normalizes schema and validates integrity before downstream modeling",
            "Uses rerunnable load/upsert behavior to keep SQLite tables stable",
            "Builds xFG, residual, and shot-difficulty feature layers",
            "Runs GAM modeling and clustering workflows for player archetype analysis",
        ],
        "tech_focus": ["Python", "SQLite", "ETL", "Schema validation", "GAM", "Clustering"],
    },
    {
        "project": "STA478 Package",
        "focus": "Reusable statistical helper toolkit developed for STA 478.",
        "notes": [
            "Includes bootstrap and permutation resampling utilities",
            "Adds variance inflation factor diagnostics and best-subset helpers",
            "Provides classification metrics for model evaluation",
            "Includes Monte Carlo simulation tools for repeated sampling studies",
        ],
        "tech_focus": ["R", "Resampling", "Diagnostics", "Monte Carlo"],
    },
    {
        "project": "Halma AI",
        "focus": "Search-based game AI for human and benchmark play modes.",
        "notes": [
            "Implements minimax with alpha-beta pruning and iterative deepening",
            "Uses move ordering and heuristic evaluation for stronger play",
            "Includes Tkinter GUI for human-versus-AI interaction",
            "Includes a headless arena mode for AI-versus-AI benchmarking",
        ],
        "tech_focus": ["Python", "Tkinter", "Minimax", "Alpha-beta pruning"],
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
        "page_class": "page-one",
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
