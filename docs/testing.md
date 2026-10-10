# Testing and Coverage

## Install dependencies

Activate the virtual environment and install the project requirements:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the test suite

```powershell
python -m pytest
```

## Run tests with coverage

```powershell
python -m pytest --cov=taskforge --cov-report=term-missing
```

## Generate an XML coverage report

```powershell
python -m pytest --cov=taskforge --cov-report=term-missing --cov-report=xml
```
The XML report is written to `coverage.xml`.
GitHub Actions also uploads this report as a workflow artifact.
