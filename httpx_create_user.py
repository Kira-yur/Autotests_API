import httpx
from tools.fakers import get_random_email


payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

responce = httpx.post("http://localhost:8000/api/v1/users", json=payload)
responce_data = responce.json()

print("otvet:", responce_data)
print("status:", responce.status_code)

# 1. сначала удалять тестового пользователя, потом создавать заного
# 2. подвтавлять 11,2,3 и т.д. в почту, чтобы создавался уникальный типо через параметризацию
# 3. создавать уникальную почту















