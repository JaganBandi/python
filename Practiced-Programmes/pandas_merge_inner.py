import pandas as pd  


orders = {
	"Order_ID": [ 601, 602, 603, 604],
    "Restaurant_ID":  ["R10", "R20", "R30", "R40"],
    "Order_Value":  [450, 600, 300, 700]
}

returants = {
"Restaurant_ID": ["R10", "R20", "R30", "R50"],
"Restaurant": ["Spice Hub", "Biryani Point", "Pizza World", "Burger Zone"],
"City":  ["Hyderabad", "Bengaluru", "Chennai", "Mumbai"]
}


orders_df = pd.DataFrame(orders)

resturnt_df = pd.DataFrame(returants)

inner_merge_df = pd.merge(orders_df, resturnt_df, on="Restaurant_ID", how="inner")

print(inner_merge_df)