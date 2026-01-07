import httpx


from tools.fakers import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
response_reg = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
response_reg_data = response_reg.json()
response_user_id = response_reg_data["user"],["id"]

print("registration:", response_reg_data)


payload_login={
    "email":create_user_payload["email"],
    "password":create_user_payload["password"]
}

response_login = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload_login)
response_login_data = response_login.json()
print("login:", response_login_data)

# get_user_payload={
#     "user_id": response_user_id
# }

get_user_headers = {
    "Authorization": f"Bearer {response_login_data['token']['accessToken']}"
}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{response_reg_data['user']['id']}", headers=get_user_headers) #а можно ли сдлеать это переменной?
get_user_response_data = get_user_response.json()

print("view", get_user_response_data)