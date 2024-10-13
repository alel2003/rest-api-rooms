from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField()
    room_type = models.CharField(max_length=30)
    price = models.FloatField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.room_type.upper()} {self.number}"
    

class Booking(models.Model):
    room  = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.room} {self.user}"