from django.shortcuts import render

# Create your views here.
from django.views import generic


def index(request):
    """ Return homepage """
    return render(request, 'index.html')


def restaurant(request):
    """ Returs restaurant page """
    return render(request, 'restaurant.html')
