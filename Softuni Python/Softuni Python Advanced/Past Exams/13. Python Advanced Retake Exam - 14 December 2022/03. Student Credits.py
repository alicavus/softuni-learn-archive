def students_credits(*args) -> str:
    student_credits_threshold = 240
    diyans_credits = 0.0
    grades = {}
    for data in args:
        course_name, course_credits, max_test_points, diyans_points = data.split("-")
        current_credits = float(course_credits) * float(diyans_points) / float(max_test_points)
        grades[course_name] = current_credits
        diyans_credits += current_credits

    result = []

    if diyans_credits >= student_credits_threshold:
        result += [
            f"Diyan gets a diploma with {diyans_credits:.1f} credits."
        ]
    else:
        result += [
            f"Diyan needs {student_credits_threshold - diyans_credits:.1f} credits more for a diploma."
        ]

    for course_data in sorted(grades.items(), key=lambda x: -x[1]):
        course_name, course_credits = course_data
        result += [
            f"{course_name} - {course_credits:.1f}"
        ]

    return "\n".join(result)

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print("-----")

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print("-----")

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

