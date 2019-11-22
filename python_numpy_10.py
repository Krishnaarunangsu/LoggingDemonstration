import numpy as np


list_1, list_2 = [1, 2, 3], [4, 5, 6]
array_1 = np.array([list_1, list_2])
#  array_1 = np.array([[list_1, list_2]])
print(f'The Array is:\n{array_1}')
print(f'The Array Properties are:\n{array_1.shape, array_1.dtype}')
print(f'First Row:\n{array_1[0]}')
print(f'Second Row:\n{array_1[1]}')
print(f'First Row:\n{array_1[:-1]}')
print(f'First Row:\n{array_1[:1]}')
print(f'Second Row:\n{array_1[1:]}')
print(f'All  Rows & Three Columns:\n{array_1[0:]}')
print(f'Both Rows and all columns:\n{array_1[:2]}')
print(f'First Column:\n{array_1[:,0]}')
print(f'Second Column:\n{array_1[:,1]}')
print(f'Third Column:\n{array_1[:,2]}')
print(f'2nd Row 3rd Element:\n{array_1[1:,2]}')
print(f'2nd Row 1st & 2nd Elements:\n{array_1[1,:2]}')



