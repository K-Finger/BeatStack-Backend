import json
from rest_framework.test import APITestCase
from django.urls import reverse

class GenerateTagsTestCase(APITestCase):
    def test_generate_tags_success(self):
        url = reverse('generate_tags')
        data = {
            'title': 'Free Gunna Type Beat 2024 | Emotional Trap Instrumental'
        }

        response = self.client.post(url, data, format='json')
        json_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('tags', json_data)
        self.assertIn('gunna', json_data['tags'])

    