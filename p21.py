def divide_numbers(numerator, denominator):
    if not isinstance(numerator, (int, float)) or isinstance(numerator, bool):
        raise TypeError("numerator must be numeric")
    if not isinstance(denominator, (int, float)) or isinstance(denominator, bool):
        raise TypeError("denominator must be numeric")
    if denominator == 0:
        raise ValueError("denominator cannot be zero")
    return numerator / denominator

print(divide_numbers(20, 4))
