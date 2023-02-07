from django.contrib import admin
from .models import Contact
# from .forms import ContactForm


@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_on')


# @admin.register(ContactForm)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message', 'date', 'subject',)
