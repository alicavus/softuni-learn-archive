students = dict()

for _ in range(int(input())):
    student, grade = tuple(input().split())
    if student not in students.keys():
        students[student] = []
    students[student].append(float(grade))

for student_name, student_grades in students.items():
    student_average = sum(student_grades) / len(student_grades)
    student_grades = " ".join(f"{grade:.2f}" for grade in student_grades)
    print(f"{student_name} -> {student_grades} (avg: {student_average:.2f})")
    