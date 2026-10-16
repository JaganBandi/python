import os
import sys

print("Starting Deployment...")

if not os.path.exists("company.py"):
	print("Error: company.py not found")
	sys.exit()

print("company.py Found")
print("Starting Application")
print("Deploying the Application")