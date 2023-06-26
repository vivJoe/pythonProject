correct_guess = 15
num_of_guess = 0
max_guesslimit = 3

while num_of_guess < max_guesslimit:
    guess = int(input("what is your guess "))
    num_of_guess += 1
    if guess != correct_guess:
        print("sorry pls try to input the correct number")

    else:
        print("congratulations, you won")
        break
if num_of_guess == max_guesslimit:
    print("sorry, you have reached the limit")



