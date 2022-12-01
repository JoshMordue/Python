total = 0
record = 0
position = 0
record_amount = 0


with open('input.txt', 'r') as elf_list:

    for line in elf_list:
        if line != '\n':
            total += int(line)

        else:
            if total > record:
                record = position
                record_amount = total
            total = 0
            position += 1

    print(total)
    print(record)
    print(position)


elf_list.close()
