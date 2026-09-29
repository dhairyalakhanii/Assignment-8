def register_student(name, age, course="Data Science", semester=1):
    if not isinstance(name, str) or not isinstance(course, str):
        raise TypeError("name and course must be strings")
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be an integer")
    if not isinstance(semester, int) or isinstance(semester, bool):
        raise TypeError("semester must be an integer")
    if not name.strip() or not course.strip():
        raise ValueError("name and course cannot be empty")
    if not 16 <= age <= 100:
        raise ValueError("age must be between 16 and 100")
    if not 1 <= semester <= 8:
        raise ValueError("semester must be between 1 and 8")
    return f"Name: {name}\nAge: {age}\nCourse: {course}\nSemester: {semester}"

print(register_student("Krishna", 35))
print(register_student("Rahul", 20, course="BCA", semester=3))
