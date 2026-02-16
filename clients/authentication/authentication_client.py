from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class RequestDict (TypedDict):
    email: str
    password: str

class RefreshDict (TypedDict)
    refreshToken: str | None

class AuthenticationClient(APIClient):

    def login(self, request: RequestDict) -> Response:
        return self.post('/api/v1/authentication/login', json=request)

    def refresh_token(self, request: RefreshDict) -> Response:
        return self.post('/api/v1/authentication/refresh', json=request)

# client = AuthenticationClient()
# client.login({"email": "", "password": ""})
