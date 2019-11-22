import numpy as np

array_1 = np.array([[3, 6, 7],[5, -3, 0]])
print(array_1.shape)

array_2 = np.array([[1, 1], [2, 1], [3, -3]])
print(array_2.shape)

array_multiplication_result = array_1.dot(array_2)
print(f'Array Multiplication Result:\n{array_multiplication_result}')
