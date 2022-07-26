def banner_text(screen_width, text):

    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text(80, "*")
banner_text(80, "Always look on the bright side of life...")
banner_text(80, "If life seems jolly rotten,")
banner_text(80, "There's something you've forgotten!")
banner_text(80, "And that's to laugh and smile and dance and sing,")
banner_text(80, " ")
banner_text(80, "When you're feeling in the dumps,")
banner_text(80, "Don't be silly chumps,")
banner_text(80, "Just purse your lips and whistle - that's the thing!")
banner_text(80, "And... always look on the bright side of life...")
banner_text(80, "*")


