import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print("Статус логина", login_response.status_code)
print("JSON логина", login_response_data)



client = httpx.Client(base_url="http://localhost:8000",
                      timeout=100,
                      headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})
# вот то что в скобках, мы передаем базовый юрл

response = client.get("/api/v1/users/me")
response_data = response.json()

print("Status:", response.status_code)
print("Otvet:", response_data)
