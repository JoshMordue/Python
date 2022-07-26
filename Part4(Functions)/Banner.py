def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    This function prints a string centred with ** on either side.

    :param text: the string which is printed
        An asterisk will print a line full of asterisks and if the
        default value is passed through " " it'll just print ** on each side.
    :param screen_width: the canvas size to print the left and right "**" on.
    :raises ValueError: If supplied with a string which is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)


