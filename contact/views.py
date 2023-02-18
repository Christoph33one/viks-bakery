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

# To give users contact message and render it to reutrn_contact.html
# class ReturnContact(request):
#     model = Contact()
#     queryset = Contact().objects.all().order_by('-read')
#     template_name = 'return_contact.html'
#     paginate_by = 3

