from django.test import TestCase
from .forms import ContactForm


class TestItem(TestCase):

    def test_item_name_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_form_email_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
