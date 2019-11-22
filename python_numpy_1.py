import numpy as np

list_1 = [1, 2, 3]
array_1 = np.array(list_1)
print(f'Numpy Array:{array_1}')
print(array_1.transpose())
print(array_1.T)

#  Transposing a 1D array into 2D array
array_3 = np.array([5,4])[np.newaxis]
print(array_3)
print(array_3.T)

list_2 = [[1, 2], [3, 4]]

array_2 = np.array(list_2)
print(f'Array before transpose:\n{array_2}')

array_2 = np.transpose(list_2)
print(f'Array before transpose:\n{array_2}')


