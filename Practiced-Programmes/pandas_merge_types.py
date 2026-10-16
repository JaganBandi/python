import pandas as pd  


employees = {
	"emp_id" : [101, 102, 103, 104],
	"Names": ["Jagan", "Priya", "Rahul", "Ravi"]
}

salary = {
	"emp_id" : [101, 102, 105],
	"Salaries" : [30000, 35000, 45000]
}

emp_df = pd.DataFrame(employees)
sal_df = pd.DataFrame(salary)

#inner merge
inner_merge = pd.merge(emp_df, sal_df, on="emp_id", how="inner")

#left merge
left_merge = pd.merge(emp_df, sal_df, on="emp_id", how="left")

#right merge
right_merge = pd.merge(emp_df, sal_df, on="emp_id", how="right")

#outer merge
outer_merge = pd.merge(emp_df, sal_df, on="emp_id", how="outer")

print("Inner Merge:",)
print(inner_merge)

print("Left Merge:",)
print(left_merge)

print("Right Merge:",)
print(right_merge)

print("Outer Merge:",)
print(outer_merge)