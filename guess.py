import random

print("What is your favourite number?")

random = random.randint(1, 100)


# print("Your favourite number is" + str(number))

minNumber = 1
maxNumber = 100

found = False

while not found:
    print ("enter a number")
    number = int(input())
    if random == number:
        print ("Yaay you did it")
        found = True

    if random > number:
        print ("Too low")

    if random < number:
        print("Too high")

print ("End of game")

