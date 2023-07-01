myPet = ['shiwawa', 'bulldog', 'golden_fish', 'cat', 'pet_bull']
print("Input the pet name you would like to have today: ")
petName = input()
if petName in myPet:
    print("congratulations, we have what you are looking for")
else:
    print("sorry, come back next time for the pet named " + petName)