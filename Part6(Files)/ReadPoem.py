jabber = open('Jabberwocky.txt', 'r')

for line in jabber:
    print(line.strip())


# jabber.close()

# with open('Jabberwocky.txt', 'r') as jabber:
#
#     # for line in jabber:
#     #     print(line.rstrip())
#
#     lines = jabber.readlines()
#
# print(lines[-1:])
# print()
#
# for line in reversed(lines):
#     print(line, end=' ') do some processing in reverse order

# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')

# with open('Jabberwocky.txt') as jabber:
#
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
#
# print("*" * 70)

with open('Jabberwocky.txt', encoding='windows-1252') as jabber:
    for line in jabber:
        print(line.rstrip())


            