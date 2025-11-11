# src/api/gorest.py
from src.core.base_client import BaseAPIClient


class GorestAPI(BaseAPIClient):
    """Specific API wrapper for GoRest endpoints."""

    def __init__(self, base_url: str, token: str):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        super().__init__(base_url=base_url, headers=headers)

    # ---- CRUD METHODS ----
    def create_user(self, payload: dict):
        """POST /users — create a new user"""
        return self.request("POST", "/users", json=payload)

    def get_user(self, user_id: int | str):
        """GET /users/{id} — fetch a user"""
        return self.request("GET", f"/users/{user_id}")

    def delete_user(self, user_id: int | str):
        """DELETE /users/{id} — delete a user"""
        return self.request("DELETE", f"/users/{user_id}")

    def list_users(self, params: dict | None = None):
        """GET /users — list all users"""
        return self.request("GET", "/users", params=params or {})
