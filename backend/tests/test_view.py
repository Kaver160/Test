# from django.db import connection
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from backend.app.models import Post
from django.test import TestCase, Client
from django.urls import reverse
from backend.app.models import Post
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.posts_url = reverse('posts')
        self.home_url = reverse('home')
        self.post1 = Post.objects.create(
            user_id= 2,
            text = 'Привет',
        )
    def test_post_view_posts_GET(self):
        responce = self.client.get(self.posts_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'app/index2.html')
    def test_all_twit_home_GET(self):
        responce = self.client.get(self.home_url)
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'app/index.html')
    def test_post_view_posts_POST(self):
            responce = self.client.post(self.posts_url,{
                # 'User':'1',
                # # "text":'Как ты',
            })
            self.assertEquals(responce.status_code, 200)
            self.assertEquals(self.post1.user_id,2)
    # def test_post_view_posts_POST_no_data(self):
    #     responce = self.client.post(self.posts_url)
    #     self.assertEquals(responce.status_code, 200)
    # #     self.assertEquals(self.post1.count(),  )
    # def test_post_view_posts_POST(self):
    #     responce = self.client.post(self.posts_url, {
    #         'User': 1,
    #         'user_id': 3,
    #         'text': 'Ghbdsd'
    #     })
    #     post2 = Post.objects.get(id=1)
    #     self.assertEquals(post2.user_id, 3)

