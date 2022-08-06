d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

keys = d.keys()
print(keys)

# new_dict = dict.fromkeys(pantry_items, 1)
# print(new_dict)

for item in d.keys():
    print(item)
