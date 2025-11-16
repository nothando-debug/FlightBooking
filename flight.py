from passenger import Passenger
from exceptions import FlightFullError
class Flight:
    def __init__(self, flight_number, origin, destination, capacity = 5):
   
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.booked_passengers = []
        self.available_seats = capacity

    def add_booking(self, passenger):
        if self.is_full() == False:
            self.booked_passengers.append(passenger)
        else:
            raise FlightFullError
        
        if passenger in self.booked_passengers:
            self.available_seats -= 1

    def is_full(self):
        if len(self.booked_passengers) >= self.capacity:
            return True
        elif self.capacity > len(self.booked_passengers):
            return False

    def __eq__(self, other):

        return(
            isinstance(other, self.__class__)
            and self.flight_number == other.flight_number
        )     
       
    def __str__(self):
       
        return f"Flight number: {self.flight_number}, From: {self.origin}, To: {self.destination}, Seats: {self.available_seats}"
    
# f = Flight("ER202", "South Africa", "Nairobi", capacity = 4)
# print(f)



        
        
