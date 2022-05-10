import pandas as pd
from pandas import read_csv
import folium
import os
import webbrowser

crimes = read_csv('Dataframe.csv',error_bad_lines=False)

vis = os.path.join('Community_Areas.geojson')
m = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")
m.choropleth(
  geo_data=vis, 
  data = crimes, 
  columns = ['Community Area', 'count'], 
  fill_color = 'YlGn', 
  key_on = 'feature.properties.area_numbe')

folium.LayerControl().add_to(m)
m.save('map.html')
webbrowser.open(filepath)



















# read the data
crimes = read_csv('Dataframe.csv',error_bad_lines=False)
# convert float to int then to string
crimes['Community Area'] = crimes['Community Area'].astype('int').astype('str')
# choropleth map
vis = 'Community_Areas.geojson'
m = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")
m.choropleth(
  geo_data=vis, 
  data = crimes, 
  columns = ['Community Area', 'count'], 
  fill_color = 'YlGn', 
  key_on = 'feature.properties.area_num_1')
  
folium.LayerControl().add_to(m)
m.save('map.html')
webbrowser.open('map.html')