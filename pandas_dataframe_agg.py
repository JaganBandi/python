import pandas as pd  

orders = {
	"Order_ID": [501, 502, 503, 504, 505, 506, 507, 508],
	"City" : ["Hyderabad", "Bengaluru", "Chennai", "Hyderabad", "Bengaluru", "Hyderabad", "Chennai", "Bengaluru"],
	"Order_value": [450, 600, 300, 250, 800, 550, 400, 700]

}

orders_df = pd.DataFrame(orders)

print("Original DataFrame:")
print(orders_df)

total_order_each_city = orders_df.groupby("City")["Order_value"].sum()

print("Total order values for each city:",)
print(total_order_each_city)

average_order_each_city = orders_df.groupby("City")["Order_value"].mean()

print("Average Order Values:",)
print(average_order_each_city)


number_of_orders_each_city = orders_df.groupby("City")["Order_value"].count()

print("Number of Orders Each City:",)
print(number_of_orders_each_city)

lowest_order_each_city = orders_df.groupby("City")["Order_value"].min()

print("Lowest Order City:",)
print(lowest_order_each_city)

higest_order_value = orders_df.groupby("City")["Order_value"].max()

print("Highest Order Value for Each City:",)
print(higest_order_value)