import pandas as pd  


april_sales = {
	"Bill_ID": [201, 202, 203],
	"Product": ["Rice", "Milk", "Oil"],
	"Revenue": [2000, 1500, 2500]
}

may_sales = {   
   "Bill_ID": [204, 205, 206],
   "Product": ["Sugar", "Rice", "Milk"],
   "Revenue": [1800, 3000, 1700]
}	


april_df = pd.DataFrame(april_sales)
may_df = pd.DataFrame(may_sales)

all_sales = pd.concat([april_df, may_df],ignore_index=True)

print("Combined Data:",)
print(all_sales)


total_revenue = all_sales["Revenue"].sum()
average_revenue = all_sales["Revenue"].mean()

print("Total Revenue:", total_revenue)
print("Avereage Revenue:", average_revenue)