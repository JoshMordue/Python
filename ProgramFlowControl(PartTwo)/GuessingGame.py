answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first try!")
else:
    if guess < answer:
        print("Please guess higher!")
    if guess > answer:
        print("Please guess Lower!")
    guess = int(input())
    if guess == answer:
        print("Well done, you've guessed it correctly!")
    else:
        print("Sorry you guessed it incorrectly again")

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
