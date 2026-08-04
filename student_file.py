import json

student = {
	"name": "Ram",
	"subject": "Maths",
	"marks": 85
}

file = open("student.json", "w")

json.dump(student, file)

print(file.name)

file.close()

print("Data Stored Successfully")