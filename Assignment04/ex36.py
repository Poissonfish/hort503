from sys import exit


def hard():
    print("Nice! Let's try something harder")
    print("Could you calculate this for me?")
    print("4 * 35 + 18 / 2 = ")

    aws = input(">")

    while True:
        if aws == "176":
            print("Nice, you correctly answer all the questions")
            exit(0)
        else:
            print("Ummm not quite right, let's try something easier")
            easy()


def easy():
    print("Ok, seems like you are not good at math.")
    print("What about this.")
    print("Say you have 10 apples, your Mom gave you another 2.")
    print("How many apples you have now?")

    choice = input("> ")

    if choice == "12":
        print("You did a good job!")
        exit(0)
    else:
        print("Oh well, it's not end of the world if you did badly in math")
        exit(0)


def start():
    print("Let's do some math")
    print("How old are you?")

    choice = input("> ")
    age = int(choice) + 20

    print(f"So after 20 years, you'll be {age}, right? (y/n)")

    choice = input("> ")

    while True:
        if "y" in choice:
            hard()
        elif "n" in choice:
            easy()
        else:
            print("I don't know what that mean")


start()
