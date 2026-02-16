import httpx

response_users = httpx.get("https://dummyjson.com/users")
response_users_data = response_users.json()

assert response_users.status_code == 200
assert isinstance(response_users_data, dict)
assert "users" in response_users_data
assert isinstance(response_users_data["users"], list)