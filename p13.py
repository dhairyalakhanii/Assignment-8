def average_marks(m1, m2, m3, m4, m5):
    marks = (m1, m2, m3, m4, m5)
    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise TypeError("All marks must be numeric")
        if not 0 <= mark <= 100:
            raise ValueError("Each mark must be between 0 and 100")
    return sum(marks) / len(marks)

print(average_marks(80, 75, 90, 85, 88))
