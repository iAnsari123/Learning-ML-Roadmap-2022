def ticket_generator(src: str, dest: str, passengers: int) -> list:
    num = 100
    result = []

    if passengers < 5:
        for i in range(1, passengers + 1):
            result.append(f"AI:{src[:3]}:{dest[:3]}:{num + i}")
    else:
        for i in range(6, passengers + 1):
            result.append(f"AI:{src[:3]}:{dest[:3]}:{num + i}")

    return result


print(ticket_generator("Mumbai", "Delhi", 10))
