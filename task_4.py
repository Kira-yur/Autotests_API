import httpx

response = httpx.get("https://dummyjson.com/users")
response_data = response.json()

if response.status_code == 200:
    assert "users" in response_data
    print('Status kod:', response.status_code, "And 'Users' available")

else:
    print("Status kod:", response.status_code)