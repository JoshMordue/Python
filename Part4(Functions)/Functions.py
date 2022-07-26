def multiply(x, y):
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    it can also be used to multiply a sequence.
    If you pass a String through the 'x' variable it will get repeated
    by the value 'y' as the returned value.

    :param x: The first number to multiply
    :param y: the number to multiply 'x' by.
    :return: the product of multiplying 'x' and 'y'
    """
    result = x * y
    return result


answer = multiply(40, 10)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)


answer = multiply(18, 3)
print(answer)


def fibonacci(n):
    """Return the 'n'th fibonacci number, for positive 'n'."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


