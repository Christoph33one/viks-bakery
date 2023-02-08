from django.contrib import admin
from .models import Contact


# Display Contact model in admin.py
@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email',
        'message', 'created_on',
        'read', 'not_read'
        )
