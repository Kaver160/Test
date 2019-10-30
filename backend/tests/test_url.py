from django.test import SimpleTestCase
from django.urls import reverse, resolve
from backend.app.views import AllTwit, PostView, Like

class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AllTwit)

    def test_posts_url_is_resolved(self):
        url = reverse('posts')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostView)

    def test_like_url_is_resolved(self):
        url = reverse('like')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Like)