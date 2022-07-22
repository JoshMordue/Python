def sum_eo(n, t):
    if n >= 0:
        if t == 'e':
            return sum(range(2, n, 2))
        if t == 'o':
            return sum(range(1, n, 2))
    return -1


x = sum_eo(10, 'e')
print(x)


