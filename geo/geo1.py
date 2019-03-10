#import folium library for visualization/maps
import folium

#create a base map
#tiles values are -- 'stamenterrain', 'Mapbox bright', 
#map=folium.Map(location=[37.296933,-121.9574983], zoom_start = 8, tiles="openstreetmap")
map=folium.Map(location=[38.296933,-77.3074983], zoom_start = 8, tiles="openstreetmap")
#mark a point
#folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
#for coordinates in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
for coordinates in [38.9072586,-77.203159],[38.8189286,-77.204159]:
    folium.Marker(location=coordinates, icon=folium.Icon(color = 'green')).add_to(map)


#save the map
map.save("map1.html")

