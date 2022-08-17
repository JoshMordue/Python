filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()


print(first)
chars = "'Twasebv"

# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    for character in chars:
        print(f'removing ' f"{character}"'')
    else:
        break

print("*" * 80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix('toves')
print(toves_removed)
