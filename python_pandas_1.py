import pandas as pd

series_1 = pd.Series(['cat', 'dog', 'cat', 'mouse'])
print(f'Original Series:\n{series_1}')
print('**********************************')
series_1_categorical = pd.Categorical(series_1)
print(f'Conversion to Category:\n{series_1_categorical}') # Gives the number of categories and labels
print('**********************************')
print(f'Codes for the Categories:\n{series_1_categorical.codes}') # The codes for the categories
print('**********************************')
print(f'Codes for the categories in columnar fashion:\n{pd.Series(series_1_categorical.codes)}') # Represent Codes for the categories in columnar fashion
