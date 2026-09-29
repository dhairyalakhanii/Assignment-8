def calculate_percentage(obtained_marks, total_marks=500):
    if not isinstance(obtained_marks, (int, float)) or isinstance(obtained_marks, bool):
        raise TypeError("obtained_marks must be numeric")
    if not isinstance(total_marks, (int, float)) or isinstance(total_marks, bool):
        raise TypeError("total_marks must be numeric")
    if total_marks <= 0:
        raise ValueError("total_marks must be greater than 0")
    if obtained_marks < 0:
        raise ValueError("obtained_marks cannot be negative")
    if obtained_marks > total_marks:
        raise ValueError("obtained_marks cannot exceed total_marks")
    return (obtained_marks / total_marks) * 100

print(calculate_percentage(425))
print(calculate_percentage(850, total_marks=1000))
