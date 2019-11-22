import numpy as np

list_1 = [[1, 2, 3], [4, 5, 6]]
array_1 = np.array(list_1)
print(f'The array is:\n{array_1}')
print(f'Shape of the array:{array_1.shape}')
print(f'Size of the array:{array_1.size}')

#  Changing the shape of the array
array_1.shape = (3, 2)
print(f'The array is:\n{array_1}')

#  Reshaping by function
print(f'The array is:\n{array_1.reshape(2,3)}')

array_2 = np.arange(24)
print(f'The dimension of the array is:{array_2.ndim}')

# now reshape it
array_3 = array_2.reshape(2, 4, 3)
print(f'The array after remodeling(2*4*3):\n{array_3}')
# array_3 is having three dimensions
