def create_email(username, domain="gmail.com"):
    if not isinstance(username, str) or not isinstance(domain, str):
        raise TypeError("username and domain must be strings")
    if not username.strip() or not domain.strip():
        raise ValueError("username and domain cannot be empty")
    return f"{username}@{domain}"

print(create_email("krishna"))
print(create_email("krishna", domain="example.com"))
