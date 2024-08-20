# qa-challenge

## How to Run Tests

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/api-test-pipeline.git
   cd api-test-pipeline

2. Install dependencies:
   pip install -r requirements.txt

3. Run tests:
   pytest --alluredir=allure-results

4. To run tests in Docker:
     docker build -t api-test .
     docker run --rm api-test 
