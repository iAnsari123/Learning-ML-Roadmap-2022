def display_grade(grade: int):
    if 80 <= grade <= 100:
        return "A"
    elif 73 <= grade <= 79:
        return "B"
    elif 65 <= grade <= 72:
        return "C"
    elif 0 <= grade <= 64:
        return "F"
    else:
        return "Z"


# Example usage
print(display_grade(85))
print(display_grade(77))
print(display_grade(70))
print(display_grade(60))
print(display_grade(110))
