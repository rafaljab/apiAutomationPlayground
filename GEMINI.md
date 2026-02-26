# API Automation Playground

A simple web application based on Django Rest Framework for playing with a test automation framework.

## Tech Stack

- **Python 3.12+**
- **Django 6.0+**
- **Django Rest Framework (DRF)**
- **uv** — an extremely fast Python package and project manager
- **Pytest** with `pytest-django` — unit and API testing
- **pre-commit** — managing git hooks
- **Flake8** — linting
- **Black** — code formatting

## Project Structure

```
apiAutomationPlayground/
├── apiAutomationPlayground/  # Main Django project settings and root routing
├── shop/                     # Shop feature application (models, views, serializers, tests)
├── media/                    # User-uploaded files
├── static/                   # Static assets (CSS, JS, images)
├── templates/                # HTML templates
├── manage.py                 # Django command-line utility
├── pyproject.toml            # Project metadata and dependencies managed by uv
├── uv.lock                   # Lockfile for reproducible builds
├── pytest.ini                # Pytest configuration
├── .flake8                   # Flake8 configuration
└── .pre-commit-config.yaml   # Pre-commit hooks configuration
```

## Code Conventions

- **Environment variables:** Secrets and environment-specific settings are loaded from a `.env` file. You should use `.env.dist` as a template.
- **Dependency Management:** Managed via `uv`. No `requirements.txt` or traditional `venv` manipulations are usually needed manually. Dependencies are split into default and `dev` groups inside `pyproject.toml`.

## Formatting

**Tool:** `black`  
**Pre-commit hook:** Configured in `.pre-commit-config.yaml`  

```bash
# Auto-fix formatting
uv run black .
```

Rules: Max line length 88 (implicitly matching Flake8).

## Linting

**Tool:** `flake8`  
**Config file:** `.flake8`  

```bash
# Run linter
uv run flake8
```

Rules: `max-line-length = 88`  
Ignored paths: `.git`, `.venv`  
Ignored rules: `E203, E701`

## Pre-commit Hooks

This project optionally utilizes `pre-commit` to automatically run `black` and `flake8` before every commit.

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run against all files manually
uv run pre-commit run --all-files
```

## Development Commands

```bash
# Install all dependencies (including dev groups) and create a .venv
uv sync --all-groups

# Run database migrations
uv run manage.py migrate

# Start the development server
uv run manage.py runserver
# (Alternatively, simply open start-app.cmd on Windows)

# Run API tests
uv run pytest
```
