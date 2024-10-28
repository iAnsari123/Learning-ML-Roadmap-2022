def trip_fare(adults: int = 0, children: int = 0):
    """
    Calculate the total fare for a trip based on the number of adults and children
    :param adults: Number of adults
    :param children: Number of children
    :return: Total fare for the trip
    """

    fare_per_adult = 37550.0
    fare_per_child = fare_per_adult / 3

    adults_fare = adults * fare_per_adult
    children_fare = children * fare_per_child

    total_fare = adults_fare + children_fare
    service_tax = total_fare * 0.07
    total_fare_with_tax = total_fare + service_tax

    discount = total_fare_with_tax * 0.1
    final_fare = total_fare_with_tax - discount

    return final_fare


# Example usage
print(trip_fare(2, 3))
