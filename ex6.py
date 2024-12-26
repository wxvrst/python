import folium
import random
import requests
cities = ["Москва", "Санкт-Петербург", "Казань", "Сочи"]
def getCoordinates(city):
    geocodeUrl = "https://geocode-maps.yandex.ru/1.x/"
    geocodeParams = {
        "geocode": city,
        "format": "json",
        "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
    }
    response = requests.get(geocodeUrl, params=geocodeParams).json()
    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = tuple(map(float, point.split()))
        return coords
    except (KeyError, IndexError):
        print(f"Не удалось получить координаты для города {city}")
        return None

def createCityMap(coords, filename="city_map.html"):
    cityMap = folium.Map(location=[coords[0], coords[1]], zoom_start=12)

    folium.Marker(location=[coords[0], coords[1]]).add_to(cityMap)

    cityMap.save(filename)
    print(f"Карта города сохранена в файл {filename}")

def guessTheCity():
    random.shuffle(cities)

    for city in cities:
        print(f"Угадай город!")

        coords = getCoordinates(city)
        if not coords:
            continue

        createCityMap(coords, f"?_map.html")

        input("Нажмите Enter, чтобы увидеть следующий город")

        userGuess = input("Введите ваш ответ: ").strip()
        if userGuess.lower() == city.lower():
            print("Правильный ответ!")
        else:
            print(f"Неправильно! Это был {city}")

guessTheCity()
