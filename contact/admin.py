from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')
