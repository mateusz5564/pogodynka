from django.shortcuts import render
from django.utils import timezone
from .models import Post

from yweather import yweather

def index(request):
    return render(request, 'pogoda\index.html')

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('dublin')
    condition = location.condition
    condition = condition.text

    return render(request, 'pogoda\pogodamiasto.html', {'condition', condition})




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'pogoda\post_list.html', {'posts': posts})

