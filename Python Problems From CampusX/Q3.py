def sum_of_divisible_by_4():
    """
    Calculate the sum of numbers divisible by 4 until the user enters 5.
    The function prompts the user to enter a number and adds it to the total sum if it is divisible by 4.
    If the user enters 5, the function returns the total sum.
    If a non-integer value is entered, the function displays an error message and continues the loop.
    """
    total_sum = 0
    while True:
        try:
            num = int(input("Enter a number(5 to quit): "))
            if num % 4 == 0:
                total_sum += num
            elif num == 5:
                return total_sum
            else:
                print(f"{num} is not divisible by 4.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print(sum_of_divisible_by_4())


if __name__ == "__main__":
    main()
