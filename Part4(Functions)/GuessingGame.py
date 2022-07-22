import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is not a valid number".format(temp))


highest = 10
answer = random.randint(1, highest)
guesses = 1
guess = 0

print(answer) #for testing purposes


while guess != answer:
    print("Please guess a number between 1 to {0}: ".format(highest))
    guess = get_integer(": ")

    if guess == 0:
        print("You gave up.")
        break
    elif guess == answer:
        print("You got it!")
        print("Amount of guesses it took: {0}".format(guesses))
        break
    else:
        if guess < answer:
            print("Please guess higher!")
        if guess > answer:
            print("Please guess Lower!")
        guesses += guesses



