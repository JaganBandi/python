storage = [100, 200, 300, 400]

get = lambda x: x + 50

result = list(map(get, storage))

print(result)