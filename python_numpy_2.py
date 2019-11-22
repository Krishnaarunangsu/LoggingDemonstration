import numpy as np

list_1 = [1, 2, 3, 4, 5]
array_1 = np.array(list_1, ndmin=2)
print(f'The array is:{array_1}')

array_2 = np.array(list_1, dtype=complex)
print(f'The array is:{array_2}')
