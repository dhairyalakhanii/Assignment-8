def find_maximum(a, b, c):
    values = (a, b, c)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("All arguments must be numeric")
    return max(values)

print(find_maximum(10, 25, 15))
