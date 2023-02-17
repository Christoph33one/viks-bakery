from django.contrib import admin
from .models import Contact


# Admin contact from / taking contact model
@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = (
        'name', 'email',
        'message', 'created_on',
        'read', 'not_read'
        )
