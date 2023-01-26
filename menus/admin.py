from django.contrib import admin
from .models import CakeItem


@admin.register(CakeItem)
class CakesAdmin(admin.ModelAdmin):

    list_filter = ('on_menu', 'updated_on')
    list_display = ('cake_name', 'on_menu')
