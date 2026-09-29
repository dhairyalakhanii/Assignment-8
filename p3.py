def student_full_name(first_name, last_name):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Names must be strings")
    return f"{first_name.title()} {last_name.title()}"

print(student_full_name("krishna", "gandhi")) # positional
print(student_full_name(first_name="krishna", last_name="gandhi")) # keyword
