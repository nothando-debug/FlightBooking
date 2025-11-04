import unittest
from booking_system import BookingSystem
from flight import Flight
from passenger import Passenger

class TestBookingSystem(unittest.TestCase):
    """Integration tests for BookingSystem."""

    def setUp(self):
        self.sys = BookingSystem()
        self.sys.add_flight("FL1", "Cape Town", "Johannesburg", capacity=2)
        self.sys.add_flight("FL2", "Johannesburg", "Nairobi", capacity=3)
        self.sys.register_passenger("Nothando", "PA1")
        self.sys.register_passenger("Paris", "PB1")

    def test_add_and_find_flight(self):
        f = self.sys.find_flight("FL1")
        self.assertIsNotNone(f)
        self.assertEqual(f.flight_number, "FL1")

    def test_make_booking_and_manifest(self):
        self.sys.make_booking("FL1", "PA1")
        manifest = self.sys.get_passenger_manifest("FL1")
        self.assertTrue(any(p.passport_number == "PA1" for p in manifest))

    def test_prevent_double_booking_system_level(self):
        self.sys.make_booking("FL2", "PA1")
        with self.assertRaises(Exception):
            self.sys.make_booking("FL2", "PA1")

    def test_cancel_booking_removes_references(self):
        self.sys.make_booking("FL1", "PA1")
        self.sys.cancel_booking("FL1", "PA1")
        manifest = self.sys.get_passenger_manifest("FL1")
        self.assertFalse(any(p.passport_number == "PA1" for p in manifest))

    def test_iter_and_len_over_bookings(self):
        self.sys.make_booking("FL1", "PA1")
        self.sys.make_booking("FL2", "PB1")
        self.assertEqual(len(self.sys), 2)
        items = list(iter(self.sys))
        self.assertEqual(len(items), 2)

    def test_str_summary(self):
        s = str(self.sys)
        self.assertIn("flights", s.lower())
        self.assertIn("passengers", s.lower())
