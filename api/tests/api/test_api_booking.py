from django.urls import reverse
from rest_framework import status
from api.tests.api.test_api import TestAPI
from datetime import datetime,  timedelta

from api.models import Booking


class TestApiRoom(TestAPI):
    def setUp(self):
        super().setUp()
        self.main_booking = Booking.objects.create(
            user = self.user,
            room=self.main_room,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=2),
        )

        self.json_booking_post = {
            "room": self.main_room.id,
            "start_date": "2015-08-22 14:45:09",
            "end_date": "2015-08-23 17:45:09",
        }

        self.json_booking_delete = {
            "is_delete": True
        }

    def test_booking_get(self):
        url = reverse('bookings')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_booking_create(self):
        url = reverse('create-bookings')
        response = self.client.post(url, self.json_booking_post, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["room"], self.json_booking_post["room"])

    def test_booking_details_delete(self):
        url = reverse('bookings-details', args=[self.main_booking.id])
        response = self.client.patch(url, self.json_booking_delete, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)