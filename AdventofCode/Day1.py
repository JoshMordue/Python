total = 0
record_amount = 0
top_three = []


with open('input.txt', 'r') as elf_list:

    for line in elf_list:
        if line != '\n':
            total += int(line)

        else:
            if total > record_amount:
                record_amount = total
                top_three.append(record_amount)
            total = 0

elf_list.close()

print(record_amount)
print(sum(top_three[-3:]))