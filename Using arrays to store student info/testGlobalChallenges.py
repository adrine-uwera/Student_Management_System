import unittest     # import unittest module
from global_challenges_student import GlobalChallengesStudent   # imports GlobalChallengesStudent class from global_challenges_student file


# class for testing ComputerScienceStudent class and inherits TestCase class from unittest module
class MyTestCase(unittest.TestCase):
    # a method to set up object to use when testing
    def setUp(self):
        # first object of the GlobalChallengesStudent class
        self.gc_student1 = GlobalChallengesStudent('m.don@alustudent.com', 'Marion Don', 'F', '2003-02-01',
                                                   'Kimironko', '+234788638856', '2020-01-01', 1, 'Health')
        # second object of the GlobalChallengesStudent class
        self.gc_student2 = GlobalChallengesStudent('M.jimmy@alustudent.com', 'Jimmy Max', 'M', '2000-07-03',
                                                   'Gikondo', '+250789888876', '2018-01-01', 3, 'Education')

    # method to test the init function
    @staticmethod
    def test__init__():
        gc_student1 = GlobalChallengesStudent('m.don@alustudent.com', 'Marion Don', 'F', '2003-02-01',
                                              'Kimironko', '+234788638856', '2020-01-01', 1, 'Health')

    # method to test the view_degree_program_outline() method
    def test_view_degree_program_outline(self):
        # test if the output of the view_degree_program_outline() is True
        self.assertTrue(self.gc_student1.view_degree_program_outline())

    # method to test promote_student() method
    def test_promote_student(self):
        # compares the output of promote_student() method to "Student is now in year 2" for gc_student1
        self.assertEqual(self.gc_student1.promote_student(), "Student is now in year 2")
        # compares the output of promote_student() method to "The student is in his/her final year" for gc_student2
        self.assertEqual(self.gc_student2.promote_student(), "The student is in his/her final year")

    # a method to test change_student_status() method
    def test_change_student_status(self):
        # compares the output of change_student_status() method to "Student done is done with the degree program" for gc_student2
        self.assertEqual(self.gc_student2.change_student_status(), "Student done is done with the degree program")
        # compares the output of change_student_status() method to "Student will graduate on 2022-12-28" for cs_student1
        self.assertEqual(self.gc_student1.change_student_status(), "Student will graduate on 2022-12-28")

    # a method to test print_student_information() method
    def test_print_student_information(self):
        # compares the output of print_student_information() method to the output below
        self.assertEqual(self.gc_student1.print_student_information(),
'''Student information: 
Student email: m.don@alustudent.com
Student name: Marion Don
Gender: F
Date of birth: 2003-02-01
Address: Kimironko
Phone number: +234788638856
Major: Global Challenges
Date of enrollment: 2020-01-01
Year:1
Status: Current
Internships:[]
Mission: Health
Expected graduation date: 2022-12-28''')


# executes the test
if __name__ == '__main__':
    unittest.main()
