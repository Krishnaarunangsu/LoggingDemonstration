import numpy as np
import pandas as pd


# Creating a Series
from pandas import Series

data_1: Series = pd.Series([5, 2, 3, 7], index=['a', 'b', 'c', 'd'])
print(data_1.values)
print(data_1.index)
print(data_1.shape)
print(data_1)
# print(data_1.transpose)
# print(data_1.mean)
data_2: Series = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
print(data_2)
print(data_1)
# Add two Series
#data_1.add(data_2, fill_values=0)
addition = data_1 + data_2
print(addition)

data_1_modified: Series = pd.Series([5, 2, 3, 7])
data_2_modified: Series = pd.Series([1, 6, 4, 9])
addition_modified = data_1_modified + data_2_modified
print(addition_modified)

subtraction_modified  = data_1_modified -  data_2_modified
print(subtraction_modified)

multiplication_modified  = data_1_modified *  data_2_modified
print(multiplication_modified)

division_modified  = data_1_modified/data_2_modified
print(division_modified)


#  https://www.w3resource.com/python-exercises/pandas/python-pandas-data-series-exercise-3.php
