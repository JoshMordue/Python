import string
lower_values = string.ascii_lowercase
upper_values = string.ascii_uppercase
answer = 0
combined = []
compare1 = []
compare2 = []
iter = 1
check_iter = 0

with open('input.txt', 'r') as input_text:
    for line in input_text:
        combined.append(line.strip('\n'))
    input_text.close()

for entry in combined:
    compare1.append(combined[iter])
    combined.pop(iter)
    iter += 1
    compare2.append(combined[iter])
    combined.pop(iter)
    iter += 1

    common_chars = set(combined[check_iter]) & set(compare1[check_iter]) & set(compare2[iter]

    for index, letter in enumerate(lower_values):
        if compare in letter:
            answer += index + 1
            print(answer)

    for index, letter in enumerate(upper_values):
        if compare in letter:
            answer += index + 27
            print(answer)








print(combined)












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




