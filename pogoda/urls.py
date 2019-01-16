from django.urls import path

from . import views

urlpatterns = [
    path('', views.mapa, name='mapa'),
    path('pogodamiasto', views.pogodamiasto, name='pogodamiasto'),
]
