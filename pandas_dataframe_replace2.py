import pandas as pd 


orders = {
		"Order_ID" : [101, 102, 103, 104, 105],
	"Product" : ["Laptop", "Phone", "Shoes", "Watch", "Tablet"],
	"Payment" : ["COD", "cod", "Online", "COD", "cod"]
}

orders_df = pd.DataFrame(orders)

print("Orginal DataFrame:",)
print(orders_df)

orders_df["Payment"] = orders_df["Payment"].replace({
	"COD" : "Cash on Delivary",
	"cod" : "Cash on Delivary",
	"Online": "Online pay"
	})

print("Replaced DataFrame:",)
print(orders_df)