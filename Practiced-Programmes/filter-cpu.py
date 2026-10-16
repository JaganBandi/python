cpu_usage = [20, 45, 80, 90, 35, 95]

server = lambda x: x > 70

result = list(filter(server, cpu_usage))

print(result)