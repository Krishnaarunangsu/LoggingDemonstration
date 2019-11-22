import numpy as np

array_1 = np.arange(10)
print(array_1)

sliced_array_1 = slice(2, 7, 2)  # args: slice(start, stop, step)
print(array_1[sliced_array_1])
print(array_1[2:7:2])
print(array_1[5])
print('*****')
print(array_1[2:]) #  Will take the start element but not the end element
print(array_1[2:5]) #  #  Will take the start element but not the end element


array_2 = np.array([[1, 2, 3],[3, 4, 5], [4, 5, 6]])
print(array_2)

# slice items starting from index
print('Now we will slice the array from the index array_2[1:]')
# print(array_2[0])
print(array_2[0:])
