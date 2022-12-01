Elfs = {'First Elf': sum([1000, 2000, 3000]),
        'Second Elf': sum([4000]),
        'Third Elf': sum([5000, 6000]),
        'Fourth Elf': sum([7000, 8000, 9000]),
        'Fifth Elf': sum([10000]),
        }

print(max(Elfs.items(), key=lambda i: i[1]))

