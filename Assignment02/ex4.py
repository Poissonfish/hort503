# assign number of available cars
cars = 100
# assign available space in each car
space_in_a_car = 4.0
# assign number of drivers
drivers = 30
# assign number of passengers
passengers = 90
# define how many cars not driven
cars_not_driven = cars - drivers
# define how many cars driven by a driver
cars_driven = drivers
# define how many people can be driven
carpool_capacity = cars_driven * space_in_a_car
# define the average number passengers for a car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


