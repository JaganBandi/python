import pandas as pd  


order_data = {
	"Order_id" : [1001, 1002, 1003, 1004, 1005],
	"Order_date": [
	    "2026-09-01",
        "2026-09-05",
        "2026-09-12",
        "2026-09-20",
        "2026-09-28"],

    "Revenue": [50000, 25000, 3000, 5000, 15000]
}

order_df = pd.DataFrame(order_data)

print("Original DateFrame:", order_df)

print(order_df.dtypes)

order_df["Order_date"] = pd.to_datetime(order_df["Order_date"])

print(order_df)

print(order_df.dtypes) 

order_df["Year"] = order_df["Order_date"].dt.year

order_df["Month"] = order_df["Order_date"].dt.month

order_df["Day"] = order_df["Order_date"].dt.day

print(order_df)