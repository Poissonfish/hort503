# Define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print a string with variable
    print(f"You have {cheese_count} cheeses!")
    # print a string with variable
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print a string
    print("Man that's enough for a party!")
    # print a string
    print("Get a blanket.\n")


# print a string
print("We can just give the function numbers directly:")
# call function we just defined with integer values
cheese_and_crackers(20, 30)

# print a string
print("OR, we can use variables from our script:")
# Assign a value to a variable
amount_of_cheese = 10
# Assign a value to a variable
amount_of_crackers = 50

# call function we just defined with variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a string
print("We can even do math inside too:")
# call function we just defined with math calculation
cheese_and_crackers(10 + 20, 5 + 6)

# print a string
print("And we can combine the two, variables and math:")
# call function we just defined with variables and math calculation
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Define another function
def drone_and_car(car_count, drone_count):
    # print a string with variable
    print(f"You have {car_count} cars!")
    # print a string with variable
    print(f"You have {drone_count} drones!")
    # print a string
    print("Man that's enough for fun!")


# Try 10 different ways to try my function
car_count = 10
drone_count = 5
drone_and_car(10, 12)
drone_and_car(2.5, 3.3)
drone_and_car(10 + 2, 12 + 5)
drone_and_car(10 - 3, 12 - 3)
drone_and_car(10 * 5, 12 * 2)
drone_and_car(10 / 2, 12 / 5)
drone_and_car(car_count, drone_count)
drone_and_car(car_count + 3, drone_count + 2)
drone_and_car(car_count - 3, drone_count - 5)
drone_and_car(car_count * 2, drone_count * 2)
drone_and_car(car_count / 3, drone_count / 2)
