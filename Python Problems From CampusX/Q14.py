from functools import reduce


def populate(num1: int, num2: int) -> int:

    if num1 > num2:
        return -1

    numbers = list(range(num1, num2 + 1))
    final_numbers = []
    for number in numbers:
        if 10 <= number <= 99 and number % 5 == 0:
            if reduce(lambda x, y: int(x) + int(y), str(number)) % 3 == 0:
                final_numbers.append(number)
    if len(final_numbers) == 0:
        return -1
    else:
        return max(final_numbers)


# Test cases
print(populate(10, 20))  # 15
print(populate(10, 30))  # 15
print(populate(10, 40))  # 15
print(populate(10, 50))  # 45
print(populate(10, 60))  # 45
print(populate(10, 70))  # 45
print(populate(10, 80))  # 75
