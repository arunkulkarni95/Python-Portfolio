# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:54:43 2020

@author: Arun
"""
import pandas as pd

df = pd.read_csv('MDCOVID19_MASTER_ZIP_CODE_CASES.csv')

zipsList = [21227,21207,21230,21251,21229,21237,21287,21231,21226,21206,21222,21225,21211,21208,\
            21205,21218,21234,21202,21201,21213,21210,21209,21216,21236,21217,21224,21215,21212,\
                21223,21214,21239,21228]

df = df[df['ZIP_CODE'].isin(zipsList)]

df = df.fillna(0)
print(df)
df = df.drop('OBJECTID', axis=1)




df = df.transpose()
print(df)
df.columns = df.iloc[0]
df = df.drop('ZIP_CODE')
df = df.reset_index()
df = df.rename(columns={'index':'Date'})

print(df)
df['Date'] = df['Date'].map(lambda x: x.lstrip('F').lstrip('t').lstrip('o').lstrip('t')\
                            .lstrip('a').lstrip('l'))

dates = pd.DataFrame()
dates = df['Date'].str.split(pat='_', expand=True)
dates[0] = dates[0].map(lambda x: x.lstrip('0'))
dates['fdate'] = dates[2].str.cat(dates[0], sep='-').str.cat(dates[1],sep='-')

dates = dates['fdate']

df = df.drop('Date',axis=1)


df.insert(0,'Date',dates)

df['Date'] = pd.to_datetime(df['Date'])

df.to_csv('COVID_Cleaned.csv')