# tests/reqres/test_users_reqres.py
import os
import pytest
from src.api.reqres import ReqresAPI

CI = os.getenv("CI") == "true"

@pytest.mark.smoke
@pytest.mark.reqres
def test_reqres_list_users_smoke():
    api = ReqresAPI()
    resp = api.list_users(page=1)

    # Если локальная сеть/прокси ломает ReqRes, не тормозим разработку
    if not CI and resp.status_code == 401 and "Missing API key" in resp.text:
        pytest.skip("ReqRes blocked by local network/proxy (401). Running only in CI.")
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "data" in body and isinstance(body["data"], list)


@pytest.mark.reqres
def test_reqres_create_user_smoke():
    api = ReqresAPI()
    payload = {"name": "QA", "job": "Automation"}
    resp = api.create_user(payload)

    if not CI and resp.status_code == 401 and "Missing API key" in resp.text:
        pytest.skip("ReqRes blocked by local network/proxy (401). Running only in CI.")
    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert body.get("id")
    assert body.get("createdAt")
