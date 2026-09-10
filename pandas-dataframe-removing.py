import pandas as pd   

employee_details = {
	"Name" : ["Jagan", "Lokesh", "Ram", "Shiva"],
	"Department" : ["DevOps", "Python", "Testing", "DevOps"],
	"Salary" : [35000, 50000, 45000, 60000],
	"Age" : [21, 22, 24, 27],
	"Location" : ["Banglore", "Hydrabad", "Chennai", "Uttakhand"]

}

employee_df = pd.DataFrame(employee_details)

employee_df = employee_df.drop(["Age", "Location"], axis=1)
employee_df = employee_df.drop(2)

print(employee_df)
