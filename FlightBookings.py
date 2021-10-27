# Rachel Ring

# Imports
import random


# create a FlightBooking class
class FlightBooking:
    # class attributes
    AISLE = 0
    MIDDLE = 1
    WINDOW = 2
    number_of_business_class = 0

    # code the initializer
    def __init__(self, flight_no_in: str, destination_in, cost_in, seat_type_in: int, business_class_in: bool = False):
        self.flight_number = str(flight_no_in)
        self.destination = destination_in
        self.__cost = cost_in
        self.seat_type = seat_type_in
        self.business_class = business_class_in
        # keep track of no of business class bookings
        if business_class_in:
            FlightBooking.number_of_business_class += 1

    # get_cost method - to return the cost of the flight
    def get_cost(self):
        return self.__cost

    # print method - print FlightBookings details
    def print(self):
        if self.business_class:
            class_type = "Business Class"
        else:
            class_type = "Economy Class"
        if self.seat_type == FlightBooking.AISLE:
            seat = "Aisle"
        elif self.seat_type == FlightBooking.MIDDLE:
            seat = "Middle"
        else:
            seat = "Window"
        print("{:30}".format("*" * 50))
        print("{:1}{:^48}{:1}".format("*", "Booking Details", "*"))
        print("{:30}".format("*" * 50))
        print(f"Flight Number\t:\t{self.flight_number}")
        print(f"Destination\t:\t{self.destination}")
        print(f"Seat Type\t:\t{seat}")
        print(f"{class_type}")
        print("{:30}".format("*" * 50))

    # apply_charge method - update cost attributes
    def apply_charges(self):
        if self.business_class:
            if self.seat_type == FlightBooking.AISLE or self.seat_type == FlightBooking.WINDOW:
                extra_cost = self.__cost * .1
                self.__cost += extra_cost
                return True
            else:
                return False
        else:
            return False

    # generate_pwd method - generates and prints password
    def generate_pwd(self):
        password = ""
        rand_num = random.randint(1, 100)
        password += str(rand_num)
        for i in range(6):
            rand_index = random.randint(0, 5)
            if not self.flight_number[rand_index] == " ":
                password += self.flight_number[rand_index]
        while len(password) < 6:
            extra_num = random.randint(0, 9)
            password += str(extra_num)
        print(f"Password:\t{password}")

    # get_number_of_business_class method - static to return number of business class bookings
    @staticmethod
    def get_number_of_business_class():
        return FlightBooking.number_of_business_class


# Main Body of Code
# create flight booking object - booking1
booking1 = FlightBooking("IE 101", "London", 100.00, 2, True)
# print booking1 details
booking1.print()
# print details as follows for object
print(f"The original cost of flight : {booking1.flight_number} to {booking1.destination} is €{booking1.get_cost()}")
# call apply_charge method - print whether or not cost was updated
if booking1.apply_charges():
    print(f"Cost Charges applied: Updated cost €{booking1.get_cost()}")
else:
    print(f"Cost Charges were not applied to this booking")
# generate_pwd and print newly made up password
booking1.generate_pwd()

# create FlightBooking object - booking2
booking2 = FlightBooking("EI 101", "London", 100.00, 0)
# print booking2 details
booking2.print()

# print number of business class bookings
print(f"Number of Business class bookings:\t{FlightBooking.number_of_business_class}")

# Exit Message
input("\nThat'll be all, hope you enjoyed your time here!\nPress Enter to Exit")
