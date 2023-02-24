# from django.test import TestCase
# from django.shortcuts import get_object_or_404
# from .models import Post, Comment


# class TestPostModel(TestCase):

#     def testSetUp(self):
#         self.user = User.objects.create_user(
#             username="admin", email="admin@admin.com", password="Y179dcv34"
#         )
#         self.post = Post.objects.create(
#             title="Test title",
#             content="Test content",
#         )

#         def test_post_create_on(self):
#             post = get_object_or_404(Post, title="Test post title")

#             self.assertEqual(self.post.content, "Test content")

#             self.assertNotEqual(self.post.content, "no content")

#             self.assertEqual(self.post.title, "Test post title")

#             self.assertEqual(self.post.created_on, testpost.created_on)

        # def test_comment_added(self):
        #     post = get_object_or_404(Post, title="test comment title")
        #     self.comment = Comment.objects.get.create(
        #         post=post, body="I have added a comment!"
        #     )
        #     self.assertEqual(self.comment.body, "I have added a comment!")

        #     self.assertNotEqual(self.comment.body, "I have not added this comment!")

        #     self.assertIsNotNone(self.comment.created_on)

