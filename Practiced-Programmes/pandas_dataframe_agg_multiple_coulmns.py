import pandas as pd  


sales = {
    "Bill_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Category": [
        "Grocery", "Dairy", "Grocery", "Beverages",
        "Dairy", "Grocery", "Beverages", "Dairy"
    ],
    "Revenue": [2000, 1500, 3000, 1200, 1800, 2500, 1600, 2200],
    "Quantity": [4, 2, 6, 3, 3, 5, 4, 4]
}


sales_df = pd.DataFrame(sales)

print("Original DataFrame:",)
print(sales_df)

result = sales_df.groupby("Category").agg({
	"Revenue": ["sum", "mean"],
	"Quantity": ["sum", "max"]
	})

print("Group Category Value:", )
print(result)