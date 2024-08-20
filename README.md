# API Test Pipeline

## How to Run Tests

1. Install dependencies: `pip install pytest requests pytest-html`
2. Run tests: `pytest`

## Pipeline Structure

- `test_api.py`: Contains all API tests.
- `pytest.ini`: Configuration for pytest, including HTML report generation.

## Advantages/Disadvantages

Advantages:
- Comprehensive coverage of API endpoints.
- Detailed error reporting for easy debugging.

Disadvantages:
- Requires manual setup and configuration.
- Limited to Python-based environments.


## To containerize your test environment, create a Dockerfile:

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]


##  Build and run your Docker container:

Build and run your Docker container:
