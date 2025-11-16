
class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
        self.bookings = []

    def add_booking(self, flight):
        self.bookings.append(flight)

    def cancel_booking(self, flight):
        self.bookings.remove(flight)

    def __eq__(self, other):

        return(
            isinstance(other, self.__class__)
            and self.passport_number == other.passport_number
        )
    @property
    def total_bookings(self):
        return len(self.bookings)
    
             
    def __repr__(self):
        return f"{self.name}, {self.passport_number}"


       