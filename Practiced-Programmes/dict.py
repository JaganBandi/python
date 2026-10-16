student1 = {"name": "Suresh", "age": 15, "marks": 80, "grade": "A", "class": 9, "subject": "telugu", "marks": 75}
student2 = dict(name = "Rajesh", age = 16, marks = 79, grade = "B", standered = 10, subject = "Maths")
print(student1)
print(type(student1))
print(student1["name"])

print(student2)

print(student2["standered"])


x = student1["name"]
print(x)

x = student2["subject"]

y = student2.keys()
print(y)

student1 ["city"] = "Anathapur"
print(y)

z = student1.values()

student1 ["year"] = 2026

print(z)

x = student1.items()

print(x)

student1 ["marks"] = 89

print(x)

if "subject" in student1:
	print("yes, the subject key is present in the student1")

else:
	print("NO, subject is not in student1")

for key, values in student1.items():
	print(key, ":",values)

		
	