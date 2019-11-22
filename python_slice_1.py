#  The slice() constructor creates a slice object representing the set of indices specified by range(start, stop, step).
# The slice object is used to slice a given sequence (string, bytes, tuple, list or range) or any object which supports sequence protocol (implements __getitem__() and __len__() method).

# Slice object represents the indices specified by range(start, stop, step).

# The syntax of slice() are:
# slice(stop)
# slice(start, stop, step)
# slice() Parameters
# slice() mainly takes three parameters which have the same meaning in both constructs:
# start - starting integer where the slicing of the object starts
# stop - integer until which the slicing takes place. The slicing stops at index stop - 1.
# step - integer value which determines the increment between each index for slicing
# If a single parameter is passed, start and step are set to None.

print(slice(3))
print(slice(1, 5, 2))

#  Get substring from a given string using slice object
py_string: str = 'Python'

# Contains indices(0, 1, 1, 2)
# i.e. that is P, y, t
index_1=slice(3)
print(py_string[index_1])

# contains indices (1, 3)
# i.e. y and h
index_2 = slice(1, 5, 2)
print(py_string[index_2])

index_3 = slice(2)
print(py_string[index_3])

# contains indices (-1, -2, -3)
# i.e. n, o and h
index_4 = slice(-1, -4, -1)
print(index_4)
print(py_string[index_4])


#  https://www.programiz.com/python-programming/methods/built-in/slice
