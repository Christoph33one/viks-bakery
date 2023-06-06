from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('choc_cake/', views.CakesMenu.as_view(), name='choc_cake'),
    path('cream_cake/', views.CreamMenu.as_view(), name='cream_cake'),
    path('cheese_cake/', views.CheeseCakeMenu.as_view(), name='cheese_cake'),
    path('edit_menu/<str:model>/<int:pk>/', views.edit_item, name='edit_menu'),

]
