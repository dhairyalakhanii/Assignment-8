def add_numbers(a, b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an int or float")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an int or float")
    return a + b

print(add_numbers(10, 20))
