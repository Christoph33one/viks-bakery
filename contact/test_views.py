from django.test import TestCase, Client
from django.urls import reverse


class TestContactViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_url = reverse('contact')

    def test_contact_GET(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('contact.html')
