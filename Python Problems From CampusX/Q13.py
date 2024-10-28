def can_be_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


def main():
    a = int(input("Enter the first side: "))
    b = int(input("Enter the second side: "))
    c = int(input("Enter the third side: "))
    if can_be_triangle(a, b, c):
        print("Yes, it can be a triangle.")
    else:
        print("No, it can't be a triangle.")

if __name__ == "__main__":
    main()