from django.shortcuts import render
from .models import Customer
# from django.http import HttpResponse


def ContactFrom(request):
    """
    Returns contact form
    """

    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("THANKS FOR CONTACING US!")
    return render(request, 'contact.html')
