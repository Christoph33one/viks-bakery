from django import forms
from .models import CakeItem, CreamCakes, CheeseCakes


class CakeItemForm(forms.ModelForm):
    class Meta:
        model = CakeItem
        fields = '__all__'


class CreamCakesForm(forms.ModelForm):
    class Meta:
        model = CreamCakes
        fields = '__all__'


class CheeseCakesForm(forms.ModelForm):
    class Meta:
        model = CheeseCakes
        fields = '__all__'
