def age_category(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be an integer")
    if age < 0:
        raise ValueError("age cannot be negative")
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"

print(age_category(10))
print(age_category(18))
print(age_category(35))
print(age_category(65))
