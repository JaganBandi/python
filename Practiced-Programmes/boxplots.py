import matplotlib.pyplot as plt 

waiting_times = [
    2, 3, 3, 4, 4, 5, 5, 6,
    6, 7, 8, 9, 10, 12, 35
]

result = plt.boxplot(
	waiting_times,
	vert=False,
	showmeans=True,
	patch_artist=True,
	notch=True,
	showfliers=False
	)

for box in result["boxes"]:
	box.set_facecolor("lightblue")

plt.title("Customer Waiting Time Analysis")
plt.ylabel("Waiting Time (minutes)")

plt.show()