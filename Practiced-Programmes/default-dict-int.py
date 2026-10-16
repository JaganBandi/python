from collections import defaultdict

colors = defaultdict(int)

colors = ["Red", "Blue", "Green", "Red", "Blue"]

count = defaultdict(int)

for color in colors:
	count[color] +=1

	print(count)