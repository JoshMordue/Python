# def factorial(counter: int) -> int:
#     """
#     function to find the factorial number of the 'Int' passed through
#
#     :param counter: Int
#     :return: the factorial number as an integer
#     """
#     if counter == 0:
#         return 1
#     else:
#         return counter*factorial(counter-1)
#
#
# for i in range(0, 36):
#     print(i, factorial(i))

def factorial(counter: int) -> int:
    """
    function to find the factorial number of the int passed through
    """
    result = 1

    for j in range(result, counter):
        result *= j
        j += 1
    return result


for i in range(0, 36):
    print(i, factorial(i))