import re

text = """

Jagan - 7981961842
Chitti - 9494942625
Peddaiah - 9573203805
Maneesha - 6302642007
Hymavathi - 9573203804
Dharshit - 5628492983
Hethvik - 4832401429
"""
result = re.findall(r"\b[6-9]\d{9}\b", text)

print("Valid Phone Numbers:")

for number in result:
	print(number)
