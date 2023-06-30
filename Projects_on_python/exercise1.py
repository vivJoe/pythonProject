def collatz(number):
    if number % 2 == 0:
        print("number is even")
        result = number // 2
    else:
        print("number is odd")
        result = 3 * number + 1

    print(result)
    return result

def collatz_sequence():
    number = int(input("Enter an interger: "))
    while number != 1:
        number = collatz(number)

collatz_sequence()