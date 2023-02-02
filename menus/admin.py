from django.contrib import admin
from .models import CakeItem, CreamCakes, CheeseCakes


# view for chocolate cakes
@admin.register(CakeItem)
class CakesAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'cake_selections', 'on_menu')


# view for cream cakes
@admin.register(CreamCakes)
class CreamAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'cake_selections', 'on_menu')


# view for cheese cakes
@admin.register(CheeseCakes)
class CheeseCakeAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'cake_selections', 'on_menu')
