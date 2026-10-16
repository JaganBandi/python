import pandas as pd  

sales_data ={
	"City": [
        "Hyderabad",
        "Hyderabad",
        "Bengaluru",
        "Bengaluru",
        "Chennai",
        "Chennai",
        "Hyderabad",
        "Bengaluru"
    ],
    "Category": [
        "Electronics",
        "Furniture",
        "Electronics",
        "Furniture",
        "Electronics",
        "Furniture",
        "Electronics",
        "Furniture"
    ],
    "Units_Sold": [20, 12, 25, 15, 18, 10, 22, 17],
    "Revenue": [
        50000,
        36000,
        62500,
        45000,
        45000,
        30000,
        55000,
        51000
    ]
}

sales_df = pd.DataFrame(sales_data)

print("Original Sales Data:",)
print(sales_df)

city_analysis = pd.pivot_table(
	sales_df,
	index="City",
	columns="Category",
	values="Revenue",
	aggfunc=["mean", "sum"]
	)

print(city_analysis)