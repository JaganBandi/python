import pandas as pd  

worker_details = {
	"Name" : ["Jagan", "Lokesh", "Ram", "Mahesh", "Shiva", "Somu"],
	"Department" : ["Linux", "Java", "Python", "Developer", "Testing", "DevOps"],
	"Salary" : [30000, 40000, 50000, 60000, 70000, 80000],
	"Experience" : [1, 3, 4, 2, 6, 7]
}

company_df = pd.DataFrame(worker_details)
print(company_df.head())
print(company_df.head(3))
print(company_df.tail())
print(company_df.tail(2))