def calculation(coin_1: int, coin_5: int, amount: int) -> int:
    five_needed = min(amount // 5, coin_5)
    remaining = amount - (five_needed * 5)

    if remaining <= coin_1:
        return five_needed, remaining
    else:
        return -1


print(calculation(coin_1=3, coin_5=3, amount=12))
print(calculation(coin_1=3, coin_5=3, amount=13))
print(calculation(coin_1=3, coin_5=3, amount=14))
