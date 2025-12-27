import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "New task",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
#
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
# data = {"username": "test_user", "password": "132456"}
# response = httpx.post("https://httpbin.org/post", data=data)
#
# print(response.status_code)
# print(response.json())
#
# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.request.headers)
# print(response.status_code)
# print(response.json())

# params = {"userId": [1,2]}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.url)
# print(response.json())

# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print("STATUS:", response.status_code)
# print("TEXT:", repr(response.text))
# print(response.json())


with httpx.Client() as client:
    response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')

print(response1.json())
print(response2.json())


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/2/invalid_url")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f"Ошибка статус: {e}")