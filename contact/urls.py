from . import views
from django.urls import path


urlpatterns = [
    path('contact/', views.Contact, name='contact'),
    # path('return_contact', views.ReturnContact, name='return_contact'),
]
