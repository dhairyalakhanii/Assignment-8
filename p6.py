def greet_student(name, message="Welcome to Python Programming"):
    if not isinstance(name, str) or not isinstance(message, str):
        raise TypeError("name and message must be strings")
    if not name.strip() or not message.strip():
        raise ValueError("name and message cannot be empty")
    return f"Hello {name}, {message}"

print(greet_student("Krishna"))
print(greet_student("Krishna", message="Good morning!"))
