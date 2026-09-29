def grade_student(marks, passing_marks=40):
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise TypeError("marks must be numeric")
    if not isinstance(passing_marks, (int, float)) or isinstance(passing_marks, bool):
        raise TypeError("passing_marks must be numeric")
    if not 0 <= marks <= 100:
        raise ValueError("marks must be between 0 and 100")
    if not 0 <= passing_marks <= 100:
        raise ValueError("passing_marks must be between 0 and 100")
    return "Pass" if marks >= passing_marks else "Fail"

print(grade_student(72))
print(grade_student(35, passing_marks=40))
