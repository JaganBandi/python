import pandas as pd  


orders = {
	 "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Phone", "Shoes", "Laptop", "Phone"],
    "Order_Value": [50000, 30000, 2000, 45000, 25000]
}


orders_df = pd.DataFrame(orders)

# original Dataset
print("Original DataFrame:", )
print(orders_df)

#total orders value 
#using sum agg function
total_order_value = orders_df["Order_Value"].sum()

print("Total Order Value:", )
print(total_order_value)

#calculate the average value
average_order_value = orders_df["Order_Value"].mean()

print("Average Order Value:" )
print(average_order_value)

#calculate the minimum Order values
lowest_order_value = orders_df["Order_Value"].min()

print("Minimum orders values:",)
print(lowest_order_value)

#calculate the maximum orders value

highest_order_value = orders_df["Order_Value"].max()
print("Maximum Orders value:",)
print(highest_order_value)

# calculate the all values using groupby() method
group_of_values = orders_df.groupby("Product")["Order_Value"].agg([
	"sum", "min", "mean", "max", ])

print("Group By Values:",)
print(group_of_values)