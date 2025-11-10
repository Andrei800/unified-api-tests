# conftest.py
import os
import pytest
from dotenv import load_dotenv
from src.core.base_client import BaseAPIClient

@pytest.fixture(scope="session")
def load_env():
    """Загружает переменные окружения из .env"""
    load_dotenv()
    return {
        "base_url": os.getenv("BASE_URL"),
        "token": os.getenv("GOREST_TOKEN")
    }

@pytest.fixture(scope="session")
def client(load_env):
    """Единый HTTP клиент для тестов"""
    headers = {
        "Authorization": f"Bearer {load_env['token']}",
        "Content-Type": "application/json"
    }
    return BaseAPIClient(base_url=load_env["base_url"], headers=headers)
