import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping and prompting,
    the user until a valid 'int' is entered.

    :param prompt: The string that the user will see,
        when they're prompted to enter the value.
    :return: The Integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("Please enter a valid number")

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



