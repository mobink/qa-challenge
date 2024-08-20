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
