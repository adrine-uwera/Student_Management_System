from student import *   # imports student file


# class for International Business And Trade student that inherits Student class
class InternationalBusinessAndTradeStudent(Student):
    def __init__(self, student_email, student_name, gender, date_of_birth, address, phone_number,
                 date_of_enrollment, year):     # initialize Computer Science student properties
        super().__init__(student_email, student_name, gender, date_of_birth, address, phone_number,
                         date_of_enrollment, year)  # Access student's properties in init method of student class (parent class)
        self.major = "International Business And Trade"     # overrides the major instance variable from parent class
        self.venture = []   # a list to store student's venture information

        # calculates the student's graduation date by adding the duration of the student's study
        self.expected_graduation_date = self.date_of_enrollment + datetime.timedelta(weeks=156)
        # 156 weeks equals to 3 years
        print("IBT student registered successfully!")   # displayed to indicate that the student was registered

    # a method for displaying degree program outline to the user
    # made a static method because this function made sense to be in here because a student would want to
    # view what course he/she will be taking through out the degree program
    @staticmethod
    def view_degree_program_outline():
        try:
            # opens the file containing the outline of the degree program in reading mode
            with open("ibt_degree_program_outline", "r") as ibt_program_outline:
                print(ibt_program_outline.read())   # reads the file and displays the information in the file
                return True     # returns true to indicate that the file was opened and read
        except OSError as e:    # handles the exception when the file couldn't be opened
            print("File not found", e)  # displays the error

    # a method to promote student
    def promote_student(self):
        if self.year == 3:  # checks of the International Business And Trade student is in his/her final year hence can't be promoted
            return "The student was in his/her final year." # displays to show that the student is in the final year
        else:   # promotes the student if he/she hasn't reached the final year
            return super().promote_student()    # accesses the promote method from parent class

    # a method for changing student status
    def change_student_status(self):
        if datetime.date.today() >= self.expected_graduation_date:    # checks if student is done with the studies
            self.status = "Alumni"  # updates student status to Alumni
            return "The student is done with the degree program!"   # displays to indicate that the student is officially done with the studies
        else:
            return f"Student will graduate {self.expected_graduation_date}"

    # a method to display student information 
    def print_student_information(self):
        # access the print_student_information method from parent class and returns all details of te student
        return super().print_student_information() + f"\nVenture:{self.venture}\nExpected graduation date:" \
                                                     f"{self.expected_graduation_date}"

    # a method to add student's venture details
    def add_venture_details(self):
        # takes user input for student's venture details
        venture_details = {"Venture name": input("Enter the venture name: "),
                           "Venture details": input("Enter the student's venture details: ")}
        self.venture.append(venture_details)    # appends student's venture details in the venture list
        return "Venture added successfully!"    # displays to indicate that the venture was recorded
