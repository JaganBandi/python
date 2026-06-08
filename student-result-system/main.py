import student as stu

name = input("Student Name:")
m1 = int(input("Enter Math Marks:"))
m2 = int(input("Enter Science Marks:"))
m3 = int(input("Enter English Marks:"))

stu.student_details(name)

total_marks = stu.total(m1, m2, m3)
print("Total:", total_marks)

avg = stu.average(total_marks)
print("Average:", round(avg, 2))

stu.grade(avg)