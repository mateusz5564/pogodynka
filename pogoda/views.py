from django.shortcuts import render
from django.utils import timezone
from .models import Post
import datetime
import requests



def index(request):
    return render(request, 'pogoda\index.html')

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):

    city = request.GET['q']
    city = str(city).capitalize()
    print(city)
    print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
    try:
        city_weather = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + city + ',pl&appid=824a9043fdbd8f369532b5cb6320c78b').json()

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

        print("____________________________________________________-----------________________")
        print(city_weather)

        #OSOBNE DNI
        dni = [[], [], [], [], [], []]
        dniindex = 0


        for x in range(0, len(pogoda)-1):
            if pogoda[0]['dt_txt'].split(" ")[0] != pogoda[1]['dt_txt'].split(" ")[0]:
                weather = {
                    'city': city,
                    'temperature': pogoda[x]['temperature'],
                    'description': pogoda[x]['description'],
                    'icon': pogoda[x]['icon'],
                    'wind_speed': pogoda[x]['wind_speed'],
                    'clouds': pogoda[x]['clouds'],
                    'day_name': datetime.datetime.strptime(pogoda[x]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A"),
                    'data': pogoda[x]['dt_txt'].split(" ")[0],
                    'godzina': pogoda[x]['dt_txt'].split(" ")[1],
                }
                dni[dniindex].append(weather)
                dniindex +=1
            elif pogoda[x]['dt_txt'].split(" ")[0] == pogoda[x+1]['dt_txt'].split(" ")[0]:
                weather = {
                    'city': city,
                    'temperature': pogoda[x]['temperature'],
                    'description': pogoda[x]['description'],
                    'icon': pogoda[x]['icon'],
                    'wind_speed': pogoda[x]['wind_speed'],
                    'clouds': pogoda[x]['clouds'],
                    'day_name': datetime.datetime.strptime(pogoda[x]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A"),
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
                    'day_name': datetime.datetime.strptime(pogoda[x]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A"),
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
                    'day_name': datetime.datetime.strptime(pogoda[x+1]['dt_txt'].split(" ")[0], "%Y-%m-%d").strftime("%A"),
                    'data': pogoda[x+1]['dt_txt'].split(" ")[0],
                    'godzina': pogoda[x+1]['dt_txt'].split(" ")[1],
                }
                dni[dniindex].append(weather)
        return render(request, 'pogoda\pogodamiasto.html', {'dni': dni, 'city': city})
    except:
        msg = "Nie znaleziono lokalizacji: "
        return render(request, 'pogoda\pogodamiasto.html', {'city': city, 'msg': msg})





def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'pogoda\post_list.html', {'posts': posts})

