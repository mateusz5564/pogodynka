from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests



def index(request):
    return render(request, 'pogoda\index.html')

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):

    city = "Warsaw"
    city_weather = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Warsaw,pl&appid=824a9043fdbd8f369532b5cb6320c78b').json()

    pogoda = []

    for x in range(0, len(city_weather['list'])):
        weather = {
            'city' : city,
            'temperature': city_weather['list'][x]['main']['temp'],
            'description': city_weather['list'][x]['weather'][0]['description'],
            'icon': city_weather['list'][x]['weather'][0]['icon'],
            'dt_txt': city_weather['list'][x]['dt_txt'],
        }
        pogoda.append(weather)

    print("SŁOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWNIK")
    print("dlugosc " + str(len(city_weather['list'])))
    print(pogoda)
    return render(request, 'pogoda\pogodamiasto.html', {'pogoda' : pogoda})




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'pogoda\post_list.html', {'posts': posts})

