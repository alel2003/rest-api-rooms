from django.contrib import admin
from .models import Room, Booking


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
