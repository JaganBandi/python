import pandas as  pd  


employees = {
	"Name": ["Jagan", "Ram", "Jagan", "Kiran", "Ram"],
    "Department": ["Python", "DevOps", "Python", "Testing", "DevOps"],
    "Salary": [45000, 55000, 45000, 50000, 55000]
}


employee_df = pd.DataFrame(employees)

employee_df = employee_df.drop_duplicates(keep = "last")

print(employee_df)

employee_df = employee_df.drop_duplicates(subset = ["Name"])

print(employee_df)

employee_df = employee_df.drop_duplicates()

print(employee_df)