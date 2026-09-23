import pandas as pd  

employees = {
	"Name" : ["Jagan", "Ram", "Kiran", "Shiva"],
	"Department": ["Python", "DevOps", "Testing", "Python"],
	"Salary" : [45000, 55000, 50000, 60000]
}

employees_df = pd.DataFrame(employees)

employees_df = employees_df.rename(columns = {
	"Name": "Employee_Name",
	"Department": "Employee_Department",
	"Salary" : "Monthly_Salary"
	},
	index={
	0: "EMP01", 
	1: "EMP02",
	2: "EMP03",
	3: "EMP04"
	})


print(employees_df)