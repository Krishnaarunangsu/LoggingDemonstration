# Python program using astype
# to convert a datatype of series

# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("data//nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)
print(data)
# storing dtype before converting
before = data.dtypes
print(f'Before Conversion:\n{before}')

# converting data types(dtypes) using astype
data['Salary'] = data['Salary'].astype(int)
data['Number'] = data['Number'].astype(str)

after = data.dtypes
print(f'After Conversion:\n{after}')
