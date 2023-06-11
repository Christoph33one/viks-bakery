from django.shortcuts import render, redirect
from django.views import generic
from .models import CakeItem, CreamCakes, CheeseCakes
from blog.models import Post
from django.conf import settings
from .forms import CakeItemForm, CreamCakesForm, CheeseCakesForm
from django.http import Http404
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Render index.html
def index(request):
    """ Returns homepage """
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
            'choclate_items': CakeItem.objects.filter(
                on_menu=True, cake_selections=0),
            'vegan_items': CakeItem.objects.filter(
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


def admin_user_check(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(admin_user_check, login_url="/accounts/login/")
def add_item(request, model):
    if model == 'cake_item':
        form = CakeItemForm(request.POST or None)
        redirect_url = 'choc_cake'
    elif model == 'cream_cake':
        form = CreamCakesForm(request.POST or None)
        redirect_url = 'cream_cake'
    elif model == 'cheese_cake':
        form = CheeseCakesForm(request.POST or None)
        redirect_url = 'cheese_cake'
    else:
        raise Http404("Invalid model name")

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "A new item has been added!"
            )
            return redirect(reverse(redirect_url))

    return render(request, 'add_menu.html', {'form': form, 'model': model})


@user_passes_test(admin_user_check, login_url="/accounts/login/")
def edit_item(request, model, pk):
    if model == 'cake_item':
        instance = get_object_or_404(CakeItem, pk=pk)
        form = CakeItemForm(request.POST or None, instance=instance)
        redirect_url = 'choc_cake'
    elif model == 'cream_cake':
        instance = get_object_or_404(CreamCakes, pk=pk)
        form = CreamCakesForm(request.POST or None, instance=instance)
        redirect_url = 'cream_cake'
    elif model == 'cheese_cake':
        instance = get_object_or_404(CheeseCakes, pk=pk)
        form = CheeseCakesForm(request.POST or None, instance=instance)
        redirect_url = 'cheese_cake'
    else:
        raise Http404("Invalid model name")

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your item has been edited"
            )
            return redirect(reverse(redirect_url))

    return render(request, 'edit_menu.html', {'form': form, 'model': model, 'pk': pk})


@user_passes_test(admin_user_check, login_url="/accounts/login/")
def delete_item(request, model, pk):
    if model == 'cake_item':
        instance = get_object_or_404(CakeItem, pk=pk)
    elif model == 'cream_cake':
        instance = get_object_or_404(CreamCakes, pk=pk)
    elif model == 'cheese_cake':
        instance = get_object_or_404(CheeseCakes, pk=pk)
    else:
        raise Http404("Invalid model name")

    if request.method == 'POST':
        instance.delete()
        messages.add_message(
            request, messages.SUCCESS, "Your item has been deleted"
        )
        return redirect(reverse('choc_cake'))

    return render(request, 'delete_menu.html', {'model': model, 'pk': pk})
