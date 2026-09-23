import pandas as pd  


employees = {
	"Name": ["Jagan", "Ram", "Kiran", "Shiva"],
    "Age": ["22", "25", "24", "23"],
    "Salary": ["45000", "55000", "50000", "60000"]
}

employee_df = pd.DataFrame(employees)
print("Original Data Frame:", )
print(employee_df)

print("Data Types:",)
print(employee_df.dtypes)

employee_df["Age"] = employee_df["Age"].astype(int)

employee_df["Salary"] = employee_df["Salary"].astype(int)

employee_df["Salary"] = employee_df["Salary"] + 5000

print("Cleaned Data Frame:",)
print(employee_df)

print("Data Types:",)
print(employee_df.dtypes)
