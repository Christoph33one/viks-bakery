from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import CakeItem


def index(request):
    """ Return homepage """
    return render(request, 'index.html')
