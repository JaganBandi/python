import pandas as pd  


sales_df = pd.read_csv("sales.csv")

print("CSV File",sales_df)

total_revenue = sales_df["Revenue"].sum()

print("Tatal Revenue", total_revenue)

average_revenue = sales_df["Revenue"].mean()

print("Average Revenue:", average_revenue)