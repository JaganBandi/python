import pandas as pd  


orders = {
	"Order_ID" : [101, 102, 103, 104, 105],
	"Product" : ["Laptop", "Phone", "Shoes", "Watch", "Tablet"],
	"Payment" : ["COD", "cod", "Online", "COD", "cod"]
}

orders_df = pd.DataFrame(orders)

print("Before Replacement:", )
print(orders_df)

orders_df["Payment"] = orders_df["Payment"].replace("COD", "Cash on Delivery")

orders_df["Payment"] = orders_df["Payment"].replace("cod", "Cash on Delivery")

print("After Replacement:",)
print(orders_df)