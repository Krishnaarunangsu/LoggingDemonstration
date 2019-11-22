import pandas as pd
import numpy as np


# simple array
list_1 = ['g','e','e','k','s']
data_1 = np.array(list_1)
series_1 = pd.Series(data_1)
print(f'Series:{series_1}')
print(f'Index of the Series:{series_1.index}')
print(f'Values of the Series:{series_1.values}')

# # creating simple array
data_2 = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
series_2 = pd.Series(data_2)
print(f'Series:\n{series_2}')

#  Accessing Element from Series with Position :
#retrieve the first six elements
print(series_2[:6])


# creating simple array
data_3 = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
series_3 = pd.Series(data_3,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])

# accessing a element using index element
print(series_3[16])
