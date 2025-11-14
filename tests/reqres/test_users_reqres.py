import time
import pytest

from src.api.reqres import ReqresAPI


@pytest.mark.smoke
@pytest.mark.reqres
def test_reqres_list_users_smoke():
    api = ReqresAPI()
    resp = api.list_users(page=1)

    # Если в окружении ReqRes режется прокси / фаерволом и отдает 401
    if resp.status_code == 401 and "Missing API key" in resp.text:
        pytest.xfail("ReqRes GET blocked by network/proxy (401).")

    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert "data" in body and isinstance(body["data"], list) and body["data"]


@pytest.mark.reqres
def test_reqres_create_user():
    api = ReqresAPI()
    payload = {"name": f"QA_{int(time.time() * 1000)}", "job": "Automation"}

    resp = api.create_user(payload)

    # POST тоже может быть заблокирован – в CI помечаем как ожидаемый xfail
    if resp.status_code == 401 and "Missing API key" in resp.text:
        pytest.xfail("ReqRes POST blocked by network/proxy (401).")

    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert body.get("id")
    assert body.get("createdAt")
