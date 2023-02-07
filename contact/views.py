from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from .forms import ContactForm


# Contact and booking tabel
def Contact(request):
    context = {'form': ContactForm()}
    if request.method == "POST":
        return HttpResponse("THANKS FOR CONTACING US!")

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
