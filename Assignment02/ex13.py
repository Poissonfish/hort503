from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
arg1 = input("What's the first arg for? ")
arg2 = input("What's the second arg for? ")
arg3 = input("What's the third arg for? ")
print(f"The script is called: {script}")
print(f"Your first variable is {first}, and it's for {arg1}")
print(f"Your second variable is '{second}', and it's for '{arg2}'.")
print(f"Your third variable is '{third}', and it's for '{arg3}'.")
