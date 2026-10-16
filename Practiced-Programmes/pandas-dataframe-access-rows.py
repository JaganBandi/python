import pandas as pd  

Company_employees = {
	"Name" : ["Jagan", "Lokesh", "Ram", "Shiva"],
	"Department" : ["DevOps", "Python", "Testing", "DevOps"],
	"salary" : [35000, 50000, 45000, 65000],
	"Experience" : [1, 2, 3, 4]
	}

company_df = pd.DataFrame(Company_employees)
company_df.index = [101, 102, 103,104]
print(company_df)

print(company_df.loc[102])
print("---------------------------")

print(company_df.loc[[101, 103]])
print("---------------------------")

print(company_df.iloc[3])
print("---------------------------")

print(company_df.iloc[[1, 3]])
print("---------------------------")