import httpx

# create_payload = {
#   "email": "user1@example.com",
#   "password": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }
#
# create_response = httpx.post('http://localhost:8000/api/v1/users', json=create_payload)
# create_response_data = create_response.json()
#
# print("Create response:", create_response_data)
# print("Status code:", create_response.status_code)

loign_payload = { #куда можно убрать это
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=loign_payload) #зачем тут жсон
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status code:", login_response.status_code)


refresh_payload = {
  "refreshToken": login_response_data['token']['refreshToken']
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print("Refresh response:", refresh_response_data)
print("Status code:", refresh_response.status_code)