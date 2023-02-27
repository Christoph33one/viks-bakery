from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Post, Comment


# class TestPostModel(TestCase):

#     def testSetUp(self):
#         self.user = User.objects.create_user(
#             username="admin", email="admin@admin.com", password="Y179dcv34"
#         )
#         self.post = Post.objects.create(
#             title="Test title",
#             content="Test content",
#         )

class TestPostModel(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test title',
            # email='Test email',
            # message='Test message'
        )

    def test_post_name(self):
        testname = get_object_or_404(Contact, name="Test title ")

        self.assertEqual(self.contact.created_on, testtitle.created_on)
