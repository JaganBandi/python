import pandas as pd  

student_details = {
	"Name": ["Bharath", "Dharshith", "Hethvik", "Shiva", "Ram"],
	"Department" : ["BCA", "BSC", "BBA", "B.com", "BA"],
	"Marks": [75, 89, 83, 73, 90],
	"Attendance" : [85, 60, 70, 95, 80]
}

student_df = pd.DataFrame(student_details)

print(student_df.describe())