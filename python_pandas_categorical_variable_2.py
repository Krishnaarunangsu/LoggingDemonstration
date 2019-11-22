import pandas as pd


dataframe_1 = pd.DataFrame({'col1':[1, 2 ,3, 4, 5], 'col2':list('abcab'), 'col3':list('ababb')})
print(dataframe_1)
dataframe_1['col2'] = pd.Categorical(dataframe_1['col2']).codes
dataframe_1['col3'] = pd.Categorical(dataframe_1['col3']).codes
print(dataframe_1)

dataframe_1['col3'], mapping_index = pd.Series(dataframe_1['col3']).factorize()
print(dataframe_1)
print(mapping_index.get_loc)
