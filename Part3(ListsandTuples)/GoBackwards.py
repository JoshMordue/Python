data = [104, 101, 4, 105, 103, 92, 305, 12, 108, 250]

min_valid = 100
max_valid = 200

# for index in range(len(data)-1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)