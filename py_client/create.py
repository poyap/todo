import requests 

endpoint = 'http://localhost:8000/todo/api/'
data = {
    "title": "example1",
    "dead_line": "2023-12-30"
}

response = requests.post(endpoint, json=data, auth=('admin', 'admin'))
print(response.json())
# print(response.headers)
# print(response.text)