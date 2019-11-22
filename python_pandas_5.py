# Python program converting
# a series into list

# importing pandas module
import pandas as pd


# making data frame
data = pd.read_csv("data//nba.csv")

# removing null values to avoid errors
data.dropna(inplace = True)
print(data)

# storing dtype before operation
dtype_before = data['Salary'].dtype
print(dtype_before)

# converting to list
salary_list = data['Salary'].tolist()

# storing dtype after operation
dtype_after = type(salary_list)

# printing dtype
print(f'Data Type of Salary before conversion:{dtype_before}\nData Type of Salary after Conversion:{dtype_after}')
