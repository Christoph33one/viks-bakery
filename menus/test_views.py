from django.test import TestCase


# Testing if view renders the index.html template. TEST PASSED
# Command to run test : python3 manage.py test blog.test_views
# To test class: run python3 manage.py test TestView
class TestViews(TestCase):
    def get_home_page(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'menus/index.html')
