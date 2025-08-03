from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)

    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"


key = 'c3ecd8694f8240e5a339af13f133a19b'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")
