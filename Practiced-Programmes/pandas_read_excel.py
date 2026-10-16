import pandas as pd

sales_df = pd.read_excel(
    "D:/python/Practiced-Programmes/Data/sales.xlsx",
    engine="openpyxl"
)

print(sales_df)

total_revenue = sales_df["Revenue"].sum()

print("Total Revenue:", total_revenue)

average_revenue = sales_df["Revenue"].mean()

print(average_revenue)

electronics_df = sales_df[sales_df["Category"] == "Electronics"]

electronics_df.to_excel("D:/python/Practiced-Programmes/Data/electronics.xlsx", index=False)

