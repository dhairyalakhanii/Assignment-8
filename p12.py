def salary_after_bonus(salary, bonus_percent=5):
    if not isinstance(salary, (int, float)) or isinstance(salary, bool):
        raise TypeError("salary must be numeric")
    if not isinstance(bonus_percent, (int, float)) or isinstance(bonus_percent, bool):
        raise TypeError("bonus_percent must be numeric")
    if salary < 0 or bonus_percent < 0:
        raise ValueError("salary and bonus_percent cannot be negative")
    return salary + (salary * bonus_percent / 100)

print(salary_after_bonus(50000))
print(salary_after_bonus(50000, bonus_percent=10))
