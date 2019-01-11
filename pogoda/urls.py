from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='mapa'),
    path('post/', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
]
