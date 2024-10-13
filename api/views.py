from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import RoomSerializers, BookingSerializers
from .models import Booking, Room

class AuthRequiredMixin:
    permission_classes = [IsAuthenticated]


class ListRoom(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class ListBooking(AuthRequiredMixin, generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers


class CreateBooking(AuthRequiredMixin, generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailsBookingDelete(AuthRequiredMixin, generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
