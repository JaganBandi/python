import pandas as pd  

vehicle_df = pd.read_json("D:/python/Practiced-Programmes/Data/vehical_sales.json")


print(vehicle_df)

suv_vehicles_sales = vehicle_df[vehicle_df["Category"] == "SUV"]

total_suv_sales = suv_vehicles_sales["Price"].sum()

suv_vehicles_sales.to_json("D:/python/Practiced-Programmes/Data/suv_vehicles_sales_df.json", orient="records")

