from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm


# Contact and booking form
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
