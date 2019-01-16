from django.urls import path

from . import views

urlpatterns = [
    path('sss', views.mapa, name='mapa'),
    path('post', views.post_list, name='post_list'),
    path('', views.index, name='index'),
    path('pogodamiasto', views.pogodamiasto, name='pogodamiasto'),
]
