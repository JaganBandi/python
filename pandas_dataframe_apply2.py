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

def calcualte_discount(value):

	if value >= 1000:
		 discount = value * 0.10

	elif value >= 500:
		 discount = value * 0.05

	else:
		discount = 0

	return discount

orders_df["Disount"] = orders_df["Order_Value"].apply(calcualte_discount)

orders_df["Final_Amount"] = orders_df["Order_Value"] - orders_df["Disount"]

print(orders_df)