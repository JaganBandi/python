import pandas as pd  
import matplotlib.pyplot as plt  

food_data = {
    "Restaurant": [
        "Pizza Hub",
        "Biryani House",
        "Burger Point",
        "Dosa Corner",
        "Fried Chicken"
    ],
    "Orders": [120, 180, 150, 90, 160]
}

food_df = pd.DataFrame(food_data)

plt.bar(
	food_df["Restaurant"],
	food_df["Orders"],
	)

plt.title("Restaurant Orders")

plt.show()
