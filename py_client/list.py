import requests 

endpoint = 'http://localhost:8000/todo/api/'

response = requests.get(endpoint, auth=('admin', 'admin'))
print(response.json())
# print(response.headers)
# print(response.text)