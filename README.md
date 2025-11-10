<h1 align="center">🧩 Unified API Tests Framework</h1>

<p align="center">
  <a href="https://github.com/Andrei800/unified-api-tests/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Andrei800/unified-api-tests/tests.yml?branch=main&label=Build&style=for-the-badge" alt="Build Status">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pytest-Automation-green?style=for-the-badge&logo=pytest" alt="Pytest">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux-blueviolet?style=for-the-badge" alt="Platform">
</p>

---

## 📘 Overview

**Unified API Tests** is a scalable, modular framework for REST API testing built on top of **Pytest** and **Requests**.  
It’s designed to handle multiple APIs (e.g., *GoRest*, *ReqRes*, *Swagger PetStore*) using a single, reusable architecture.  

This project demonstrates a real-world QA automation setup — with environment management, CI/CD integration, and professional reporting.

---

## 🚀 Key Features

- **Unified Base Client (`BaseAPIClient`)**
  - Handles `429 Too Many Requests` with retry & exponential backoff  
  - Built-in CI throttling and jitter control  
  - Timeout, rate limit, and session management  
  - Detailed request logging and timing  

- **Environment Configuration**
  - Loads `.env` for API tokens and base URLs  
  - Secure and excluded from GitHub  

- **Real QA Project Structure**
  - Modular design (`core`, `api`, `utils`, `tests`)  
  - Pytest fixtures, parametrization, and markers (`e2e`, `negative`, `performance`)  
  - CI/CD integration with GitHub Actions and HTML reports  

- **Extensible Architecture**
  - Add new API modules (e.g., ReqRes or PetStore) without changing the core  
  - Shared utilities for validation, data generation, and assertions  

---

## 🧱 Project Structure
unified-api-tests/
├── src/
│ ├── core/ # Core logic (Base client, retry logic)
│ │ └── base_client.py
│ ├── api/ # Specific API wrappers (GoRest, ReqRes, PetStore)
│ └── utils/ # Helper functions, validators, etc.
│
├── tests/
│ ├── gorest/ # GoRest API test suite
│ ├── reqres/ # ReqRes API test suite
│ └── petstore/ # PetStore Swagger tests
│
├── reports/ # HTML reports (pytest-html)
├── .github/workflows/ # CI/CD workflow configs
├── conftest.py # Fixtures and env loader
├── pytest.ini
├── requirements.txt
└── README.md



---

## ⚙️ Installation

- git clone https://github.com/Andrei800/unified-api-tests.git
- cd unified-api-tests

- python -m venv .venv
- source .venv/Scripts/activate   # or . .venv/bin/activate on Linux/Mac
- pip install -r requirements.txt



---

Create a .env file in the project root:

- BASE_URL=https://gorest.co.in/public/v2
- GOREST_TOKEN=<your_token_here>


---
## 🧪 Running Tests

- pytest -v --html=reports/report.html --self-contained-html
- After the run, open the generated HTML report:
/reports/report.html



---

## 🔄 Continuous Integration (CI)

Each push to the main branch automatically triggers:

- Dependency installation

- Test execution via GitHub Actions

- Upload of the HTML report as an artifact

Status	Description
<p align="center">

🟢 Build Passing — CI pipeline completed successfully
<br>
🧩 Python 3.12 — Compatible and validated version
<br>
🧪 Pytest — Core testing engine
<br>
☁️ GitHub Actions — Automated test runs on every push

</p>



---

## 📈 Roadmap

 - Add ReqRes API test suite

 - Implement JSON Schema validation

 - Integrate Allure Reports

 - Add nightly scheduled builds (GitHub cron)

 - Build a results dashboard (Streamlit / HTML)


---

## 👨‍💻 Author

- Andrei — QA Automation Engineer
- 📫 GitHub Profile: [Andrei](https://github.com/Andrei800)

🌍 Focus: REST API Automation, CI/CD, and Test Framework Design



---

🧠 Keywords

pytest • requests • QA Automation • API Testing • Python • CI/CD • backoff • jsonschema • pytest-html • Faker • DevOps QA



---

<p align="center"> <b>If you like this project, give it a ⭐ and follow for more QA tools!</b> </p> 
