import pandas as pd

delivery_date = {
	"Order_ID": [501, 502, 503, 504],
    "Order_Date": [
        "2026-09-01",
        "2026-09-05",
        "2026-09-10",
        "2026-09-15"
    ],
    "Delivery_Date": [
        "2026-09-03",
        "2026-09-08",
        "2026-09-12",
        "2026-09-20"
    ]
}


delivery_df = pd.DataFrame(delivery_date)

delivery_df["Order_Date"] = pd.to_datetime(delivery_df["Order_Date"])

delivery_df["Delivery_Date"] = pd.to_datetime(delivery_df["Delivery_Date"])


delivery_df["Delivery_Days"] = (delivery_df["Delivery_Date"] - delivery_df["Order_Date"] ).dt.days

print(delivery_df)