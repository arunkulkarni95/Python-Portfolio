# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:36:26 2020

@author: Arun
"""

import pandas as pd
import folium
from folium import plugins

df = pd.read_csv('MASTER_MERGED.csv')

df = df.rename(columns={'Zip':'zipcode1','Neigh':'LABEL'})
df['zipcode1'] = df['zipcode1'].astype(str)

baltMap = folium.Map(location=[39.2904,-76.6122], tiles='OpenStreetMap', zoom_start=13)
#folium.GeoJson('zipcode.geojson').add_to(baltMap)
#folium.GeoJson('Maryland_Baltimore_City_Neighborhoods.geojson').add_to(baltMap)


covid_choro = folium.Choropleth(geo_data='zipcode.geojson', geo_path='zipcode.geojson',\
                   data=df, columns=['zipcode1','TotalCOVIDCases'],\
                       key_on='feature.properties.zipcode1',fill_color='YlGn',fill_opacity=0.8,\
                           legend_name='COVID-19 Total Reported Cases').add_to(baltMap)

mhinc_choro = folium.Choropleth(geo_data='Maryland_Baltimore_City_Neighborhoods.geojson',\
                                geo_path='Maryland_Baltimore_City_Neighborhoods.geojson',data=df,\
                                    columns=['LABEL','MHINC'],\
                                        key_on='feature.properties.LABEL',fill_color='OrRd',fill_opacity=0.8,\
                                            legend_name='Neighborhood Median Household Income').add_to(baltMap)

    
mhinc_choro.geojson.add_child(folium.features.GeoJsonTooltip(['NBRDESC','LABEL'],labels=False))
covid_choro.geojson.add_child(folium.features.GeoJsonTooltip(['zipcode1','zipname']))

folium.LayerControl().add_to(baltMap)
baltMap.save('COVID_MHINC.html')
