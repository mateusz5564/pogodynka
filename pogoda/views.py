from django.shortcuts import render
from django.utils import timezone
from .models import Post
import datetime
import requests

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):

    dni_tygodnia = {"Monday": "Poniedziałek", "Tuesday": "Wtorek", "Wednesday": "Środa", "Thursday": "Czwartek",
                    "Friday": "Piątek", "Saturday": "Sobota", "Sunday": "Niedziela"}

    if request.GET.get('q') is None:
        city = "Warszawa"
        city = str(city).capitalize()
    else:
        city = request.GET['q']
        city = str(city).capitalize()

    try:
        city_weather = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=824a9043fdbd8f369532b5cb6320c78b').json()

        pogoda = []

        for x in range(0, len(city_weather['list'])):
            weather = {
                'city' : city,
                'temperature': str(int(((city_weather['list'][x]['main']['temp'])-273.15))) + " °C",
                'description': city_weather['list'][x]['weather'][0]['description'],
                'icon': city_weather['list'][x]['weather'][0]['icon'],
                'wind_speed': str(city_weather['list'][x]['wind']['speed']) + " m/s",
                'clouds': str(city_weather['list'][x]['clouds']['all']) + "%",
                'dt_txt': city_weather['list'][x]['dt_txt'],
            }
            pogoda.append(weather)


        #OSOBNE DNI
        dni = [[], [], [], [], [], []]
        dniindex = 0


        for x in range(0, len(pogoda)-1):
            if pogoda[x]['dt_txt'].split(" ")[0] == pogoda[x+1]['dt_txt'].split(" ")[0]:
                weather = {
                    'city': city,
                    'temperature': pogoda[x]['temperature'],
                    'description': pogoda[x]['description'],
                    'icon': pogoda[x]['icon'],
                    'wind_speed': pogoda[x]['wind_speed'],
                    'clouds': pogoda[x]['clouds'],
                    'day_name': dni_tygodnia[datetime.datetime.strptime(pogoda[x]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A")],
                    'data': pogoda[x]['dt_txt'].split(" ")[0],
                    'godzina': pogoda[x]['dt_txt'].split(" ")[1],
                }
                dni[dniindex].append(weather)
            else:
                weather = {
                    'city': city,
                    'temperature': pogoda[x]['temperature'],
                    'description': pogoda[x]['description'],
                    'icon': pogoda[x]['icon'],
                    'wind_speed': pogoda[x]['wind_speed'],
                    'clouds': pogoda[x]['clouds'],
                    'day_name': dni_tygodnia[datetime.datetime.strptime(pogoda[x]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A")],
                    'data': pogoda[x]['dt_txt'].split(" ")[0],
                    'godzina': pogoda[x]['dt_txt'].split(" ")[1],
                }
                dni[dniindex].append(weather)
                dniindex += 1
            if x == len(pogoda)-2:
                weather = {
                    'city': city,
                    'temperature': pogoda[x+1]['temperature'],
                    'description': pogoda[x+1]['description'],
                    'icon': pogoda[x+1]['icon'],
                    'wind_speed': pogoda[x+1]['wind_speed'],
                    'clouds': pogoda[x+1]['clouds'],
                    'day_name': dni_tygodnia[datetime.datetime.strptime(pogoda[x+1]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A")],
                    'data': pogoda[x+1]['dt_txt'].split(" ")[0],
                    'godzina': pogoda[x+1]['dt_txt'].split(" ")[1],
                }
                dni[dniindex].append(weather)
        return render(request, 'pogoda\pogodamiasto.html', {'dni': dni, 'city': city})
    except:
        msg = "Nie znaleziono lokalizacji "
        return render(request, 'pogoda\pogodamiasto.html', {'city': city, 'msg': msg})


