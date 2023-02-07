from . import views
from django.urls import path


urlpatterns = [
    path('contact/', views.Contact, name='contact'),
]
