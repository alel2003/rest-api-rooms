from rest_framework import serializers
from .models import Room, Booking


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "room", "start_date", "end_date", "created_at", "is_delete"]