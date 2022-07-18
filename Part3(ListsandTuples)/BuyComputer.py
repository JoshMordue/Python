available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "HDMI",
                   "DVD Drive"
                   ]

current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("Computer")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        if current_choice == '3':
            computer_parts.append("Keyboard")
        if current_choice == '4':
            computer_parts.append("Mouse")
        if current_choice == '5':
            computer_parts.append("Mouse Mat")
        if current_choice == '6':
            computer_parts.append("HDMI cable")
    else:
        print("Please add options from the list below:")
        for id, part in enumerate(available_parts):
            print("{0}: {1}".format(id + 1, part))

    current_choice = input()

print(computer_parts)