# tests/reqres/test_users_reqres.py
import time
import pytest
from src.api.reqres import ReqresAPI


@pytest.mark.smoke
def test_reqres_create_user_smoke():
    api = ReqresAPI()  # base_url уже задан по умолчанию
    payload = {"name": f"QA_{int(time.time()*1000)}", "job": "Automation"}

    resp = api.create_user(payload)
    assert resp.status_code == 201, resp.text

    body = resp.json()
    # ReqRes эхо-ит name/job и добавляет id/createdAt
    assert body.get("name") == payload["name"]
    assert body.get("job") == payload["job"]
    assert "id" in body and body["id"]
    assert "createdAt" in body
