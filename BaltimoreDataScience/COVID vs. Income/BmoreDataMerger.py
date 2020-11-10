# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:43:35 2020

@author: Arun

Script to consolidate CSA, Zip Code, and Neighborhood Data with Median
Household Income and COVID Case count for Baltimore City
"""

import pandas as pd

#read data
c2n = pd.read_excel('CSA-to-NSA-2010.xlsx')
hinc = pd.read_excel('Vital Signs Indicator Median Household Income.xlsx')
z2c = pd.read_excel('Zip-to-CSA-2010.xls')
covidzip = pd.read_csv('MDCOVID19_MASTER_ZIP_CODE_CASES.csv')

#filter for Baltimore City Zip Codes
zipsList = [21227,21207,21230,21251,21229,21237,21287,21231,21226,21206,21222,21225,21211,21208,\
            21205,21218,21234,21202,21201,21213,21210,21209,21216,21236,21217,21224,21215,21212,\
                21223,21214,21239,21228]

covidzip = covidzip[covidzip['ZIP_CODE'].isin(zipsList)]

covidzip = covidzip.fillna(0)

zipsLatest = pd.DataFrame()

zipsLatest['Zip'] = covidzip['ZIP_CODE'].astype(int)
zipsLatest['TotalCOVIDCases'] = covidzip.iloc[:,-1]

#rename columns appropriately
z2c = z2c.rename(columns={'Zip2010':'Zip','CSA2010':'CSA'})
c2n = c2n.rename(columns={'CSA2010':'Community'})

#merge, rename Household income and CSAs-to-Neighborhoods
df = pd.merge_ordered(hinc, c2n, fill_method='ffill')
df = df.rename(columns={'2018 Data':'MHINC','NSA2010':'Neigh','Community':'CSA'})
df = df[['Neigh','CSA','MHINC']]

#merge with Zip Codes
df = pd.merge_ordered(z2c,df,fill_method='ffill')

#drop commas from household income numbers, convert to float
df['MHINC'] = df['MHINC'].replace(',','',regex=True)
df['MHINC'] = df['MHINC'].astype(float)

#convert zips to ints
df['Zip'] = df['Zip'].astype(int)

#merge with latest covid cases
df = pd.merge_ordered(zipsLatest,df,fill_method='ffill')
df = df[['Zip','Neigh','CSA','MHINC','TotalCOVIDCases']]

#export as CSV
df.to_csv('MASTER_MERGED.csv',index=False)

