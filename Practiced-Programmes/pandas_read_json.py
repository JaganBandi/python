import pandas as  pd  

vehicle_df = pd.read_json("D:/python/Practiced-Programmes/Data/vehical_sales.json")

print(vehicle_df)


hyderabad_vehicles = vehicle_df[vehicle_df["City"] == "Hyderabad"]

total_vehicle_sales = hyderabad_vehicles["Price"].sum()

average_vehicle_price = hyderabad_vehicles["Price"].mean()

print(total_vehicle_sales)
print(average_vehicle_price) 