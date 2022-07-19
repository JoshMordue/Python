# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"
#                   ]

# del computer_parts[0:2]
# print(computer_parts)
#
# del computer_parts[-2:]
# print(computer_parts)

data = [3, 4, 6, 100, 102, 150, 152, 1466]

min_value = 100
max_value = 150

for index, value in enumerate(data):
    if (value < min_value) or (value > max_value):
        del data[index]
        


print(data)