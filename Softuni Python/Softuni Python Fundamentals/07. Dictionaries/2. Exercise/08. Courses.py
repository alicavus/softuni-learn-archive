class Course:
    def __init__(self, name: str):
        self.name = name
        self.students = []
    
    def students_count(self):
        return len(self.students)
    
    def students_list(self):
        return "\n".join([f'-- {student}' for student in self.students])

courses = {}

while True:
    course_info = input()

    if course_info == "end":
        for course in courses:
            print(f"{courses[course].name}: {courses[course].students_count()}")
            print(courses[course].students_list())

        break

    course_name, student_name = course_info.split(" : ")

    if course_name not in courses:
        courses[course_name] = Course(course_name)
    
    courses[course_name].students += [student_name]


