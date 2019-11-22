#  Creating a Series by passing a list of values, letting pandas create a default integer index:

import numpy as np
import pandas as pd

# Create a Series
series_1 = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f'The Series is :\n{series_1}')

#  Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20190101', periods=6)
print(dates)

df_1 = pd.DataFrame(np.random.randn(5)) # 5 rows and 1 column as no column is specified so default is 1
df_2 = pd.DataFrame(np.random.randn(6, 4)) # 6 rows & 4 columns
print(df_1)
print('***************************************')
print(df_2)

# randomly constructing 3D array
array_1 = np.random.randn(2, 2, 2)
print(f'3D Array filled with random values : \n{array_1}') # 2*2*2

# https://www.geeksforgeeks.org/numpy-random-randn-python/
