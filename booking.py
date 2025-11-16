from passenger import Passenger
from flight import Flight

class Booking:
    def __init__(self, passenger, flight):
        self.status = ""
        self.passenger = passenger
        self.flight = flight
      

    def confirm(self):
        if self.status == "Confirmed":
            raise Exception
        self.passenger.add_booking(self.flight)
        self.flight.add_booking(self.passenger)
        self.status = "Confirmed"


    def cancel(self):
        self.passenger.cancel_booking(self.flight)
        self.flight.booked_passengers.remove(self.passenger)
        self.status = "Cancelled"

    def __str__(self):
        return f"{self.passenger}, {self.flight}, {self.status}"





