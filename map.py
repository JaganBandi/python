salaries = [10000, 20000, 30000, 50000]

add = lambda salaries: salaries + 1000

result = list(map(add, salaries))

print(result)