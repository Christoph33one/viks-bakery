from django.test import TestCase


class TestViews(TestCase):

    # Testing if index.html template renders in views.py  TEST PASSED
    def test_all_menus(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_choc_cake_menu(self):
        response = self.client.get('/choc_cake.html')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'choc_cake.html')








# Command to run test : python3 manage.py test blog.test_views
