def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")


directions_to_timesSq()


# parameters and arguments
def trip_welcome(destination):
    print("Welcome to Tripcademy!")
    print("Looks like you're going to " + destination + " today.")


def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


print(generate_trip_instructions("Grand Central Station"))


def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print(car_rental_total + hotel_total + plane_ticket_price)


print(calculate_expenses(200, 100, 100, 5))
