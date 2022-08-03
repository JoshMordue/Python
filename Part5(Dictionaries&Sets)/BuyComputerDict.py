available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "HDMI",
                   "6": "DVD Drive"
                   }

current_choice = None

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print("Invalid entry please see below the valid options: ")
    print(available_parts)

    current_choice = input("> ")