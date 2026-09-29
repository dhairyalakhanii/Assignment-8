def calculate_fare(distance_km, rate_per_km=12, minimum_fare=50):
    values = (distance_km, rate_per_km, minimum_fare)
    if any(not isinstance(x, (int, float)) or isinstance(x, bool) for x in values):
        raise TypeError("All parameters must be numeric")
    if distance_km <= 0:
        raise ValueError("distance must be positive")
    if rate_per_km < 0 or minimum_fare < 0:
        raise ValueError("rate and minimum fare cannot be negative")
    fare = distance_km * rate_per_km
    return max(fare, minimum_fare)

print(calculate_fare(10))
print(calculate_fare(10, rate_per_km=15, minimum_fare=80))
