def smallest_number_three(a: int, b: int, c: int):
    # generate docstring for this function including the parameters and return type
    """
    This function takes in three integers and returns the smallest of the three
    :param a: int
    :param b: int
    :param c: int
    :return: int
    """

    return min(a, b, c)


print(smallest_number_three(1, 2, 3))
