import pandas as pd   

students = {
	"Name": ["Jagan", "Ram", "Kiran", "Shiva"],
    "Marks": [75, 92, 68, 85]
}

student_df = pd.DataFrame(students)

Lowest_values = student_df.sort_values(by = "Marks")
Higest_values = student_df.sort_values(by = "Marks", ascending = False)

print("Ascending Order:", Lowest_values)
print("Decending Order:", Higest_values)