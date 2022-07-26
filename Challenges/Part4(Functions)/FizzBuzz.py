def fizz_buzz(number: int) -> str:
    """
    Plays FizzBuzz
    :param number: the number to check
    :return: "Fizz" if it's a number divisible by 3, "Buzz" if it's divisible by 5
        "Fizz Buzz" if it's divisible by 15.
    """
    if number % 15 == 0:
        return "fizz buzz"
    if number % 5 == 0:
        return "buzz"
    if number % 3 == 0:
        return "fizz"
    return str(number)


for i in range(1, 101):
    print(fizz_buzz(i))
