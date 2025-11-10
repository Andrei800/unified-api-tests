🧩 Unified API Tests Framework

Unified API Tests is a scalable, modular framework for REST API testing built on top of pytest and requests.
It’s designed to handle multiple APIs (e.g., GoRest, ReqRes, Swagger PetStore) using a single, reusable test architecture.

🚀 Key Features

✅ Unified Base Client (BaseAPIClient)

Handles 429 Too Many Requests with retry & exponential backoff

Built-in CI throttling and jitter control

Timeout, rate limit, and session management

Detailed request logging and timing

✅ Environment configuration

Uses .env for API tokens and base URLs

Secure and excluded from GitHub

✅ Real QA project structure

Modular design (core, api, utils, tests)

Pytest fixtures, parametrization, and markers (e2e, negative, performance)

CI/CD integration with GitHub Actions + HTML reports

✅ Extensible architecture

Easily add new API modules with minimal changes

Shared utilities for schema validation, data generation, and assertions

🧱 Project Structure
unified-api-tests/
├── src/
│   ├── core/              # Core logic (Base client, helpers)
│   │   └── base_client.py
│   ├── api/               # Specific API clients (GoRest, ReqRes, PetStore)
│   └── utils/             # Reusable utilities and data tools
│
├── tests/
│   ├── gorest/            # GoRest API test suite
│   ├── reqres/            # ReqRes API test suite
│   └── petstore/          # Swagger PetStore tests
│
├── reports/               # HTML test reports (pytest-html)
├── .github/workflows/     # CI/CD pipeline configuration
├── conftest.py            # Shared pytest fixtures
├── pytest.ini
├── requirements.txt
└── README.md

⚙️ Installation
git clone https://github.com/Andrei800/unified-api-tests.git
cd unified-api-tests

python -m venv .venv
source .venv/Scripts/activate   # or . .venv/bin/activate on Linux/Mac
pip install -r requirements.txt


Then create a .env file in the project root:

BASE_URL=https://gorest.co.in/public/v2
GOREST_TOKEN=<your_token_here>

🧪 Running Tests
pytest -v --html=reports/report.html --self-contained-html


After execution, open reports/report.html to view the test report.

🔄 Continuous Integration

Every push to main automatically triggers:

Dependency installation

Test run via GitHub Actions

Upload of the HTML report as an artifact






📈 Roadmap

Add ReqRes API module

Implement JSON Schema Validation

Integrate Allure Reports

Add nightly build (cron job) for scheduled runs

Build a Test Dashboard for aggregated analytics

👨‍💻 Author

Andrei — QA Automation Engineer
📫 https://github.com/Andrei800
