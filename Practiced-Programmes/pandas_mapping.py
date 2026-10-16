import pandas as pd  


orders = {
	"Order_ID": [501, 502, 503, 504, 505, 506],
    "Restaurant": ["Biryani House", "Pizza Hub", "Burger Point",
                   "Biryani House", "Pizza Hub", "Burger Point"],
    "Status_Code": ["P", "D", "C", "D", "P", "D"],
    "Order_Value": [350, 500, 250, 400, 600, 300]
}


orders_df = pd.DataFrame(orders)

status_mapping = {
	"P": "Preparing",
	"D": "Delivered",
	"C": "Cancelled"
}

orders_df["Status"] = orders_df["Status_Code"].map(status_mapping)

print(orders_df)