import unittest     # import unittest module
from entrepreneurship_student_class import EntrepreneurshipStudent  # imports EntrepreneurshipStudent from entrepreneurship_student_class file


# class for testing ComputerScienceStudent class and inherits TestCase class from unittest module
class MyTestCase(unittest.TestCase):
    # a method to set up object to use when testing
    def setUp(self):
        # first object of the EntrepreneurshipStudent class
        self.ent_student1 = EntrepreneurshipStudent("K.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                                    "Kabeza", "+242788786299", "2020-11-26", 1)
        # second object of the EntrepreneurshipStudent class
        self.ent_student2 = EntrepreneurshipStudent("l.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                                    "Kabeza", "+242788786299", "2019-11-26", 2)

    # method to test the init function
    @staticmethod
    def test__init__():
        ent_student3 = EntrepreneurshipStudent("m.rema@alustudent.com", "Kuma Rema", "M", "2000-05-08",
                                               "Kabeza", "+242788786299", "2019-11-26", 2)

    # method to test the view_degree_program_outline() method
    def test_view_degree_program_outline(self):
        # test if the output of the view_degree_program_outline() is True
        self.assertTrue(self.ent_student1.view_degree_program_outline())

    # method to test promote_student() method
    def test_promote_student(self):
        # compares the output of promote_student() method to "Student is now in year 2" for ent_student1
        self.assertEqual(self.ent_student1.promote_student(), "Student is now in year 2")
        # compares the output of promote_student() method to "The student is in his/her final year" for ent_student2
        self.assertEqual(self.ent_student2.promote_student(), "The student was in his/her final year.")

    # a method to test change_student_status() method
    def test_change_student_status(self):
        # compares the output of change_student_status() method to "Student will graduate on 2022-11-24" for ent_student1
        self.assertEqual(self.ent_student1.change_student_status(), "Student will graduate 2022-11-24")
        # compares the output of change_student_status() method to "Student done is done with the degree program" for ent_student2
        self.assertEqual(self.ent_student2.change_student_status(), "The student is done with the degree program!")

    # a method to test print_student_information() method
    def test_print_student_information(self):
        # compares the output of print_student_information() method to the output below
        self.assertEqual(self.ent_student1.print_student_information(),
'''Student information: 
Student email: K.rema@alustudent.com
Student name: Kuma Rema
Gender: M
Date of birth: 2000-05-08
Address: Kabeza
Phone number: +242788786299
Major: Entrepreneurship
Date of enrollment: 2020-11-26
Year:1
Status: Current
Internships:[]
Venture:[]
Expected graduation date:2022-11-24''')

    # test the add_venture_details() method
    def test_add_venture_details(self):
        # compare the output of the add_venture_details() method to "Venture added successfully!"
        self.assertEqual(self.ent_student1.add_venture_details(), "Venture added successfully!")


# executes the test
if __name__ == '__main__':
    unittest.main()
