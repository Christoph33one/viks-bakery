from django.contrib import admin
from .models import CakeItem, CreamCakes


# Register your models here.
@admin.register(CakeItem)
class CakesAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'cake_selections', 'on_menu')


@admin.register(CreamCakes)
class CreamAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'cake_selections', 'on_menu')
