import matplotlib.pyplot as plt

delivery_times = [
    15, 18, 20, 22, 25, 28,
    30, 32, 35, 35, 38, 40,
    42, 45, 48, 50, 52, 55,
    60, 65
]

plt.hist(
    delivery_times,
    bins=5,
    color="skyblue",
    edgecolor="black",
    density=False
    )

plt.title("Food Delivary Time Distribution")
plt.xlabel("Delivary Time (Minutes)")
plt.ylabel("Number Of Delivary")

plt.show()