import requests
def findSouthCity(cities):
    res = None
    minLatitude = float("inf")

    for city in cities:
        geocodeUrl = f"https://geocode-maps.yandex.ru/1.x/"
        geocodeParams = {
            "geocode": city,
            "format": "json",
            "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
        }
        response = requests.get(geocodeUrl, params=geocodeParams).json()
        try:
            point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lon, lat = map(float, point.split())
            if lat < minLatitude:
                res = city
                minLatitude = lat
        except (KeyError, IndexError):
            print(f"Не удалось найти координаты для города {city}.")

    print(f"Самый южный город: {res}")

findSouthCity(["Москва", "Сочи", "Воронеж"])
