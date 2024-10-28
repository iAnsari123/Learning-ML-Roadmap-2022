# Any purchase with a total bill amount above Rs.30000 is entitled to 5% discount.
# If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
# Assume that quantity required by the customer for any gem will always be greater than 0.
# Perform case-sensitive comparison wherever applicable. gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
# Price of gems available in the store. gems_list and price_list have one-to-one correspondence price_list=[1760,2119,1599,3920,3999]
# List of gems required by the customer reqd_gems=["Ivory","Emerald","Garnet"]
# Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
# reqd_quantity=[3,10,12]


def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    total_bill_amount = 0

    for gem, quantity in zip(reqd_gems, reqd_quantity):
        if gem in gems_list:
            total_bill_amount += price_list[gems_list.index(gem)] * quantity
        else:
            return -1

    if total_bill_amount > 30000:
        total_bill_amount *= 0.95

    return total_bill_amount


# Example usage
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]
price_list = [1760, 2119, 1599, 3920, 3999]
reqd_gems = ["Ivory", "Emerald", "Garnet"]
reqd_quantity = [3, 10, 12]

print(
    calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
)  # Output should be the total bill amount after discount if applicable
