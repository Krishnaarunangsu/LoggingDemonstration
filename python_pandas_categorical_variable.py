import numpy as np
import pandas as pd


dataframe_1 = pd.DataFrame({'col1':[1, 2 ,3, 4, 5], 'col2':list('abcab'), 'col3':list('ababb')})
#  dataframe_2 = pd.DataFrame({'col1':[1, 2, 3, 4, 5], 'col2':list('abcab'), 'col3':list('ababb')})

print(dataframe_1)
dataframe_1['col2'] = dataframe_1['col2'].astype(dtype='category')
dataframe_1['col3'] = dataframe_1['col3'].astype(dtype='category')
print(dataframe_1.dtypes)
cat_columns = dataframe_1.select_dtypes(['category']).columns
print(cat_columns)
dataframe_1[cat_columns] = dataframe_1[cat_columns].apply(lambda x: x.cat.codes)
# dataframe_1.col3 = pd.Categorical(dataframe_1.col3).codes

print(dataframe_1)
dataframe_1['col3'] = pd.Categorical(dataframe_1['col3']).codes
print(dataframe_1['col3'])


