numbers = input("Please input your numbers separated by ',' : ")

split_numbers = numbers.split(",")
int_numbers = []

for number in split_numbers:
    int_numbers.append(int(number))

a, b, c = int_numbers

result = a + b - c

print(result)
