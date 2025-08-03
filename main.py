from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    global map_url
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng},\n Страна: {country},\n Регион: {region}",
                    "map_url": osm_url
                        }
            else:
                return {
                    "coordinates": f"Широта: {lat}, Долгота: {lng},\n Страна: {country}",
                    "map_url": osm_url
                        }

        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка {e}"


def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result= get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
    map_url = result['map_url']


def show_map():
    if map_url:
        webbrowser.open(map_url)


key = 'c3ecd8694f8240e5a339af13f133a19b'
map_url = None

root = Tk()
root.title("Координаты городов")
root.geometry("350x160")

entry = Entry(root)
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(root, text="Введите город и нажмите на кнопку")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

root.mainloop()
