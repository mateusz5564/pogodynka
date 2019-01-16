from django.urls import path

from . import views

urlpatterns = [
    path('mapa', views.mapa, name='mapa'),
    path('post', views.post_list, name='post_list'),
    path('', views.pogodamiasto, name='pogodamiasto'),
]
