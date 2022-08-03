available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "HDMI",
                   "DVD Drive"
                   ]

#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = []
available_parts.sort()

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            #It's already in so remove it
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
            print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for id, part in enumerate(available_parts):
            print("{0}: {1}".format(id + 1, part))

    current_choice = input()

print(computer_parts)