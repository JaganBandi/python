import pandas as pd   

employee = {
	"Name" : ["Jagan", "Ram", "Shiva"],
	"Department": ["DevOps", "Linux administrator", "Testing"],
	"Salary" : [30000, 40000, 50000],
	"Experience" : [1, 2, 4]
}

employee_df = pd.DataFrame(employee)

salary = employee_df["Salary"]

print(salary)
print(type(salary))

print("-------------Display Two Columns-------------")

employee_info = employee_df[["Name", "Department"]]

print(employee_info)
print(type(employee_info))

