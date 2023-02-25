from django.test import TestCase, Client
from django.urls import reverse


class TestCakeMenusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.cakes_menu_url = reverse('choc_cake')
        self.cream_cake_url = reverse('cream_cake')
        self.cheese_cake_menu_url = reverse('cheese_cake')

    def test_menus_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'index_url')

    def test_choc_cake_menus_GET(self):
        response = self.client.get(self.cakes_menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'choc_cake.html')

    def test_cream_cake_menus_GET(self):
        response = self.client.get(self.cheese_cake_menu_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cheese_cake.html')
