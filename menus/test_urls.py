from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menus.views import index, CakesMenu, CreamMenu, CheeseCakeMenu


class TestMenusUrls(SimpleTestCase):

    def Test_cake_menu_urls_reverse(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def Test_choc_cake_menu_urls_reverse(self):
        url = reverse('choc_cake')
        self.assertEquals(resolve(url).func.view_class, CakesMenu)

    def Test_cream_cake_menu_urls_reverse(self):
        url = reverse('cream_cake')
        self.assertEquals(resolve(url).func.view_class, CreamMenu)

    def Test_cheese_cake_menu_urls_reverse(self):
        url = reverse('cheese_cake')
        self.assertEquals(resolve(url).func.view_class, CheeseCakeMenu)

    # def Test_cake_menu_urls_reverse(self):
    #     url = reverse('404')

    #     self.assertEquals(resolve(url).func, 404)
