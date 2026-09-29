def login_check(username, password, min_password_length=8):
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("username and password must be strings")
    if not isinstance(min_password_length, int) or isinstance(min_password_length, bool):
        raise TypeError("min_password_length must be an integer")
    if not username.strip() or not password:
        raise ValueError("username and password cannot be empty")
    if min_password_length < 1:
        raise ValueError("minimum password length must be positive")
    return len(password) >= min_password_length

print(login_check("krishna", "python123"))
print(login_check("krishna", "python123", min_password_length=10))
