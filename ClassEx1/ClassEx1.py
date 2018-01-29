def request_number():
    inputNum = []
    for i in range(10):
        print("Input a float number :")
        inputNum.append(float(input()))
    return inputNum


def calculate_average(inputNum):
    sum = 0
    for i in range(10):
        sum += inputNum[i]
    return sum / 10


def main():
    inputNum = request_number()
    avg = calculate_average(inputNum)
    print(f"The average is {avg}")


main()
