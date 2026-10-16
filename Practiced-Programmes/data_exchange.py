import json

student = {
    "name": "Jagan",
    "course": "DevOps",
    "marks": 75
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data))