import numpy as np  

performance = np.array([65, 82, 75, 90, 55, 88, 72])

print("Performance:", performance)

high_perforamce = performance[performance > 80]

print("High Performance:", high_perforamce)

medium_performance = performance[(performance > 70) & (performance < 90)]

print("Medium Performance :", medium_performance)

seclectd = performance[(performance > 80) | (performance < 60)]

print("Selected Performace:", seclectd)