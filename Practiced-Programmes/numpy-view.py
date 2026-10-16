import numpy as np   

data = np.array([10, 20, 30, 40])

data_view = data.view()

data_view[2] = 300

print("Original Data:", data)
print("Data View    :", data_view) 