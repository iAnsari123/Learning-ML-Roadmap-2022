""" 7.
Write a python program that displays a message as follows for a given number:
● If it is a multiple of three, display "Zip"
● If it is a multiple of five, display "Zap".
● If it is a multiple of both three and five, display "Zoom".
● If it does not satisfy any of the above given conditions, display
"Invalid".
"""


def display_message(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return "Zoom"
    elif number % 3 == 0:
        return "Zip"
    elif number % 5 == 0:
        return "Zap"
    else:
        return "Invalid"


# Example usage
print(display_message(15))
print(display_message(9))
print(display_message(10))
print(display_message(7))
