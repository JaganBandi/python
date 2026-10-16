import sys

original_stdout = sys.stdout 

file =open("deployment.log", "w")

sys.stdout = file

print("Deployment Started")
print("Deployment Completed")

file.close()

sys.stdout = original_stdout

print("Log Saved Successfully")