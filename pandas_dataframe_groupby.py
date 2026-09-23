import pandas as pd  


sales = {
	"Bill_ID": [1001, 1002, 1003, 1004,1005, 1006, 1007],
	"Category": ["Grocery", "Dairy", "Grocery", "Beverages", "Dairy", "Grocery", "Beverages"],
	"Revenue" : [2000, 1500, 3000, 1200, 1800, 2500, 1600]
	}


sales_df = pd.DataFrame(sales)

Total_revenue_for_category = sales_df.groupby("Category")["Revenue"].sum()

print(Total_revenue_for_category)

