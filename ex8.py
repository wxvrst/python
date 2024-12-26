import math
import requests
def getCoords(address):
    geocodeUrl = f"https://geocode-maps.yandex.ru/1.x/"
    geocodeParams = 
    {
        "geocode": address,
        "format": "json",
        "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
    }
    response = requests.get(geocodeUrl, params=geocodeParams).json()
    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        return tuple(map(float, point.split()))
    except (KeyError, IndexError):
        print(f"Не удалось найти координаты для {address}")
        return

def calculateDistance(home, uni):
    def lonlatDistance(a, b):
        degreeToMeters = 111 * 1000
        aLon, aLat = a
        bLon, bLat = b
        radiansLat = math.radians((aLat + bLat) / 2.0)
        cosLat = math.cos(radiansLat)
        dx = abs(aLon - bLon) * degreeToMeters * cosLat
        dy = abs(aLat - bLat) * degreeToMeters
        return math.sqrt(dy ** 2 + dx ** 2)

    homeCoords = getCoords(home)
    uniCoords = getCoords(uni)
    if homeCoords and uniCoords:
        distance = lonlatDistance(homeCoords, uniCoords)
        print(f"Расстояние от дома до университета: {distance / 1000} км")
    else:
        print("Не удалось рассчитать расстояние")

calculate_distance("Красная площадь, Москва", "Ленинский проспект, 1")
