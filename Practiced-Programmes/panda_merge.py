import pandas as pd  

orders = {
	"Order_ID":  [501, 502, 503, 504],
    "Restaurant_ID": ["R01", "R02", "R01", "R03"],
    "Order_Value": [350, 500, 250, 400]
}

returants = {
	"Restaurant_ID": ["R01", "R02", "R03"],
     "Restaurant": ["Pizza Hub", "Biryani House", "Burger Point"],
     "City" :["Hyderabad", "Bengaluru", "Chennai"]
}

orders_df = pd.DataFrame(orders)
resturnt_df = pd.DataFrame(returants)


merge_df = pd.merge(orders_df, resturnt_df, on="Restaurant_ID")

print(merge_df)
