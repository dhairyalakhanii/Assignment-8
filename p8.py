def calculate_bill(amount, tax_rate=5):
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("amount must be numeric")
    if not isinstance(tax_rate, (int, float)) or isinstance(tax_rate, bool):
        raise TypeError("tax_rate must be numeric")
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if not 0 <= tax_rate <= 100:
        raise ValueError("tax_rate must be between 0 and 100")
    tax = amount * tax_rate / 100
    return amount + tax

print(calculate_bill(1000))
print(calculate_bill(1000, tax_rate=18))
