from collections import Counter

languages = ["Python", "Java", "Python", "JavaScript", "Python", "Java"]

count = Counter(languages)

print(count)
print(count["Python"])