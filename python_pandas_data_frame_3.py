import pandas as pd
import numpy as np

dataframe_1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])
print(dataframe_1)
print('\n')
for index, row in dataframe_1.iterrows():
    print(f'Index:{index},Row A:{row["A"]}, Row B:{row["B"]}')

dataframe_1.to_csv('data//myDataFrameTab.csv', sep='\t')
