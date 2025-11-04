
# Flight Booking Project
Your task is to implement a flight booking system with the following capabilities:

- Create **Flights** with capacities and destinations.  
- Register **Passengers** with unique identifiers.  
- Allow **Bookings** linking passengers to flights.  
- Manage the system via a **BookingSystem** class.  
- Handle errors and edge cases, like full flights or duplicate bookings.  

You will write code to pass the provided `unittest` tests, giving hands-on experience with Python OOP.



## 🧩 Classes and Responsibilities

### 1. `Flight`
- Represents a single flight.  
- Key attributes: `flight_number`, `origin`, `destination`, `capacity`, `booked_passengers`.  
- Key methods:
  - `add_booking(passenger)` → Adds a passenger; raises `FlightFullError` if full.  
  - `available_seats` (property) → Returns seats left.  
  - `__eq__` → Compares flights by `flight_number`.  
  - `__str__` → Human-readable summary including flight number and seats left.  
- **Concepts learned:** Encapsulation, dunder methods, exception handling, list management.

### 2. `Passenger`
- Represents a traveler.  
- Key attributes: `name`, `passport_number`, `bookings`.  
- Key methods:
  - `add_booking(flight)` → Adds a flight to passenger’s bookings.  
  - `cancel_booking(flight)` → Removes a flight from bookings.  
  - `total_bookings` (property) → Returns number of bookings.  
  - `__eq__` → Compares passengers by `passport_number`.  
  - `__repr__` → Debug-friendly string with name and passport.  
- **Concepts learned:** Properties, dunder methods, composition.

### 3. `Booking`
- Connects a `Passenger` to a `Flight`.  
- Key attributes: `passenger`, `flight`, `status`.  
- Key methods:
  - `confirm()` → Links passenger and flight; sets status to `Confirmed`.  
  - `cancel()` → Unlinks passenger and flight; sets status to `Cancelled`.  
  - `__str__` → Displays passenger, flight, and status.  
- **Concepts learned:** Composition, state management, dunder methods.

### 4. `BookingSystem`
- Manages all flights, passengers, and bookings.  
- Key methods:
  - `add_flight(...)` → Adds a flight.  
  - `register_passenger(...)` → Registers a new passenger.  
  - `make_booking(flight_number, passport_number)` → Creates and confirms a booking.  
  - `cancel_booking(flight_number, passport_number)` → Cancels a booking.  
  - `get_passenger_manifest(flight_number)` → Returns list of passengers on a flight.  
  - Iteration and `len()` support over active bookings.  
- **Concepts learned:** Aggregation, iteration, len(), system-level composition, exception handling.

### 5. `exceptions.py`
- Contains custom exceptions like `FlightFullError`.  
- Helps students learn **how to define and use custom exceptions**.

---

## 🧪 Tests

All functionality is verified via **unit tests**:

- `test_flight.py` → Tests flight creation, bookings, dunder methods, and capacity.  
- `test_passenger.py` → Tests passenger creation, booking management, and equality.  
- `test_booking.py` → Tests booking confirmation, cancellation, and linkage.  
- `test_booking_system.py` → Tests system-level operations, iteration, len, and manifests.  

**Purpose:** Students write code to pass these tests, learning **TDD and OOP in action**.  

---

## 📚 Python/OOP Concepts Covered

- **Classes and Objects** → Creating `Flight`, `Passenger`, `Booking`, `BookingSystem`.  
- **Composition/Aggregation** → Linking passengers to flights via bookings.  
- **Dunder Methods** → `__eq__`, `__str__`, `__repr__`.  
- **Properties** → `Passenger.total_bookings`, `Flight.available_seats`.  
- **Exception Handling** → Custom exceptions like `FlightFullError`.  
- **Iteration and len()** → Over active bookings in `BookingSystem`.  
- **TDD Workflow** → Implement code to pass tests.  




To start

```python -m unittest discover -s tests```

x0 O/
