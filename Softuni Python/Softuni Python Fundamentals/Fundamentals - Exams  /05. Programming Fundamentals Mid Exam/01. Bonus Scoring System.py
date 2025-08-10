from math import ceil

number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())

students_attendances = [int(input()) for _ in '1' * number_of_students]

max_attendance = max(students_attendances) if students_attendances else 0
max_bonus = max_attendance / total_number_of_lectures * (5 + additional_bonus) if total_number_of_lectures else 0

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
