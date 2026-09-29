def count_vowels(text, include_y=False):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(include_y, bool):
        raise TypeError("include_y must be Boolean")
    vowels = "aeiou"
    if include_y:
        vowels += "y"
    return sum(1 for ch in text.lower() if ch in vowels)

print(count_vowels("Python Programming"))
print(count_vowels("Python Programming", include_y=True))
