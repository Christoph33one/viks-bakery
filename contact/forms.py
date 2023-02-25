from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    name = forms.CharField(label='Your full name', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50)
    message = forms.CharField(label='Add your message', widget=forms.Textarea)
