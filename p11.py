def calculate_discount(price, discount_percent=10):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        raise TypeError("price must be numeric")
    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
        raise TypeError("discount_percent must be numeric")
    if price <= 0:
        raise ValueError("price must be greater than 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")
    return price - (price * discount_percent / 100)

print(calculate_discount(1000))
print(calculate_discount(1000, discount_percent=20))
