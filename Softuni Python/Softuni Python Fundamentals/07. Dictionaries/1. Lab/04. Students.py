school = {}

while True:
    course_info = input()

    if ":" not in course_info:
        if course_info in school:
            for id, student in school[course_info].items():
                print(f'{student} - {id}')
        break

    name, id, course = course_info.split(':', maxsplit=3)

    course = course.lower()
    course = course.replace(" ", "_")

    if course not in school:
        school.update({course:dict()})
    
    school[course][id] = name

