from django.test import TestCase


class TestViews(TestCase):

    def test_views(self):
        response = self.client.get('404.html')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
