from django import forms
from .models import CakeItem, CreamCakes, CheeseCakes


class CakeItemForm(forms.ModelForm):
    """
    Retrieves model objects for editing cake menu
    excuding image object
    """
    class Meta:
        model = CakeItem
        exclude = ['featured_image']


class CreamCakesForm(forms.ModelForm):
    """
    Retrieves all model objects for editing cake menu
    excuding image object
    """
    class Meta:
        model = CreamCakes
        exclude = ['featured_image']


class CheeseCakesForm(forms.ModelForm):
    """
    Retrieves all model objects for editing cake menu
    excuding image object
    """
    class Meta:
        model = CheeseCakes
        exclude = ['featured_image']
