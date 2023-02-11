from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm


# Contact form
def Contact(request):
    context = {'form': ContactForm()}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send form to admin user
            form.save()

        return HttpResponse(
            "<H1><a href="">THANKS FOR CONTACTING US!</a></H1>")

    return render(request, 'contact.html', context)


# NOTES

# user to update and delete their details. This updates the customer model
# SEND AN EMAIL TO THE USER?
# HAVE A MESSAGE THAT TELLS THE USER THAT THEIR MESSAGE HAS BEEN SENT. JAVASCRIPT???
# ASK WHAT ELSE TO ADD FOR THE FORM? IMPORTANT!!!