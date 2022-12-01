# Elfs = {'First Elf': sum([1000, 2000, 3000]),
#         'Second Elf': sum([4000]),
#         'Third Elf': sum([5000, 6000]),
#         'Fourth Elf': sum([7000, 8000, 9000]),
#         'Fifth Elf': sum([10000]),
#         }


with open('input.txt', 'r') as elf_list:
    elfs = {}
    position = 0
    for line in elf_list:
        if int(line) > 0:
            ('position', val) = line.split()
            elf_list[int(position)] = val
        else:
            position += 1

    elf_list.close()






print("The Elf with the most calories is the " + (max(Elfs.keys(), key=lambda i: i[1])))

