class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []
    
    def __repr__(self):
        return f'{self.name} -> {self.get_average_grade():.2f}'
    
    def get_average_grade(self):
        avg = 0
        for grade in self.grades:
            avg += grade
        
        return avg / len(self.grades) if self.grades else 0
    
    def add_grade(self, grade: float):
        self.grades += [grade]

    
success_grade = 4.5

grades = {}

count_of_grades = int(input())

for _ in 'a' * count_of_grades:
    student_name = input()
    grade = float(input())

    if student_name not in grades:
        grades[student_name] = Student(student_name)
    
    grades[student_name].add_grade(grade)

for student in grades:
    if grades[student].get_average_grade() >= success_grade:
        print(grades[student])
