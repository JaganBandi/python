import pandas as pd  


vehicals = {
	  "Vehicle_ID": [101, 102, 103, 104, 105, 106],
    "Model": ["Swift", "Nexon", "Creta", "Nexon EV", "City", "Grand Vitara"],
    "Fuel_Code": ["P", "D", "D", "E", "P", "H"],
    "Price": [750000, 1200000, 1500000, 1600000, 1400000, 1800000]
}


vehicals_df = pd.DataFrame(vehicals)


fule_mapping = {
	"P" : "Petrol",
	"D" : "Diesel",
	"E" : "Electric",
	"H" : "Hybrid"
}

vehicals_df["Fuel Code"] = vehicals_df["Fuel_Code"].map(fule_mapping)

print(vehicals_df) 