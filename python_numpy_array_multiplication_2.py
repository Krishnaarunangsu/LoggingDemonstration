import numpy as np
#  Transposing a 1D array into 2D array


array_4 = np.array([7,2, 9, 10])[np.newaxis]
print(array_4)
print(array_4.T)
array_5 = array_4.T
print(array_5.shape)

array_6 = np.array([[5.2, 3.0, 4.5],[9.1, 0.1, 0.3]])
print(array_6.shape)
print(array_5.dot(array_6))
