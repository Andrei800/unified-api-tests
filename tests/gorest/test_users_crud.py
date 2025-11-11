import time

import pytest


@pytest.mark.e2e
def test_create_get_delete_user(gorest):
    payload = {
        "name": f"QA_{int(time.time()*1000)}",
        "gender": "male",
        "email": f"qa_{int(time.time()*1000)}@example.com",
        "status": "active",
    }

    # Create user
    resp = gorest.create_user(payload)
    assert resp.status_code == 201, resp.text
    user_id = resp.json()["id"]

    # Get user
    resp = gorest.get_user(user_id)
    assert resp.status_code == 200
    assert resp.json()["email"] == payload["email"]

    # Delete user
    resp = gorest.delete_user(user_id)
    assert resp.status_code in (200, 204)

    # Verify deletion
    resp = gorest.get_user(user_id)
    assert resp.status_code == 404
