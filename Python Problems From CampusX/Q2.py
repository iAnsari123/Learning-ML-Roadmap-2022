import pytest


def is_palindrome(number: int) -> bool:
    """
    Check if a given number is a palindrome.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(number) == str(number)[::-1]


print(is_palindrome(12321))  # True


class TestIsPalindrome:

    # Check if a single-digit number is identified as a palindrome
    def test_single_digit_palindrome(self):
        assert is_palindrome(7) == True

    # Check behavior with a negative number
    def test_negative_number(self):
        assert is_palindrome(-121) == False


test = TestIsPalindrome()
test.test_single_digit_palindrome()
test.test_negative_number()
