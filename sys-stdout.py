import sys

file = open("deployment.txt", "w")

sys.stdout = file

print("Deployment Started")
print("Checking Application")
print("Application Deployed Successfully")

file.close()