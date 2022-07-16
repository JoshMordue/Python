shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

item_to_find = "Spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index;
#         print("The item to find is found at {}".format(index))
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
    print("The item to find is found at {}".format(found_at))
else:
    print("No item found in the list.")
