# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:50:41 2020

@author: Arun
"""

import pandas as pd

df = pd.read_csv('MDCOVID19_MASTER_ZIP_CODE_CASES.csv')

#print(df)

df = df[(df['ZIP_CODE'] >= 21201) & (df['ZIP_CODE'] <= 21298)]

#print(df)

#df = df.fillna(0)


#print(df)

df = df.transpose()
#print(df[df.isna().any(axis=1)])

#print(df)
df.columns

df.reset_index(drop=True)
df = df.drop('OBJECTID')



df.columns = df.iloc[0]
df = df.drop('ZIP_CODE')
df = df.reset_index()
df = df.rename(columns={'index':'Date'})
df = df.set_index('Date')


#print(df.columns)

tit = 'Baltimore City COVID-19 Cases by Zip Code'

df1 = df.reset_index()

ax = df1.plot(kind='line',title=tit,legend=False)

ax.set_xlabel('Days Since 4/11/20')
ax.set_ylabel('Total COVID-19 Cases')

print(df)
print(df[df.isna().any(axis=1)])
print(df.iloc[-1])
print(df.iloc[-1].max())
print(df.iloc[-1].min())
