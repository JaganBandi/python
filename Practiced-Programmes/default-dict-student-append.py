from collections import defaultdict

students = defaultdict(list)

students["BCA"].append("Jagan")
students["BCA"].append("Kiran")
students["BSC"].append("Ram")

print(students)
print(students["BCA"])
print(students['BSC'])