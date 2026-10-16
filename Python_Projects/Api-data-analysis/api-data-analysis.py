import requests
import pandas as pd
import matplotlib.pyplot as plt  

url = "https://jsonplaceholder.typicode.com/posts"

try:
	responce = requests.get(url, timeout=10)
	responce.raise_for_status()

	posts = responce.json()
	print("Data Type:", type(posts))
	print("First Record:", posts[0])
	print("Avaliable feilds:", posts[0].keys())

	print("Total Records:", len(posts))

except requests.exceptions.RequestException as error:
	print("API Requeste Failed:", error)


data_df = pd.DataFrame(posts)

print(data_df.head())

data_df.to_csv("posts.csv", index=False)

print("Dataset Shape:", data_df.shape)
print("Column Names:", data_df.columns.tolist())

user_posts = data_df.groupby("userId")["id"].count()

print("Post by Each User:")
print(user_posts)


plt.bar(user_posts.index, user_posts.values)

plt.xlabel("User ID")
plt.ylabel("Number of Posts")
plt.title("Number of Post by Each User")

plt.show()