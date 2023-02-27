from django.shortcuts import render, redirect
from django.views import generic
from .models import CakeItem, CreamCakes, CheeseCakes
from blog.models import Post
from django.conf import settings


# Render index.html
def index(request):
    """ Returns homepage """

    # import post_list from blog views and model to render in index.html
    post_list = Post.objects.all()

    return render(
        request,
        "index.html",
        {
            "post_list": post_list,

        }

    )


# Generic view to render chocolatecake.html
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


# Generic view to render creamcake.html
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


# Generic view to render cheesecake.html
class CheeseCakeMenu(generic.ListView):
    """
    To render cream cake menu from the database
    """
    model = CheeseCakes
    template_name = 'cheese_cake.html'
    context_object_name = 'cheese_cakes'

    def get_queryset(self):

        queryset = {
            'cheese_items': CheeseCakes.objects.all().filter(
                on_menu=True, cake_selections=0),
            'vegan_items': CheeseCakes.objects.all().filter(
                on_menu=True, cake_selections=1)
        }
        return queryset

