import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

responce = requests.get(url)

print("Status Code:", responce.status_code)

if responce.status_code == 200:
	print("request successfully")
	print(responce.json())

else:
	print("request failed")