# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:40:29 2020

@author: Arun
"""

import pandas as pd
import folium
from folium import plugins

df1 = pd.read_csv('MDCOVID19_MASTER_ZIP_CODE_CASES.csv')
df2 = pd.read_csv('Vacant_Buildings.csv')

#print(df1)

#filter COVID by bmore zips
zipsList = [21227,21207,21230,21251,21229,21237,21287,21231,21226,21206,21222,21225,21211,21208,\
            21205,21218,21234,21202,21201,21213,21210,21209,21216,21236,21217,21224,21215,21212,\
                21223,21214,21239,21228]

df1 = df1[df1['ZIP_CODE'].isin(zipsList)]

df1 = df1.fillna(0)

#print(df1)

zipsLatest = pd.DataFrame()

zipsLatest['zipcode1'] = df1['ZIP_CODE'].astype(str)
zipsLatest['LatestCases'] = df1.iloc[:,-1]
zipsLatest = zipsLatest.reset_index()

print(zipsLatest.sort_values(by='LatestCases', ascending=False))

#filter vacant housing coords
latlong= df2['Location'].astype(str)
latlong = latlong.map(lambda x: x.lstrip('(').rstrip(')'))
latlong = latlong.str.split(expand=True)
latlong.iloc[:,0] = latlong.iloc[:,0].map(lambda x: x.rstrip(','))
latlong.iloc[:,:] = latlong.iloc[:,:].astype(float)
latlong.columns = ['latitude','longitude']

#build map
baltMap = folium.Map(location=[39.2904,-76.6122], tiles='OpenStreetMap', zoom_start=13)

folium.GeoJson('zipcode.geojson').add_to(baltMap)

choropleth = folium.Choropleth(geo_data='zipcode.geojson', geo_path='zipcode.geojson',\
                   data=zipsLatest, columns=['zipcode1','LatestCases'],\
                       key_on='feature.properties.zipcode1',fill_color='YlGn',fill_opacity=0.8,\
                           legend_name='COVID-19 Total Reported Cases').add_to(baltMap)

for i,row in latlong.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(baltMap)

baltMap.add_child(plugins.HeatMap(data=latlong[['latitude', 'longitude']].to_numpy(), radius=25, blur=10))

choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['zipcode1','zipname'],labels=False))

folium.LayerControl().add_to(baltMap)

baltMap.save('baltChoropleth.html')