# Testing and Coverage Guide

## Running Tests

Run the full automated test suite using `pytest`:

```bash
python -m pytest -v
```

## Measuring Test Coverage

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate a terminal coverage report:

```bash
python -m pytest --cov=taskforge --cov-report=term-missing
```

Generate an XML coverage report for CI or external tools:

```bash
python -m pytest --cov=taskforge --cov-report=xml
```

## Continuous Integration (CI)

GitHub Actions runs the test suite on every push and pull request via `.github/workflows/tests.yml`. It runs all tests with `pytest-cov`, outputs coverage metrics, and uploads `coverage.xml` as a workflow artifact.
