import random


def get_hex(number):
    if number > 15:
        return hex(number)[2:]
    else:
        _hex = hex(number)[2:]
        _hex = "0" + _hex
        return _hex


def get_random_colour():
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    z = random.randint(0, 255)

    x = get_hex(x)
    y = get_hex(y)
    z = get_hex(z)

    colour = "#" + x + y + z
    colour = colour.upper()

    return colour

