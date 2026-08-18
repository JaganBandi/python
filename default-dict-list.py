from collections import defaultdict

employees = defaultdict(list)

employees["DevOps"].append("Jagan")
employees["DevOps"].append("Kalyan")
employees["Python Devoloper"].append("Shiva")

print(employees["DevOps"])
print(employees["Python Devoloper"])
print(employees)