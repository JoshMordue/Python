def sum_eo(n, t):
    """
    The method takes two of the users inputs, a positive number
    and if it's odd or even to calculate the sum of all the numbers
    that are odd or even from 0 to equal the number provided.
    :param n: the positive number
    :param t: the users input for odd or even
    :return: the sum of the range, if an invalid character has been entered it returns 0
    """
    if n >= 0:
        if t == 'e':
            return sum(range(2, n, 2))
        if t == 'o':
            return sum(range(1, n, 2))
    return -1


x = sum_eo(10, 'e')
print(x)


