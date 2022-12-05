with open('input.txt', 'r') as instructions:
    crates, ins = instructions.read().split("\n\n")

stack = crates[1::4]
i = 1
for line in stack:
    stack_i = []
    stack_i = line[[::-1]::9]
    i += 1
    print(stack_i)





















# stack1 = ["D","L","J","R","V","G","F",]
        # stack2 = ["",]
        # stack3 = ["R","W","Z","H","Q"]
        # stack4 = ["R","Z","J","V","D","W"]
        # stack5 = ["B","M","H","S"]
        # stack6 = ["B","P","V","H","J","N","G","L"]
        # stack7 = ["S","L","D","H","F","Z","Q","J"]
        # stack8 = ["B","Q","G","J","F","S","W"]
        # stack9 = ["J","D","C","S","M","W","Z"]

