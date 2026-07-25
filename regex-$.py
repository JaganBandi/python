import re

Tools = "Docker, Jenkins, Ansible, Kubernetes, Cloud"

result = re.search("Cloud$", Tools)

if result:
	print("Pattern is found")

else : 
	print("Pattern Not Found")