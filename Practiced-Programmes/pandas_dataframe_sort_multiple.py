import pandas as pd  


students = {
	 "Name": ["Jagan", "Ram", "Kiran", "Shiva", "Venky"],
    "Department": ["BCA", "BCA", "BSC", "BCA", "BSC"],
    "Marks": [85, 92, 78, 92, 88]
}


student_df = pd.DataFrame(students)

Multiple_sorting = student_df.sort_values(by=["Department", "Marks"])

print(Multiple_sorting)