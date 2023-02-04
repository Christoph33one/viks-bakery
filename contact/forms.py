from django import forms


class ContactForm(form.Forms):
    """Contact form for user to submit an enquiry"""
    name = forms.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return self.name
