# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:05:12 2020

@author: Arun
"""

import pandas as pd

#import raw data
#reorganize/rename columns
df = pd.read_csv('Attacks by country, time, and destination port.csv')

df = df.rename(columns={'Country':'country','src_port: Descending':'src_port','dest_port: Descending':'dest_port'\
                        ,'Count':'count','timestamp:Descending':'time'})
df = df[['country','src_port','dest_port','count']]

#break-up by country
usa = df[df['country'] == 'United States']
vietnam = df[df['country'] == 'Vietnam']
china = df[df['country'] == 'China']
india = df[df['country'] == 'India']
russia = df[df['country'] == 'Russia']
canada = df[df['country'] == 'Canada']
philippines = df[df['country'] == 'Philippines']
colombia = df[df['country'] == 'Colombia']
brazil = df[df['country'] == 'Brazil']
taiwan = df[df['country'] == 'Taiwan']

#populate list of dataframes
countries = []
countries.append(usa)
countries.append(vietnam)
countries.append(china)
countries.append(india)
countries.append(russia)
countries.append(canada)
countries.append(philippines)
countries.append(colombia)
countries.append(brazil)
countries.append(taiwan)

final = pd.DataFrame()

#sort by source port, reset index
for df in countries:
    df.reset_index(drop=True,inplace=True)
    df.sort_values(by=['src_port'])    
    df = df.sort_values(by='src_port')
    df.reset_index(drop=True,inplace=True)
    final = final.append(df)

final.reset_index(drop=True,inplace=True)
us_and_russia_ports = final[(final['country'] == 'United States') | (final['country'] == 'Russia')]
all_countries_ports = final



#export new dataframes
all_countries_ports.to_csv('all_countries.csv')
us_and_russia_ports.to_csv('us_and_russia.csv')