import pandas as pd  

employee_data = {
	"Name" : ["Ram", "Srinu", "Shiva", "Hari", "Ravi", "Vishnu"],
	"Department": ["Python", "Python", "DevOps", "Tester", "DevOps", "tester"],
	"Salary": [25000, 50000, 45000, 60000, 70000, 30000]
}

emp_df = pd.DataFrame(employee_data)

result = emp_df.groupby("Department")["Salary"].sum()

print(result)
