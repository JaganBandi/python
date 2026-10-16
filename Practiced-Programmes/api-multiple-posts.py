import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    posts = response.json()

    print("Total Posts:", len(posts))
    print("\nFirst 5 Posts:")

    for post in posts[:5]:
        print("ID:", post["id"])
        print("Title:", post["title"])
        print("-" * 40)
else:
    print("Request failed!")
