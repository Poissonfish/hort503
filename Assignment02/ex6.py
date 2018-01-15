# assign number of people
types_of_people = 10
# put a numeric variable into a string and store it into another variable
x = f"There are {types_of_people} types of people."

# assign another two string variables
binary = "binary"
do_not = "don't"
# put string variables into a string and store it into another variable
y = f"Those who know {binary} and those who {do_not}."

# print out the two string variables
print(x)
print(y)

# print out a string thaht contains a string variable
print(f"I said: {x}")
print(f"I also said: '{y}'")

# another way to put variable in a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# cat two strings
print(w + e)
