def power(base, exponent=2):
    if not isinstance(base, (int, float)) or isinstance(base, bool):
        raise TypeError("base must be numeric")
    if not isinstance(exponent, (int, float)) or isinstance(exponent, bool):
        raise TypeError("exponent must be numeric")
    return base ** exponent

print(power(5)) # default exponent
print(power(2, 3))
