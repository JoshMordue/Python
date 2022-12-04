import numpy as np

first_range = []
second_range = []

with open('input.txt', 'r') as input_text:
    total_range = input_text.read().strip().split()
    input_text.close()

total_range = '.'.join(str(x) for x in total_range)

index = ''
for letter in total_range:
    if letter == ',':
        first_range.append(index)
        index = ''
        continue
    elif letter == '.':
        second_range.append(index)
        index = ''
    else:
        index += letter

for entry in first_range:
    first_range1, first_range2 = entry.split('-')
    second_range1, second_range2 = entry.split('-')

print(first_range1)
print(first_range2)

total = 0
check = 0
for entry in first_range:
    r = np.arange(start=int(first_range1) stop=int(first_range2))
    c = np.arange(start=int(second_range1), stop=int(second_range2))


    print(r)
    print(c)
    for number in r:
        exists = number in c

        if exists:
            check += 1
            if check == len(r):
                total += 1

    for number in c:
        exists = c in r

        if exists:
            check += 1
            if check == len(c):
                total += 1



print(total)