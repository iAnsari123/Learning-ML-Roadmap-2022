# The road transport corporation (RTC) of a city wants to know whether a particular bus-route is running on profit or loss.
# Assume that the following information are given: Price per litre of fuel = 70
# Mileage of the bus in km/litre of fuel = 10 Price(Rs) per ticket = 80
# The bus runs on multiple routes having different distance in kms and number of passengers.
# Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.


def bus_route_profit(distance: int, passengers: int) -> int:
    fuel_cost = distance / 10 * 70
    income = passengers * 80
    profit = income - fuel_cost
    if profit < 0:
        return -1
    else:
        return round(profit)


assert bus_route_profit(100, 50) == 300
assert bus_route_profit(50, 30) == 50
assert bus_route_profit(200, 100) == 300
print("ALL test cases passed")
