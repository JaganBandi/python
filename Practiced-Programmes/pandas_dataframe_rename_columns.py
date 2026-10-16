import pandas as pd  

employees = {
    "emp_name": ["Jagan", "Ram", "Kiran", "Shiva"],
    "emp_dept": ["Python", "DevOps", "Testing", "Python"],
    "emp_salary": [45000, 55000, 50000, 60000],
    "emp_exp": [1, 2, 3, 4]
}

employee_df = pd.DataFrame(employees)

print("Original DataFrame:", employee_df)

employee_df = employee_df.rename(columns = {
	"emp_name": "Employee_name",
	"emp_dept": "Department",
	"emp_salary": "Salary",
	"emp_exp": "Experience"

	})

print("Renamed DataFrame:", employee_df)
