class EmptyFileNameError(Exception):
	pass

class InvalidFileExtenctionError(Exception):
	pass

try:
	filename = input("Enter Your File Name:")

	if filename == "":
		raise EmptyFileNameError("File Name Cannot Be Empty")

	if not filename.endswith(".txt"):
		raise InvalidFileExtenctionError("Only .txt files are allowed.")

	print("\n Reading File....\n")

	file = open("D:/Bandi.txt", "r")

	data = file.read()

	print(data)

	file.close()

except EmptyFileNameError as e:
	print(e)

except InvalidFileExtenctionError as e:
	print(e)

except FileNotFoundError:
	print("File Not Found Error.")

else:
	print("File Read Succesfully..")

finally:
	print("Programme End")

