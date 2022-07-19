pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)

print(letters)

numbers = [2.3, 2.5, 5.2, 5.3, 6.3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "Kerry",
         "Terry",
         "Michael",
         "Ben"]

names.sort(key=str.casefold)
print(names)