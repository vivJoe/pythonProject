import random
secret_number = random.randint(1, 15)
print("I am thinking of a number between 1 and 15")

for guessTaken in range(1, 5):
    print("Take a guess")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        break  #This condition is the correct guess!

if guess == secret_number:
    print("Good job! You guesses my number in " + str(guessTaken) + " guesses!")
else:
    print("Nope, The number I was thinking of was " + str(secret_number))