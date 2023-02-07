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






# def Contact_form_view(request):
#     """
#     Returns contact form
#     """

#     if request.method == "POST":
#         contact = Contact()
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         contact.name = name
#         contact.email = email
#         contact.message = message
#         # contact.save()
#
#     return render(request, 'contact.html')
