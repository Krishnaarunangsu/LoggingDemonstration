import pandas as pd

series_1 = pd.Series(['a', 'b', 'c', 'd', 'a'], dtype='category') # 1-D Array
print(f'Series:\n{series_1}')

dataframe_1 = pd.DataFrame({'grade':['a', 'b', 'c', 'd', 'a']}, dtype='category') # 2-D Array
print(f'DataFrame:\n{dataframe_1}')

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c','d'], ['a', 'b', 'c']) #  as 'd' is not included in the level so the output will include NaN
print(f'Cat:\n{cat}')
