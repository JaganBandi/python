import pandas as pd   

employee = {
	"Name" : ["Jagan", "Ram", "Shiva"],
	"Salary": [30000, 40000, 50000],
	"Experiance" : [1, 3, 4]
}

employee_df = pd.DataFrame(employee)

employee_df["Anual Salary"] = employee_df["Salary"] * 12

employee_df["Experiance_Level"] = ["Junior", "Mid-Level", "Senior"]

employee_df["Salary"] = employee_df["Salary"] + 5000

print(employee_df)