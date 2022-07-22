def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()

def is_palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")





if is_palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))

# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))




