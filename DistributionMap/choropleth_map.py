from http.client import responses
import pandas as pd # library for data analysis
import numpy as np # library for multi-dimensional arrays, high-level mathematical functions
import json # library to handle JSON files
import geojson
import folium

# from geopy.geocoders import Nominatim 
# convert an address into latitude and longitude values
import requests # library to handle requests


# import the data. 
data_all = pd.read_csv("res_number.csv")


INDICATOR = 'The number of restaurants'
data = data_all[data_all['IndicatorName']==INDICATOR]
data.head()

# grab the districts and res num column
map_data = data_all[['District', 'Restaurant number']]
map_data.head()

# import geojson data.
geojson_url = 'https://raw.githubusercontent.com/Surllian/SEPM/Tae/districts.geojson'
response = requests.get(geojson_url)
geojson = response.json()


M = folium.Map(location=[10.8131, 106.6897], zoom_start=10.3)


folium.Choropleth(
   geo_data = geojson,
   data = map_data,
   columns=['District','Restaurant number'],
   key_on='feature.id',
   fill_color='YlOrRd',
   fill_opacity=0.7,
   line_opacity=0.2,
   legend_name="Number of restaurant",
).add_to(M)
M