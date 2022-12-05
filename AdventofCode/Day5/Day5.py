with open('input.txt', 'rt') as instructions:
    crates, ins = instructions.read().split("\n\n")

stack_width = 4
p = re.compile(r"[A-Z]")
# reverse it, so we've got the stack numbers at the top
stack_data = stack_data[::-1]
num_stacks = len(stack_data[0].split())



movements = crates(ins.splitlines())

print(stacks)
print(movements)
























# stack1 = ["D","L","J","R","V","G","F",]
        # stack2 = ["",]
        # stack3 = ["R","W","Z","H","Q"]
        # stack4 = ["R","Z","J","V","D","W"]
        # stack5 = ["B","M","H","S"]
        # stack6 = ["B","P","V","H","J","N","G","L"]
        # stack7 = ["S","L","D","H","F","Z","Q","J"]
        # stack8 = ["B","Q","G","J","F","S","W"]
        # stack9 = ["J","D","C","S","M","W","Z"]

