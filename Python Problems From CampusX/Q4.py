def is_palindrome(num: int):
    """
    Check if a number is a palindrome of the sum of its digits raised to the power of 3.

    Parameters:
    num (int): The number to be checked for palindrome property.

    Returns:
    bool: True if the number is a palindrome of the sum of its digits raised to the power of 3, False otherwise.
    """
    return sum([int(x) ** 3 for x in str(num)]) == num


print(is_palindrome(153))
print(is_palindrome(370))
print(is_palindrome(371))
