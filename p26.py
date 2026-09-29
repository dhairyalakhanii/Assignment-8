def repeat_text(text, times=2, separator=" "):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(times, int) or isinstance(times, bool):
        raise TypeError("times must be an integer")
    if not isinstance(separator, str):
        raise TypeError("separator must be a string")
    if times < 1:
        raise ValueError("times must be at least 1")
    return separator.join([text] * times)

print(repeat_text("Python"))
print(repeat_text("Hello", times=3, separator="-"))
