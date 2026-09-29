def convert_temperature(celsius, scale="F"):
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("celsius must be numeric")
    if not isinstance(scale, str):
        raise TypeError("scale must be a string")
    scale = scale.upper()
    if scale not in ("F", "K"):
        raise ValueError("scale must be 'F' or 'K'")
    if scale == "F":
        return (celsius * 9 / 5) + 32
    return celsius + 273.15

print(convert_temperature(25))
print(convert_temperature(25, "K"))
