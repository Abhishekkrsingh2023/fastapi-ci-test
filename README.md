# Simple FastAPI CI/CD Project

A simple FastAPI backend with automated linting (Ruff) and unit tests (pytest) configured with GitHub Actions CI.

---

## Project Structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── app/
│   ├── __init__.py
│   └── main.py             # FastAPI app with sample endpoints
├── tests/
│   ├── __init__.py
│   └── test_main.py        # Automated tests using TestClient & pytest
├── .gitignore
├── requirements.txt        # Dependencies (FastAPI, Ruff, Pytest, etc.)
└── README.md
```

---

## 1. Local Setup

### Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the FastAPI server
```bash
uvicorn app.main:app --reload
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) or check the interactive API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 2. Running Linting and Tests Locally

Before pushing your changes, you can verify everything locally:

### Run Ruff (Linter)
```bash
ruff check .
```
*(Optional: run `ruff format .` if you want automatic code formatting)*

### Run Pytest (Tests)
```bash
pytest
```

---

## 3. How CI/CD Works with GitHub Actions

The workflow file is located at [`.github/workflows/ci.yml`](.github/workflows/ci.yml).

- **Triggers (`on: [push, pull_request]`)**: Automatically runs whenever you push commits or open a pull request.
- **Environment**: Runs on an Ubuntu virtual runner (`ubuntu-latest`).
- **Pipeline Steps**:
  1. Checks out repository code (`actions/checkout@v4`).
  2. Sets up Python 3.11 with pip caching (`actions/setup-python@v5`).
  3. Installs dependencies from `requirements.txt`.
  4. Runs `ruff check .` to enforce clean code and catch issues.
  5. Runs `pytest` to execute automated test cases.

If any test fails or Ruff finds linting errors, the pipeline status turns red (failure) and prevents broken code from passing silently.

