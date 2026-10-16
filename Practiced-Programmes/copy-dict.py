x = {
	"name": "Jagan",
	"age": 21,
	"location": "Kalachtla",
	"Studies": "Grauduate"
}

x["age"] = 25
print(x)

y = x.copy()
x["name"] = "praveen"
print(y)

z = dict(x)
x["name"] = "Rahul"
print(z)

