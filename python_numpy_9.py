# array to begin with
import numpy as np
a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print('Our array is:')
print(a)
print('\n')

#  this returns an array of items in the second column
print('The items in the second column are:')
print(a[...,1])

#  this returns array of items in the second row
print('The items in the second row are:')
print(a[1,...])
print('\n')

# Now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[...,1:])

e = np.array([(1, 2, 3), (4, 5, 6)])
print(e)
print(f'First Row:{e[0]}')
print(f'First Column:{e[:,0]}')
print(f'Second Row:{e[1]}')
print(f'Second Column:{e[:,1]}')
## Second Row, two values
print(e[1, :2])
