def deposit(balance, amount):
    if not isinstance(balance, (int, float)) or isinstance(balance, bool):
        raise TypeError("balance must be numeric")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("amount must be numeric")
    if balance < 0:
        raise ValueError("balance cannot be negative")
    if amount <= 0:
        raise ValueError("deposit amount must be greater than 0")
    return balance + amount

print(deposit(10000, 2500))
