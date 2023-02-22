from django.test import TestCase


class TestViews(TestCase):

    # Testing if all html templates render in views.py - all three tests pass
    def test_all_menus(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_choc_cake_menu(self):
        response = self.client.get('choc_cake.html')

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        # why is it passing with the render of 404?

    def test_choc_cake_menu(self):
        response = self.client.get('cream_cake.html')

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_choc_cake_menu(self):
        response = self.client.get('cheese_cake.html')

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')








# Command to run test : python3 manage.py test blog.test_views
