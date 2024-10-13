from django.urls import reverse
from rest_framework import status
from api.tests.api.test_api import TestAPI


class TestApiRoom(TestAPI):
    def test_room_get(self):
        url = reverse('rooms')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)
