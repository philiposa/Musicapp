from django.test import TestCase, Client
from django.urls import reverse
from .models import Album, Podcast, Episode
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .serializer import PodcastSerializer, EpisodeSerializer
from rest_framework.test import APIRequestFactory


class TestViews(TestCase):

    def test_index_GET(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/index.html')

    def test_detail_GET(self):
        client = Client()
        response = client.get(reverse('detail', Album.album_id))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'music/detail.html')





