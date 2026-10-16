import pandas as pd  

customers = pd.DataFrame({
	"customer_id": [1, 2, 3],
    "name": ["Jagan", "Rahul", "Priya"]
})

orders = pd.DataFrame({
	"customer_id": [1, 2, 4],
    "amount": [500, 700, 900]
})


outer_merge = pd.merge(customers, orders, on="customer_id", how="outer")

print(outer_merge)