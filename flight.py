class Flight:
    def __init__(self, origin, destination):
        self.flight_number = "NF101"
        self.origin = origin
        self.destination = destination
        self.capacity = 0
        self.booked_passengers = []