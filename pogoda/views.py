from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'pogoda\index.html')

def mapa(request):
    return render(request, 'pogoda\mapa.html')

def pogodamiasto(request):
    return render(request, 'pogoda\pogodamiasto.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'pogoda\post_list.html', {'posts': posts})

