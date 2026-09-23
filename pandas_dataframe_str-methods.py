import pandas as pd  

employees = {
	 "Name": [" Jagan ", "RAM", " kiran ", "Shiva"],
    "Department": ["python", "DEVOPS", " Python ", "testing"]
}


employee_df = pd.DataFrame(employees)

print("Original Data Frame:",)

print(employee_df)

employee_df["Name"] = employee_df["Name"].str.strip().str.title()

employee_df["Department"] = employee_df["Department"].str.strip().str.title()

print("\n Cleaned Data Frame:",)

print(employee_df)

python_employees = employee_df[
           employee_df["Department"].str.contains("Python")
           ]

print("\n Python Employees",)

print(python_employees)