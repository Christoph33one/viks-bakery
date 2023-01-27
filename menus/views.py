from django.shortcuts import render
from django.views import generic
from .models import CakeItem

# Create your views here.


# Render index.html
def index(request):
    """ Return homepage """
    return render(request, 'index.html')


def cakes_menu(request):
    """ Returs restaurant page """
    return render(request, 'cake_menu.html')


# Render restaurant.html
def restaurant(request):
    """ Returs restaurant page """
    return render(request, 'restaurant.html')


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
            'white_items': CakeItem.objects.all().filter(
                on_menu=True, cake_selections=0),
            'dark_items': CakeItem.objects.all().filter(
                on_menu=True, cake_selections=1)
        }
        return queryset
