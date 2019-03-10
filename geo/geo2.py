#Import libraries

import folium
import pandas as pd
from folium.plugins import MarkerCluster

#Load data
data=pd.read_csv("volcanos_usa.csv")
lat=data['LAT']
lon=data['LON']
elevation=data['ELEV']

#Elevation function
def getElevation(elev):
    if(elev < 1000):
        return  "green"
    elif(elev < 3000):
        return "orange"
    else:
        return "red"

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "CartoDB dark_matter")

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Plot makers
for lat, lon, elevation in zip(lat,lon,elevation):
    #folium.Marker(location=[lat,lon], popup=str(elevation)+" m", icon=folium.Icon(color=getElevation(elevation))).add_to(map)
     folium.CircleMarker(location=[lat, lon], radius = 9, popup=str(elevation)+" m", fill_color=getElevation(elevation), color="gray", fill_opacity = 0.9).add_to(map)

#save the map
map.save("volcano_maps.html")

