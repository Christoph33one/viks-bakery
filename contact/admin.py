from django.contrib import admin
from .models import Contact
# from .forms import ContactForm


# Display Contact model in admin.py
@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email',
        'message', 'created_on',
        'approved', 'not_approved'
        )


# @admin.register(ContactForm)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message', 'date', 'subject',)
