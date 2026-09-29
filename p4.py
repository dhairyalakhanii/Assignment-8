def calculate_simple_interest(principal, rate, time):
    values = (principal, rate, time)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("All parameters must be numeric")
    if any(x < 0 for x in values):
        raise ValueError("Parameters cannot be negative")
    return (principal * rate * time) / 100

print(calculate_simple_interest(10000, 5, 2))
