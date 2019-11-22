import pandas as pd
import numpy as np

name_list = ['Avery Bradley', 'John Holland', 'Jonas Jerebko', 'Jordon Mickey', 'Terry Rozier',
             'Jared Sullinger', 'Evan Turner']
team_list = ['Boston Celtics', 'Boston Celtics', 'Boston Celtics', 'Boston Celtics',
             'Boston Celtics', 'Boston Celtics','Boston Celtics']
# number_list:list = [0.0, 30.0, 8.0, '', 12.0, 7.0, 11.0 ]
number_list:list = [0.0, 30.0, 8.0, np.nan, 12.0, 7.0, 11.0 ]
position_list:list = ['PG', 'SG', 'PF', 'PF', 'PG', 'C', 'SG']
#  age_list = [25, 27, 29, 21, 22, '', 27]
age_list = [25, 27, 29, 21, 22, np.nan, 27]
# Construct the data frame
dataframe_nba = pd.DataFrame({'Name': name_list, 'Team': team_list, 'Points': number_list,
                              'Position':position_list , 'Age': age_list})

dataframe_nba_new = pd.DataFrame(np.column_stack([name_list, team_list, number_list, position_list, age_list]),
                                 columns=['Name', 'Team', 'Points', 'Position', 'Age'])

print(f'The Dataframe is:\n{dataframe_nba}')
print('*************************************************************')
print(f'The Dataframe is:\n{dataframe_nba_new}')

#  https://stackoverflow.com/questions/30522724/take-multiple-lists-into-dataframe
#  https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
#  https://stackoverflow.com/questions/28503445/assigning-column-names-to-a-pandas-series
#  https://stackoverflow.com/questions/26047209/what-is-the-difference-between-a-pandas-series-and-a-single-column-dataframe
#  https://stackoverflow.com/questions/42211304/pandas-get-string-label-from-factorized-dataframe
#  https://stackoverflow.com/questions/26097916/convert-pandas-series-to-dataframe
