from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTest(TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "Рамадан Али", 6.0)
    
    def test_constructor(self):
        self.assertEqual("1234", self.student._SeniorStudent__student_id)
        self.assertEqual("Рамадан Али", self.student._SeniorStudent__name)
        self.assertEqual(6.0, self.student._SeniorStudent__student_gpa)
        self.assertEqual(set(), self.student.colleges)
    
    def test_properties(self):
        self.assertEqual(self.student._SeniorStudent__student_id, self.student.student_id)
        self.assertEqual(self.student._SeniorStudent__name, self.student.name)
        self.assertEqual(self.student._SeniorStudent__student_gpa, self.student.student_gpa)

        self.assertIsInstance(self.student._SeniorStudent__student_id, str)
        self.assertIsInstance(self.student._SeniorStudent__name, str)
        self.assertIsInstance(self.student._SeniorStudent__student_gpa, float)
    
    def test_student_id_setter_short_than_four_digits(self):
        with self.assertRaises(ValueError) as ctx:
            self.student.student_id = " 123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
            self.student.student_id = ""
        self.assertEqual("Student ID must be at least 4 digits long!", str(ctx.exception))
    
    def test_student_id_setter_ok(self):
        self.student.student_id = " 12345A "
        self.assertEqual("12345A", self.student._SeniorStudent__student_id)
    
    def test_name_setter_null_or_empty(self):
        with self.assertRaises(ValueError) as ctx:
           self.student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
           self.student.name = "                        "
        self.assertEqual("Student name cannot be null or empty!", str(ctx.exception))
    
    def test_student_gpa_setter_less_or_equal_to_one(self):
        with self.assertRaises(ValueError) as ctx:
           self.student.student_gpa = 1
        self.assertEqual("Student GPA must be more than 1.0!", str(ctx.exception))
        with self.assertRaises(ValueError) as ctx:
           self.student.student_gpa = 0.7
        self.assertEqual("Student GPA must be more than 1.0!", str(ctx.exception))
    
    def test_apply_to_college_not_fullfill_gpa_required(self):
        result = self.student.apply_to_college(6.1, "Coolege A")
        self.assertEqual("Application failed!", result)
    
    def test_apply_to_college_gpa_required_ok(self):
        result = self.student.apply_to_college(3.0, "Coolege A")
        self.assertIn("COOLEGE A", self.student.colleges)
        self.assertEqual("Рамадан Али successfully applied to Coolege A.", result)
    
    def test_update_gpa_less_or_equal_to_one(self):
        result = self.student.update_gpa(1.0)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(6.0, self.student._SeniorStudent__student_gpa)
        result = self.student.update_gpa(0.7)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(6.0, self.student._SeniorStudent__student_gpa)
    
    def test_update_gpa_ok(self):
        result = self.student.update_gpa(1.1)
        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(1.1, self.student._SeniorStudent__student_gpa)
    
    def test_eq(self):
        self.assertEqual(SeniorStudent("6666", " Андрей Стоянов ", 6.0), self.student)
        self.assertNotEqual(SeniorStudent("6666", "Чарлз Дарвин", 5.0), self.student)

if __name__ == "__main__":
    main()