def is_eligible_for_vote(age, citizenship=True):
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be an integer")
    if not isinstance(citizenship, bool):
        raise TypeError("citizenship must be Boolean")
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18 and citizenship

print(is_eligible_for_vote(20))
print(is_eligible_for_vote(17, citizenship=True))
