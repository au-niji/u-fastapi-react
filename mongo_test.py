import requests
import json

url = "http://127.0.0.1:8000/api/todo"
payload = {
    "title": "task A",
    "description": "test"
}

res = requests.post(url, data=json.dumps(payload))
print(res)
