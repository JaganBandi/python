import pandas as pd  

food_data = {
	"Resturants" : ["Pizza", "Biriyani House", "Pizza Hub", "Burgur point", "Biriyani House", "Burgur point"],
	"City" : ["Hyderabad", "Hyderabad", "Bengulure", "Hyderabad", "Bengulure", "Bengulure"],
	"Order_Value": [500, 600, 700, 400, 800, 350]
}

food_df = pd.DataFrame(food_data)

print(food_df)

city_summary = pd.pivot_table(food_df, index="City", values="Order_Value", aggfunc="mean")

print(city_summary)

print("-------------Average Order Value-------------------")

resturant_summary = pd.pivot_table(food_df, index="City", columns="Resturants", values="Order_Value", aggfunc="mean")

print(resturant_summary)