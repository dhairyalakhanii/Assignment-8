def calculate_order_total(quantity, unit_price,
                          discount_percent=0, delivery_charge=50):
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise TypeError("quantity must be a positive integer")
    if not isinstance(unit_price, (int, float)) or isinstance(unit_price, bool):
        raise TypeError("unit_price must be numeric")
    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool):
        raise TypeError("discount_percent must be numeric")
    if not isinstance(delivery_charge, (int, float)) or isinstance(delivery_charge, bool):
        raise TypeError("delivery_charge must be numeric")
    if quantity <= 0:
        raise ValueError("quantity must be greater than 0")
    if unit_price <= 0:
        raise ValueError("unit_price must be greater than 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    if delivery_charge < 0:
        raise ValueError("delivery_charge cannot be negative")
    subtotal = quantity * unit_price
    discount = subtotal * discount_percent / 100
    return subtotal - discount + delivery_charge

# Positional arguments
print(calculate_order_total(2, 500))
# Keyword arguments
print(calculate_order_total(quantity=3, unit_price=800,
                            discount_percent=10, delivery_charge=75))
# Default values
print(calculate_order_total(5, 100))
# Invalid input examples
try:
    print(calculate_order_total(0, 500))
except (TypeError, ValueError) as e:
    print(type(e).__name__, ":", e)
try:
    print(calculate_order_total(2, "500"))
except (TypeError, ValueError) as e:
    print(type(e).__name__, ":", e)
try:
    print(calculate_order_total(2, 500, discount_percent=120))
except (TypeError, ValueError) as e:
    print(type(e).__name__, ":", e)
