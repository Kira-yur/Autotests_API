from clients.api_client import APIClient
from httpx import Response, URL
from typing import TypedDict

class requestDict(TypedDict):
    email: str
    password: str

class requestRefresh(TypedDict):
    refreshToken: str
class clientAuthenticationClient(APIClient):
    def login(self, request: requestDict) -> Response:
        return self.post('/api/v1/authentication/login', json=request)

    def refresh(self, request: requestRefresh) -> Response:
        return self.post('/api/v1/authentication/refresh', json=request)