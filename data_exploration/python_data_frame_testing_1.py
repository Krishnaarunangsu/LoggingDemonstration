import numpy as np
import pandas as pd


df1=pd.DataFrame({'a':[1,2,3,4,4]})
df2=pd.DataFrame({'a':[6,7,8,9,10]})

expected_res=pd.Series([7,9,11,13,15])
print(pd.testing.assert_series_equal((df1['a']+df2['a']),expected_res,check_names=False))


# https://stackoverflow.com/questions/41852686/how-do-you-unit-test-python-dataframes
# https://pandas.pydata.org/pandas-docs/version/0.22.0/api.html#testing-functions
