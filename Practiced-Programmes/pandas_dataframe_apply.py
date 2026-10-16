import pandas as pd  


orders = {
	"Order_ID": [501, 502, 503, 504, 505, 506],
    "Restaurant": [
        "Pizza Hub", "Burger Point", "Biryani House",
        "Pizza Hub", "Burger Point", "Biryani House"
    ],
    "Order_Value": [350, 800, 1200, 450, 600, 1500]
}

orders_df = pd.DataFrame(orders)

def calssify_order(value):
	if value >= 1000:
		return "Premium"

	elif value >= 500:
		return "Regular"

	else:
		return "Normal" 

orders_df["Order_Type"] = orders_df["Order_Value"].apply(calssify_order)

print(orders_df)
