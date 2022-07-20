data = [104, 101, 4, 105, 103, 92, 305, 12, 108, 250]

min_valid = 100
max_valid = 200

for index in range(len(data)-1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

print(data)