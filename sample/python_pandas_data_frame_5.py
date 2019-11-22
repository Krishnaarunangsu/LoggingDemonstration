import pandas as pd
import numpy as np

data = {

    'name':['Mount Everest', 'K2', 'Kanchanjunga', 'Lhotse'],
    'height(m)':[8848,  8611, 8586, 8516 ],
    'summited': [1953, 1954, 1955, 1956],
    'mountain_range': ['Mahalangur Himalaya', 'Baltoro Karakoram', 'Kanchanjunga Himalaya', 'Mahalangur Himalaya']

}

#  df_peaks = pd.DataFrame(data,index=data['name'])
df_peaks = pd.DataFrame(data)
df_peaks.set_index('name', inplace= True)
print(df_peaks)
print('**********************************************')
#  Select a column by name(label)
var = df_peaks.loc[:, 'summited']
print(var)
print('**********************************************')
#  Get a numpy array instead of pandas Series
print(var.values)
print('**********************************************')
#  Select a row by label
row_1 = df_peaks.loc['K2', :]
print(row_1)
print('**********************************************')
#  Select a value by row & column level
value_1 = df_peaks.loc['K2', 'summited']
print(value_1)
print('**********************************************')
#  Select several rows by label
value_2 = df_peaks.loc[['K2', 'Lhotse'], :]
print(value_2)
print('**********************************************')
#  Select several consecutive columns by label
#  value_3 = df_peaks.loc[:]
#  value_3 = df_peaks.loc[:,]
value_3 = df_peaks.loc[:,'height(m)':'summited']
print(value_3)
print('**********************************************')
#  Select rows based on a column value
df_peaks_intermediate = var
df_peaks__custom_select = df_peaks.loc[var > 1954,:]
print(df_peaks__custom_select)
