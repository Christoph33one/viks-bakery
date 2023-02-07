from django import forms


class ContactForm(forms.Form):

    INQURIES_CHOICE = (
        (1, "General enquiries "),
        (2, "Booking a tabel"),
    )

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    subject = forms.ChoiceField(
        choices=INQURIES_CHOICE,
        widget=forms.RadioSelect()
    )


class Meta:
    ordering = ['subject']

    def __str__(self):
        return self.name


# from .models import Contact
# from django import forms


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact()
#         fields = '__all__'
