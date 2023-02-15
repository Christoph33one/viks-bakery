from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm


# Contact form
def Contact(request):
    context = {'form': ContactForm()}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send form to admin user
            form.save()
            # send a reply message to the user
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us, one of our staff will be in "
                "touch with you")

    return render(request, 'contact.html', context)


# NOTES
# user to update and delete their details. This updates the customer model
# SEND AN EMAIL TO THE USER?
# ASK WHAT ELSE TO ADD FOR THE FORM? IMPORTANT!!!
