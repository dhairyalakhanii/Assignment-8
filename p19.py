def withdraw(balance, amount):
    if not isinstance(balance, (int, float)) or isinstance(balance, bool):
        raise TypeError("balance must be numeric")
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise TypeError("amount must be numeric")
    if balance < 0:
        raise ValueError("balance cannot be negative")
    if amount <= 0:
        raise ValueError("amount must be greater than 0")
    if amount > balance:
        raise ValueError("amount exceeds available balance")
    return balance - amount

print(withdraw(10000, 2500))
