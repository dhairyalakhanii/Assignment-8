def book_ticket(passenger_name, seats=1, ticket_price=150):
    if not isinstance(passenger_name, str):
        raise TypeError("passenger_name must be a string")
    if not isinstance(seats, int) or isinstance(seats, bool):
        raise TypeError("seats must be an integer")
    if not isinstance(ticket_price, (int, float)) or isinstance(ticket_price, bool):
        raise TypeError("ticket_price must be numeric")
    if not passenger_name.strip():
        raise ValueError("passenger_name cannot be empty")
    if seats <= 0:
        raise ValueError("seats must be positive")
    if ticket_price <= 0:
        raise ValueError("ticket_price must be positive")
    return seats * ticket_price

# Positional arguments
print(book_ticket("Krishna", 2, 150))
# Keyword arguments
print(book_ticket(passenger_name="Rahul", seats=3, ticket_price=200))
# Default arguments
print(book_ticket("Amit"))
