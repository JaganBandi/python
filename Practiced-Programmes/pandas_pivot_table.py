import pandas as pd  

student_marks = {
	"Student": ["Mahesh", "Ram", "Somu", "Hari", "Kalyan", "Lokesh"],
	"Department": ["Python", "Python", "Python", "DevOps", "DevOps", "DevOps"],
	"Subject" : ["Python", "Python", "SQL", "Linux", "Linux", "SQL"],
	"Marks": [80, 70, 75, 85, 65, 90]
	}


student_df = pd.DataFrame(student_marks)

marks_data = pd.pivot_table(student_df,
	index="Department",
	columns="Subject",
	values="Marks",
	aggfunc="mean"
	)

print(marks_data)