import pandas as pd  


sales_df = pd.read_csv("D:/python/Practiced-Programmes/Data/sales.csv")

print(sales_df)

total_revenue = sales_df["Revenue"].sum()

print("Total Revenue:",)
print(total_revenue)

average_revenue = sales_df["Revenue"].mean()

print("Average Revenue:", average_revenue)

fashion_df = sales_df[sales_df["Category"] == "Fashion"]

fashion_df.to_csv("D:/python/Practiced-Programmes/Data/fashoins_sales.csv", index=False)