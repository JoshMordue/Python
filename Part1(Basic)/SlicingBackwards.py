letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
print(backwards)
#slice a string to produce the characters qpo
backwards = letters[16:13:-1] #qpo
print(backwards)

print()
#Slice a string to produce edcba
backwards = letters[4::-1] #edcba
print(backwards)

print()
#Slice the string to produce the last 8 characters in reverse order
backwards = letters[:-9:-1] #zyxwvuts
print(backwards)

print()
print(letters[-4:])
print(letters[-1:])
print(letters[:1])