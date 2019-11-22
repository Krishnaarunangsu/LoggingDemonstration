import numpy as np
x = np.empty([3,2], dtype = int) # numpy.empty(shape, dtype = float, order = 'C')
print(x)


y = np.zeros([5, 2])
print(y)

z = np.zeros((5,), dtype = np.int)
print(z)

m = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(m)

n = np.ones([5,])
print(n)

o = np.ones([5,1])
print(o)

p = np.ones([1, 5])
print(p)

q = np.ones([2,2], dtype = int)
print(q)

l = [1,2,3]
arr = np.asarray(l, dtype=float)
print(arr)

# ndarray from tuple
t =(1, 2, 3)
arr_2 = np.asarray(t)
print(arr_2)


# ndarray from list of tuples
s = [(1,2,3),(4,5)]
arr_3 = np.asarray(s)
print(arr_3)

#  ttps://stackoverflow.com/questions/43362986/numpy-frombuffer-attributeerror-str-object-has-no-attribute-buffer
s = b'hello world'
buffer_array = np.frombuffer(s, dtype='S1', count=5, offset=6)
print(buffer_array)

