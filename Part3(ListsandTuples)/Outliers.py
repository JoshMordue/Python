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

# process the low values in the list

for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break

print(data)
del data[:stop]
print(data)

# process high values in the list
start = 0

for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_value:
        # we have the index of last item to keep
        # set start to the position of the first item to delete
        # which is 1 after 'index'
        start = index + 1
        break

del data[start:]
print(data)