import numpy as np

list_1 = range(5)
iter_1 = iter(list_1)

# use iterator to create ndarray
x = np.fromiter(iter_1, dtype = float)
print(x)

iterable = (x*x for x in range(5))
#  y = np.fromiter(iterable, float, count=3)
y = np.fromiter(iterable, float)
print(y)

my_list = [0,2,4,6]
it = iter(my_list)
n = np.fromiter(it, dtype = float)
print(n)
print(type(n))

m = np.fromstring('3 5', dtype=int, sep=' ')
print(m)
