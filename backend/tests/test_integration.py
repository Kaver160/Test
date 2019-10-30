from rest_framework import status
from rest_framework.test import APIClient
import unittest
from backend.app.models import Post
from django.urls import reverse

class TestModelApi(unittest.TestCase):
        def setUp(self):
            self.client = APIClient()

        def test_Post_list(self):
            responce = self.client.get(reverse('posts'))
            self.assertEquals(responce.status_code, status.HTTP_200_OK)
