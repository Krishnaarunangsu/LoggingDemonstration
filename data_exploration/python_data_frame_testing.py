import pandas as pd

from pandas.util.testing import assert_frame_equal
df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df2 = pd.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
#print(assert_frame_equal(df1,df1))
#print(assert_frame_equal(df1,df2))
print(assert_frame_equal(df1, df2, check_dtype=False))

#  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.testing.assert_frame_equal.html
