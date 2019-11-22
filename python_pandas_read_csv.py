# importing pandas module
import pandas as pd

# making data frame
dataframe_1 = pd.read_csv("data//nba.csv")
ser = pd.Series(dataframe_1['Name'])
data = ser.head(10)
print(data)


# using indexing operator
print(data[3:6])
print(data[:6])

# using .loc[] function
print(data.loc[3:6])
print(data.loc[:6])

# using .iloc[] function
print(data.iloc[3:6])
print(data.iloc[:6])
