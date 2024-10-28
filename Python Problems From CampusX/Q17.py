def compress_string(s):
    result = ""
    count = 1
    for index in range(len(s)):

        if index == len(s) - 1:
            result += str(count) + s[index]
            break

        if s[index + 1] == s[index]:
            count += 1
        else:
            result += str(count) + s[index]
            count = 1

    return result


print(compress_string("aaabbbccc"))
print(compress_string("AAABBBCCC"))         # Output: 3A3B3C
print(compress_string("abc"))
