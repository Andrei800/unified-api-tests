import os

import pytest
from dotenv import load_dotenv

from src.api.gorest import GorestAPI


@pytest.fixture(scope="session")
def env():
    load_dotenv()
    base = os.getenv("BASE_URL")
    token = os.getenv("GOREST_TOKEN")
    assert base, "BASE_URL is missing in .env"
    assert token, "GOREST_TOKEN is missing in .env"
    return {"base_url": base, "token": token}


@pytest.fixture(scope="session")
def gorest(env):
    headers = {
        "Authorization": f"Bearer {env['token']}",
        "Content-Type": "application/json",
    }
    api = GorestAPI(env["base_url"], env["token"])
    api.session.headers.update(headers)
    return api
