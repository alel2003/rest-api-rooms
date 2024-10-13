from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from datetime import datetime,  timedelta


from api.models import Room, Booking


class TestSetup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")

        self.main_room = Room.objects.create(
            number=1,
            room_type="TEST ROOM ONE",
            price=90.0,
        )

        self.main_booking = Booking.objects.create(
            user = self.user,
            room = self.main_room,
            start_date  = datetime.now(),
            end_date = datetime.now() + timedelta(days=2),
        )