import pandas as pd


data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}


df_1_purchases = pd.DataFrame(data)
print(df_1_purchases)

df_1_purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(df_1_purchases)

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
print("Data Series:")
print(s1)
print(s2)
df = pd.concat([s1, s2], axis=1)
print("New DataFrame combining two series:")
print(df)


series_1 = pd.Series([1, 2], index=['A', 'B'], name='s1')
print(series_1)
series_2 = pd.Series([3, 4], index=['A', 'B'], name='s2')
print(series_2)
df_3 = pd.concat([series_1, series_2], axis=1)
print(df_3)
df_4 = pd.concat([series_1, series_2], axis=1).reset_index()

print(df_4)

df_5 = series_1.to_frame().join(series_2)
print(df_5)


df_6 = pd.DataFrame(data=dict(s1=series_1, s2=series_2), index=series_1.index)
print(df_6)

#  https://stackoverflow.com/questions/18062135/combining-two-series-into-a-dataframe-in-pandas
#  https://www.kdnuggets.com/2017/01/pandas-cheat-sheet.html
#  https://stackoverflow.com/questions/39941321/create-dataframe-from-multiple-series?rq=1
#  https://cmdlinetips.com/2018/01/how-to-create-pandas-dataframe-from-multiple-lists/
#  https://thispointer.com/python-pandas-how-to-create-dataframe-from-dictionary/
#  https://www.digitalocean.com/community/tutorials/how-to-install-the-pandas-package-and-work-with-data-structures-in-python-3
#  https://www.geeksforgeeks.org/python-pandas-series/
