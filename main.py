import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
import recup_datas



dataframe = recup_datas.datas_display()

m = folium.Map(location=[48.866669, 2.33333], zoom_start=12)
folium.GeoJson('arrondissements_paris.geojson').add_to(m)
for i in range(0,len(dataframe)):
    location = [dataframe.iloc[i]['geo_point_2d_lat'],dataframe.iloc[i]['geo_point_2d_long']]
    (folium.Marker(
        location, popup = dataframe.iloc[i]['adresse'] )
     .add_to(m))


#
#
#
# folium.Marker(
#      [48.8360452467052,2.293417776948326], popup="Liberty Bell", tooltip="Liberty Bell"
#  ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)