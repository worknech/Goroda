from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return lat, lng
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


key = 'c3ecd8694f8240e5a339af13f133a19b'
city = 'Химки'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
