from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant.html/', views.restaurant, name='restaurant'),
    path('choc_cake/', views.CakesMenu.as_view(), name='choc_cake'),

]
