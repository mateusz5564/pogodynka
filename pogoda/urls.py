from django.urls import path

from . import views

urlpatterns = [
    path('sss', views.mapa, name='mapa'),
    path('post', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
    path('', views.pogodamiasto, name='pogodamiasto'),
]
