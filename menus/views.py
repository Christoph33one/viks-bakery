from django.shortcuts import render
from django.views import generic
from .models import CakeItem, CreamCakes

# Create your views here.


# Render index.html
def index(request):
    """ Return homepage """
    return render(request, 'index.html')


# Render restaurant.html
def restaurant(request):
    """ Returs restaurant page """
    return render(request, 'restaurant.html')


# Render cake_menu.html
def cakes_menu(request):
    """ Returs cake menu page """
    return render(request, 'cake_menu.html')


# Generic view for chocale cake menu
class CakesMenu(generic.ListView):
    """
    To render the cake menus from the database
    """
    model = CakeItem
    template_name = 'choc_cake.html'
    context_object_name = 'cake_items'

    def get_queryset(self):

        queryset = {
            'choclate_items': CakeItem.objects.all().filter(
                on_menu=True, cake_selections=0),
            'vegan_items': CakeItem.objects.all().filter(
                on_menu=True, cake_selections=1)
        }
        return queryset


# Generic view for cream cakes menu
class CreamMenu(generic.ListView):
    """
    To render cream cake menu from the database
    """
    model = CreamCakes
    template_name = 'cream_cake.html'
    context_object_name = 'cream_cakes'

    def get_queryset(self):

        queryset = {
            'white_items': CreamCakes.objects.all().filter(
                on_menu=True, cake_selections=0),
            'vegan_items': CreamCakes.objects.all().filter(
                on_menu=True, cake_selections=1)
        }
        return queryset

    # def get_queryset(self):

    #     cakes = CakeItem.objects.all()

    #     return cakes

        # CakeItem.objects.all()
