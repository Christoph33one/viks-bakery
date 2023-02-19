from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm


# Contact form
def Contact(request):
    context = {'form': ContactForm()}
    # form has been submitted
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # form is valid
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # render email to MailTrap.io
            html = render_to_string('email.html', {
                'name': name,
                'email': email,
                'message': message
            })
            send_mail('The contact form subject', 'We have your message', 'noreply@viktorija.com', ['viktorija.com'], html_message=html)
            # send form to admin user
            form.save()
            # send a reply message to the user
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us, one of our staff will be in "
                "touch with you")
            return redirect('index')
        else:
            message.add_message(
                request,
                messages.ERROR,
                "Something is wrong")
            return redirect(handle_not_found)

    return render(request, 'contact.html', context)


def handle_not_found(request, exception):
    return render(request, '404.html')
