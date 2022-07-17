activities = ["Exit", "Learn Python", "Learn Java", "Go Swimming", "Go to the Gym", "Have Dinner", "Go to bed"]
choice = "-"
max = int(len(activities)) - 1

while choice != 0:
    for option in activities:
        print(activities.index(option), ": ", option)

    choice = int(input("Please select the number associated with the activity: "))

    if 0 < choice <= max:
        print("You selected {0}".format(choice))
        break
    elif choice != 0:
        print("Please enter a valid number between 1 and {}".format(max))
    else:
        print("You selected no activities")





