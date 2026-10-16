import pandas as pd  

import matplotlib.pyplot as plt  

fitness_data = {
    "Workout_Hours": [1, 2, 3, 4, 5, 6],
    "Calories_Burned": [150, 220, 300, 390, 480, 550]
}

fitness_df = pd.DataFrame(fitness_data)

plt.scatter(
	fitness_df["Workout_Hours"],
	fitness_df["Calories_Burned"],
	c=fitness_df["Calories_Burned"],
	s=100,
	cmap="viridis",
	alpha=0.5,
	edgecolors="orange",
	marker="^"
	)

plt.colorbar()

plt.title("Workout Hours VS Calories Bruned")
plt.xlabel("Workout Hours")
plt.ylabel("Calories Bruned")

plt.show()