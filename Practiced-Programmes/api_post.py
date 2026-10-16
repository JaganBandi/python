import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
	"title": "My first API test",
	"body": "Learning API requests with python",
	"userid": 1 
}

responce = requests.post(url, json=data)

print("Status Code:", responce.status_code)
print("Responce data:",)
print(responce.json())