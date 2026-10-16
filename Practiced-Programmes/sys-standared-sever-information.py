import sys

print("Enter Your Server Name:")
server_name = sys.stdin.readline().strip()

print("Enter Environment:")
environment_name = sys.stdin.readline().strip()

print("Enter Your Application Name:")
application_name = sys.stdin.readline().strip()

print("\n-------Server Information------------")
print("Server Name      :", server_name)
print("Environment Name :", environment_name)
print("Application Name :", application_name)

