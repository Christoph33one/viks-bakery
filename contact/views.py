from django.shortcuts import render
# from .models import contact


# Create your views here.
def contact(request):
    return render(request, 'contact.html')
