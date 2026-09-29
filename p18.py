def calculate_net_salary(basic_salary, hra_percent=20, da_percent=10):
    values = (basic_salary, hra_percent, da_percent)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("All parameters must be numeric")
    if basic_salary < 0:
        raise ValueError("basic_salary cannot be negative")
    if not 0 <= hra_percent <= 100:
        raise ValueError("hra_percent must be between 0 and 100")
    if not 0 <= da_percent <= 100:
        raise ValueError("da_percent must be between 0 and 100")
    hra = basic_salary * hra_percent / 100
    da = basic_salary * da_percent / 100
    return basic_salary + hra + da

print(calculate_net_salary(50000))
print(calculate_net_salary(50000, hra_percent=25, da_percent=12))
