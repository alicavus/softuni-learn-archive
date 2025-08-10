from project.student import Student
from unittest import TestCase, main

class StudentTest(TestCase):
    def setUp(self):
        self.student = Student("Андрей Стоянов", {
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"]})
    
    def test_init_courses_dict(self):
        self.assertEqual("Андрей Стоянов",  self.student.name)
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"]},  self.student.courses)
    
    def test_init_courses_none(self):
        self.student = Student("Андрей Стоянов",  None)
        self.assertEqual("Андрей Стоянов",  self.student.name)
        self.assertEqual({},  self.student.courses)
    
    def test_enroll_course_already_enrolled_empty_notes(self):
        result = self.student.enroll("Гейминг", [])
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"]},  self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)
    
    def test_enroll_course_already_enrolled_lists_notes(self):
        result = self.student.enroll("Гейминг", ["Конзолни игри"])
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност", "Конзолни игри"]},  self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)
    
    def test_enroll_course_add_course_empty_notes_yes(self):
        result = self.student.enroll("Пайтън", [], "Y")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": []},  self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
    
    def test_enroll_course_add_course_empty_notes(self):
        result = self.student.enroll("Пайтън", [])
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": []},  self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
    
    def test_enroll_course_add_course_empty_notes_other(self):
        result = self.student.enroll("Пайтън", [], "K")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": []},  self.student.courses)
        self.assertEqual("Course has been added.", result)
    
    def test_enroll_course_add_course_notes(self):
        result = self.student.enroll("Пайтън", ["Лупъбъл ифове", "Аксесване велюту"], "Y")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": ["Лупъбъл ифове", "Аксесване велюту"]},  self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
    
    def test_enroll_course_add_course_notes_yes(self):
        result = self.student.enroll("Пайтън", ["Лупъбъл ифове", "Аксесване велюту"], "Y")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": ["Лупъбъл ифове", "Аксесване велюту"]},  self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)
    
    def test_enroll_course_add_course_notes_other(self):
        result = self.student.enroll("Пайтън", ["Лупъбъл ифове", "Аксесване велюту"], "Z")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност"],
            "Пайтън": []},  self.student.courses)
        self.assertEqual("Course has been added.", result)
    
    def test_add_notes(self):
        result =  self.student.add_notes("Гейминг", "Детски игри")
        self.assertEqual({
            "Джава ООР": [
                "Класове и Обекти",
                "Унаследяване",
                "Капсулация",
                "Полиформизъм"
                ],
            "Гейминг": ["Добавена реалност", "Детски игри"]},  self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_wrong_course(self):
        with self.assertRaises(Exception) as ctx:
            self.student.add_notes("Лупъбъл елсове", "Елснати форчета")
        self.assertEqual("Cannot add notes. Course not found.", str(ctx.exception))
    
    def test_leave_existing_course(self):
        result = self.student.leave_course("Джава ООР")
        self.assertEqual({"Гейминг": ["Добавена реалност"]},  self.student.courses)
        self.assertEqual("Course has been removed", result)
    
    def test_leave_wrong_course(self):
        with self.assertRaises(Exception) as ctx:
            self.student.leave_course("Градинарство с Ути Бъчваров")
        self.assertEqual("Cannot remove course. Course not found.", ctx.exception.__str__())

if __name__ == "__main__":
    main()