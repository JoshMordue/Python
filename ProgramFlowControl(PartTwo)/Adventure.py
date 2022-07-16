available_exits = ["North", "South", "East", "West"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "Quit".casefold():
        print("Game over")
        break

print("Aren't you glad you got out of there")