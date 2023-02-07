from . import views
from django.urls import path


urlpatterns = [
    path('contact/', views.Contact_form_view, name='contact'),
]
