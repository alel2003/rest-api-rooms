from django.urls import path
from .views import ListRoom, ListBooking, CreateBooking, DetailsBookingDelete

urlpatterns = [
    path('rooms/', ListRoom.as_view(), name='rooms'),
    path('bookings/', ListBooking.as_view(), name='bookings'),
    path('books/', CreateBooking.as_view(), name='create-bookings'),
    path('bookings/<int:pk>/', DetailsBookingDelete.as_view(),
         name='bookings-details'),
]
