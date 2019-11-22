import numpy as np
import pandas as pd

series_1 = pd.Series()
print(f'Series-1:{series_1}')

#  Create a Series from ndarray
#  If data is an ndarray, then index passed must be of the same length. If no index is passed,
# then by default index will be range(n) where n is array length,
#  i.e., [0,1,2,3…. range(len(array))-1].
#  We did not pass any index, so by default, it assigned the indexes
# ranging from 0 to len(data)-1, i.e., 0 to 3.
data_1 = np.array(['a', 'b', 'c', 'd', 'e'])
series_2 =pd.Series(data_1)
print(f'Array Data:{data_1}')
print(f'Series-2:\n{series_2}')

#  Set index
series_3 = pd.Series(data_1, index= [100, 101, 102, 103, 104])
print(f'Series-3:\n{series_3}')

#  Create a Series from Dictionary
#  A dict can be passed as input and if no index is specified,
#  then the dictionary keys are taken in a sorted order to construct index.
#  If index is passed, the values in data corresponding to the labels in the index will be pulled out.
dict_1 = {'a':0.,'b':1.,'c':2.}
series_4 = pd.Series(dict_1) #  Observe − Dictionary keys are used to construct index.
print(f'Series-4:\n{series_4}')

series_5 = pd.Series(dict_1, index= ['b', 'c', 'd','a']) #  Observe − Index order is persisted and the missing element is
# filled with NaN (Not a Number).
print(f'Series-5:\n{series_5}')

#  Create a Series from Scalar
#  If data is a scalar value, an index must be provided.
#  The value will be repeated to match the length of index
series_6 = pd.Series(5, index=[0, 1, 2, 3])
print(f'Series-6:\n{series_6}')

#  Accessing Data from Series with Position
#  Data in the series can be accessed similar to that in an ndarray.
list_1:list = [1, 2, 3, 4, 5]
series_index: list = ['a', 'b', 'c', 'd', 'e']
series_7 = pd.Series(list_1, index=series_index)
print(f'Series-7:\n{series_7}')

#  Retrieve the first element.
#  As we already know, the counting starts from zero for the array,
#  which means the first element is stored at zeroth position and so on.
print(series_7[0])
print('******************')
#  Retrieve the first three elements in the Series.
# If a : is inserted in front of it, all items from that index onwards will be extracted.
#  If two parameters (with : between them) is used, items between the two indexes (not including the stop index)
print(series_7[0:3])
print('******************')
print(series_7[0:4]) # 5 will not printed which is at the 4th position
print('******************')
print(series_7[:3])

#  Retrieve the last three elements.
print(series_7[-3:])
print('******************')
print(series_7[:-3])

#  Retrieve Data Using Label (Index)
# A Series is like a fixed-size dict in that you can get and set values by index label.

#  Retrieve a single element using index label value.
list_2:list = [1, 2, 3, 4, 5]
index_list_2 = ['a', 'b', 'c', 'd', 'e']
series_8 = pd.Series(list_2, index= index_list_2)
print(f'Series-8:{series_8}')
#  Retrieve a single element
print(f'Retrieve the element at index c:{series_8["c"]} ')

#  Retrieve multiple elements
print(f'Retrieve multiple elements at index a c e:\n{series_8[["a", "c", "e"]]}')
#  print(f'Retrieve the element at index c:{series_8["f"]} ') #  Key Not Exist

#  https://appdividend.com/2019/01/16/python-pandas-series-tutorial-data-structure-example/
#  https://towardsdatascience.com/pandas-series-a-lightweight-intro-b7963a0d62a2
#

