import pandas as pd   

employee_details = {
	"Name": ["Jagan", "Lokesh", "Ram", "Shiva", "Venky", "Kiran"],
    "Department": ["DevOps", "Python", "Testing", "DevOps", "Linux", "Python"],
    "Salary": [35000, 50000, 45000, 65000, 40000, 55000],
    "Experience": [1, 2, 3, 4, 5, 6]
}

employee_df = pd.DataFrame(employee_details)

print(employee_df)

highest_salary = employee_df[employee_df["Salary"] > 45000]

employee_experience = employee_df[employee_df["Experience"] >= 4]

employee_dept = employee_df[employee_df["Department"] == "DevOps"]

print("-----------------Filter Data-----------------")
print("Highest Salary", highest_salary)
print("Highest Experience:", employee_experience)
print("Employee Department:", employee_dept)

