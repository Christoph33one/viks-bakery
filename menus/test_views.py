from django.test import TestCase
# from django.test import TestCase, Client


class TestViews(TestCase):

    def test_this_thing(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '/index.html')

# class TestMenusViews(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.menus_url = reverse('menus')
#         self.choc_cake_url = reverse('choc_cake')
#         self.cream_cake_url = reverse('cream_cake')
#         self.cheese_cake_url = reverse('cheese_cake')

#     def test_cake_menus_GET(self):

#         self.assertEquals(responce.status_code, 200)
#         self.assertTemplateNotUsed(response, 'cake_menu.html')



# Testing if view renders the index.html template. TEST PASSED
# Command to run test : python3 manage.py test blog.test_views
# To test class: run python3 manage.py test TestView
# class TestViews(TestCase):
#     def test_get_home_page(self):
#         responce = self.client.get('/')
#         self.assertEqual(responce.status_code, 200)
#         self.assertTemplateUsed(response, 'menus/index.html')
