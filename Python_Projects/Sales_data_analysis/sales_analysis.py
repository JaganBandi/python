# import the libraries
import pandas as pd  
import matplotlib.pyplot as plt

# Load the data 
sales = pd.read_csv("sales_data.csv")

sales["TotalSales"] = sales["Quantity"] * sales["UnitPrice"]

print(sales[["Product", "Quantity", "UnitPrice", "TotalSales"]])

total_revenue = sales["TotalSales"].sum()
print("Total Revenue:", total_revenue)

# revenue by product
product_revenue = sales.groupby("Product")["TotalSales"].sum()
print("Revenue by Product")
print(product_revenue)

highest_product = product_revenue.idxmax()
highest_revenue = product_revenue.max()

print("Highest Revenue Product:", highest_product)
print("Highest:", highest_revenue)

# revenue by region
region_revenue = sales.groupby("Region")["TotalSales"].sum()

print("\nRevenue by Region:",)
print(region_revenue)

highest_region = region_revenue.idxmax()
highest_region_revenue = region_revenue.max()

print("Highest Revenue Region:", highest_region)
print("Highest Regional Revenue:", highest_region_revenue)

# visulize the the results using matplotlib library
plt.figure(figsize=(8, 5))

plt.bar(product_revenue.index, product_revenue.values)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")

for product, revenue in product_revenue.items():
	plt.text(product, revenue, str(revenue), ha="center", va="bottom")

plt.tight_layout()
plt.show()


# visualize revenue by region

plt.figure(figsize=(8, 5))

plt.bar(region_revenue.index, region_revenue.values)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (Rs.)")

for region, revenue in region_revenue.items():
	plt.text(region, revenue, str(revenue), ha="center", va="bottom")

plt.tight_layout()

plt.show()