import sys
import os

if not os.path.exists("application.py"):
    sys.stderr.write("ERROR: application.py not found\n")
    sys.exit()

sys.stdout.write("Application found\n")
sys.stdout.write("Deployment started\n")