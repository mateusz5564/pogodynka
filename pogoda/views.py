from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests

def index(request):
    return render(request, 'pogoda\index.html')

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):
    condition = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Warsaw,pl&appid=824a9043fdbd8f369532b5cb6320c78b')

    condition.__str__()

    print("paweł nie pulluje z gita")

    return render(request, 'pogoda\pogodamiasto.html', {'condition' : condition})




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'pogoda\post_list.html', {'posts': posts})

