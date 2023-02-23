from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import PostList, PostDetail, PostLike


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_like_url_is_resolved(self):
        url = reverse('post_like', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail', args=['some-slugs'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)
