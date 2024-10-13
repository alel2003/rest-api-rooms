from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Room


class TestAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuserapi", password="password"
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {str(refresh.access_token)}")

        self.main_room = Room.objects.create(
            number=3,
            room_type="TEST API",
            price=90.0,
        )
