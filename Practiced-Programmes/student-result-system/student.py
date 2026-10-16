def student_details(name):
	print("Student Name:", name)

def total(m1, m2, m3):
    total_marks = m1 + m2 + m3
    return total_marks

def average(total):
	return total / 3
	
def grade(avg):

	if avg >= 90:
		print("Grade:", "A")

	elif avg >= 70:
		print("Grade:", "B")

	elif avg >= 60:
		print("Grade:", "C")

	elif avg >= 35:
		print("Grade:", "D")

	else:
		print("Fail")
    

