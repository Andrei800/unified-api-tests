# src/api/reqres.py
from src.core.base_client import BaseAPIClient


class ReqresAPI(BaseAPIClient):
    """Wrapper for https://reqres.in public API (no auth)."""

    def __init__(self, base_url: str = "https://reqres.in/api"):
        super().__init__(base_url, "")

    def create_user(self, payload: dict):
        """POST /users — creates a user (returns id, createdAt)."""
        return self.request("POST", "/users", json=payload)

    def get_user(self, user_id: int | str):
        """GET /users/{id} — fetch user (demo endpoint)."""
        return self.request("GET", f"/users/{user_id}")

    def list_users(self, page: int = 1):
        """GET /users?page=n — list users."""
        return self.request("GET", "/users", params={"page": page})
