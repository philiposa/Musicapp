from django.test import SimpleTestCase
from django.urls import reverse, resolve


class SimpleTestViews(SimpleTestCase):

    def test_podcast_url(self):
        url = reverse('get_podcast')
        self.assertEqual(resolve(url).route, 'podcast/')

    def test_episode_url(self):
        url = reverse('get_episode')
        self.assertEqual(resolve(url).route, 'episode/')

    def test_detail_url(self):
        url = reverse('detail', args=[1])
        self.assertEqual(resolve(url).route, 'music/<int:album_id>')

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).route, 'music/')

