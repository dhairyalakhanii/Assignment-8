def shipping_charge(weight, express=False):
    if not isinstance(weight, (int, float)) or isinstance(weight, bool):
        raise TypeError("weight must be numeric")
    if not isinstance(express, bool):
        raise TypeError("express must be Boolean")
    if weight <= 0:
        raise ValueError("weight must be positive")
    # Reasonable rule: Rs. 50 base + Rs. 20 per kg
    charge = 50 + (weight * 20)
    if express:
        charge += 100
    return charge

print(shipping_charge(3))
print(shipping_charge(3, express=True))
