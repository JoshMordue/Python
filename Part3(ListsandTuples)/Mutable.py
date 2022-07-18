shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]

print(shopping_list)
print(id(shopping_list))