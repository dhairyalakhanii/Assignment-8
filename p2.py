def rectangle_area(length, width):
    if not isinstance(length, (int, float)) or isinstance(length, bool):
        raise TypeError("length must be numeric")
    if not isinstance(width, (int, float)) or isinstance(width, bool):
        raise TypeError("width must be numeric")
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be greater than 0")
    return length * width

print(rectangle_area(10, 5))
