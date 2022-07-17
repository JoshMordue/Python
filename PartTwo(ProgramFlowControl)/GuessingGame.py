import random

highest = 10
answer = random.randint(1, highest)
guesses = 1
guess = 0

print(answer) #for testing purposes


while guess != answer:
    print("Please guess a number between 1 to {0}: ".format(highest))
    guess = int(input())

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



#
# elif guess == 0:
#     print("You gave up.")
# else:
#     if guess < answer:
#         print("Please guess higher!")
#     if guess > answer:
#         print("Please guess Lower!")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you've guessed it correctly!")
#     else:
#         print("Sorry you guessed it incorrectly again")

# if guess < answer:
#     print("Please guess higher!")
#     guess = int(input())
#     if guess == answer:
#         print("You got it the second time!")
# elif guess > answer:
#     print("Please guess lower!")
#     guess = int(input())
#     if guess == answer:
#         print("You got it the second time!")
# else:
#     print("You got it first time!")
