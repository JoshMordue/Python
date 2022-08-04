from Contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}

for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-" * 10)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break

    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t {food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t You need to buy: {quantity_to_buy} of {food_item}")
