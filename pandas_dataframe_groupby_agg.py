import pandas as pd  

sales = {
    "Order_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "Category": [ "Electronics", "Fashion", "Electronics", "Grocery", "Fashion", "Electronics", "Grocery",
        "Fashion"
    ],
    "Order_Value": [5000, 2000, 7000, 1500, 3000, 4000, 2500, 3500]
   }

sales_df = pd.DataFrame(sales)

print("Original DataFrame:",)
print(sales_df)

result = sales_df.groupby("Category")["Order_Value"].agg([
 	"sum", "mean", "min", "max"])

print(result)
