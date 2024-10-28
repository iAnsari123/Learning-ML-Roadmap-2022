def is_palindrome(s):
    return s == s[::-1]


# Test cases
assert is_palindrome("madam") == True, "Test case 1 failed"
assert is_palindrome("racecar") == True, "Test case 2 failed"
assert is_palindrome("level") == True, "Test case 3 failed"
assert is_palindrome("hello") == False, "Test case 4 failed"
assert is_palindrome("world") == False, "Test case 5 failed"
assert is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()) == True, "Test case 6 failed"
assert is_palindrome("Madam In Eden Im Adam".replace(" ", "").lower()) == True, "Test case 7 failed"
assert is_palindrome("This is not a palindrome".replace(" ", "").lower()) == False, "Test case 8 failed"
assert is_palindrome("121") == True, "Test case 9 failed"
assert is_palindrome("12321") == True, "Test case 10 failed"
assert is_palindrome("123") == False, "Test case 11 failed"
assert is_palindrome("12345") == False, "Test case 12 failed"

print("All test cases passed!")