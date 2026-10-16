from collections import Counter

numbers = [1, 3, 1, 2, 3, 4, 2, 1, 3, 3]

count = Counter(numbers)

print(count)
print(count[3])
print(count.most_common(3))
