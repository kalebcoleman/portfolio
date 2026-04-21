from __future__ import annotations

from typing import Any

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

PROFILE: dict[str, str] = {
    "name": "Kaleb Coleman",
    "headline": "Data Science Student Building Machine Learning, Modeling, and AI Systems",
    "intro": (
        "I am a data science student focused on machine learning, deep learning, data "
        "engineering, robotics-adjacent AI, and research-oriented modeling. I build "
        "reproducible technical projects that move from raw data collection through "
        "analysis, experimentation, and communication."
    ),
    "summary": (
        "My work is centered on applied ML, statistical modeling, autonomous decision systems, "
        "and technical research projects that are useful in both lab and industry settings."
    ),
    "degree": "B.S. in Data Science",
    "minor": "Cybersecurity minor",
    "graduation": "Expected May 2026",
    "email": "kaleb.a.coleman@gmail.com",
    "phone": "480-359-8122",
    "linkedin_url": "https://linkedin.com/in/kaleb-coleman-a1807a284",
    "github_url": "https://github.com/kalebcoleman",
    "resume_url": "https://docs.google.com/document/d/1Vox1f_4pb3lWcYDWgTEYG1koPp9b1vb4VD6p2ZpMkpQ/edit?usp=sharing",
    "site_description": (
        "Kaleb Coleman portfolio featuring machine learning, AI, data science, and research-focused "
        "technical projects."
    ),
}

NAV_ITEMS: list[dict[str, Any]] = [
    {"label": "Home", "endpoint": "home"},
    {"label": "Projects", "endpoint": "projects"},
    {"label": "Skills", "endpoint": "skills"},
    {"label": "Experience", "endpoint": "experience"},
    {"label": "Contact", "endpoint": "contact"},
]

SKILLS: list[dict[str, Any]] = [
    {
        "name": "Languages",
        "summary": "Core programming languages used across modeling, data pipelines, and application work.",
        "items": ["Python", "R", "SQL", "TypeScript", "JavaScript", "C", "HTML/CSS"],
    },
    {
        "name": "ML / AI",
        "summary": "Modeling and experimentation tools for predictive analytics, deep learning, and generative work.",
        "items": [
            "PyTorch",
            "scikit-learn",
            "PyGAM",
            "CNNs",
            "RNNs",
            "Autoencoders",
            "Diffusion models",
            "Clustering",
            "Dimensionality reduction",
            "Feature engineering",
        ],
    },
    {
        "name": "Data / Databases",
        "summary": "Data collection, validation, storage, and reproducible analysis workflows.",
        "items": [
            "pandas",
            "NumPy",
            "SQLite",
            "PostgreSQL",
            "SQLAlchemy",
            "API ingestion",
            "Schema validation",
            "ETL pipelines",
            "CSV/report workflows",
            "R Markdown",
        ],
    },
    {
        "name": "Tools / Systems",
        "summary": "Workflow, deployment, and engineering tools used to ship and maintain projects.",
        "items": [
            "Flask",
            "Streamlit",
            "Git/GitHub",
            "Docker",
            "GitHub Actions",
            "Linux/CLI",
            "Selenium",
            "Tkinter",
            "Slurm/HPC workflows",
            "Testing and automation",
        ],
    },
]

PROJECTS: list[dict[str, Any]] = [
    {
        "name": "NBA Shot Data Engineering Package",
        "repo_name": "spatialSportsR",
        "repo_url": "https://github.com/kalebcoleman/spatialSportsR",
        "summary": (
            "End-to-end NBA shot analytics package combining R data infrastructure with Python "
            "modeling workflows. The project supports multi-source ingestion, rerunnable SQLite "
            "updates, shot-quality modeling, and player-level archetype analysis."
        ),
        "stack": ["R", "Python", "SQLite", "scikit-learn", "PyGAM", "Streamlit"],
        "highlights": [
            "Built a five-season training pipeline with roughly 1.1M historical shots and ~136K out-of-sample evaluation shots.",
            "Documented ~63% unseen-data xFG accuracy and delivered residual, SDI, and player archetype analysis outputs.",
            "Structured the repo as both an R package and analytics application with dashboard support.",
        ],
        "featured": True,
    },
    {
        "name": "NAU Course Catalog Scraper",
        "repo_name": "nau-course-scraping",
        "repo_url": "https://github.com/kalebcoleman/nau-course-scraping",
        "summary": (
            "Automated course-catalog pipeline built in collaboration with NAU's Institute of Advanced "
            "Applications of Artificial Intelligence. It extracts course prefixes from PDF source data, "
            "scrapes catalog records with Selenium, and supports downstream AI and ethics analysis."
        ),
        "stack": ["Python", "Selenium", "pdfplumber", "pandas", "R Markdown"],
        "highlights": [
            "Scrapes term-level course records and exports structured CSV outputs for later analysis.",
            "Supports focused AI-course detection, broader recall analysis, and ethics-oriented reporting flows.",
            "Designed as a reproducible data collection and reporting workflow rather than a one-off scraper.",
        ],
        "featured": False,
    },
    {
        "name": "Image Reconstruction and Generative Modeling",
        "repo_name": "ImageReconstruction",
        "repo_url": "https://github.com/kalebcoleman/ImageReconstruction",
        "summary": (
            "Research-style image reconstruction training project for MNIST-family datasets, covering "
            "autoencoders, denoising autoencoders, variational autoencoders, and diffusion models. "
            "The training pipeline is built for reproducibility, Slurm workflows, and GPU-backed HPC execution."
        ),
        "stack": ["Python", "PyTorch", "Diffusion", "GPU training", "Slurm", "HPC workflows"],
        "highlights": [
            "Supports multiple model families from a single CLI with isolated outputs and saved run configuration.",
            "Includes Slurm-safe dataset handling, run isolation, and GPU-oriented experiment workflows for shared compute environments.",
            "Covers diffusion experiments, autoencoder baselines, and reproducible parameter sweeps for model comparison.",
        ],
        "featured": True,
    },
    {
        "name": "Halma Game AI",
        "repo_name": "halma-ai",
        "repo_url": "https://github.com/kalebcoleman/halma-ai",
        "summary": (
            "Turn-based game AI project that combines search, heuristics, and a local interface for "
            "interactive play and benchmarking. It is a clean example of autonomous decision-making "
            "logic implemented in a fully runnable system."
        ),
        "stack": ["Python", "Minimax", "Alpha-beta pruning", "Tkinter", "Search heuristics"],
        "highlights": [
            "Implements minimax with optional alpha-beta pruning, move ordering, and iterative deepening.",
            "Provides both a GUI surface and a headless arena for AI-vs-AI benchmarking.",
            "Supports multiple board sizes and configurable per-move search budgets.",
        ],
        "featured": True,
    },
    {
        "name": "AI Multitool Assistant",
        "repo_name": "ai-multitool-assistant",
        "repo_url": "https://github.com/kalebcoleman/ai-multitool-assistant",
        "summary": (
            "Full-stack AI application that combines chat, PDF question answering, notes, and real-time "
            "tool integrations in one authenticated workflow. It extends the portfolio beyond modeling "
            "into practical AI product engineering."
        ),
        "stack": ["Django REST", "React", "JWT", "Gemini", "LlamaIndex", "RAG"],
        "highlights": [
            "Connects a React frontend and Django backend around authenticated AI workflows and user-scoped data.",
            "Supports PDF indexing and question answering alongside real-time tools such as weather, stocks, and news.",
            "Shows end-to-end application design in addition to modeling-oriented repository work.",
        ],
        "featured": False,
    },
]

EXPERIENCE: list[dict[str, str]] = [
    {
        "title": "Data Analyst",
        "organization": "Recording Academy (GRAMMYs)",
        "period": "Recent experience",
        "summary": (
            "Worked on web audience analysis, exploratory data analysis, segmentation, and testing-oriented "
            "insights to support digital content decisions."
        ),
    },
    {
        "title": "Project Collaboration",
        "organization": "NAU Institute of Advanced Applications of Artificial Intelligence",
        "period": "Academic collaboration",
        "summary": (
            "Built a course-catalog scraping and analysis workflow used to examine AI and ethics-related "
            "curriculum coverage through reproducible data collection and reporting."
        ),
    },
]

RESEARCH_ITEMS: list[dict[str, str]] = [
    {
        "title": "Research-facing portfolio direction",
        "summary": (
            "Current work emphasizes machine learning, diffusion and deep learning experiments, data engineering, "
            "game AI, and technical projects that fit research labs, robotics-adjacent AI, and graduate preparation."
        ),
    },
    {
        "title": "Private-data project timing",
        "summary": (
            "A larger applied project will be added after May 8 once the underlying private data can be discussed "
            "safely. Until then, the portfolio only references the scale and outcome, not the protected dataset itself."
        ),
    },
]

AWARDS: list[dict[str, str]] = [
    {
        "title": "Visualization award-winning analytics project",
        "summary": (
            "Recognized for collaborative analytics and data storytelling on a project built from millions of rows. "
            "The underlying data remains private until May 8, so the site intentionally mentions the award and scale "
            "without disclosing the protected subject matter."
        ),
    }
]

EDUCATION: dict[str, str] = {
    "school": "Northern Arizona University",
    "program": "B.S. in Data Science",
    "details": "Cybersecurity minor",
    "timeline": "Expected graduation: May 2026",
}

CONTACT_METHODS: list[dict[str, str]] = [
    {
        "label": "Email",
        "value": PROFILE["email"],
        "href": f"mailto:{PROFILE['email']}",
        "note": "Best for research, internship, and project conversations.",
    },
    {
        "label": "LinkedIn",
        "value": "kaleb-coleman-a1807a284",
        "href": PROFILE["linkedin_url"],
        "note": "Professional background and current updates.",
    },
    {
        "label": "GitHub",
        "value": "kalebcoleman",
        "href": PROFILE["github_url"],
        "note": "Code, project repositories, and technical work.",
    },
    {
        "label": "Phone",
        "value": PROFILE["phone"],
        "href": f"tel:+1{PROFILE['phone'].replace('-', '')}",
        "note": "Available for direct follow-up when needed.",
    },
]


def featured_projects(limit: int = 3) -> list[dict[str, Any]]:
    return [project for project in PROJECTS if project["featured"]][:limit]


def build_context(*, page_title: str, active_page: str, **extra: Any) -> dict[str, Any]:
    context: dict[str, Any] = {
        "profile": PROFILE,
        "nav_items": NAV_ITEMS,
        "page_title": page_title,
        "page_description": PROFILE["site_description"],
        "active_page": active_page,
    }
    context.update(extra)
    return context


@app.get("/")
def index() -> Any:
    return redirect(url_for("home"))


@app.get("/home")
def home() -> str:
    return render_template(
        "home.html",
        **build_context(
            page_title="Home",
            active_page="home",
            featured_projects=featured_projects(3),
            skills=SKILLS,
        ),
    )


@app.get("/projects")
def projects() -> str:
    return render_template(
        "projects.html",
        **build_context(
            page_title="Projects",
            active_page="projects",
            projects=PROJECTS,
        ),
    )


@app.get("/skills")
def skills() -> str:
    return render_template(
        "skills.html",
        **build_context(
            page_title="Skills",
            active_page="skills",
            skills=SKILLS,
        ),
    )


@app.get("/experience")
def experience() -> str:
    return render_template(
        "experience.html",
        **build_context(
            page_title="Experience",
            active_page="experience",
            experience_items=EXPERIENCE,
            research_items=RESEARCH_ITEMS,
            awards=AWARDS,
            education=EDUCATION,
        ),
    )


@app.get("/contact")
def contact() -> str:
    return render_template(
        "contact.html",
        **build_context(
            page_title="Contact",
            active_page="contact",
            contact_methods=CONTACT_METHODS,
        ),
    )


@app.get("/resume")
def resume() -> Any:
    return redirect(PROFILE["resume_url"])


@app.get("/1")
def legacy_page_one() -> Any:
    return redirect(url_for("home"))


@app.get("/2")
def legacy_page_two() -> Any:
    return redirect(url_for("projects"))


@app.get("/3")
def legacy_page_three() -> Any:
    return redirect(url_for("projects"))


@app.get("/4")
def legacy_page_four() -> Any:
    return redirect(url_for("experience"))


@app.get("/5")
def legacy_page_five() -> Any:
    return redirect(url_for("projects"))


if __name__ == "__main__":
    app.run(debug=True)
