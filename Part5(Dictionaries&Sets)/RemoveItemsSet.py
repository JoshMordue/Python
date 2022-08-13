small_ints = set(range(21))
print(small_ints)

# clears the set
# small_ints.clear()
# print(small_ints)

# removing entry 10 and 11
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

# discard crashes if the entry has not been found, whereas discard does not
