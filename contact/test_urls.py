from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import Contact


class TestContact(SimpleTestCase):

    def test_contact_form_urls(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, Contact)
