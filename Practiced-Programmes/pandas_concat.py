import pandas as pd  


group_one = {
	"emp_id" : [101, 102, 103, 104],
	"Name" : ["Jagan", "Ram", "Shiva", "Srinu"],
	"Department": ["Python", "DevOps", "Testing", "HR"]
}

group_two = {
	"emp_id": [105, 106, 107],
	"Name": ["Pradeep", "Ravi", "Lokesh"],
	"Department": ["Sales", "Developer", "Mechanical"]
}

one_df = pd.DataFrame(group_one)
two_df = pd.DataFrame(group_two)

all_employees = pd.concat([one_df, two_df], ignore_index=True)

print("Combined Data:",)
print(all_employees)

employee_data = pd.concat([one_df, two_df], axis=1)

print("Column Wise Data:",)
print(employee_data)

company_data = pd.concat([one_df, two_df],
	keys= ["group_one", "group_two"]
	)

print("Company Data:",company_data)
