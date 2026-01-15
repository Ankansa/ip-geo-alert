from typing import List
from fastapi import Request


class EndpointRuleEngine:
    """
    Stores API endpoints that should trigger mail alerts.
    """

    def __init__(self):
        self._rules = []

    def add(self, path: str, methods: List[str] | None = None):
        """
        Register endpoint rule.

        Example:
            add("/api/v1/login", ["POST"])
            add("/api/v1/admin/delete")
        """

        self._rules.append({
            "path": path.rstrip("/"),
            "methods": [m.upper() for m in methods] if methods else None,
        })

    def should_trigger(self, request: Request) -> bool:
        req_path = request.url.path.rstrip("/")
        req_method = request.method.upper()

        for rule in self._rules:
            if rule["path"] != req_path:
                continue

            if rule["methods"] is None:
                return True

            if req_method in rule["methods"]:
                return True

        return False
