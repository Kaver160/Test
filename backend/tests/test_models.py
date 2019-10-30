from django.test import TestCase
from backend.app.models import Post

class TestModels(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            user_id = 1,
            text= 'Привет',
        )
    def test_post_models(self):
        self.assertEquals(self.post1.text, 'Привет')