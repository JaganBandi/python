import json 

employee = {
	"id": 101,
	"Name": "Kalyan"
}

data = json.dumps(employee)

print(type(employee))
print(type(data))