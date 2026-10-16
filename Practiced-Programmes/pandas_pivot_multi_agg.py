import pandas as pd  


vehical_data = {
	"City": ["Hyderabad", "Hyderabad", "Bengalure", "Bengalure", "Chennai", "Chennai"],
	"Category": ["Suv", "Sedan", "Suv", "Sedan", "Suv", "Sedan"],
	"Unit_Sold": [10, 8, 15, 12, 7, 9],
	"Revenue": [2500000, 1800000, 3750000, 2700000, 1750000, 2025000]

	}

vehical_df = pd.DataFrame(vehical_data)

print("Original DataFrame:",)
print(vehical_df)

city_analysis = pd.pivot_table(
	vehical_df,
	index="City",
	values=["Unit_Sold", "Revenue"],
	aggfunc= ["mean", "sum"]
	)

print(city_analysis)