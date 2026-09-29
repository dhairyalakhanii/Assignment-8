def calculate_bmi(weight_kg, height_m):
    values = (weight_kg, height_m)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("Weight and height must be numeric")
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be greater than 0")
    return round(weight_kg / (height_m ** 2), 2)

print(calculate_bmi(70, 1.75))
