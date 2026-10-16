import pandas as pd  


order_data = {
	"Order_ID": [501, 502, 503, 504, 505, 506],
	"Order_Date": ["2026-09-01", "2026-09-03", "2026-09-05", "2026-09-08", "2026-09-12", "2026-09-15"],
	"Order_Values": [450, 630, 350, 750, 500, 900]

}

order_df = pd.DataFrame(order_data)
print(order_df)

order_df["Order_Date"] = pd.to_datetime(order_df["Order_Date"])

print("Date Convertion",)
print(order_df)

print("------------filter Date -------------------")

filtered_date = order_df[order_df["Order_Date"] > "2026-09-05"]

print(filtered_date) 
