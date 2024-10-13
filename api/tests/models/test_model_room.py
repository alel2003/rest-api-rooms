from api.tests.test_setup import TestSetup
from api.models import Room


class TestModelRoom(TestSetup):
    def test_create_room(self):
        self.room_data = Room.objects.create(
            number=2,
            room_type="TEST ROOM TWO",
            price=30.0,
        )

    def test_room_data_str(self):
        self.assertEqual(str(self.main_room), "TEST ROOM ONE 1")

    def test_room_update(self):
        room_to_update = Room.objects.get(pk=self.main_room.pk)
        room_to_update.is_available = True
        room_to_update.save()
        self.assertEqual(room_to_update.is_available, True)

    def test_room_get(self):
        received_room = Room.objects.get(pk=self.main_room.pk)
        self.assertEqual(received_room, self.main_room)

    def test_room_delete(self):
        room_to_delete = Room.objects.get(pk=self.main_room.pk)
        room_to_delete.delete()

        with self.assertRaises(Room.DoesNotExist):
            Room.objects.get(pk=self.main_room.pk)
