import pandas as pd  


order_df = pd.read_excel("D:/python/Practiced-Programmes/Data/food_delivary.xlsx", engine="openpyxl")

print(order_df)

hyderabad_orders = order_df[order_df["City"] == "Hyderabad"]
hyderabad_orders = order_df[order_df["City"] == "Hyderabad"].copy()

hyderabad_orders["Total_Order_Value"] = hyderabad_orders["Order_Value"].sum()
hyderabad_orders["Average_Order_Value"] = hyderabad_orders["Order_Value"].mean()

hyderabad_orders.to_excel(
    "D:/python/Practiced-Programmes/Data/hyderabad_food_orders.xlsx",
    index=False
)
hyderabad_orders.to_excel("D:/Python/Practiced-Programmes/Data/hydrabad_food_orders.xlsx", index="false")

