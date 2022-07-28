def sum_numbers(*numbers: float) -> float:
    """Returns the value of all the variables passed through as a 'Float'"""
    result = 0
    for number in numbers:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(12.5, 6.25, 11.778))


# def sum_numbers(*numbers: float) -> float:
#   """Returns the value of all the variables passed through as a 'Float'"""
#    #return sum(numbers)
#    a simpler way of solving it using inbuilt functions

