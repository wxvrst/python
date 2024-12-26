import requests

def find_nearest(address):
    geocodeUrl = "https://geocode-maps.yandex.ru/1.x/"
    geocodeParams = {
        "geocode": address,
        "format": "json",
        "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
    }
    response = requests.get(geocodeUrl, params=geocodeParams).json()

    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    except (KeyError, IndexError):
        print("Не удалось найти координаты для данного адреса")
        return

    coords = tuple(map(float, point.split()))
    print(f"Координаты адреса: {coords}")

    searchUrl = "https://search-maps.yandex.ru/v1/"
    searchParams = {
        "apikey": "6c058cdf-afa0-40e6-8d9f-740452796714",
        "text": "аптека",
        "ll": f"{coords[0]},{coords[1]}",
        "type": "biz",
        "lang": "ru_RU",
        "results": 5,
    }
    searchResponse = requests.get(searchUrl, params=searchParams).json()

    if 'features' in searchResponse and searchResponse['features']:
        pharmacy = searchResponse['features'][0]
        name = pharmacy['properties']['CompanyMetaData']['name']
        address = pharmacy['properties']['CompanyMetaData'].get('address', 'Адрес не указан')
        print(f"Ближайшая аптека: {name}, адрес: {address}")
    else:
        print("Аптеки поблизости не найдены")

address = input("Введите адрес: ")
find_nearest(address)
