# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

#  https://www.kaggle.com/omarayman/categorical-data-analysis-in-python/data
#  https://stackoverflow.com/questions/29803093/check-which-columns-in-dataframe-are-categorical/29821799#29821799

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory


# Data = pd.read_csv("data/anonymous-survey-responses.csv")
Data = pd.read_csv("../data/anonymous-survey-responses.csv")
# Data = pd.read_csv("../data/myDataFrame.csv")
#print(Data.head())
print(f'Data Columns:\n{Data.columns}')
print(f'DataFrame Information:\n{Data.info()}')

Counts = Data["Just for fun, do you prefer dogs or cat?"].value_counts()
Names = Counts.index
print(f'Index is:{Names}')

postion_of_bars = list(range(len(Names)))
plt.bar(postion_of_bars,Counts)
plt.xticks(postion_of_bars,Names)


sns.countplot(Data["Just for fun, do you prefer dogs or cat?"]).set_title("Dogs Vs Cats")
plt.show()
