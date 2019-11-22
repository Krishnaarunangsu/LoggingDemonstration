import pandas as pd


labels, uniques = pd.factorize(['a', 'b'])
print(f'Labels:{labels}')
print(f'Unique Codes:{uniques}')

