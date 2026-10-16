import pandas as pd  

company_worker_details = {
	"Name": ["Jagan", "Lokesh", "Ram", "Shiva", "Venky", "Kiran"],
    "Department": ["DevOps", "Python", "Testing", "DevOps", "Linux", "Python"],
    "Salary": [35000, 50000, 45000, 65000, 40000, 55000],
    "Experience": [1, 2, 3, 4, 5, 6]
}

company_df = pd.DataFrame(company_worker_details)
print(company_df)
print("\n--------------------------\n")

print(company_df.shape)
print("\n--------------------------\n")
print(company_df.columns)
print("\n--------------------------\n")
print(company_df.index)
print("\n--------------------------\n")
print(company_df.dtypes)

print(company_df.info())