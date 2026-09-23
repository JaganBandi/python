import pandas as pd   


sales = {
	"Sale_ID" :  [701, 702, 703, 704],
   "Vehicle_ID": ["V01", "V02", "V03", "V04"],
   "Sale_Amount": [800000, 1200000, 1500000, 900000]
}

vehicle = {
"Vehicle_ID": ["V01", "V02", "V03", "V05"],
"Model": ["Swift", "Creta", "Nexon", "Baleno"],
"Fuel":  ["Petrol", "Diesel", "Petrol", "Petrol"]
} 


sales_df = pd.DataFrame(sales)
vehical_df = pd.DataFrame(vehicle)

left_merge_df = pd.merge(sales_df, vehical_df,on="Vehicle_ID", how="left")

print(left_merge_df)