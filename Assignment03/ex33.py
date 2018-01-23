def ex33(max):
    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


ex33(3)


def ex33_2(max, increase):
    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increase
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


ex33_2(4, 2)
