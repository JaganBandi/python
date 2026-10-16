import pandas as pd  


order_data = {
	 "Order_ID": [501, 502, 503, 504, 505, 506],
    "Order_Date": [
        "2026-09-01",
        "2026-09-03",
        "2026-09-05",
        "2026-09-08",
        "2026-09-12",
        "2026-09-15"
    ],
    "Order_Value": [450, 630, 350, 750, 500, 900]
}


order_df = pd.DataFrame(order_data)

order_df["Order_Date"] = pd.to_datetime(order_df["Order_Date"])

filter_date = order_df[(order_df["Order_Date"] >= "2026-09-03") &
                      (order_df["Order_Date"] <= "2026-09-12")]


print(filter_date)