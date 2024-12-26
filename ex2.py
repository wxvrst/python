import folium
from geopy.distance import geodesic

def createMap(t):
    map = folium.Map(location=coords[0], zoom_start=12)
    folium.PolyLine(coords, color="green", weight=2, opacity=1).add_to(map)

    middleIndex = len(t)
    middlePoint = coords[middleIndex]
    folium.Marker(location=middlePoint, popup="Avg").add_to(map)

    map.save("map.html")
    print("Карта пути создана: map.html")

    totalDistance = 0
    for i in range(len(coords) - 1):
        totalDistance += geodesic(coords[i], coords[i + 1]).meters
    return totalDistance

coords = [(55, 37), (55.5, 37.5), (56, 38)]
print(f"Length: {createMap(coords)}m")
