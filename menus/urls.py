from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant.html/', views.restaurant, name='restaurant'),
]
