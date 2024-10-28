from functools import reduce


def display_product(*args):

    if 7 in args:
        if args.index(7) == 0:
            return args[1] * args[2]
        elif args.index(7) == 1:
            return args[2]
        else:
            return args[1]
    else:
        return reduce(lambda x, y: x * y, args)


# Example usage
print(display_product(1, 5, 3))
print(display_product(3, 7, 8))
print(display_product(7, 4, 3))
print(display_product(1, 5, 7))
print(display_product(3, 7, 8))
print(display_product(1, 33, 7))
