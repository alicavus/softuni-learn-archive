def gather_credits(needed_credits: int, *args) -> str:
    enrolled_credits = 0
    enrolled_courses = {}
    for course_data in args:
        if enrolled_credits >= needed_credits:
            break
        course_name, course_credit = course_data
        if course_name in enrolled_courses:
            continue
        enrolled_courses[course_name] = course_credit
        enrolled_credits += course_credit

    result = []

    if enrolled_credits < needed_credits:
        result += [f"You need to enroll in more courses! You have to gather {needed_credits - enrolled_credits} credits more."]
    else:
        result += [f"Enrollment finished! Maximum credits: {enrolled_credits}."]
        result += [f"Courses: {', '.join(sorted(enrolled_courses.keys()))}"]

    return "\n".join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
