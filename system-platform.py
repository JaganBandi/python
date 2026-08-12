import sys

if sys.platform == "win32":
	print("Running on Windows")

elif sys.platform == "linux":
	print("Running on Linux")

elif sys.platform == "darwin":
	print("Running on macOS")