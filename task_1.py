import httpx

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

create_user_payload = {
    "firstName": "Kirill",
    "lastName": "Ivanov",
    "age": 29
}

response_create_user = httpx.post('https://dummyjson.com/users/add',
                                  json=create_user_payload,
                                  headers=headers)

print("Status_kod", response_create_user.status_code)
#print("Text:", response_create_user.text)
#print("Headers", response_create_user.headers)



assert response_create_user.status_code == 201

response_create_user_data = response_create_user.json()

assert response_create_user_data["firstName"] == create_user_payload["lastName"], "Assert firstName is fall"
assert response_create_user_data["lastName"] == create_user_payload["firstName"], "Assert firstName is fall"
assert response_create_user_data["id"] is not None