parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in Norwegian Blue".format(letter))
else:
    print("{} is not in Norwegian Blue".format(letter))