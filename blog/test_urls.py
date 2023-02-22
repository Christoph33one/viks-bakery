from django.test import TestCase
from django.urls import reverse, resolve
from .views import PostList, PostDetail, PostLike


class TestUrls(TestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func.view_class, PostList)

    # def test_like_url_is_resolved(self):
    #     url = reverse('post_like')
    #     self.assertEquals(resolve(url).func.view_class, PostLike)

    # def test_like_url_is_resolved(self):
    #     url = reverse('post_datail')
    #     self.assertEquals(resolve(url).func.view_class, PostDetail)


