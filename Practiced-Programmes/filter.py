employee_ids = [1, 2, 3, 4, 5, 6]

even = lambda x: x % 2 == 0

result = list(filter(even, employee_ids))

print(result)