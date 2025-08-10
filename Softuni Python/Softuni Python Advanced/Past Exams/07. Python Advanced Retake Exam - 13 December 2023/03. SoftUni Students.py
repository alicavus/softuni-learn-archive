def softuni_students(*args, **kwargs) -> str:
    valid_students = {}
    invalid_students = []

    for student_data in args:
        course_id, student_username = student_data

        if course_id not in kwargs:
            invalid_students.append(student_username)

        else:
            valid_students[student_username] = kwargs[course_id]

    result = []

    for valid_student, valid_course in sorted(valid_students.items(), key=lambda x: x[0]):
        result += [f"*** A student with the username {valid_student} has successfully finished the course {valid_course}!"]

    if invalid_students:
        result += [f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"]

    return "\n".join(result)

print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
