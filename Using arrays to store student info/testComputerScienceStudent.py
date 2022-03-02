import unittest     # import unittest module
from computer_science_student import ComputerScienceStudent  # imports ComputerScienceStudent class from computer_science_student file


# class for testing ComputerScienceStudent class and inherits TestCase class from unittest module
class TestComputerScienceStudent(unittest.TestCase):
    # a method to set up object to use when testing
    def setUp(self):
        # first object of the ComputerScienceStudent class
        self.cs_student1 = ComputerScienceStudent('a.ana@alustudent.com', 'Allie Ana', 'F', '2003-02-01',
                                                  'Kimironko', '+234788888888', '2021-01-09', 1, 'AllieAn')
        # second object of the ComputerScienceStudent class
        self.cs_student2 = ComputerScienceStudent('k.rema@alustudent.com', 'Kofi Rema', 'M', '2000-07-03',
                                                  'Gikondo', '+250789888876', '2017-01-01', 4, 'KofiRem')

    # method to test the init function
    def test__init__(self):
        # an object of the ComputerScienceStudent class
        # expected output is "Computer science student registered successfully!"
        cs_student1 = ComputerScienceStudent('a.ana@alustudent.com', 'Allie Ana', 'F', '2003-02-01',
                                             'Kimironko', '+234788888888', '2021-01-09', 1, 'AllieAn')

    # method to test the view_degree_program_outline() method
    def test_view_degree_program_outline(self):
        # test if the output of the view_degree_program_outline() is True
        self.assertTrue(self.cs_student1.view_degree_program_outline())

    # method to test promote_student() method
    def test_promote_student(self):
        # compares the output of promote_student() method to "Student is now in year 2" for cs_student1
        self.assertEqual(self.cs_student1.promote_student(), "Student is now in year 2")
        # compares the output of promote_student() method to "The student is in his/her final year" for cs_student2
        self.assertEqual(self.cs_student2.promote_student(), "The student is in his/her final year")

    # a method to test change_student_status() method
    def test_change_student_status(self):
        # compares the output of change_student_status() method to "Student done is done with the degree program" for cs_student2
        self.assertEqual(self.cs_student2.change_student_status(), "Student done is done with the degree program")
        # compares the output of change_student_status() method to "Student will graduate on 2025-01-04" for cs_student1
        self.assertEqual(self.cs_student1.change_student_status(), "Student will graduate on 2025-01-04")

    # a method to test print_student_information() method
    def test_print_student_information(self):
        # compares the output of print_student_information() method to the output below
        self.assertEqual(self.cs_student1.print_student_information(),
'''Student information: 
Student email: a.ana@alustudent.com
Student name: Allie Ana
Gender: F
Date of birth: 2003-02-01
Address: Kimironko
Phone number: +234788888888
Major: Computer Science
Date of enrollment: 2021-01-09
Year:1
Status: Current
Internships:[]
Github username: AllieAn
Expected graduation date: 2025-01-04''')


# executes the test
if __name__ == '__main__':
    unittest.main()
