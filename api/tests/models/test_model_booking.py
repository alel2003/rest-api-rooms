from datetime import datetime,  timedelta
from api.tests.test_setup import TestSetup
from api.models import Booking


class TestModelBooking(TestSetup):
    def test_create_booking(self):
        self.booking_data = Booking.objects.create(
            user = self.user,
            room=self.main_room,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=2),
        )

    def test_booking_data_str(self):
        print(self.main_booking)

    def test_booking_get(self):
        booking_to_update = Booking.objects.get(pk=self.main_booking.pk)
        self.assertEqual(booking_to_update, self.main_booking)

    def test_booking_update(self):
        booking_to_update = Booking.objects.get(pk=self.main_booking.pk)
        booking_to_update.is_delete = True
        booking_to_update.save()
        self.assertEqual(booking_to_update.is_delete, True)


    def test_booking_delete(self):
        booking_to_delete = Booking.objects.get(pk=self.main_booking.pk)
        booking_to_delete.delete()

        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(pk=self.main_booking.pk)