import httpx

response_all_users = httpx.get("https://dummyjson.com/users")

assert response_all_users.status_code == 200

response_all_users_data = response_all_users.json()

assert "users" in response_all_users_data and 

print("Status kod:", response_all_users.status_code)
print("Data:", response_all_users_data)