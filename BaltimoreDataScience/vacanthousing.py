# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:08:47 2020

@author: Arun
"""

import pandas as pd

df = pd.read_csv('Vacant_Buildings.csv')

print(df.shape)
print(df.head())
print(df.columns)
print(df['Location'].astype(str))

latlong= df['Location'].astype(str)
print(latlong)

latlong = latlong.map(lambda x: x.lstrip('(').rstrip(')'))
print(latlong)

latlong = latlong.str.split(expand=True)
print(latlong)

latlong.iloc[:,0] = latlong.iloc[:,0].map(lambda x: x.rstrip(','))

print(latlong)

latlong.iloc[:,:] = latlong.iloc[:,:].astype(float)

latlong.columns = ['latitude','longitude']
print(latlong)