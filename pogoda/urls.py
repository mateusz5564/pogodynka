from django.urls import path

from . import views

urlpatterns = [
    path('', views.mapa, name='mapa'),
    path('post', views.post_list, name='post_list'),
    path('pogodamiasto', views.pogodamiasto, name='pogodamiasto'),
]
