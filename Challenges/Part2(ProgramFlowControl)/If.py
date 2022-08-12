# Write a small program to ask for a name and an Age.
# When both values have been entered, check if the person is the right age to go on an 18-30 holiday.
# They must be over 18 and under 31.
# If they are welcome them to the holiday otherwise print a polite message refusing them entry.

print("Welcome to the admissions process")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Have a great holiday {}!".format(name))
else:
    print("Our apologies you're not in our age range to allow entry.")