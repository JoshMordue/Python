for i in range(1, 13):
    print("No. {:3} squared is {:3} and cubed is {:<4}".format(i, i**2, i**3))

print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you {0}? ".format(name)))

if age < 18:
    print("You cannot Vote!")
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda you die in Return of the Jedi.")
else:
    print("You can Vote!")
    print("Please put an X in the box")


