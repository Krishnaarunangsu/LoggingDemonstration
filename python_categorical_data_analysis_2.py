import pandas as pd
import numpy as np
import copy


df_flights = pd.read_csv('https://raw.githubusercontent.com/ismayc/pnwflights14/master/data/flights.csv')

print(df_flights.head())


import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()
readRDS = robjects.r['readRDS']
RDSlocation = 'Downloads/datasets/nyc_flights/flights.RDS' #location of the file
df_rds = readRDS(RDSlocation)
df_rds = pandas2ri.ri2py(df_rds)

df_rds.head(2)

from rpy2.robjects import r
import rpy2.robjects.pandas2ri as pandas2ri
file="~/Downloads/datasets/nyc_flights/flights.rda" #location of the file
rf=r['load'](file)
df_rda=pandas2ri.ri2py_dataframe(r[rf[0]])

df_rda.head(2)

print(df_flights.info())

