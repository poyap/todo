import requests 

endpoint = 'http://localhost:8000/todo/api/8aad5d34-92ff-462f-b367-9fc21a5acd59/'
data = {
    "title": "New example",
    "dead_line": "2023-12-25"
}

response = requests.get(endpoint, json=data, auth=('admin', 'admin'))
print(response)
print(response.json())
# print(response.headers)
# print(response.text)