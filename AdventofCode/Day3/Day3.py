import string
lower_values = string.ascii_lowercase
upper_values = string.ascii_uppercase
string_compare = ''
answer = 0

with open('input.txt', 'r') as input_text:
    rucksacks = input_text.read().strip().split()
    input_text.close()


for i in range(0, len(rucksacks), 3):
    compare1, compare2, compare3 = rucksacks[i:i+3]
    common_chars = set(compare1) & set(compare2) & set(compare3)

    print(common_chars)
    string_compare = repr(common_chars).strip("{'}")

    for index, letter in enumerate(lower_values):
        if string_compare in letter:
            answer += index + 1
            print(answer)

    for index, letter in enumerate(upper_values):
        if string_compare in letter:
            answer += index + 27
            print(answer)

print(answer)

#task 1
# for index, letter in enumerate(lower_values):
#     if compare in letter:
#          answer += index + 1
#          print(answer)
#
# for index, letter in enumerate(upper_values):
#     if compare in letter:
#         answer += index + 27
#         print(answer)


# import string
# lower_values = string.ascii_lowercase
# upper_values = string.ascii_uppercase
# answer = 0
#
# with open('input.txt', 'r') as input_text:
#     for line in input_text:
#         x = line.strip()
#         y, z = x[:len(x)//2:], x[len(x)//2:]
#
#         y_check = set(y)
#         z_check = set(z)
#
#         common_chars = z_check & y_check
#
#         compare = repr(common_chars).strip("{'}")
#
#         for index, letter in enumerate(lower_values):
#             if compare in letter:
#                 answer += index + 1
#                 print(answer)
#
#         for index, letter in enumerate(upper_values):
#             if compare in letter:
#                 answer += index + 27
#                 print(answer)




