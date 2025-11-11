import time
import pytest
from src.api.gorest import GorestAPI

@pytest.mark.e2e
def test_create_get_delete_user():
    """Full positive chain: create → get → delete → get 404"""
    api = GorestAPI(
        base_url="https://gorest.co.in/public/v2",
        headers={"Authorization": f"Bearer {pytest.GOREST_TOKEN}", "Content-Type": "application/json"}
    )

    payload = {
        "name": f"QA_{int(time.time()*1000)}",
        "gender": "male",
        "email": f"qa_{int(time.time()*1000)}@example.com",
        "status": "active"
    }

    # Create user
    resp = api.create_user(payload)
    assert resp.status_code == 201, resp.text
    user_id = resp.json()["id"]

    # Get user
    resp = api.get_user(user_id)
    assert resp.status_code == 200
    assert resp.json()["email"] == payload["email"]

    # Delete user
    resp = api.delete_user(user_id)
    assert resp.status_code in (200, 204)

    # Verify deletion
    resp = api.get_user(user_id)
    assert resp.status_code == 404
