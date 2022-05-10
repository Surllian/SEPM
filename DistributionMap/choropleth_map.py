from http.client import responses
import pandas as pd # library for data analysis
from pandas import DataFrame, read_csv
import numpy as np # library for multi-dimensional arrays, high-level mathematical functions
import json # library to handle JSON files
import geojson
import folium
import pandas

# from geopy.geocoders import Nominatim 
# convert an address into latitude and longitude values
import requests # library to handle requests


# import the data. 
data_all = pd.read_csv("res_number.csv")
# data_all['RestaurantNumber'] = data_all['RestaurantNumber'].astype('int')


INDICATOR = 'The number of restaurants'
data = data_all[data_all['IndicatorName']==INDICATOR]
data.head()

# grab the districts and res num column
map_data = data_all[['District', 'RestaurantNumber']]
map_data.head()

# import geojson data.
# geojson_url = 'https://raw.githubusercontent.com/Surllian/SEPM/Tae/DistributionMap/districts.geojson'
# response = requests.get(geojson_url)
# geojson = response.json()

url = 'https://raw.githubusercontent.com/Surllian/SEPM/Tae/DistributionMap'
country_shapes = f'{url}/districts.geojson'

M = folium.Map(location=[10.8131, 106.6897], zoom_start=10.3)


folium.Choropleth(
   # geo_data = geojson,
   geo_data = country_shapes,
   data = map_data,
   columns=['District','RestaurantNumber'],
   key_on='feature.properties.name',
   # key_on='feature.id',

   fill_color='YlOrRd',
   fill_opacity=0.9,
   line_opacity=0.5,
   legend_name="The number of restaurant",
).add_to(M)
M