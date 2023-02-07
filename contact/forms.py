from django import forms
from datetime import datetime
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date', 'subject']
    
    INQURIES_CHOICE = (
        (1, "General enquiries "),
        (2, "Booking a tabel"),
    )

    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    time = forms.TimeField()  # not working in admin panel?
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))

    subject = forms.ChoiceField(
        choices=INQURIES_CHOICE,
        widget=forms.RadioSelect()
    )
